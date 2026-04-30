import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

"""Run this ONCE to add the exam column to existing tables."""
from app import app, db
from models import Question, QuizAttempt
import sqlite3, os

db_path = os.path.join(os.path.dirname(__file__), 'instance', 'comptia.db')
if not os.path.exists(db_path):
    db_path = os.path.join(os.path.dirname(__file__), 'comptia.db')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Add exam column to questions if it doesn't exist
try:
    cursor.execute("ALTER TABLE questions ADD COLUMN exam VARCHAR(10) DEFAULT 'core1'")
    print("Added exam column to questions")
except Exception as e:
    print(f"questions.exam: {e}")

# Add exam column to quiz_attempts if it doesn't exist
try:
    cursor.execute("ALTER TABLE quiz_attempts ADD COLUMN exam VARCHAR(10) DEFAULT 'core1'")
    print("Added exam column to quiz_attempts")
except Exception as e:
    print(f"quiz_attempts.exam: {e}")

conn.commit()
conn.close()

# Set all existing questions to core1
with app.app_context():
    updated = Question.query.filter(
        (Question.exam == None) | (Question.exam == '')
    ).update({'exam': 'core1'})
    db.session.commit()
    print(f"Set {updated} existing questions to core1")
    print(f"Total questions: {Question.query.count()}")
    print(f"Core 1 questions: {Question.query.filter_by(exam='core1').count()}")
    print(f"Core 2 questions: {Question.query.filter_by(exam='core2').count()}")