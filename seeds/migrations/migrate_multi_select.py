import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

"""Run this ONCE to add multi_select support to the database."""
import sqlite3, os

db_path = os.path.join(os.path.dirname(__file__), 'instance', 'comptia.db')
if not os.path.exists(db_path):
    db_path = os.path.join(os.path.dirname(__file__), 'comptia.db')

print(f"Using DB: {db_path}")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

migrations = [
    ("ALTER TABLE questions ADD COLUMN multi_select BOOLEAN DEFAULT 0",
     "questions.multi_select"),
    ("ALTER TABLE attempt_answers ADD COLUMN chosen_choice_ids TEXT DEFAULT ''",
     "attempt_answers.chosen_choice_ids"),
]

for sql, label in migrations:
    try:
        cursor.execute(sql)
        print(f"Added column: {label}")
    except Exception as e:
        print(f"Skipped {label} (already exists): {e}")

conn.commit()
conn.close()
print("Migration complete!")