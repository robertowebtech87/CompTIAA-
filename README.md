# CompTIA A+ Exam Prep Platform

A full-featured quiz platform to study for your CompTIA A+ certification exam.

## Features
- ✅ Admin panel to add/edit/delete questions
- ✅ Randomized quiz sessions (you choose how many questions)
- ✅ Countdown timer (1 min per question, like the real exam)
- ✅ Scaled scoring (100–900 scale, passing = 675)
- ✅ Results page with correct/wrong breakdown and explanations
- ✅ Score history with progress chart

## Setup

### 1. Create a virtual environment
```bash
cd comptia_quiz
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python app.py
```

### 4. Open in your browser
```
http://localhost:5000
```

The SQLite database (`comptia.db`) is created automatically on first run.

## How to use

1. Go to **Admin** → Add your CompTIA A+ questions with 4 choices, mark the correct one, add the domain (e.g. "Networking", "Hardware") and an optional explanation.
2. Go **Home**, choose how many questions, click **Start Quiz**.
3. Answer all questions, navigate with Prev/Next or the dots.
4. Submit and review your results.
5. Track your progress in **History**.

## Exam info
- CompTIA A+ Core 1 (220-1101) — passing score: **675/900**
- CompTIA A+ Core 2 (220-1102) — passing score: **700/900**

