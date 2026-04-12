from flask import Flask, render_template, request, jsonify, redirect, url_for
from models import db, Question, Choice, QuizAttempt, AttemptAnswer
from datetime import datetime
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
    recent = QuizAttempt.query.order_by(QuizAttempt.created_at.desc()).limit(5).all()
    return render_template('index.html', core1=core1, core2=core2, recent=recent)

# ── Quiz ──────────────────────────────────────────────────────────────────────

@app.route('/quiz/start', methods=['POST'])
def start_quiz():
    num_questions = int(request.form.get('num_questions', 20))
    selected_domains = request.form.getlist('domains')
    exam = request.form.get('exam', 'core1')

    query = Question.query.filter_by(active=True, exam=exam)
    if selected_domains and 'all' not in selected_domains:
        query = query.filter(Question.domain.in_(selected_domains))

    questions = query.all()
    if not questions:
        return redirect(url_for('index'))
    sample = random.sample(questions, min(num_questions, len(questions)))
    question_ids = [q.id for q in sample]
    domains_label = ', '.join(selected_domains) if selected_domains and 'all' not in selected_domains else 'All Categories'
    passing_score = 675 if exam == 'core1' else 700
    return render_template('quiz.html', question_ids=question_ids,
                           total=len(question_ids),
                           time_limit=len(question_ids) * 60,
                           domains_label=domains_label,
                           exam=exam,
                           passing_score=passing_score)

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
    return jsonify({'id': q.id, 'text': q.text, 'choices': choices,
                    'domain': q.domain, 'explanation': q.explanation,
                    'multi_select': bool(q.multi_select), 'correct_count': correct_count})

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
    return render_template('results.html', attempt=attempt, details=details,
                           domain_breakdown=domain_breakdown,
                           passing_score=passing_score)

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
    passing_score = 675 if exam == 'core1' else 700
    return render_template('quiz.html', question_ids=question_ids,
                           total=len(question_ids),
                           time_limit=len(question_ids) * 60,
                           domains_label='Missed Questions',
                           exam=exam, passing_score=passing_score)

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

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # migrate existing questions to core1
        Question.query.filter_by(exam=None).update({'exam': 'core1'})
        db.session.commit()
    app.run(debug=True)