from app import app, db
from models import Question, Choice

questions_data = [

    # Q1 - Wi-Fi frequency range
    {
        'text': 'Which Wi-Fi frequency band offers better range through walls and obstacles?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '2.4 GHz has longer wavelengths that penetrate walls and obstacles better than 5 GHz or 6 GHz. The trade-off is that 2.4 GHz is slower and more congested.',
        'choices': [
            ('5 GHz', False),
            ('6 GHz', False),
            ('2.4 GHz', True),
            ('60 GHz', False),
        ]
    },

    # Q2 - LTE
    {
        'text': 'What does LTE stand for in mobile networking?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'LTE stands for Long-Term Evolution. It is a standard for 4G wireless broadband communication used by mobile devices.',
        'choices': [
            ('Long-Term Evolution', True),
            ('Low-Traffic Ethernet', False),
            ('Latency Transfer Extension', False),
            ('Local Transmission Endpoint', False),
        ]
    },

    # Q3 - Location services methods
    {
        'text': 'Which three methods are used by location services to determine a mobile device\'s position?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Location services use GPS for satellite-based positioning, Wi-Fi Positioning System (WPS) using nearby Wi-Fi networks, and cellular triangulation using signal strength from cell towers.',
        'choices': [
            ('GPS, Bluetooth, NFC', False),
            ('GPS, Wi-Fi Positioning, Cellular Triangulation', True),
            ('GPS, 5G, Satellite', False),
            ('Wi-Fi, NFC, Infrared', False),
        ]
    },

    # Q4 - Geofencing
    {
        'text': 'What is geofencing?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Geofencing sets a virtual perimeter on a map. When a device crosses that boundary notifications or actions can be triggered automatically — for example alerting a parent when a child leaves school.',
        'choices': [
            ('Encrypting a Wi-Fi network perimeter', False),
            ('Blocking apps from accessing location data', False),
            ('Setting a virtual perimeter on a map to trigger notifications if a device crosses it', True),
            ('A method of cellular triangulation', False),
        ]
    },

    # Q5 - MDM enrollment
    {
        'text': 'In Mobile Device Management (MDM), what is the first step before a device receives its configuration?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Enrollment is the first step in MDM. The device must be registered with the MDM system before any configuration policies or settings can be pushed to it.',
        'choices': [
            ('Installing antivirus software', False),
            ('Connecting to corporate Wi-Fi', False),
            ('Enrollment', True),
            ('Enabling two-factor authentication', False),
        ]
    },

    # Q6 - BYOD advantage
    {
        'text': 'What is a major advantage of BYOD (Bring Your Own Device) for organizations?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'BYOD reduces hardware costs for the organization because employees use their own devices. The trade-off is reduced control over device configuration and potential security risks.',
        'choices': [
            ('Full control over device configurations', False),
            ('Reduced hardware costs for the organization', True),
            ('Elimination of malware risk', False),
            ('Simplified compliance management', False),
        ]
    },

    # Q7 - BYOD risk NOT listed
    {
        'text': 'Which of the following is NOT a commonly listed risk of BYOD policies?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Higher hardware costs for employees is not a risk of BYOD — in fact employees bear the device cost. The actual risks include data leakage, malware from personal apps, and difficulty remotely wiping personal devices.',
        'choices': [
            ('Data leakage', False),
            ('Malware from personal apps', False),
            ('Inability to remote wipe personal devices', False),
            ('Higher hardware costs for employees', True),
        ]
    },

    # Q8 - Cloud synchronization
    {
        'text': 'What does cloud-based synchronization ensure across multiple devices?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Cloud-based synchronization ensures that data such as contacts emails photos and documents remains consistent and up-to-date across all of a user\'s devices.',
        'choices': [
            ('Faster CPU performance on all devices', False),
            ('Consistent up-to-date data across all devices', True),
            ('Reduced battery consumption on all devices', False),
            ('Automatic factory resets when issues occur', False),
        ]
    },

    # Q9 - Android Google Account Sync
    {
        'text': 'On Android, where do you configure Google Account Sync settings?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Google Account Sync settings are found under Settings > Google Account Sync on Android devices. This controls which data types are synced with your Google account.',
        'choices': [
            ('Settings > Connections', False),
            ('Settings > Google Account Sync', True),
            ('Settings > Developer Options', False),
            ('Settings > Security', False),
        ]
    },

    # Q10 - Android storage tool
    {
        'text': 'Which tool does Android offer to help optimize and manage storage on a device?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Files by Google is the built-in Android storage management tool. It helps identify and remove junk files duplicate photos and unused apps to free up storage space.',
        'choices': [
            ('iCloud', False),
            ('iTunes', False),
            ('Files by Google', True),
            ('OneDrive', False),
        ]
    },

    # Q11 - Battery charge range (already have 20-80 but adding with this exact phrasing)
    {
        'text': 'What is the recommended battery charge range to maintain optimal battery health on a mobile device?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Keeping battery charge between 20% and 80% is the recommended range for optimal lithium-ion battery health. Regularly charging to 100% or draining to 0% accelerates degradation.',
        'choices': [
            ('100% to 50%', False),
            ('90% to 10%', False),
            ('80% to 20%', True),
            ('60% to 5%', False),
        ]
    },

    # Q12 - Factory reset backup first
    {
        'text': 'Before performing a factory reset on a mobile device what is the most important step?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Backing up data is the most critical step before a factory reset. A factory reset erases all data on the device so without a backup all photos contacts and app data will be permanently lost.',
        'choices': [
            ('Disable Wi-Fi', False),
            ('Uninstall all apps', False),
            ('Back up your data', True),
            ('Update the operating system', False),
        ]
    },

    # Q13 - Re-enable after factory reset
    {
        'text': 'After a factory reset which setting should be re-enabled to help locate a lost device?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Find My Device (Android) or Find My iPhone (iOS) should be re-enabled after a factory reset. These services allow remote location locking and wiping of the device if it is lost or stolen.',
        'choices': [
            ('Bluetooth', False),
            ('NFC', False),
            ('Find My Device or Find My iPhone', True),
            ('Mobile data', False),
        ]
    },

    # Q14 - Local backup
    {
        'text': 'What type of backup stores data on an external drive rather than in the cloud?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A local backup stores data on a physical device such as an external hard drive or computer. This differs from cloud backup which stores data on remote servers.',
        'choices': [
            ('App-specific backup', False),
            ('Cloud backup', False),
            ('Local backup', True),
            ('MDM backup', False),
        ]
    },

    # Q15 - Redundant backups
    {
        'text': 'What does maintaining redundant backups mean?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Redundant backups means having more than one copy of your data stored in more than one location. This protects against data loss if one backup location fails or is destroyed.',
        'choices': [
            ('Backing up only the most recently changed files', False),
            ('Having more than one copy in more than one location', True),
            ('Deleting old backups regularly to save space', False),
            ('Synchronizing backups across apps', False),
        ]
    },

    # Q16 - BitLocker for local backup
    {
        'text': 'Which encryption tool can be used to protect a locally stored backup on a Windows computer?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'BitLocker is the Windows built-in encryption tool that can encrypt drives including those containing local backups. FileVault is the macOS equivalent and iCloud Keychain is for password storage.',
        'choices': [
            ('FileVault', False),
            ('iCloud Keychain', False),
            ('BitLocker', True),
            ('Google Play Protect', False),
        ]
    },

    # Q17 - iPhones more secure against malware
    {
        'text': 'What is a key reason iPhones are considered more secure against malware compared to Android devices?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'iOS only allows app installation from the Apple App Store (formerly iTunes Store) where apps are vetted by Apple. This closed ecosystem significantly reduces malware risk compared to Android which can allow sideloading.',
        'choices': [
            ('iPhones have more RAM than Android devices', False),
            ('Apps can only be installed from the Apple App Store', True),
            ('iPhones do not support Wi-Fi connections', False),
            ('iOS uses blockchain-based security', False),
        ]
    },

    # Q18 - Signs of malware infection
    {
        'text': 'Which of the following is a sign that a mobile device may be infected with malware?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Unusual battery drain and excessive background data usage are common signs of malware as malicious software often runs continuously in the background consuming power and sending data.',
        'choices': [
            ('Faster battery charging than usual', False),
            ('Increased screen brightness automatically', False),
            ('Unusual battery drain and excessive background data usage', True),
            ('Improved app load times', False),
        ]
    },

    # Q19 - Mobile overheating reason
    {
        'text': 'What is the main reason mobile devices are more prone to overheating compared to desktop computers?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Mobile devices have minimal ventilation because all components are packed into a very small space. Unlike desktops which have fans and airflow space mobile devices rely on passive cooling in a cramped enclosure.',
        'choices': [
            ('They use more powerful processors than desktops', False),
            ('They have minimal ventilation with everything packed into a small space', True),
            ('They rely on cellular connections that generate heat', False),
            ('They run more background processes than desktops by default', False),
        ]
    },

    # Q20 - Zero trust mobile
    {
        'text': 'What does zero trust security mean in the context of mobile devices?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Zero trust means nothing is automatically trusted — every access request requires continuous verification regardless of whether it comes from inside or outside the network.',
        'choices': [
            ('Disabling all network connections by default', False),
            ('Using only cloud-based apps', False),
            ('Continuous verification for all access — nothing is assumed trusted', True),
            ('Blocking all third-party applications', False),
        ]
    },

    # Q21 - 4G vs 5G
    {
        'text': 'What is the primary difference between 4G and 5G cellular networks?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '5G offers significantly lower latency higher speeds and improved reliability compared to 4G. Both support voice and data — 5G does not remove voice call support.',
        'choices': [
            ('5G only works indoors', False),
            ('4G supports voice calls while 5G does not', False),
            ('5G offers lower latency higher speeds and improved reliability', True),
            ('4G uses higher radio frequencies than 5G', False),
        ]
    },

    # Q22 - WPS location
    {
        'text': 'What is WPS in the context of mobile device location services?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'WPS stands for Wi-Fi Positioning System. It uses the public IP address and signal strength of nearby Wi-Fi sources to help determine a device\'s location even without GPS.',
        'choices': [
            ('Wireless Power Standard — for wireless charging', False),
            ('Wi-Fi Positioning System — uses nearby Wi-Fi sources to determine location', True),
            ('Wide-area Positioning Sensor — a satellite-based system', False),
            ('Wireless Protocol Standard — for network communications', False),
        ]
    },

    # Q23 - MDM lost or stolen device
    {
        'text': 'What does MDM allow administrators to do if a corporate device is lost or stolen?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'MDM allows administrators to remotely lock or wipe a lost or stolen device to prevent unauthorized access to corporate data.',
        'choices': [
            ('Automatically replace the device', False),
            ('Notify local authorities directly', False),
            ('Remotely lock or wipe the device', True),
            ('Transfer data to a new device automatically', False),
        ]
    },

    # Q24 - MDM enforce secure Wi-Fi
    {
        'text': 'What is one way MDM can enforce secure Wi-Fi usage on corporate devices?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'MDM can restrict devices to only connect to trusted corporate Wi-Fi networks preventing employees from using potentially insecure public hotspots with corporate devices.',
        'choices': [
            ('Disabling all Wi-Fi permanently on the device', False),
            ('Restricting connections to trusted networks only', True),
            ('Requiring users to manually enter credentials each time', False),
            ('Limiting Wi-Fi to 2.4 GHz band only', False),
        ]
    },

    # Q25 - Lite app version
    {
        'text': 'What is a "lite" version of a mobile app known for?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Lite versions of apps are designed to consume fewer system resources including storage RAM and battery. They are useful on devices with limited hardware or storage.',
        'choices': [
            ('Having more features than the full version', False),
            ('Being available only on iOS', False),
            ('Consuming fewer system resources', True),
            ('Requiring a paid subscription', False),
        ]
    },

    # Q26 - Memory leaks fix
    {
        'text': 'Which of the following actions helps resolve memory leaks on a mobile device?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Restarting the device periodically clears RAM and stops any processes that may have memory leaks — where an app consumes increasing memory without releasing it.',
        'choices': [
            ('Enabling NFC', False),
            ('Clearing the app store cache', False),
            ('Restarting the device periodically', True),
            ('Disabling location services', False),
        ]
    },

    # Q27 - VPN protection
    {
        'text': 'What does a VPN do to protect a mobile device user?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A VPN encrypts all traffic between the device and the VPN server. This protects data from being intercepted especially on public or unsecured Wi-Fi networks.',
        'choices': [
            ('Blocks all incoming calls', False),
            ('Encrypts all traffic between the device and the VPN server', True),
            ('Prevents apps from accessing the camera', False),
            ('Disables cellular data automatically', False),
        ]
    },

    # Q28 - Jailbreaking definition
    {
        'text': 'What is jailbreaking a mobile device?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Jailbreaking removes the manufacturer\'s software restrictions allowing apps to be installed from any source outside the official app store. This increases malware risk significantly.',
        'choices': [
            ('Enabling two-factor authentication', False),
            ('Forcing a factory reset remotely', False),
            ('Removing software restrictions to allow app installation from any source', True),
            ('Enrolling a device into an MDM system', False),
        ]
    },

    # Q29 - Phishing attack purpose
    {
        'text': 'What is a phishing attack typically designed to do?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Phishing attacks trick users into revealing credentials such as usernames and passwords by impersonating legitimate services through fake emails websites or messages.',
        'choices': [
            ('Overload a device\'s CPU', False),
            ('Corrupt cloud backups', False),
            ('Trick users into revealing their credentials', True),
            ('Disable the device\'s Wi-Fi connection', False),
        ]
    },

    # Q30 - Factory reset as last resort
    {
        'text': 'When should a factory reset be considered a last resort rather than a first troubleshooting step?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A factory reset should be a last resort when there are only minor issues that could be resolved by simpler steps like clearing caches rebooting or uninstalling recent apps since it erases all data.',
        'choices': [
            ('When the device is being sold', False),
            ('When there are minor issues that could be resolved by clearing caches rebooting or uninstalling recent apps', True),
            ('When the device has malware', False),
            ('When the operating system needs updating', False),
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