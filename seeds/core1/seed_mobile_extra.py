import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app import app, db
from models import Question, Choice

questions_data = [

    {
        'text': 'What allows a mobile phone to make and receive calls over a Wi-Fi network instead of a cellular network?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Wi-Fi calling allows a phone to route voice calls over a Wi-Fi network instead of cellular. This is useful in areas with poor cellular signal but good Wi-Fi coverage.',
        'choices': [
            ('Bluetooth tethering', False),
            ('Wi-Fi calling', True),
            ('NFC pairing', False),
            ('Hotspot mode', False),
        ]
    },
    {
        'text': 'How does 5G technology specifically benefit Internet of Things (IoT) devices?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '5G allows IoT devices to send large amounts of data instantly without bandwidth constraints. Its low latency and high capacity make it ideal for connecting thousands of IoT devices simultaneously.',
        'choices': [
            ('It reduces the number of devices that can connect simultaneously', False),
            ('It allows IoT devices to send large amounts of data instantly without bandwidth constraints', True),
            ('It replaces the need for Wi-Fi in IoT devices entirely', False),
            ('It limits IoT devices to voice communication only', False),
        ]
    },
    {
        'text': 'What does EDGE stand for in the context of cellular networks?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'EDGE stands for Enhanced Data Rates for GSM Evolution. It is a 2.75G technology that improved data speeds over standard GPRS on GSM networks before 3G became widespread.',
        'choices': [
            ('Extended Data Gateway Environment', False),
            ('Enhanced Data Rates for GSM Evolution', True),
            ('Encrypted Digital GSM Exchange', False),
            ('Extended Device Global Enablement', False),
        ]
    },
    {
        'text': 'What is the maximum throughput of standard LTE (4G)?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Standard LTE (4G) has a maximum theoretical throughput of 150 Mbps. LTE-Advanced can reach higher speeds but the base LTE standard tops at 150 Mbps.',
        'choices': [
            ('50 Mbps', False),
            ('100 Mbps', False),
            ('150 Mbps', True),
            ('300 Mbps', False),
        ]
    },
    {
        'text': 'What does airplane mode do on a mobile device?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Airplane mode disables all wireless communications on the device including cellular Wi-Fi Bluetooth and NFC. This is required during flights to prevent interference with aircraft systems.',
        'choices': [
            ('Disables only cellular data', False),
            ('Disables only Wi-Fi and Bluetooth', False),
            ('Disables all wireless communications on the device', True),
            ('Enables GPS while disabling data connections', False),
        ]
    },
    {
        'text': 'What is the purpose of creating a partitioned area on a personal device in a BYOD environment?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'In a BYOD environment a partitioned or containerized area separates personal private data from corporate data on the same device. This protects company data without affecting personal content.',
        'choices': [
            ('To speed up the device processor', False),
            ('To separate personal private data from corporate data on the same phone', True),
            ('To allow two users to share the same device', False),
            ('To create a backup of the operating system', False),
        ]
    },
    {
        'text': 'Which of the following can an administrator disable directly from the MDM Restrictions tab?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'From the MDM Restrictions tab administrators can disable device features such as the camera FaceTime Siri and voice dialing to enforce corporate security and usage policies.',
        'choices': [
            ('The device physical SIM card', False),
            ('The device battery charging speed', False),
            ('Camera FaceTime Siri and voice dialing', True),
            ('The device screen resolution', False),
        ]
    },
    {
        'text': 'What unique device identifier can be found listed in an MDM console?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'The IMEI (International Mobile Equipment Identity) is a unique identifier for mobile devices that is listed in MDM consoles. It is used to identify and track specific devices.',
        'choices': [
            ('SIM PIN', False),
            ('Bluetooth MAC address', False),
            ('IMEI', True),
            ('USB serial number', False),
        ]
    },
    {
        'text': 'In MDM synchronization settings what data types can an administrator choose to sync selectively?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'MDM sync settings allow administrators to selectively sync calendar contacts mail reminders and notes. This gives fine-grained control over what corporate data is synchronized to enrolled devices.',
        'choices': [
            ('Only email and photos', False),
            ('Only app installations', False),
            ('Calendar contacts mail reminders and notes', True),
            ('Only documents and videos', False),
        ]
    },
    {
        'text': 'What restriction can an MDM administrator set regarding automatic app downloads over cellular data?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'MDM administrators can control whether automatic downloads are allowed over cellular data and can set limits on the size of apps that can be downloaded over the mobile network to control data usage.',
        'choices': [
            ('Block all app usage on cellular', False),
            ('Limit which app store the user accesses', False),
            ('Control whether automatic downloads are allowed and what size apps can be downloaded over the mobile network', True),
            ('Prevent users from opening apps while on cellular', False),
        ]
    },
    {
        'text': 'During Bluetooth pairing what is typically used to verify and confirm the connection between two devices?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'During Bluetooth pairing a PIN (Personal Identification Number) is typically used to verify and confirm the connection. Both devices must agree on the PIN to establish the trusted link.',
        'choices': [
            ('A Wi-Fi password', False),
            ('A personal identification number (PIN)', True),
            ('An NFC tap', False),
            ('A QR code scan', False),
        ]
    },
    {
        'text': 'After the initial Bluetooth pairing is complete what happens the next time you connect to the same device?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'After initial pairing both devices store the link key. The next time they are within range they automatically reconnect without needing to repeat the pairing process.',
        'choices': [
            ('You must repeat the full pairing process each time', False),
            ('The device automatically reconnects without needing to go through pairing again', True),
            ('You must re-enter the PIN every time', False),
            ('You need to put the device into discoverable mode again each time', False),
        ]
    },
    {
        'text': 'How do wireless speakers typically connect to a mobile device?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Wireless speakers connect to mobile devices via Bluetooth. They are paired once and then automatically reconnect when in range providing wire-free audio.',
        'choices': [
            ('USB-C', False),
            ('NFC', False),
            ('Lightning', False),
            ('Bluetooth', True),
        ]
    },
    {
        'text': 'How do external webcams and cameras typically connect to a desktop or laptop computer?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'External webcams and cameras typically connect via USB. USB provides both data transfer and power in a single connection making it the standard for external cameras.',
        'choices': [
            ('Bluetooth', False),
            ('NFC', False),
            ('USB', True),
            ('HDMI', False),
        ]
    },
    {
        'text': 'What must you verify before starting the Bluetooth pairing process on both devices?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Before pairing you must ensure Bluetooth is enabled on both devices and that both are set to discoverable mode so each device can find the other during the search process.',
        'choices': [
            ('That both devices are connected to the same Wi-Fi network', False),
            ('That Bluetooth is enabled and both devices are set to discoverable mode', True),
            ('That both devices have NFC turned off', False),
            ('That both devices are fully charged', False),
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