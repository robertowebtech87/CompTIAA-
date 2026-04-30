import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app import app, db
from models import Question, Choice

questions_data = [

    # ── LCD DISPLAY TYPES: IPS, TN, VA ───────────────────────────────────────

    {
        'text': 'What does IPS stand for in display technology and what is its main advantage?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'IPS stands for In-Plane Switching. Its main advantage is excellent colour accuracy and wide viewing angles — the image looks consistent even when viewed from the side.',
        'choices': [
            ('Integrated Panel Screen — offers the highest refresh rate', False),
            ('In-Plane Switching — excellent colour accuracy and wide viewing angles', True),
            ('Internal Pixel System — lowest power consumption', False),
            ('In-Phase Scanning — best contrast ratio', False),
        ]
    },
    {
        'text': 'What does TN stand for in display technology and what is its main advantage?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'TN stands for Twisted Nematic. Its main advantage is the fastest response times and highest refresh rates making it popular for gaming. The trade-off is poor viewing angles and colour accuracy.',
        'choices': [
            ('True Neon — brightest display technology', False),
            ('Twisted Nematic — fastest response times and refresh rates ideal for gaming', True),
            ('Total Neutrality — most energy-efficient panel type', False),
            ('Thin Nano — thinnest display technology available', False),
        ]
    },
    {
        'text': 'What does VA stand for in display technology and what is it best known for?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'VA stands for Vertical Alignment. It is best known for the highest contrast ratios of all LCD types producing deeper blacks than IPS or TN. It sits between IPS and TN in terms of viewing angles and response time.',
        'choices': [
            ('Variable Aperture — adjusts brightness automatically', False),
            ('Vertical Alignment — highest contrast ratios and deepest blacks among LCD types', True),
            ('Visual Acuity — sharpest pixel density', False),
            ('Variable Array — most flexible display for curved screens', False),
        ]
    },
    {
        'text': 'A graphic designer needs a laptop with the most accurate colour reproduction. Which LCD panel type should they choose?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'IPS panels offer the best colour accuracy and widest viewing angles making them ideal for creative professionals like graphic designers photographers and video editors.',
        'choices': [
            ('TN — fastest panel for accurate real-time editing', False),
            ('VA — highest contrast makes colours appear most vivid', False),
            ('IPS — best colour accuracy and wide viewing angles', True),
            ('OLED — only available in desktop monitors', False),
        ]
    },
    {
        'text': 'A competitive gamer needs the fastest possible display response time. Which LCD panel type is most suitable?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'TN (Twisted Nematic) panels have the fastest response times (as low as 1ms) and support the highest refresh rates making them the choice for competitive gaming where speed matters most.',
        'choices': [
            ('IPS — best colours for seeing game details clearly', False),
            ('VA — highest contrast for dark game environments', False),
            ('TN — fastest response times and highest refresh rates', True),
            ('OLED — self-lit pixels respond instantly', False),
        ]
    },
    {
        'text': 'Which statement correctly compares IPS TN and VA display panels?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'TN is fastest but worst colours and viewing angles. IPS has best colours and viewing angles but moderate speed. VA has best contrast/blacks but slowest response. Each panel type involves trade-offs.',
        'choices': [
            ('TN has the best colour accuracy IPS is the fastest and VA has the worst contrast', False),
            ('TN is fastest with worst colours IPS has best colours and angles VA has best contrast with slower response', True),
            ('All three panel types have identical image quality — only price differs', False),
            ('VA panels are always superior to both TN and IPS in every category', False),
        ]
    },
    {
        'text': 'Which TWO statements about LCD display types are correct? (Select TWO)',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'IPS offers the best viewing angles among LCD types making it ideal for professional use. TN has the fastest response time making it popular for gaming.',
        'choices': [
            ('IPS offers the best viewing angles among LCD panel types', True),
            ('VA panels have the fastest response times of all LCD types', False),
            ('TN panels have the fastest response times making them popular for gaming', True),
            ('All LCD types produce identical black levels', False),
        ]
    },

    # ── MICROSOFT 365 SYNC ────────────────────────────────────────────────────

    {
        'text': 'What does Microsoft 365 synchronise across a user\'s devices?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Microsoft 365 synchronises email (Outlook) contacts calendar OneDrive files and Office application settings across all devices signed in with the same Microsoft account.',
        'choices': [
            ('Only Word and Excel documents', False),
            ('Email contacts calendar OneDrive files and Office settings across all signed-in devices', True),
            ('Only the user\'s Wi-Fi passwords', False),
            ('Only OneDrive photo storage', False),
        ]
    },
    {
        'text': 'How does a user set up Microsoft 365 on a mobile device for email and calendar sync?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'To sync Microsoft 365 on a mobile device the user signs in with their Microsoft account credentials in the device account settings or Outlook app. This enables email calendar and contacts to sync automatically.',
        'choices': [
            ('Install any email app and configure it with POP3 settings', False),
            ('Sign in with Microsoft account credentials which enables email calendar and contacts sync', True),
            ('Only available on Windows mobile devices', False),
            ('Requires a separate MDM application to be installed first', False),
        ]
    },

    # ── GOOGLE WORKSPACE SYNC ─────────────────────────────────────────────────

    {
        'text': 'What data does Google Workspace synchronise across a user\'s devices?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Google Workspace syncs Gmail contacts Google Calendar Google Drive files and Google Docs Sheets and Slides across all devices signed into the same Google account.',
        'choices': [
            ('Only Google Chrome bookmarks and passwords', False),
            ('Gmail contacts Google Calendar and Google Drive files across signed-in devices', True),
            ('Only YouTube watch history and playlists', False),
            ('Only Android app purchases', False),
        ]
    },
    {
        'text': 'A new employee needs to access corporate Gmail calendar and Drive on their phone. What should the IT technician configure?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Adding the corporate Google Workspace (formerly G Suite) account to the device\'s account settings will automatically sync Gmail contacts calendar and Drive files to the phone.',
        'choices': [
            ('Install Gmail only and configure it with IMAP settings', False),
            ('Add the corporate Google Workspace account to device account settings to sync Gmail calendar contacts and Drive', True),
            ('Configure a VPN then access everything through a browser only', False),
            ('Install each Google app separately and log in individually to each one', False),
        ]
    },

    # ── ICLOUD SYNC ───────────────────────────────────────────────────────────

    {
        'text': 'What data does iCloud synchronise across Apple devices?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'iCloud syncs photos mail contacts calendar notes reminders iMessages app data and device settings across all Apple devices signed into the same Apple ID.',
        'choices': [
            ('Only Apple Music and podcast subscriptions', False),
            ('Photos mail contacts calendar notes reminders and app data across Apple devices with the same Apple ID', True),
            ('Only iMessages and FaceTime history', False),
            ('Only App Store purchases and downloads', False),
        ]
    },
    {
        'text': 'A user gets a new iPhone and wants their photos contacts and calendar from their old iPhone to appear automatically. What service handles this?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'iCloud automatically syncs photos contacts and calendar across Apple devices using the same Apple ID. As long as iCloud backup and sync is enabled on both devices the data transfers automatically.',
        'choices': [
            ('iTunes backup and manual restore', False),
            ('iCloud — automatically syncs photos contacts and calendar across devices with the same Apple ID', True),
            ('AirDrop transfers all data between iPhones directly', False),
            ('Google Photos handles iPhone photo sync automatically', False),
        ]
    },

    # ── DATA CAPS ─────────────────────────────────────────────────────────────

    {
        'text': 'What is a mobile data cap and how does it affect device usage?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A data cap is a limit on the amount of cellular data a plan allows per billing cycle. When reached the carrier may throttle speeds charge overage fees or stop data service until the next cycle.',
        'choices': [
            ('A limit on how many apps can be installed on a device', False),
            ('A carrier-set limit on cellular data usage per billing cycle — exceeding it causes throttling or extra charges', True),
            ('A physical restriction preventing data from being deleted', False),
            ('A security feature that caps the speed of untrusted apps', False),
        ]
    },
    {
        'text': 'How can a technician help a user avoid exceeding their mobile data cap?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'To avoid exceeding a data cap: enable Wi-Fi whenever possible restrict background app data set data usage warnings in device settings and configure large downloads (updates) to occur on Wi-Fi only.',
        'choices': [
            ('Disable all wireless connectivity when not actively using the phone', False),
            ('Enable Wi-Fi when available restrict background data set data warnings and configure updates for Wi-Fi only', True),
            ('Purchase a new SIM card with a different carrier', False),
            ('Factory reset the device to clear the data usage counter', False),
        ]
    },
    {
        'text': 'A user reports that their mobile internet has become extremely slow halfway through the month even though they have cellular signal. What is the most likely cause?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'This is a classic symptom of hitting a data cap. When the monthly data allowance is reached carriers typically throttle speeds to 2G-level rather than cutting service completely.',
        'choices': [
            ('The cellular tower in the area is damaged', False),
            ('The user has reached their monthly data cap and the carrier has throttled their speed', True),
            ('The phone\'s antenna is malfunctioning', False),
            ('Too many apps are running in the background', False),
        ]
    },
    {
        'text': 'Which TWO of the following correctly describe what happens when a mobile data cap is reached? (Select TWO)',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'When a data cap is reached carriers typically throttle speeds significantly (to 2G-level) and/or charge overage fees. The device does not lose Wi-Fi capability and the phone number remains active.',
        'choices': [
            ('The carrier may throttle data speeds significantly', True),
            ('The phone number becomes inactive until next billing cycle', False),
            ('The carrier may charge overage fees for additional data', True),
            ('Wi-Fi connectivity is also disabled automatically', False),
        ]
    },
    {
        'text': 'Which TWO settings help a mobile device user manage and monitor data cap usage? (Select TWO)',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Setting a data usage warning/limit in device settings alerts the user before they hit their cap. Enabling Wi-Fi preferred mode for downloads prevents large files from using cellular data.',
        'choices': [
            ('Setting a data usage warning or limit in device settings', True),
            ('Enabling airplane mode permanently', False),
            ('Configuring large downloads and updates to use Wi-Fi only', True),
            ('Disabling the device screen auto-lock', False),
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