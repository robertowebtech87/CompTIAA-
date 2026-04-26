from flask import Flask, render_template, request, jsonify, redirect, url_for
from models import db, Question, Choice, QuizAttempt, AttemptAnswer, SpacedRepetition
from datetime import datetime, date, timedelta
from sqlalchemy import func
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comptia.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'comptia-a-plus-study-key'

db.init_app(app)

# ── Helpers ───────────────────────────────────────────────────────────────────

def get_domain_stats(exam=None):
    query = db.session.query(
        Question.domain,
        func.count(AttemptAnswer.id).label('total'),
        func.sum(AttemptAnswer.is_correct.cast(db.Integer)).label('correct')
    ).join(Question, AttemptAnswer.question_id == Question.id)
    if exam:
        query = query.filter(Question.exam == exam)
    rows = query.group_by(Question.domain).order_by(Question.domain).all()
    stats = []
    for domain, total, correct in rows:
        if total and domain:
            pct = round((correct or 0) / total * 100, 1)
            stats.append({
                'domain': domain, 'total': total,
                'correct': correct or 0, 'wrong': total - (correct or 0),
                'percent': pct,
                'level': 'strong' if pct >= 75 else ('ok' if pct >= 50 else 'weak')
            })
    stats.sort(key=lambda x: x['percent'])
    return stats

def get_exam_stats(exam):
    total_q = Question.query.filter_by(active=True, exam=exam).count()
    total_attempts = QuizAttempt.query.filter_by(exam=exam).count()
    best_score = db.session.query(func.max(QuizAttempt.score_percent))\
        .filter_by(exam=exam).scalar() or 0
    domain_counts = db.session.query(
        Question.domain, func.count(Question.id)
    ).filter_by(active=True, exam=exam)\
     .group_by(Question.domain).order_by(Question.domain).all()
    domains = [{'name': d, 'count': c} for d, c in domain_counts if d]
    return {
        'total_questions': total_q,
        'total_attempts': total_attempts,
        'best_score': round(best_score, 1),
        'domains': domains
    }

# ── Home ──────────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    core1 = get_exam_stats('core1')
    core2 = get_exam_stats('core2')
    intro = get_exam_stats('intro')
    recent = QuizAttempt.query.order_by(QuizAttempt.created_at.desc()).limit(5).all()
    return render_template('index.html', core1=core1, core2=core2, intro=intro, recent=recent)

# ── Quiz ──────────────────────────────────────────────────────────────────────

@app.route('/quiz/start', methods=['POST'])
def start_quiz():
    num_questions = int(request.form.get('num_questions', 20))
    selected_domains = request.form.getlist('domains')
    exam = request.form.get('exam', 'core1')
    per_q_timer = request.form.get('per_q_timer') == '1'
    retry_ids = request.form.get('retry_ids', '')

    # If retry_ids provided — use exact same questions
    if retry_ids:
        question_ids = [int(i) for i in retry_ids.split(',') if i]
        domains_label = 'Try Again'
    else:
        query = Question.query.filter_by(active=True, exam=exam)
        if selected_domains and 'all' not in selected_domains:
            query = query.filter(Question.domain.in_(selected_domains))
        questions = query.all()
        if not questions:
            return redirect(url_for('index'))
        sample = random.sample(questions, min(num_questions, len(questions)))
        question_ids = [q.id for q in sample]
        domains_label = ', '.join(selected_domains) if selected_domains and 'all' not in selected_domains else 'All Categories'

    passing_score = 675 if exam == 'core1' else (700 if exam == 'core2' else 700)
    return render_template('quiz.html', question_ids=question_ids,
                           total=len(question_ids),
                           time_limit=len(question_ids) * 60,
                           domains_label=domains_label,
                           exam=exam,
                           passing_score=passing_score,
                           simulation_mode=False,
                           per_q_timer=per_q_timer)

@app.route('/api/question/<int:qid>')
def get_question(qid):
    q = Question.query.get_or_404(qid)
    choices = [{'id': c.id, 'text': c.text} for c in q.choices]
    random.shuffle(choices)
    correct_count = sum(1 for c in q.choices if c.is_correct)
    return jsonify({'id': q.id, 'text': q.text, 'choices': choices,
                    'domain': q.domain, 'explanation': q.explanation,
                    'multi_select': bool(q.multi_select), 'correct_count': correct_count})

@app.route('/api/study/question/<int:qid>')
def get_study_question(qid):
    q = Question.query.get_or_404(qid)
    choices = [{'id': c.id, 'text': c.text, 'correct': c.is_correct} for c in q.choices]
    random.shuffle(choices)
    correct_count = sum(1 for c in q.choices if c.is_correct)
    try:
        is_multi = bool(q.multi_select)
    except Exception:
        is_multi = False
    return jsonify({'id': q.id, 'text': q.text, 'choices': choices,
                    'domain': q.domain, 'explanation': q.explanation or '',
                    'multi_select': is_multi, 'correct_count': correct_count})

@app.route('/api/submit', methods=['POST'])
def submit_quiz():
    data = request.json
    answers = data.get('answers', {})
    question_ids = data.get('question_ids', [])
    time_taken = data.get('time_taken', 0)
    exam = data.get('exam', 'core1')
    passing_score = 675 if exam == 'core1' else 700

    correct = 0
    attempt = QuizAttempt(total_questions=len(question_ids),
                          time_taken=time_taken, created_at=datetime.utcnow(),
                          exam=exam)
    db.session.add(attempt)
    db.session.flush()
    for qid in question_ids:
        q = Question.query.get(qid)
        if not q:
            continue
        if q.multi_select:
            correct_ids = set(str(c.id) for c in q.choices if c.is_correct)
            user_ids_raw = answers.get(str(qid), [])
            if isinstance(user_ids_raw, list):
                user_ids = set(str(i) for i in user_ids_raw)
            else:
                user_ids = {str(user_ids_raw)} if user_ids_raw else set()
            is_correct = user_ids == correct_ids
            chosen_ids_str = ','.join(sorted(user_ids))
            db.session.add(AttemptAnswer(attempt_id=attempt.id, question_id=qid,
                                         chosen_choice_id=None,
                                         chosen_choice_ids=chosen_ids_str,
                                         is_correct=is_correct))
        else:
            correct_choice = next((c for c in q.choices if c.is_correct), None)
            user_choice_id = answers.get(str(qid))
            is_correct = bool(correct_choice and user_choice_id and int(user_choice_id) == correct_choice.id)
            db.session.add(AttemptAnswer(attempt_id=attempt.id, question_id=qid,
                                         chosen_choice_id=user_choice_id,
                                         chosen_choice_ids='',
                                         is_correct=is_correct))
        if is_correct:
            correct += 1
    total = len(question_ids)
    score_percent = (correct / total * 100) if total else 0
    scaled_score = int(100 + (score_percent / 100) * 800)
    passed = scaled_score >= passing_score
    attempt.correct_answers = correct
    attempt.score_percent = score_percent
    attempt.scaled_score = scaled_score
    attempt.passed = passed
    db.session.commit()
    return jsonify({'attempt_id': attempt.id, 'correct': correct, 'total': total,
                    'score_percent': round(score_percent, 1),
                    'scaled_score': scaled_score, 'passed': passed,
                    'passing_score': passing_score})

@app.route('/results/<int:attempt_id>')
def results(attempt_id):
    attempt = QuizAttempt.query.get_or_404(attempt_id)
    answers = AttemptAnswer.query.filter_by(attempt_id=attempt_id).all()
    details = []
    domain_map = {}
    for aa in answers:
        q = Question.query.get(aa.question_id)
        if not q:
            continue
        correct_choices = [c for c in q.choices if c.is_correct]
        correct_texts = ' | '.join(c.text for c in correct_choices)
        if q.multi_select:
            chosen_ids = [int(i) for i in aa.chosen_choice_ids.split(',') if i]
            chosen_texts = ' | '.join(
                c.text for c in q.choices if c.id in chosen_ids
            ) or 'Not answered'
            your_answer = chosen_texts
        else:
            user_choice = Choice.query.get(aa.chosen_choice_id) if aa.chosen_choice_id else None
            your_answer = user_choice.text if user_choice else 'Not answered'
        details.append({
            'question': q.text, 'domain': q.domain,
            'your_answer': your_answer,
            'correct_answer': correct_texts,
            'is_correct': aa.is_correct,
            'explanation': q.explanation or '',
            'multi_select': bool(q.multi_select),
            'correct_count': len(correct_choices)
        })
        d = q.domain or 'Uncategorized'
        if d not in domain_map:
            domain_map[d] = {'total': 0, 'correct': 0}
        domain_map[d]['total'] += 1
        if aa.is_correct:
            domain_map[d]['correct'] += 1
    domain_breakdown = []
    for domain, counts in sorted(domain_map.items()):
        pct = round(counts['correct'] / counts['total'] * 100, 1) if counts['total'] else 0
        domain_breakdown.append({
            'domain': domain, 'correct': counts['correct'],
            'total': counts['total'], 'percent': pct,
            'level': 'strong' if pct >= 75 else ('ok' if pct >= 50 else 'weak')
        })
    domain_breakdown.sort(key=lambda x: x['percent'])
    passing_score = 675 if attempt.exam == 'core1' else 700
    quiz_domains = list(set(d['domain'] for d in details if d['domain']))
    return render_template('results.html', attempt=attempt, details=details,
                           domain_breakdown=domain_breakdown,
                           passing_score=passing_score,
                           quiz_domains=quiz_domains)

# ── History ───────────────────────────────────────────────────────────────────

@app.route('/history')
def history():
    exam = request.args.get('exam', 'core1')
    attempts = QuizAttempt.query.filter_by(exam=exam)\
        .order_by(QuizAttempt.created_at.desc()).all()
    domain_stats = get_domain_stats(exam=exam)
    missed_count = db.session.query(func.count(func.distinct(AttemptAnswer.question_id)))\
        .join(Question, AttemptAnswer.question_id == Question.id)\
        .filter(AttemptAnswer.is_correct == False, Question.exam == exam).scalar() or 0
    return render_template('history.html', attempts=attempts,
                           domain_stats=domain_stats,
                           missed_count=missed_count,
                           exam=exam)

# ── Study Mode ────────────────────────────────────────────────────────────────

@app.route('/study')
def study():
    exam = request.args.get('exam', 'core1')
    domain_counts = db.session.query(
        Question.domain, func.count(Question.id)
    ).filter_by(active=True, exam=exam).group_by(Question.domain).order_by(Question.domain).all()
    domains = [{'name': d, 'count': c} for d, c in domain_counts if d]
    total = Question.query.filter_by(active=True, exam=exam).count()
    return render_template('study.html', domains=domains, total=total, exam=exam)

@app.route('/study/start', methods=['POST'])
def start_study():
    selected_domains = request.form.getlist('domains')
    exam = request.form.get('exam', 'core1')
    query = Question.query.filter_by(active=True, exam=exam)
    if selected_domains and 'all' not in selected_domains:
        query = query.filter(Question.domain.in_(selected_domains))
    questions = query.all()
    if not questions:
        return redirect(url_for('study', exam=exam))
    random.shuffle(questions)
    question_ids = [q.id for q in questions]
    return render_template('study_session.html', question_ids=question_ids,
                           total=len(question_ids), exam=exam)

# ── Missed Questions ──────────────────────────────────────────────────────────

@app.route('/missed')
def missed():
    exam = request.args.get('exam', 'core1')
    wrong_qids = db.session.query(AttemptAnswer.question_id)\
        .join(Question, AttemptAnswer.question_id == Question.id)\
        .filter(AttemptAnswer.is_correct == False, Question.exam == exam)\
        .distinct().all()
    wrong_qids = [r[0] for r in wrong_qids]
    missed_questions = []
    for qid in wrong_qids:
        q = Question.query.get(qid)
        if not q:
            continue
        total_seen = AttemptAnswer.query.filter_by(question_id=qid).count()
        total_wrong = AttemptAnswer.query.filter_by(question_id=qid, is_correct=False).count()
        correct_choice = next((c for c in q.choices if c.is_correct), None)
        missed_questions.append({
            'id': q.id, 'text': q.text, 'domain': q.domain,
            'correct_answer': correct_choice.text if correct_choice else 'N/A',
            'explanation': q.explanation or '',
            'total_seen': total_seen, 'total_wrong': total_wrong,
            'wrong_pct': round(total_wrong / total_seen * 100) if total_seen else 0
        })
    missed_questions.sort(key=lambda x: x['wrong_pct'], reverse=True)
    return render_template('missed.html', missed=missed_questions, exam=exam)

@app.route('/missed/quiz', methods=['POST'])
def missed_quiz():
    exam = request.form.get('exam', 'core1')
    wrong_qids = db.session.query(AttemptAnswer.question_id)\
        .join(Question, AttemptAnswer.question_id == Question.id)\
        .filter(AttemptAnswer.is_correct == False, Question.exam == exam)\
        .distinct().all()
    question_ids = [r[0] for r in wrong_qids]
    random.shuffle(question_ids)
    if not question_ids:
        return redirect(url_for('missed', exam=exam))
    passing_score = 675 if exam == 'core1' else (700 if exam == 'core2' else 700)
    return render_template('quiz.html', question_ids=question_ids,
                           total=len(question_ids),
                           time_limit=len(question_ids) * 60,
                           domains_label='Missed Questions',
                           exam=exam, passing_score=passing_score,
                           simulation_mode=False)

# ── Admin ─────────────────────────────────────────────────────────────────────

@app.route('/admin')
def admin():
    exam = request.args.get('exam', 'core1')
    questions = Question.query.filter_by(exam=exam).order_by(Question.id.desc()).all()
    return render_template('admin.html', questions=questions, exam=exam)

@app.route('/admin/question/new', methods=['GET', 'POST'])
def new_question():
    exam = request.args.get('exam', request.form.get('exam', 'core1'))
    if request.method == 'POST':
        is_multi = request.form.get('multi_select', '0') == '1'
        correct_multi = request.form.getlist('correct_multi')
        q = Question(text=request.form['text'], domain=request.form.get('domain', ''),
                     explanation=request.form.get('explanation', ''),
                     exam=request.form.get('exam', 'core1'),
                     multi_select=is_multi, active=True)
        db.session.add(q)
        db.session.flush()
        for i in range(1, 5):
            ct = request.form.get(f'choice_{i}')
            if ct:
                if is_multi:
                    is_correct = str(i) in correct_multi
                else:
                    is_correct = request.form.get('correct') == str(i)
                db.session.add(Choice(question_id=q.id, text=ct, is_correct=is_correct))
        db.session.commit()
        return redirect(url_for('admin', exam=exam))
    return render_template('question_form.html', question=None, exam=exam)

@app.route('/admin/question/<int:qid>/edit', methods=['GET', 'POST'])
def edit_question(qid):
    q = Question.query.get_or_404(qid)
    if request.method == 'POST':
        is_multi = request.form.get('multi_select', '0') == '1'
        correct_multi = request.form.getlist('correct_multi')
        q.text = request.form['text']
        q.domain = request.form.get('domain', '')
        q.explanation = request.form.get('explanation', '')
        q.exam = request.form.get('exam', 'core1')
        q.multi_select = is_multi
        for c in q.choices:
            db.session.delete(c)
        db.session.flush()
        for i in range(1, 5):
            ct = request.form.get(f'choice_{i}')
            if ct:
                if is_multi:
                    is_correct = str(i) in correct_multi
                else:
                    is_correct = request.form.get('correct') == str(i)
                db.session.add(Choice(question_id=q.id, text=ct, is_correct=is_correct))
        db.session.commit()
        return redirect(url_for('admin', exam=q.exam))
    return render_template('question_form.html', question=q, exam=q.exam)

@app.route('/admin/question/<int:qid>/delete', methods=['POST'])
def delete_question(qid):
    q = Question.query.get_or_404(qid)
    exam = q.exam
    db.session.delete(q)
    db.session.commit()
    return redirect(url_for('admin', exam=exam))

@app.route('/admin/question/<int:qid>/toggle', methods=['POST'])
def toggle_question(qid):
    q = Question.query.get_or_404(qid)
    q.active = not q.active
    db.session.commit()
    return jsonify({'active': q.active})




# ── Progress Dashboard ────────────────────────────────────────────────────────

@app.route('/dashboard')
def dashboard():
    from datetime import date, timedelta

    # ── Study Streak ──────────────────────────────────────────────────────────
    all_attempts = QuizAttempt.query.order_by(QuizAttempt.created_at.desc()).all()
    study_days = sorted(set(a.created_at.date() for a in all_attempts), reverse=True)
    streak = 0
    today = date.today()
    check = today
    for d in study_days:
        if d == check or d == check - timedelta(days=1):
            streak += 1
            check = d
        else:
            break
    # If studied yesterday but not today, still show streak
    if study_days and study_days[0] < today - timedelta(days=1):
        streak = 0

    # ── Per-exam stats ────────────────────────────────────────────────────────
    def exam_stats(exam):
        attempts = QuizAttempt.query.filter_by(exam=exam).order_by(QuizAttempt.created_at).all()
        if not attempts:
            return {
                'total_attempts': 0, 'total_questions': 0,
                'overall_accuracy': 0, 'best_score': 0,
                'best_scaled': 0, 'passed_count': 0,
                'last_score': 0, 'last_scaled': 0,
                'sim_attempts': 0, 'sim_best': 0,
                'score_trend': [], 'dates_trend': [],
                'passing_score': 675 if exam == 'core1' else 700
            }
        total_q = sum(a.total_questions for a in attempts)
        total_correct = sum(a.correct_answers for a in attempts)
        accuracy = round(total_correct / total_q * 100, 1) if total_q else 0
        best = max(a.scaled_score for a in attempts)
        passed = sum(1 for a in attempts if a.passed)
        last = attempts[-1]
        sims = [a for a in attempts if a.total_questions >= 80]
        # Score trend — last 10 attempts
        recent = attempts[-10:]
        return {
            'total_attempts': len(attempts),
            'total_questions': total_q,
            'overall_accuracy': accuracy,
            'best_score': round(max(a.score_percent for a in attempts), 1),
            'best_scaled': best,
            'passed_count': passed,
            'last_score': round(last.score_percent, 1),
            'last_scaled': last.scaled_score,
            'sim_attempts': len(sims),
            'sim_best': max((a.scaled_score for a in sims), default=0),
            'score_trend': [a.scaled_score for a in recent],
            'dates_trend': [a.created_at.strftime('%d %b') for a in recent],
            'passing_score': 675 if exam == 'core1' else 700
        }

    core1 = exam_stats('core1')
    core2 = exam_stats('core2')

    # ── Domain weakness per exam ──────────────────────────────────────────────
    def domain_summary(exam):
        stats = get_domain_stats(exam=exam)
        if not stats:
            return [], []
        weak = [s for s in stats if s['total'] >= 5][:3]
        strong = [s for s in sorted(stats, key=lambda x: x['percent'], reverse=True) if s['total'] >= 5][:3]
        return weak, strong

    c1_weak, c1_strong = domain_summary('core1')
    c2_weak, c2_strong = domain_summary('core2')

    # ── Activity heatmap — last 30 days ───────────────────────────────────────
    last_30 = {}
    for i in range(30):
        d = today - timedelta(days=i)
        last_30[d] = 0
    for a in all_attempts:
        d = a.created_at.date()
        if d in last_30:
            last_30[d] += a.total_questions

    activity = [{'date': str(d), 'count': last_30[d]}
                for d in sorted(last_30.keys())]

    # ── Total questions available ─────────────────────────────────────────────
    c1_available = Question.query.filter_by(active=True, exam='core1').count()
    c2_available = Question.query.filter_by(active=True, exam='core2').count()

    # SR due counts
    c1_due = db.session.query(SpacedRepetition).join(Question)        .filter(Question.exam=='core1', SpacedRepetition.next_review<=today).count()
    c2_due = db.session.query(SpacedRepetition).join(Question)        .filter(Question.exam=='core2', SpacedRepetition.next_review<=today).count()

    return render_template('dashboard.html',
        streak=streak,
        today=today,
        core1=core1, core2=core2,
        c1_weak=c1_weak, c1_strong=c1_strong,
        c2_weak=c2_weak, c2_strong=c2_strong,
        activity=activity,
        c1_available=c1_available,
        c2_available=c2_available,
        total_attempts=len(all_attempts),
        total_questions_done=sum(a.total_questions for a in all_attempts),
        c1_due=c1_due,
        c2_due=c2_due
    )


# ── Spaced Repetition ─────────────────────────────────────────────────────────

def sm2_update(sr, correct):
    """Update SM-2 spaced repetition data based on answer correctness."""
    today = date.today()
    sr.last_reviewed = today

    if correct:
        sr.repetitions += 1
        if sr.repetitions == 1:
            sr.interval = 1
        elif sr.repetitions == 2:
            sr.interval = 3
        else:
            sr.interval = round(sr.interval * sr.easiness)
        # Update easiness factor (keep between 1.3 and 2.5)
        sr.easiness = max(1.3, min(2.5, sr.easiness + 0.1))
    else:
        # Wrong answer — reset repetitions, review tomorrow
        sr.repetitions = 0
        sr.interval = 1
        sr.easiness = max(1.3, sr.easiness - 0.2)

    sr.next_review = today + timedelta(days=sr.interval)
    return sr

def get_or_create_sr(question_id):
    """Get or create a SpacedRepetition record for a question."""
    sr = SpacedRepetition.query.filter_by(question_id=question_id).first()
    if not sr:
        sr = SpacedRepetition(
            question_id=question_id,
            next_review=date.today(),
            interval=1,
            easiness=2.5,
            repetitions=0
        )
        db.session.add(sr)
    return sr

@app.route('/review')
def review():
    exam = request.args.get('exam', 'core1')
    today = date.today()

    # Questions due for review today or overdue
    due = db.session.query(SpacedRepetition).join(Question)        .filter(Question.exam == exam,
                Question.active == True,
                SpacedRepetition.next_review <= today)        .order_by(SpacedRepetition.next_review).all()

    due_ids = [sr.question_id for sr in due]

    # New questions not yet in SR system
    reviewed_ids = db.session.query(SpacedRepetition.question_id).all()
    reviewed_ids = [r[0] for r in reviewed_ids]
    new_q = Question.query.filter_by(active=True, exam=exam)        .filter(~Question.id.in_(reviewed_ids) if reviewed_ids else True)        .limit(10).all()
    new_ids = [q.id for q in new_q]

    # Stats
    total_in_sr = db.session.query(SpacedRepetition).join(Question)        .filter(Question.exam == exam).count()
    total_q = Question.query.filter_by(active=True, exam=exam).count()

    # Upcoming reviews
    upcoming = db.session.query(SpacedRepetition, Question)        .join(Question, SpacedRepetition.question_id == Question.id)        .filter(Question.exam == exam,
                SpacedRepetition.next_review > today)        .order_by(SpacedRepetition.next_review)        .limit(5).all()

    return render_template('review.html',
        exam=exam,
        due_count=len(due_ids),
        new_count=len(new_ids),
        due_ids=due_ids,
        new_ids=new_ids,
        total_in_sr=total_in_sr,
        total_q=total_q,
        upcoming=upcoming,
        today=today
    )

@app.route('/review/start', methods=['POST'])
def start_review():
    exam = request.form.get('exam', 'core1')
    mode = request.form.get('mode', 'due')  # 'due' or 'new'
    today = date.today()

    if mode == 'due':
        due = db.session.query(SpacedRepetition).join(Question)            .filter(Question.exam == exam,
                    Question.active == True,
                    SpacedRepetition.next_review <= today)            .order_by(SpacedRepetition.next_review).all()
        question_ids = [sr.question_id for sr in due]
    else:
        reviewed_ids = [r[0] for r in db.session.query(SpacedRepetition.question_id).all()]
        new_q = Question.query.filter_by(active=True, exam=exam)            .filter(~Question.id.in_(reviewed_ids) if reviewed_ids else True)            .limit(20).all()
        question_ids = [q.id for q in new_q]

    if not question_ids:
        return redirect(url_for('review', exam=exam))

    random.shuffle(question_ids)
    passing_score = 675 if exam == 'core1' else 700
    return render_template('quiz.html',
        question_ids=question_ids,
        total=len(question_ids),
        time_limit=len(question_ids) * 90,
        domains_label='Spaced Review',
        exam=exam,
        passing_score=passing_score,
        simulation_mode=False,
        per_q_timer=False,
        review_mode=True
    )

@app.route('/api/sr/update', methods=['POST'])
def update_sr():
    """Called after each quiz to update SR data for answered questions."""
    data = request.json
    answers = data.get('answers', {})
    question_ids = data.get('question_ids', [])

    for qid_str in question_ids:
        qid = int(qid_str) if isinstance(qid_str, str) else qid_str
        q = Question.query.get(qid)
        if not q:
            continue
        # Determine if correct
        answer_val = answers.get(str(qid))
        if q.multi_select:
            correct_ids = set(str(c.id) for c in q.choices if c.is_correct)
            if isinstance(answer_val, list):
                user_ids = set(str(i) for i in answer_val)
            else:
                user_ids = set()
            correct = user_ids == correct_ids
        else:
            correct_choice = next((c for c in q.choices if c.is_correct), None)
            correct = bool(correct_choice and answer_val and
                          int(answer_val) == correct_choice.id)
        sr = get_or_create_sr(qid)
        sm2_update(sr, correct)

    db.session.commit()
    return jsonify({'updated': len(question_ids)})

# ── Exam Simulation Mode ──────────────────────────────────────────────────────

@app.route('/quiz/simulate', methods=['GET', 'POST'])
def simulate():
    exam = request.args.get('exam', request.form.get('exam', 'core1'))
    if request.method == 'GET':
        core1_count = Question.query.filter_by(active=True, exam='core1').count()
        core2_count = Question.query.filter_by(active=True, exam='core2').count()
        return render_template('simulate.html',
                               exam=exam,
                               core1_count=core1_count,
                               core2_count=core2_count,
                               simulation_mode=False)

    # POST — start the simulation
    questions = Question.query.filter_by(active=True, exam=exam).all()
    if not questions:
        return redirect(url_for('simulate'))
    sample = random.sample(questions, min(90, len(questions)))
    question_ids = [q.id for q in sample]
    passing_score = 675 if exam == 'core1' else 700
    return render_template('quiz.html',
                           question_ids=question_ids,
                           total=len(question_ids),
                           time_limit=90 * 60,
                           domains_label='Exam Simulation',
                           exam=exam,
                           passing_score=passing_score,
                           simulation_mode=True)

# ── PBQ Labs ──────────────────────────────────────────────────────────────────

LABS = {
    'core1': [
        {'id': 'ip-config',           'title': 'IP Configuration',              'desc': 'Configure IP address, subnet mask and default gateway like a real Windows network dialog.', 'time': 8,  'difficulty': 'Medium'},
        {'id': 'cable-id',            'title': 'Cable Identification',           'desc': 'Match the correct cables and connectors to their ports on a PC back panel.', 'time': 6,  'difficulty': 'Easy'},
        {'id': 'boot-order',          'title': 'BIOS Boot Order',               'desc': 'Set the correct boot sequence in a simulated BIOS to boot from the right device.', 'time': 5,  'difficulty': 'Easy'},
        {'id': 'soho-network',        'title': 'SOHO Network Setup',            'desc': 'Connect and configure devices in a small office/home office network diagram.', 'time': 10, 'difficulty': 'Hard'},
        {'id': 'component-match',     'title': 'Component Matching',            'desc': 'Identify and match hardware components to their correct slots on a motherboard.', 'time': 7,  'difficulty': 'Medium'},
        {'id': 'printer-trouble',     'title': 'Printer Troubleshooting',       'desc': 'Diagnose and resolve common printer issues from a set of reported symptoms.', 'time': 8,  'difficulty': 'Medium'},
        {'id': 'ram-install',         'title': 'RAM Installation',              'desc': 'Select and install the correct RAM for a given system specification.', 'time': 6,  'difficulty': 'Easy'},
        {'id': 'display-trouble',     'title': 'Display Troubleshooting',       'desc': 'Identify the cause of display issues from symptoms and select the correct fix.', 'time': 7,  'difficulty': 'Medium'},
        {'id': 'motherboard-ports',   'title': 'Motherboard Ports ID',          'desc': 'Identify ports and connectors found on a typical motherboard and PC back panel.', 'time': 7,  'difficulty': 'Medium'},
        {'id': 'cable-crimp',         'title': 'Network Cable Crimping',        'desc': 'Order the correct steps to crimp an RJ45 connector onto a Cat6 cable.', 'time': 6,  'difficulty': 'Easy'},
        {'id': 'wireless-trouble',    'title': 'Wireless Troubleshooting',      'desc': 'Diagnose and resolve Wi-Fi connectivity issues step by step.', 'time': 8,  'difficulty': 'Medium'},
        {'id': 'hardware-scenario',   'title': 'Hardware Troubleshooting',      'desc': 'Given hardware symptoms, identify the faulty component and correct action.', 'time': 9,  'difficulty': 'Hard'},
    ],
    'core2': [
        {'id': 'win-network',         'title': 'Windows Network Settings',      'desc': 'Fix a broken network configuration in a simulated Windows Settings interface.', 'time': 8,  'difficulty': 'Medium'},
        {'id': 'permissions',         'title': 'User Permissions',              'desc': 'Set the correct NTFS file permissions for users based on a given scenario.', 'time': 9,  'difficulty': 'Hard'},
        {'id': 'malware-removal',     'title': 'Malware Removal Steps',         'desc': 'Order the correct steps for removing malware from an infected system.', 'time': 7,  'difficulty': 'Medium'},
        {'id': 'backup-config',       'title': 'Backup Configuration',          'desc': 'Configure the correct backup strategy for a given business requirement.', 'time': 6,  'difficulty': 'Medium'},
        {'id': 'sim-terminal',        'title': 'Simulated Terminal',            'desc': 'Use ping, ipconfig, and tracert in a simulated command prompt to diagnose issues.', 'time': 10, 'difficulty': 'Hard'},
        {'id': 'security-config',     'title': 'Security Settings',             'desc': 'Configure Windows Defender and Firewall settings for a given security scenario.', 'time': 8,  'difficulty': 'Hard'},
        {'id': 'win-trouble',         'title': 'Windows Troubleshooting',       'desc': 'Click through a Windows problem scenario selecting the correct diagnostic steps.', 'time': 9,  'difficulty': 'Hard'},
        {'id': 'win-install',         'title': 'Windows Installation Steps',    'desc': 'Order the correct steps to perform a clean Windows installation.', 'time': 7,  'difficulty': 'Medium'},
        {'id': 'mobile-trouble',      'title': 'Mobile Device Troubleshooting', 'desc': 'Diagnose and resolve common smartphone and tablet issues.', 'time': 8,  'difficulty': 'Medium'},
        {'id': 'operational-procedures', 'title': 'Operational Procedures',     'desc': 'Apply correct IT procedures for ticketing, change management, and professional conduct.', 'time': 8, 'difficulty': 'Medium'},
    ]
}

@app.route('/pbq')
def pbq():
    exam = request.args.get('exam', 'core1')
    return render_template('pbq_home.html', labs=LABS, exam=exam)

@app.route('/pbq/<exam>/<lab_id>')
def pbq_lab(exam, lab_id):
    lab_list = LABS.get(exam, [])
    lab = next((l for l in lab_list if l['id'] == lab_id), None)
    if not lab:
        return redirect(url_for('pbq', exam=exam))
    return render_template(f'pbq/{exam}/{lab_id}.html', lab=lab, exam=exam)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # migrate existing questions to core1
        Question.query.filter_by(exam=None).update({'exam': 'core1'})
        db.session.commit()
    app.run(debug=True, host='0.0.0.0')