import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app import app, db
from models import Question, Choice

questions_data = [

    # ── TONE GENERATOR / INDUCTIVE PROBE ─────────────────────────────────────

    {
        'text': 'How does a tone generator and inductive probe work together to find a cable?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'The tone generator is connected to one end of the cable and puts an analog tone onto the wire. The inductive probe is then moved along cables at the other end — without touching the copper — until it picks up the tone through induction, identifying the correct cable.',
        'choices': [
            ('The tone generator sends a light signal and the probe detects it visually', False),
            ('The tone generator puts an analog tone on the wire and the inductive probe detects it without touching the copper', True),
            ('Both devices must be connected to the same switch port to work', False),
            ('The probe sends a signal back to the generator which displays the cable ID', False),
        ]
    },
    {
        'text': 'When using a tone generator and inductive probe, do you need to touch the copper wire to find the cable?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'No — the inductive probe works by induction meaning it detects the tone through the outer insulation of the cable without any physical contact with the copper inside. This makes it safe and usable on live cables.',
        'choices': [
            ('Yes — the probe must pierce the insulation to make copper contact', False),
            ('No — the inductive probe detects the tone through the cable insulation without touching the copper', True),
            ('Yes — but only at the connector end where copper is exposed', False),
            ('No — but you must remove the cable jacket first to get a reading', False),
        ]
    },

    # ── PoE DETAILS ──────────────────────────────────────────────────────────

    {
        'text': 'What are the two wattage options for PoE++ (802.3bt) and what introduced this standard?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'PoE++ (802.3bt) provides either 51 watts at 600mA or 71.3 watts at 960mA depending on switch capability. This standard was introduced with 10-Gigabit Ethernet running over copper cables and allows powering devices like laptops.',
        'choices': [
            ('15.4W and 30W — introduced with Gigabit Ethernet', False),
            ('51W at 600mA or 71.3W at 960mA — introduced with 10-Gigabit Ethernet over copper', True),
            ('100W flat — introduced with 40-Gigabit Ethernet', False),
            ('25.5W and 45W — introduced with Wi-Fi 6 deployments', False),
        ]
    },
    {
        'text': 'A device requires PoE++ power. Can it be powered by a PoE+ switch?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'No. PoE standards are downward compatible but not upward compatible. A PoE++ device that needs 51-71W cannot be powered by PoE+ (25.5W) or original PoE (15.4W). You must use a switch that supports the required PoE standard.',
        'choices': [
            ('Yes — all PoE standards are fully compatible with each other', False),
            ('No — PoE standards are downward compatible but not upward compatible — a PoE++ device requires PoE++ power', True),
            ('Yes — but only if the device has a power adapter as backup', False),
            ('No — PoE+ and PoE++ use different cable types', False),
        ]
    },
    {
        'text': 'Which types of devices are commonly powered using PoE? (Select THREE)',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': True,
        'explanation': 'PoE is commonly used to power desk phones IP cameras and wireless access points. These devices are often in locations where running a separate power cable is inconvenient — PoE delivers both data and power over a single Ethernet cable.',
        'choices': [
            ('Desk phones (VoIP)', True),
            ('Desktop PC tower computers', False),
            ('Wireless access points mounted on ceilings', True),
            ('IP cameras', True),
            ('Fiber optic switches', False),
        ]
    },

    # ── MANAGED SWITCH DETAILS ────────────────────────────────────────────────

    {
        'text': 'Which THREE features are available on a managed switch that an unmanaged switch cannot provide?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': True,
        'explanation': 'Managed switches support VLANs for network segmentation SNMP for remote monitoring and port mirroring (SPAN) to copy traffic to an analyzer. Unmanaged switches are plug-and-play with no configuration options.',
        'choices': [
            ('VLAN configuration on individual ports', True),
            ('Automatic cable fault detection and repair', False),
            ('SNMP remote monitoring and management', True),
            ('Port mirroring to copy traffic to an analyzer', True),
            ('Wireless access point integration', False),
        ]
    },

    # ── VPN ALWAYS-ON ─────────────────────────────────────────────────────────

    {
        'text': 'What does an always-on VPN configuration mean?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'An always-on VPN automatically establishes the encrypted tunnel the moment the user logs into their device and has internet access. The user does not need to manually start VPN software — the connection is always encrypted back to the corporate concentrator.',
        'choices': [
            ('The VPN server runs 24/7 allowing connections at any time', False),
            ('The VPN automatically connects when the user logs in so all traffic is always encrypted without manual intervention', True),
            ('The VPN connection cannot be disconnected by the user', False),
            ('The VPN stays connected even when there is no internet access', False),
        ]
    },

    # ── CABLE MODEM / DOCSIS ──────────────────────────────────────────────────

    {
        'text': 'What does DOCSIS stand for and what speeds does modern cable internet support?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'DOCSIS stands for Data Over Cable Service Interface Specification. Modern DOCSIS 3.1 commonly provides speeds from 50 Mbps up to 1 Gbps and beyond making cable internet viable for both home and corporate environments.',
        'choices': [
            ('Data Output Cable Service Interface Standard — speeds up to 100Mbps', False),
            ('Data Over Cable Service Interface Specification — speeds from 50Mbps up to 1Gbps and higher', True),
            ('Direct Over Copper Service Interface System — speeds up to 200Mbps', False),
            ('Digital Output Communication Service Interface — speeds up to 500Mbps', False),
        ]
    },

    # ── DSL DISTANCE ─────────────────────────────────────────────────────────

    {
        'text': 'What is the maximum distance from a central office for DSL service and how does distance affect speed?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'DSL requires being within approximately 10,000 feet of the central office. The closer you are the faster the speeds. At maximum distance speeds drop significantly — the signal degrades over the copper telephone wire as distance increases.',
        'choices': [
            ('Maximum 1 mile — distance has no effect on speed', False),
            ('Maximum 10,000 feet — the closer to the central office the faster the speeds', True),
            ('Maximum 50 miles — speeds are consistent regardless of distance', False),
            ('Maximum 1,000 feet — beyond this DSL is not available', False),
        ]
    },

    # ── SATELLITE / WAN TYPES ────────────────────────────────────────────────

    {
        'text': 'What is the difference between terrestrial and non-terrestrial WAN connections?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'Terrestrial WAN connections use infrastructure on Earth such as fiber cables copper lines or point-to-point wireless towers. Non-terrestrial connections use satellites in orbit. Both can be used to connect wide area networks across long distances.',
        'choices': [
            ('Terrestrial is faster while non-terrestrial is more reliable', False),
            ('Terrestrial uses Earth-based infrastructure while non-terrestrial uses satellites in orbit', True),
            ('Terrestrial is wireless while non-terrestrial always uses cables', False),
            ('They are identical in function — the names just describe the ISP type', False),
        ]
    },

    # ── WISP TECHNOLOGIES ────────────────────────────────────────────────────

    {
        'text': 'What wireless technologies might a WISP use to provide internet service?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'A WISP may use meshed 802.11 networks (same as home Wi-Fi), 5G home internet using mobile carrier infrastructure, or proprietary wireless technologies. The customer needs an external antenna to connect to the WISP network.',
        'choices': [
            ('Only licensed microwave links — no unlicensed frequencies allowed', False),
            ('Meshed 802.11 networks, 5G home internet, or proprietary wireless technologies requiring an external antenna', True),
            ('Only satellite connections relayed through ground stations', False),
            ('Only DSL technology delivered wirelessly', False),
        ]
    },

    # ── MAN DETAILS ──────────────────────────────────────────────────────────

    {
        'text': 'What is Metro Ethernet and who sometimes builds their own MAN infrastructure?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'Metro Ethernet is an Ethernet-based metropolitan area network standard connecting locations across a city. Local governments sometimes build their own MAN using fiber because they have right-of-way to place cables in public infrastructure.',
        'choices': [
            ('Metro Ethernet is a wireless standard used only in subway systems', False),
            ('Metro Ethernet is Ethernet connectivity across a city — local governments sometimes build their own MAN using fiber right-of-way', True),
            ('Metro Ethernet requires all connections to go through the ISP central office', False),
            ('Metro Ethernet only works between buildings owned by the same company', False),
        ]
    },

    # ── SAN DETAILS ──────────────────────────────────────────────────────────

    {
        'text': 'What is block-level access in a SAN and how does the SAN appear to connected servers?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'Block-level access means the SAN allows individual blocks of data to be read or written — not just whole files. To connected servers the SAN appears as a locally attached storage device even though it is on a separate high-speed network.',
        'choices': [
            ('Block-level access means only read-only access is permitted to protect data', False),
            ('The SAN appears as local storage to servers and allows block-level data access for efficient large file manipulation', True),
            ('Block-level means data is transferred in fixed 512-byte blocks only', False),
            ('The SAN appears as a network share like a file server to connected devices', False),
        ]
    },

    # ── APIPA EXACT RANGE ────────────────────────────────────────────────────

    {
        'text': 'What is the exact usable range of APIPA addresses a device can assign itself?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'The APIPA block is 169.254.0.0 through 169.254.255.255. However the first 256 addresses and last 256 are reserved leaving 169.254.1.0 through 169.254.254.255 as the actual usable range for self-assigned addresses.',
        'choices': [
            ('169.254.0.0 through 169.254.255.255 — the entire block is usable', False),
            ('169.254.1.0 through 169.254.254.255 — first and last 256 addresses are reserved', True),
            ('169.254.0.1 through 169.254.0.254 — only the first subnet is used', False),
            ('169.254.128.0 through 169.254.255.255 — only the upper half is available', False),
        ]
    },

    # ── IPv4 OCTET ───────────────────────────────────────────────────────────

    {
        'text': 'What is an octet in IPv4 addressing and what is the maximum value of any octet?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'An octet is one of the four groups in an IPv4 address — each consisting of 8 bits (1 byte). Because 8 bits can represent values from 0 to 255 no octet in an IPv4 address can ever exceed 255.',
        'choices': [
            ('A group of 4 bits — maximum value 15', False),
            ('A group of 8 bits (1 byte) — maximum value 255', True),
            ('A group of 16 bits — maximum value 65535', False),
            ('A group of 10 bits — maximum value 1023', False),
        ]
    },

    # ── SOA RECORD ───────────────────────────────────────────────────────────

    {
        'text': 'What is a DNS SOA record and what information does it contain?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'SOA stands for Start of Authority. It is the first record in a DNS zone and contains administrative information including the primary nameserver responsible email address serial number and timing parameters like refresh and retry intervals.',
        'choices': [
            ('Secure Origin Authority — stores SSL certificate details for a domain', False),
            ('Start of Authority — the first record in a DNS zone containing admin info primary nameserver and timing parameters', True),
            ('Source of Address — identifies which IP addresses can query the DNS server', False),
            ('Standard Object Assignment — assigns object IDs to DNS resources', False),
        ]
    },

    # ── DKIM DETAIL ──────────────────────────────────────────────────────────

    {
        'text': 'In DKIM where is the public key stored and where is the private key kept?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'In DKIM the public key is stored as a TXT record in the DNS server — anyone can retrieve it. The private key is kept securely on the email server and is used to digitally sign outgoing emails. Receiving servers use the public key from DNS to verify the signature.',
        'choices': [
            ('Both keys are stored on the email server for security', False),
            ('Public key is in the DNS TXT record — private key is on the email server used to sign outgoing messages', True),
            ('Public key is sent in each email — private key is in the DNS record', False),
            ('Both keys are stored in the DMARC record in DNS', False),
        ]
    },

    # ── NTP CLIENT ───────────────────────────────────────────────────────────

    {
        'text': 'How does NTP time synchronisation work on a client device?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'Every operating system (Windows macOS Linux) has a built-in NTP client. The client is configured with the address of an NTP server and periodically checks in with that server to keep the local clock accurate. The NTP servers themselves reference a central reference clock.',
        'choices': [
            ('The NTP server pushes time updates to all devices every second', False),
            ('Each OS has a built-in NTP client that periodically checks an NTP server to maintain accurate time', True),
            ('Devices only sync time when manually triggered by an administrator', False),
            ('Time synchronisation only occurs when a device first starts up', False),
        ]
    },

    # ── IoT SECURITY ─────────────────────────────────────────────────────────

    {
        'text': 'Why should IoT devices be placed on their own segmented network?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'IoT manufacturers (refrigerator makers coffee machine companies etc) excel at making appliances but may not prioritise network security. Placing IoT devices on a segmented network limits the damage if one is compromised — attackers cannot use it to reach corporate resources.',
        'choices': [
            ('IoT devices use more bandwidth so they need a separate network for performance', False),
            ('IoT manufacturers may not prioritise security so segmentation limits damage if a device is compromised', True),
            ('IoT devices only support 2.4GHz Wi-Fi which requires a separate network', False),
            ('IoT devices cannot communicate with computers so they must be isolated', False),
        ]
    },

    # ── FIBER VS COPPER ──────────────────────────────────────────────────────

    {
        'text': 'What are the key advantages of fiber over copper for long-distance network connections?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'Fiber can carry much more data over much longer distances than copper. It is immune to electromagnetic interference. While fiber is more expensive to install and repair than copper its advantages make it the preferred choice for WAN and core network connections.',
        'choices': [
            ('Fiber is cheaper and easier to repair than copper making it ideal everywhere', False),
            ('Fiber carries more data over longer distances and is immune to interference though more expensive to install and repair', True),
            ('Fiber and copper are identical in performance — fiber is just newer', False),
            ('Fiber only works indoors while copper handles long-distance outdoor runs', False),
        ]
    },

    # ── SWITCH PORT COUNT ────────────────────────────────────────────────────

    {
        'text': 'What is a typical port count for a workgroup switch vs a core network switch?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'Workgroup switches typically have 24 or 48 ports for connecting end devices in an office floor or department. Core switches in the center of an enterprise network may have hundreds of interfaces to interconnect multiple workgroup switches.',
        'choices': [
            ('Workgroup switches have 4-8 ports while core switches have 12-24 ports', False),
            ('Workgroup switches typically have 24 or 48 ports while core switches may have hundreds of interfaces', True),
            ('All switches have exactly 48 ports regardless of type', False),
            ('Workgroup switches have 100+ ports while core switches have fewer high-speed ports', False),
        ]
    },

    # ── LOOPBACK PLUG DETAIL ─────────────────────────────────────────────────

    {
        'text': 'What is the key difference between a loopback plug and a crossover cable?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'A loopback plug connects the transmit pins back to the receive pins of the SAME port — it loops traffic back into itself for diagnostic testing. A crossover cable connects two devices together by crossing TX to RX between them. They look similar but serve completely different purposes.',
        'choices': [
            ('They are identical — loopback is just an older name for crossover cable', False),
            ('A loopback plug loops TX to RX on the same port for diagnostics while a crossover cable connects two separate devices', True),
            ('A loopback plug is used for fiber while a crossover cable is for copper only', False),
            ('A crossover cable is passive while a loopback plug requires power', False),
        ]
    },

    # ── PHYSICAL TAP VS PORT MIRROR ──────────────────────────────────────────

    {
        'text': 'Why would a network engineer use port mirroring (SPAN) instead of a physical network tap?',
        'domain': 'Networking', 'exam': 'core1', 'multi_select': False,
        'explanation': 'Installing a physical tap requires breaking the network connection which disrupts production traffic. Port mirroring uses built-in switch functionality to copy traffic without any physical interruption making it ideal when you cannot disrupt the live network.',
        'choices': [
            ('Port mirroring captures more data than a physical tap', False),
            ('Port mirroring uses switch functionality to copy traffic without disrupting the live connection — no cable interruption needed', True),
            ('Physical taps are illegal so port mirroring is the only legal option', False),
            ('Port mirroring works on wireless while physical taps only work on wired networks', False),
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