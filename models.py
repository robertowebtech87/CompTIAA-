from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Question(db.Model):
    __tablename__ = "questions"
    id            = db.Column(db.Integer, primary_key=True)
    text          = db.Column(db.Text, nullable=False)
    domain        = db.Column(db.String(120), default="")
    exam          = db.Column(db.String(10), default="core1")
    explanation   = db.Column(db.Text, default="")
    active        = db.Column(db.Boolean, default=True)
    multi_select  = db.Column(db.Boolean, default=False)
    choices       = db.relationship("Choice", backref="question",
                                    cascade="all, delete-orphan", lazy=True)

class Choice(db.Model):
    __tablename__ = "choices"
    id          = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=False)
    text        = db.Column(db.Text, nullable=False)
    is_correct  = db.Column(db.Boolean, default=False)

class QuizAttempt(db.Model):
    __tablename__ = "quiz_attempts"
    id              = db.Column(db.Integer, primary_key=True)
    exam            = db.Column(db.String(10), default="core1")
    total_questions = db.Column(db.Integer, default=0)
    correct_answers = db.Column(db.Integer, default=0)
    score_percent   = db.Column(db.Float, default=0.0)
    scaled_score    = db.Column(db.Integer, default=0)
    passed          = db.Column(db.Boolean, default=False)
    time_taken      = db.Column(db.Integer, default=0)
    created_at      = db.Column(db.DateTime)
    answers         = db.relationship("AttemptAnswer", backref="attempt",
                                      cascade="all, delete-orphan", lazy=True)

class AttemptAnswer(db.Model):
    __tablename__ = "attempt_answers"
    id                = db.Column(db.Integer, primary_key=True)
    attempt_id        = db.Column(db.Integer, db.ForeignKey("quiz_attempts.id"), nullable=False)
    question_id       = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=False)
    chosen_choice_id  = db.Column(db.Integer, nullable=True)
    chosen_choice_ids = db.Column(db.Text, default="")
    is_correct        = db.Column(db.Boolean, default=False)

class SpacedRepetition(db.Model):
    __tablename__ = "spaced_repetition"
    id            = db.Column(db.Integer, primary_key=True)
    question_id   = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=False, unique=True)
    interval      = db.Column(db.Integer, default=1)      # days until next review
    easiness      = db.Column(db.Float, default=2.5)      # SM-2 easiness factor
    repetitions   = db.Column(db.Integer, default=0)      # times answered correctly in a row
    next_review   = db.Column(db.Date, nullable=False)     # date of next review
    last_reviewed = db.Column(db.Date, nullable=True)
    question      = db.relationship("Question", backref="sr_data")