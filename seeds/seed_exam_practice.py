from app import app, db
from models import Question, Choice

questions_data = [

    # Q3 - Laptop vs Desktop considerations (multi-select)
    {
        'text': 'Which considerations are most likely to be of concern when it comes to the key components of a laptop computer versus those of a desktop computer? (Choose all that apply)',
        'domain': 'Laptops',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Laptops sacrifice physical size and upgradeability compared to desktops. They are also more susceptible to overheating due to their compact design limiting airflow.',
        'choices': [
            ('Processing speed', False),
            ('Physical size', True),
            ('Colour of the components', False),
            ('Upgradeability', True),
            ('Susceptibility to overheating', True),
        ]
    },

    # Q4 - Capacitive vs resistive (multi-select)
    {
        'text': 'Which attributes correctly distinguish capacitive touchscreens from resistive touchscreens? (Choose all that apply)',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Capacitive screens use a conductive layer that supports multi-touch gestures like pinch-to-zoom. They are also more sensitive and responsive than resistive screens which require physical pressure.',
        'choices': [
            ('Capacitive screens work with any object including gloved hands', False),
            ('Capacitive screens are cheaper to manufacture', False),
            ('Capacitive supports multi-touch gestures', True),
            ('Capacitive are more sensitive and responsive', True),
        ]
    },

    # Q7 - RAM temporary working space
    {
        'text': 'Which key computer hardware component represents a temporary working space for active data and running programs?',
        'domain': 'Hardware',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'RAM (Random Access Memory) is volatile memory that temporarily holds data and instructions that the CPU is actively using. It is lost when the computer is powered off.',
        'choices': [
            ('Hard Disk Drive (HDD)', False),
            ('Random Access Memory (RAM)', True),
            ('Central Processing Unit (CPU)', False),
            ('Solid State Drive (SSD)', False),
        ]
    },

    # Q10 - Cleaning primary factor
    {
        'text': 'Which factor is the primary consideration when it comes to cleaning computer components?',
        'domain': 'Maintenance',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Dust is the primary concern when cleaning computer components. Dust accumulation blocks airflow, causes overheating, and can lead to component failure over time.',
        'choices': [
            ('Moisture and liquid spills', False),
            ('Static electricity buildup', False),
            ('Dust', True),
            ('Corrosion from humidity', False),
        ]
    },

    # Q12 - Partitioning and formatting
    {
        'text': 'Which step of replacing a hard drive involves dividing up the disk space and applying the file system?',
        'domain': 'Storage',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Partitioning divides the drive into logical sections. Formatting applies the file system (such as NTFS) so the drive can store and retrieve data. Both steps are required before an OS can use a new drive.',
        'choices': [
            ('Physical installation', False),
            ('BIOS detection', False),
            ('Driver installation', False),
            ('Partitioning and formatting', True),
        ]
    },

    # Q13 - Webcam fps
    {
        'text': 'For which type of integrated peripheral would the "fps" (frames per second) value be an important consideration?',
        'domain': 'Laptops',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'FPS (frames per second) determines how smooth video capture appears. A webcam rated at 30fps captures smoother video than one at 15fps making it an important spec when choosing a webcam.',
        'choices': [
            ('Microphone', False),
            ('Fingerprint reader', False),
            ('Bluetooth adapter', False),
            ('Webcam', True),
        ]
    },
]

with app.app_context():
    added = 0
    skipped = 0
    for qd in questions_data:
        existing = Question.query.filter_by(text=qd['text']).first()
        if existing:
            skipped += 1
            continue
        q = Question(
            text=qd['text'],
            domain=qd['domain'],
            exam=qd.get('exam', 'core1'),
            explanation=qd.get('explanation', ''),
            multi_select=qd.get('multi_select', False),
            active=True
        )
        db.session.add(q)
        db.session.flush()
        for choice_text, is_correct in qd['choices']:
            db.session.add(Choice(question_id=q.id, text=choice_text, is_correct=is_correct))
        added += 1
    db.session.commit()
    total = Question.query.count()
    core1 = Question.query.filter_by(exam='core1').count()
    print(f'Added {added} questions. Skipped {skipped} duplicates.')
    print(f'Core 1 total: {core1} | Overall: {total}')