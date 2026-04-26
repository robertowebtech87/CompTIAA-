from app import app, db
from models import Question, Choice

questions_data = [

    # Q16
    {
        'text': 'What are mobile device connections used for beyond simply charging the battery?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Mobile device connections are used for connectivity, data synchronization, backing up the device, and verifying device ownership — not just charging.',
        'choices': [
            ('Only for charging and playing audio through speakers', False),
            ('Connectivity, data synchronization, backing up the device, and verifying device ownership', True),
            ('Only for charging and transferring photos', False),
            ('Connecting to external monitors and projectors only', False),
        ]
    },

    # Q17
    {
        'text': 'What are the older USB connector types commonly found on older mobile devices?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Mini USB and Micro USB (specifically mini-B and micro-B plugs) were popular on older mobile devices and some may still be found in use today.',
        'choices': [
            ('USB-A and USB-B', False),
            ('Mini USB and Micro USB (mini-B and micro-B)', True),
            ('USB-C and Thunderbolt', False),
            ('Lightning and USB-C', False),
        ]
    },

    # Q18
    {
        'text': 'What are the main characteristics that make USB-C stand out from older USB connectors?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'USB-C has 24 pins can be plugged in any orientation supports higher speeds and can carry different signal types including DisplayPort HDMI and Thunderbolt through the same physical connector.',
        'choices': [
            ('USB-C is smaller but only supports USB data — no video or power', False),
            ('USB-C has 24 pins works in any orientation supports higher speeds and carries DisplayPort HDMI and Thunderbolt signals through one connector', True),
            ('USB-C is identical to Micro USB but with a different color', False),
            ('USB-C only supports charging not data transfer', False),
        ]
    },

    # Q19
    {
        'text': 'What is the Lightning connector and which devices use it?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Lightning is a proprietary Apple connector with 8 pins. It was commonly used on older iPhone and iPad devices before Apple moved to USB-C.',
        'choices': [
            ('A universal connector with 24 pins used across all smartphones', False),
            ('A proprietary Apple connector with 8 pins used on older iPhones and iPads', True),
            ('A Google-developed connector used on Android tablets', False),
            ('A USB standard connector used on Windows laptops only', False),
        ]
    },

    # Q20
    {
        'text': 'What advantages did the Lightning connector introduce over older USB connections on mobile devices?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Lightning supports higher power output for faster charging can be inserted in either orientation without flipping and has a simple design that works across many Apple devices.',
        'choices': [
            ('It supports faster data transfer than USB-C', False),
            ('Higher power output for faster charging reversible insertion and a simple design across Apple devices', True),
            ('It works with all Android and Windows devices', False),
            ('It has more pins than USB-C providing more bandwidth', False),
        ]
    },

    # Q21
    {
        'text': 'What is the main challenge of supporting mobile devices from multiple different manufacturers?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Each manufacturer may use a different connector type meaning a technician may need to carry several different cables to support all devices. The industry is moving toward a universal USB-C standard.',
        'choices': [
            ('Different devices run different operating systems making apps incompatible', False),
            ('Each manufacturer may use a different connector requiring multiple cables — the industry is moving toward USB-C as a universal standard', True),
            ('Different devices have different screen sizes making cases incompatible', False),
            ('Battery capacities vary making power banks unreliable across devices', False),
        ]
    },

    # Q22
    {
        'text': 'What are the common uses of NFC on mobile devices?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'NFC is commonly used for contactless payments at point-of-sale terminals identification and access control through doors and transferring information between phones.',
        'choices': [
            ('Only for wireless charging of mobile devices', False),
            ('Contactless payments access control through doors and transferring information between phones', True),
            ('High-speed file transfers between devices on the same Wi-Fi network', False),
            ('Connecting Bluetooth headphones without a pairing process', False),
        ]
    },

    # Q23
    {
        'text': 'How can NFC be used as an access control solution in organizations?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Organizations can place NFC sensors on walls allowing employees to use their phone or smartwatch to authenticate and gain access — replacing the need to carry a separate ID or access card.',
        'choices': [
            ('By scanning QR codes displayed on employee badges', False),
            ('By placing NFC sensors on walls allowing employees to use their phone or smartwatch for access instead of a separate ID card', True),
            ('By connecting employee devices to a central Bluetooth hub', False),
            ('By requiring employees to enter a PIN on their phone at each door', False),
        ]
    },

    # Q24
    {
        'text': 'What type of network does Bluetooth create and what is it designed for?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Bluetooth creates a Personal Area Network (PAN) designed for personal use such as connecting wireless headphones headsets keyboards and mice to a mobile device over short distances.',
        'choices': [
            ('A Wide Area Network (WAN) for internet access across cities', False),
            ('A Personal Area Network (PAN) designed for personal use connecting devices over short distances', True),
            ('A Local Area Network (LAN) for sharing files in an office', False),
            ('A Metropolitan Area Network (MAN) for connecting buildings', False),
        ]
    },

    # Q25
    {
        'text': 'What is the difference between a mobile hotspot and tethering?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A hotspot allows multiple devices to connect to the phone for internet access. Tethering is when only one single device connects. Both depend on the phone\'s software and the mobile carrier\'s plan.',
        'choices': [
            ('They are identical features with different names', False),
            ('A hotspot allows multiple devices to connect while tethering only allows one device to connect', True),
            ('A hotspot uses Wi-Fi while tethering uses Bluetooth only', False),
            ('Tethering is faster than a hotspot because it uses a direct cable connection only', False),
        ]
    },

    # Q26
    {
        'text': 'What should you do before using hotspot or tethering functionality on your phone?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'You should contact your mobile provider to confirm whether hotspot functionality is available and supported on your plan as it may not be included or may have data limits.',
        'choices': [
            ('Enable airplane mode first then turn on the hotspot', False),
            ('Contact your mobile provider to confirm hotspot is available and supported on your plan', True),
            ('Disable Wi-Fi before enabling the hotspot feature', False),
            ('Update the phone firmware before enabling tethering', False),
        ]
    },

    # Q27
    {
        'text': 'What is a stylus and how does it typically connect to a mobile device?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A stylus is a pen-like input device for precise control on a touchscreen. It usually connects via Bluetooth and often supports pressure sensitivity and programmable buttons.',
        'choices': [
            ('A stylus is a physical keyboard that connects via USB', False),
            ('A pen-like input device for precise touchscreen control that connects via Bluetooth and supports pressure sensitivity and programmable buttons', True),
            ('A stylus is a drawing tool that only works on resistive touchscreens', False),
            ('A voice input device that connects via the headphone jack', False),
        ]
    },

    # Q28
    {
        'text': 'Why is compatibility important when choosing a stylus for a mobile device?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Not all styluses work with all devices. For example an Apple tablet requires the Apple Pencil or a compatible stylus for the full range of features. Using the correct stylus ensures the best connection and functionality.',
        'choices': [
            ('All styluses work with all touchscreens so compatibility does not matter', False),
            ('Not all styluses work with all devices — an Apple tablet for example requires the Apple Pencil or compatible stylus for full features', True),
            ('Compatibility only matters for wireless styluses not wired ones', False),
            ('Stylus compatibility only affects charging speed not functionality', False),
        ]
    },

    # Q29
    {
        'text': 'What are the three connection types available for wired headsets on mobile devices?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Wired headsets for mobile devices can connect via USB the analog TRRS connector (3.5mm audio jack) or Lightning on older Apple iPhone models.',
        'choices': [
            ('RJ45 HDMI and DisplayPort', False),
            ('USB the analog TRRS 3.5mm jack and Lightning for older Apple devices', True),
            ('USB-C Micro USB and Mini USB only', False),
            ('Bluetooth Wi-Fi and NFC', False),
        ]
    },

    # Q30
    {
        'text': 'What does TRRS stand for and what does each part of the connector represent?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'TRRS stands for Tip-Ring-Ring-Sleeve. The tip is at the end the sleeve is at the back and the two rings in the middle carry separate audio signals typically left audio and microphone.',
        'choices': [
            ('Transfer-Rate-Receive-Signal — used for data transfer', False),
            ('Tip-Ring-Ring-Sleeve — tip at the end sleeve at the back two rings carrying left audio and microphone signals', True),
            ('Transistor-Resistor-Relay-Switch — an electronic standard', False),
            ('Transmit-Receive-Ring-Signal — a network connector standard', False),
        ]
    },

    # Q31
    {
        'text': 'What is a potential drawback of using wireless Bluetooth headsets throughout a full work day?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'The battery in wireless Bluetooth headsets may run out after extended use requiring the user to switch to a wired headset to continue using it.',
        'choices': [
            ('Bluetooth headsets can overheat and cause burns after prolonged use', False),
            ('The battery may run out after extended use requiring a switch to a wired headset', True),
            ('Bluetooth interference causes hearing damage over long sessions', False),
            ('Wireless headsets lose their pairing after 4 hours of continuous use', False),
        ]
    },

    # Q32
    {
        'text': 'How do external wireless speakers connect to a mobile device and what advantage do they offer?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'External wireless speakers connect via Bluetooth and provide better sound quality and fidelity than the built-in speakers of a phone while remaining portable and battery powered.',
        'choices': [
            ('Via NFC — they offer lower latency than Bluetooth speakers', False),
            ('Via Bluetooth — they provide better sound quality than built-in phone speakers while remaining portable', True),
            ('Via Wi-Fi — they offer unlimited range compared to Bluetooth', False),
            ('Via USB — they draw power from the phone without needing their own battery', False),
        ]
    },

    # Q33
    {
        'text': 'What problem does a docking station solve for laptop users in an office environment?',
        'domain': 'Laptops',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A docking station allows a laptop to connect and disconnect from all desk peripherals (monitor keyboard mouse network) in one single step without touching individual cables.',
        'choices': [
            ('It upgrades the laptop RAM and storage automatically', False),
            ('It allows the laptop to connect and disconnect from all desk peripherals in one step without touching individual cables', True),
            ('It provides a backup battery when the laptop battery fails', False),
            ('It allows the laptop to run cooler by providing external ventilation', False),
        ]
    },

    # Q34
    {
        'text': 'What is the key difference between a docking station and a port replicator?',
        'domain': 'Laptops',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A docking station is device-specific and may support full-size adapter cards. A port replicator is more portable connects via USB works with almost any laptop and does not support additional adapter cards.',
        'choices': [
            ('A docking station is wireless while a port replicator uses cables', False),
            ('A docking station is device-specific and supports adapter cards while a port replicator is portable universal via USB and does not support adapter cards', True),
            ('Port replicators are more expensive than docking stations', False),
            ('Docking stations only work with Windows laptops while port replicators work with all systems', False),
        ]
    },

    # Q35
    {
        'text': 'What is a trackpad and what advantage does it have over a traditional mouse?',
        'domain': 'Laptops',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A trackpad is a touch-sensitive surface that replaces the mouse. It supports multi-finger gestures such as pinching to zoom which are difficult to replicate with a traditional mouse.',
        'choices': [
            ('A trackpad is a pressure-sensitive drawing surface for artists only', False),
            ('A touch-sensitive surface that replaces the mouse and supports multi-finger gestures like pinching to zoom', True),
            ('A trackpad is a small external keyboard for shortcut keys', False),
            ('A trackpad is identical to a mouse but without physical buttons', False),
        ]
    },

    # Q36
    {
        'text': 'How can you disable the trackpad on a laptop and why might that be useful?',
        'domain': 'Laptops',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'On many laptops a function key combination such as Fn+F10 can enable or disable the trackpad. This is useful to prevent accidental cursor movement or clicks while typing.',
        'choices': [
            ('Remove the trackpad physically — useful when replacing it with a mouse', False),
            ('Use a function key combination such as Fn+F10 — useful to prevent accidental clicks while typing', True),
            ('Disable it in Device Manager — useful for security purposes', False),
            ('Cover it with tape — the only reliable way to prevent accidental input', False),
        ]
    },

    # Q37
    {
        'text': 'What is a drawing pad and how does it differ from a regular trackpad?',
        'domain': 'Laptops',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A drawing pad is an external digitizer with its own stylus providing precise input for artistic or detailed work. It connects via Bluetooth or USB and differs from a trackpad which is mainly for cursor navigation.',
        'choices': [
            ('A drawing pad is identical to a trackpad but with a stylus included', False),
            ('An external digitizer with its own stylus for precise artistic input connecting via Bluetooth or USB unlike a trackpad which is mainly for cursor navigation', True),
            ('A drawing pad is a touchscreen display for viewing artwork', False),
            ('A drawing pad is a pressure-sensitive keyboard for graphic designers', False),
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