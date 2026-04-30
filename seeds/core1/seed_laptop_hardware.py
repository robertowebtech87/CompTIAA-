import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app import app, db
from models import Question, Choice

questions_data = [

    {
        'text': 'What advantage do Lithium-ion and Lithium-ion Polymer batteries share over older battery technologies like Nickel-cadmium?',
        'domain': 'Laptops',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Older batteries like Ni-Cd suffered from memory effect — if not fully discharged before recharging they would lose capacity over time. Li-ion and Li-Po do not have this problem.',
        'choices': [
            ('They are cheaper to manufacture and easier to recycle', False),
            ('They do not suffer from memory effect so they can be recharged at any time without reducing overall battery capacity', True),
            ('They last twice as long per charge as older technologies', False),
            ('They can be charged wirelessly without a cable', False),
        ]
    },
    {
        'text': 'What is the difference between a modular laptop battery and a built-in laptop battery?',
        'domain': 'Laptops',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Modular batteries can be removed by the user by pressing a release button. Built-in batteries are integrated into the chassis and require a technician to disassemble the entire device.',
        'choices': [
            ('Modular batteries last longer than built-in batteries', False),
            ('A modular battery can be removed and replaced by the user while a built-in battery requires disassembling the entire device to replace', True),
            ('Built-in batteries are always larger capacity than modular ones', False),
            ('Modular batteries are only found in gaming laptops', False),
        ]
    },
    {
        'text': 'How is a laptop keyboard typically connected to the system board and how can you test if it is faulty?',
        'domain': 'Laptops',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Laptop keyboards connect via a ribbon cable. Plugging in an external USB keyboard allows you to determine whether the issue is with the keyboard hardware itself or with the operating system.',
        'choices': [
            ('Via USB internally — test by opening Device Manager', False),
            ('Via a ribbon cable — test by plugging in an external USB keyboard to determine if the issue is hardware or software', True),
            ('Via Bluetooth — test by re-pairing the keyboard', False),
            ('Via PCIe — test by reseating the keyboard connector on the motherboard', False),
        ]
    },
    {
        'text': 'Why must you be especially careful when replacing a single keycap on a laptop keyboard?',
        'domain': 'Laptops',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Laptop keycaps are much more fragile than desktop keycaps and the retention clips and scissor mechanisms underneath can be easily damaged. Always follow manufacturer instructions.',
        'choices': [
            ('Laptop keycaps contain electronic components that can short circuit', False),
            ('Laptop keycaps are much more fragile than desktop keycaps and the mechanisms underneath can be easily damaged — manufacturer instructions must be followed carefully', True),
            ('Replacing a keycap requires special tools only available from the manufacturer', False),
            ('A single wrong keycap can corrupt the keyboard firmware', False),
        ]
    },
    {
        'text': 'What happens if the RAM in a laptop is soldered directly to the motherboard?',
        'domain': 'Laptops',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Soldered RAM cannot be removed or upgraded as a standalone module. To get more RAM the entire system board would need to be replaced which is usually not cost effective.',
        'choices': [
            ('The RAM runs faster because it has a direct connection', False),
            ('The RAM cannot be upgraded or replaced — the entire motherboard would need to be replaced to increase the memory', True),
            ('The laptop automatically manages RAM more efficiently', False),
            ('Soldered RAM is always dual channel for better performance', False),
        ]
    },
    {
        'text': 'What is the key installation difference between a 2.5-inch laptop drive and an M.2 drive?',
        'domain': 'Laptops',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A 2.5-inch drive needs separate data and power cables. An M.2 drive uses a single slot connector for both data and power, is much smaller, and is significantly easier to install.',
        'choices': [
            ('A 2.5-inch drive is faster than an M.2 drive', False),
            ('A 2.5-inch drive requires separate data and power connections while an M.2 drive uses a single slot connector for both making it smaller and easier to install', True),
            ('M.2 drives require an external power adapter', False),
            ('2.5-inch drives connect via USB while M.2 drives use SATA', False),
        ]
    },
    {
        'text': 'What is drive imaging or cloning software and why is it useful when upgrading a laptop to an SSD?',
        'domain': 'Laptops',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Cloning software creates an exact copy of all data from the old drive to the new one. This saves significant time because the OS and all applications do not need to be reinstalled from scratch.',
        'choices': [
            ('Software that takes screenshots of drive contents for documentation', False),
            ('Software that creates an exact duplicate of all data from one drive to another saving time by avoiding reinstalling the OS and applications from scratch', True),
            ('A tool that compresses drive contents to fit on a smaller SSD', False),
            ('Software that monitors drive health and predicts failures', False),
        ]
    },
    {
        'text': 'What type of wireless interface cards are found in older laptops and how are they installed?',
        'domain': 'Laptops',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Older laptops use mini PCI or mini PCIe cards for Wi-Fi and Bluetooth. They install in a slot on the system board similar to a memory module and require connecting the built-in antenna wires to the card.',
        'choices': [
            ('USB wireless dongles plugged into internal USB headers', False),
            ('Mini PCI or mini PCIe cards installed in a slot on the system board similar to memory — the built-in antenna wires must be connected to the card', True),
            ('Full-size PCIe cards installed in a dedicated expansion bay', False),
            ('M.2 cards that only support Wi-Fi 6 and newer standards', False),
        ]
    },
    {
        'text': 'Why are wireless antenna wires in a laptop routed around the outside of the display?',
        'domain': 'Laptops',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Routing the antenna wires to the top of the display gets the antennas as high as possible when the screen is open which significantly improves wireless signal strength and reception.',
        'choices': [
            ('To keep the antenna wires away from the display backlight which causes interference', False),
            ('To get the antennas as high as possible when the screen is open which improves wireless signal strength and reception', True),
            ('Because the display frame is made of a material that amplifies the signal', False),
            ('To allow the antenna to be easily replaced without disassembling the base', False),
        ]
    },
    {
        'text': 'What are the two biometric authentication options in Windows Hello and what hardware does each require?',
        'domain': 'Laptops',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Windows Hello Face uses facial recognition and requires an infrared or compatible camera. Windows Hello Fingerprint uses a fingerprint reader that must be built into or attached to the laptop.',
        'choices': [
            ('Voice recognition requiring a microphone and iris scan requiring a special display', False),
            ('Windows Hello Face uses facial recognition requiring a compatible camera and Windows Hello Fingerprint uses a fingerprint reader built into the laptop', True),
            ('PIN authentication requiring a numeric keypad and pattern recognition requiring a touchscreen', False),
            ('Retina scan requiring a special monitor and hand geometry requiring a tablet', False),
        ]
    },
    {
        'text': 'What is NFC, what is its typical range, and what are some use cases beyond contactless payments?',
        'domain': 'Laptops',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'NFC (Near Field Communication) has a range of about 4cm or less. Beyond payments it is used for authentication on hospital workstations and in warehouses manufacturing and shipping/receiving environments.',
        'choices': [
            ('Near Frequency Communication — 30cm range — used for wireless charging and Bluetooth pairing', False),
            ('Near Field Communication — range of approximately 4cm or less — used for authentication on hospital workstations and in warehouse manufacturing and shipping environments', True),
            ('Network File Communication — 1 metre range — used for file transfer between devices', False),
            ('Near Field Connection — 10cm range — used exclusively for contactless payments', False),
        ]
    },
    {
        'text': 'Where are the camera and microphones typically located on a laptop display?',
        'domain': 'Laptops',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'The camera is centered at the top of the screen bezel with microphones positioned to the left and right of it for balanced stereo audio capture.',
        'choices': [
            ('Camera on the left side of the display with a single microphone on the right', False),
            ('Camera centered at the top of the screen with microphones to the left and right of it', True),
            ('Camera at the bottom of the display with microphones built into the keyboard area', False),
            ('Camera on the right side of the display with microphones along the bottom edge', False),
        ]
    },
    {
        'text': 'What is a limitation of built-in laptop cameras and how can it be addressed?',
        'domain': 'Laptops',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Built-in laptop cameras offer limited image quality and functionality compared to dedicated cameras. Users who need higher definition video can attach an external USB camera to the top of the display.',
        'choices': [
            ('Built-in cameras cannot be used for video calls — the only solution is a dedicated webcam device', False),
            ('Built-in cameras offer limited quality and functionality — users who need higher definition can attach an external camera to the top of the laptop display', True),
            ('Built-in cameras only work with specific video conferencing software', False),
            ('Built-in cameras are limited to 720p and cannot be replaced', False),
        ]
    },
    {
        'text': 'What does the term "memory effect" mean and why is it not a concern with modern laptop batteries?',
        'domain': 'Laptops',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Memory effect occurred in older Ni-Cd batteries where partial charges caused the battery to "remember" a lower capacity reducing its effective range. Lithium-ion and Li-Po batteries used in modern laptops do not suffer from this problem.',
        'choices': [
            ('A phenomenon where the battery remembers recent application usage and optimizes power for those apps', False),
            ('A problem with older Ni-Cd batteries where partial charging caused permanent capacity reduction — not a concern with modern Li-ion and Li-Po batteries', True),
            ('When a battery stores too much charge and becomes permanently swollen', False),
            ('A feature where the battery learns your usage patterns to extend life', False),
        ]
    },
    {
        'text': 'Which of the following correctly describes the SO-DIMM memory module used in laptops?',
        'domain': 'Laptops',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'SO-DIMM stands for Small Outline Dual In-line Memory Module. It is physically smaller than the standard DIMM used in desktops making it suitable for the compact space inside laptops.',
        'choices': [
            ('Standard Output Dual In-line Memory Module — same size as desktop RAM but with different pins', False),
            ('Small Outline Dual In-line Memory Module — a smaller form factor than desktop DIMMs designed specifically for use in laptops and compact devices', True),
            ('Solid Online DIMM — a type of non-volatile memory that retains data without power', False),
            ('System Optimized DIMM — RAM that runs at higher speeds than standard desktop memory', False),
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