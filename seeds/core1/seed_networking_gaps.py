import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app import app, db
from models import Question, Choice

questions_data = [

    # ── SSID / AP CONFIGURATION ───────────────────────────────────────────────

    {
        'text': 'What is an SSID and what are best practices when configuring one?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'An SSID (Service Set Identifier) is the name of a wireless network. Best practices include always changing the default SSID, setting a unique easy-to-identify name, and remembering that SSIDs are case-sensitive — "CompanyWiFi" is not the same as "companywifi".',
        'choices': [
            ('The password used to secure a wireless network', False),
            ('The name of a wireless network — should be changed from default and is case-sensitive', True),
            ('The wireless channel number assigned to an access point', False),
            ('The MAC address broadcast by a wireless access point', False),
        ]
    },
    {
        'text': 'When configuring a new wireless access point what FOUR settings should always be changed from defaults? (Select THREE)',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': True,
        'explanation': 'When setting up a new access point you should always change the default SSID to a unique name, assign a static IP address for administration, and change the default administrator username and password. Leaving defaults makes the AP easy to attack.',
        'choices': [
            ('Change the default SSID to a unique name', True),
            ('Assign a static IP address for administration', True),
            ('Change the default administrator username and password', True),
            ('Disable the antenna to reduce signal range', False),
        ]
    },
    {
        'text': 'Which wireless channels should a 2.4GHz access point use to minimise interference?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'The 2.4GHz band has 11 channels but only channels 1, 6, and 11 are non-overlapping. Using only these three channels prevents co-channel interference between nearby access points. The 5GHz band has 24 non-overlapping channels so channel selection is less critical.',
        'choices': [
            ('Channels 2, 7, and 12', False),
            ('Channels 1, 6, and 11', True),
            ('Any channel from 1 to 11', False),
            ('Channels 3, 6, and 9', False),
        ]
    },

    # ── SIGNAL DEGRADATION ────────────────────────────────────────────────────

    {
        'text': 'What are the THREE main causes of wireless signal degradation?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': True,
        'explanation': 'Wireless signals degrade due to distance (all signals weaken with distance — 2.4GHz travels further than 5GHz), walls and barriers (especially metal pipes vents and thick reinforced walls), and interference from other wireless networks and high-voltage appliances.',
        'choices': [
            ('Distance from the access point', True),
            ('Walls and physical barriers especially metal and thick walls', True),
            ('Interference from other wireless devices and appliances', True),
            ('The color of the access point enclosure', False),
        ]
    },
    {
        'text': 'Which household appliances can cause interference with 2.4GHz Wi-Fi networks?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'Microwaves toaster ovens HVAC systems and other high-voltage appliances can cause interference with 2.4GHz Wi-Fi because they operate on similar frequencies. This is one reason 5GHz is often preferred — it has much less interference from household devices.',
        'choices': [
            ('LED light bulbs and phone chargers', False),
            ('Microwaves toaster ovens and HVAC systems', True),
            ('Televisions and computer monitors', False),
            ('USB hubs and wired keyboards', False),
        ]
    },

    # ── IoT PROTOCOLS ─────────────────────────────────────────────────────────

    {
        'text': 'Which wireless protocols can IoT devices use to communicate? (Select THREE)',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': True,
        'explanation': 'IoT devices can use many wireless protocols including Z-Wave and Zigbee (designed specifically for smart home automation with low power), Bluetooth (short range device pairing), NFC (very short range), IR (infrared remote control), RFID (tracking), and 802.11 (Wi-Fi).',
        'choices': [
            ('Z-Wave and Zigbee', True),
            ('Bluetooth and NFC', True),
            ('802.11 (Wi-Fi)', True),
            ('DSL and DOCSIS', False),
        ]
    },
    {
        'text': 'What are Z-Wave and Zigbee primarily used for in IoT environments?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'Z-Wave and Zigbee are wireless protocols designed specifically for smart home and IoT automation. They use low power, operate on different frequencies than Wi-Fi (reducing interference), and are used in devices like smart lights, thermostats, door locks and sensors.',
        'choices': [
            ('High-speed data transfer between computers', False),
            ('Low-power smart home and IoT automation devices like lights thermostats and sensors', True),
            ('Long-range outdoor wireless internet access', False),
            ('Secure encrypted communication between enterprise servers', False),
        ]
    },

    # ── DNS HOSTNAME / FQDN ───────────────────────────────────────────────────

    {
        'text': 'What is the difference between a hostname, domain name, and FQDN?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'A hostname identifies a specific device (e.g. workstation01). A domain name identifies a specific network (e.g. companyx.lan). An FQDN (Fully Qualified Domain Name) combines both to uniquely identify a device on a specific network (e.g. workstation01.companyx.lan).',
        'choices': [
            ('They are all the same thing — just different terms for the same concept', False),
            ('Hostname = device name, Domain = network name, FQDN = hostname + domain combined', True),
            ('Hostname is for IPv6, domain is for IPv4, FQDN is for both', False),
            ('Domain name is assigned by DHCP, hostname and FQDN are assigned manually', False),
        ]
    },

    # ── VPN PROTOCOLS ─────────────────────────────────────────────────────────

    {
        'text': 'Which protocols can be used to create a VPN tunnel?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'VPNs can use various protocols including PPTP (older, less secure), L2TP (Layer 2 Tunneling Protocol), IPSec (IP Security — commonly paired with L2TP), OpenVPN (open-source, highly secure), and SSL-VPN (uses SSL/TLS, works through web browsers).',
        'choices': [
            ('Only HTTPS can be used for VPN connections', False),
            ('PPTP L2TP IPSec OpenVPN and SSL-VPN are all valid VPN protocols', True),
            ('VPNs only use SSH as their tunneling protocol', False),
            ('FTP and SFTP are the standard VPN protocols', False),
        ]
    },

    # ── NIC DETAILS ───────────────────────────────────────────────────────────

    {
        'text': 'What do the link light and activity light on a NIC indicate?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'The link light verifies the cable is plugged in at both ends and a physical connection exists. The activity light blinks as data passes through the interface. If the link light is off the cable is unplugged or faulty. Each NIC has a unique 48-bit MAC address.',
        'choices': [
            ('Link light shows internet speed, activity light shows Wi-Fi signal strength', False),
            ('Link light verifies cable connection at both ends, activity light blinks as data passes through', True),
            ('Both lights indicate the same thing — network activity', False),
            ('Link light shows power status, activity light shows IP address assignment', False),
        ]
    },

    # ── FIREWALL / DMZ ────────────────────────────────────────────────────────

    {
        'text': 'What is a DMZ in the context of a firewall?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'A DMZ (Demilitarized Zone) is a network segment that the firewall does not fully protect — it is intentionally exposed to the internet. Web servers email servers and other public-facing services are placed in the DMZ so internet users can reach them without accessing the internal LAN.',
        'choices': [
            ('A zone where all traffic is blocked by the firewall', False),
            ('A network segment intentionally exposed to the internet for public-facing services', True),
            ('The area between two firewalls where management traffic flows', False),
            ('A wireless zone with reduced security for guest devices', False),
        ]
    },

    # ── SOHO ROUTER ───────────────────────────────────────────────────────────

    {
        'text': 'What makes a SOHO router different from a standard router?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'A SOHO (Small Office Home Office) router is a multifunction device that combines routing, wireless access point, switch, firewall, and DHCP server all in one. It may also include content filtering, file server, print server, and VPN capabilities — making it a complete networking solution for small environments.',
        'choices': [
            ('A SOHO router only provides routing with no wireless capability', False),
            ('A SOHO router combines router switch wireless AP firewall and DHCP server all in one device', True),
            ('A SOHO router is only for home use and cannot connect to the internet', False),
            ('A SOHO router is identical to an enterprise router but smaller', False),
        ]
    },

    # ── CAN ───────────────────────────────────────────────────────────────────

    {
        'text': 'What is a CAN (Campus Area Network)?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'A CAN (Campus Area Network) spans a limited geographical area such as a college campus, corporate campus, or military base. It is larger than a LAN but smaller than a MAN. It is privately owned and managed by the organisation.',
        'choices': [
            ('A network connecting devices within a single room', False),
            ('A privately owned network spanning a limited area like a college or corporate campus', True),
            ('A network connecting multiple cities together', False),
            ('A wireless network using cellular towers across a country', False),
        ]
    },

    # ── SATELLITE INTERNET ────────────────────────────────────────────────────

    {
        'text': 'What is the main disadvantage of satellite internet and what services does it make unusable?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'Satellite internet suffers from high latency because signals must travel to space and back. This high latency makes it unsuitable for real-time services like VoIP calls, video streaming, and online gaming. It requires a satellite dish with a clear unobstructed view of the sky.',
        'choices': [
            ('Low bandwidth — cannot support multiple users simultaneously', False),
            ('High latency making it unsuitable for VoIP video streaming and online gaming', True),
            ('Only available in urban areas with clear weather', False),
            ('Requires a phone line making it unavailable in rural areas', False),
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
    networking = Question.query.filter_by(exam='core1', domain='Networking').count()
    print(f'Added {added} questions. Skipped {skipped} duplicates.')
    print(f'Networking: {networking} | Core 1: {core1} | Overall: {total}')