"""Run this ONCE to create the spaced_repetition table."""
import sqlite3, os

db_path = os.path.join(os.path.dirname(__file__), "instance", "comptia.db")
if not os.path.exists(db_path):
    db_path = os.path.join(os.path.dirname(__file__), "comptia.db")

print(f"Using DB: {db_path}")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS spaced_repetition (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_id INTEGER NOT NULL UNIQUE,
            interval INTEGER DEFAULT 1,
            easiness REAL DEFAULT 2.5,
            repetitions INTEGER DEFAULT 0,
            next_review DATE NOT NULL,
            last_reviewed DATE,
            FOREIGN KEY (question_id) REFERENCES questions(id)
        )
    """)
    print("Created spaced_repetition table")
except Exception as e:
    print(f"Error: {e}")

conn.commit()
conn.close()
print("Migration complete!")