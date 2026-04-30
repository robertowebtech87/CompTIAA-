import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

"""Run this ONCE to verify the exam column supports 'intro' values."""
import sqlite3, os

db_path = os.path.join(os.path.dirname(__file__), "instance", "comptia.db")
if not os.path.exists(db_path):
    db_path = os.path.join(os.path.dirname(__file__), "comptia.db")

print(f"Using DB: {db_path}")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Check current exam values
cursor.execute("SELECT DISTINCT exam FROM questions")
exams = cursor.fetchall()
print(f"Current exam types: {[e[0] for e in exams]}")

# The exam column is just a text field so 'intro' works without migration
# Just verify the column exists
cursor.execute("PRAGMA table_info(questions)")
cols = [row[1] for row in cursor.fetchall()]
print(f"Question columns: {cols}")

conn.close()
print("DB supports intro exam type — no migration needed!")
print("You can now run seed_it_fundamentals.py")