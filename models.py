from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Question(db.Model):
    __tablename__ = 'questions'
    id          = db.Column(db.Integer, primary_key=True)
    text        = db.Column(db.Text, nullable=False)
    domain      = db.Column(db.String(120), default='')
    exam        = db.Column(db.String(10), default='core1')  # 'core1' or 'core2'
    explanation = db.Column(db.Text, default='')
    active      = db.Column(db.Boolean, default=True)
    choices     = db.relationship('Choice', backref='question',
                                  cascade='all, delete-orphan', lazy=True)

class Choice(db.Model):
    __tablename__ = 'choices'
    id          = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    text        = db.Column(db.Text, nullable=False)
    is_correct  = db.Column(db.Boolean, default=False)

class QuizAttempt(db.Model):
    __tablename__ = 'quiz_attempts'
    id              = db.Column(db.Integer, primary_key=True)
    exam            = db.Column(db.String(10), default='core1')  # which exam this attempt was for
    total_questions = db.Column(db.Integer, default=0)
    correct_answers = db.Column(db.Integer, default=0)
    score_percent   = db.Column(db.Float, default=0.0)
    scaled_score    = db.Column(db.Integer, default=0)
    passed          = db.Column(db.Boolean, default=False)
    time_taken      = db.Column(db.Integer, default=0)
    created_at      = db.Column(db.DateTime)
    answers         = db.relationship('AttemptAnswer', backref='attempt',
                                      cascade='all, delete-orphan', lazy=True)

class AttemptAnswer(db.Model):
    __tablename__ = 'attempt_answers'
    id               = db.Column(db.Integer, primary_key=True)
    attempt_id       = db.Column(db.Integer, db.ForeignKey('quiz_attempts.id'), nullable=False)
    question_id      = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    chosen_choice_id = db.Column(db.Integer, nullable=True)
    is_correct       = db.Column(db.Boolean, default=False)