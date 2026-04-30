import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app import app, db
from models import Question, Choice

questions_data = [

    # ── NetBIOS / SMB ─────────────────────────────────────────────────────────

    {
        'text': 'What ports does NetBIOS/NetBT use?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'NetBIOS over TCP/IP (NetBT) uses ports 137 (name services) and 139 (session services). These are used for Windows file and printer sharing on older networks.',
        'choices': [
            ('Ports 80 and 443', False),
            ('Ports 137 and 139', True),
            ('Ports 161 and 162', False),
            ('Ports 389 and 636', False),
        ]
    },
    {
        'text': 'What protocol uses port 445 and what is it used for?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 445 is used by SMB (Server Message Block) also known as CIFS (Common Internet File System). It is used for Windows file sharing printer sharing and other network resources.',
        'choices': [
            ('SMTP — email sending', False),
            ('SMB/CIFS — Windows file and printer sharing', True),
            ('SNMP — network device monitoring', False),
            ('SSH — secure remote access', False),
        ]
    },
    {
        'text': 'What is the difference between NetBIOS (ports 137/139) and SMB (port 445)?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'NetBIOS/NetBT (137/139) is the older method for Windows networking name resolution and sessions. SMB on port 445 is the modern direct hosting method that does not require NetBIOS and is used in current Windows environments.',
        'choices': [
            ('They are identical — just different names for the same protocol', False),
            ('NetBIOS 137/139 is the older method while SMB port 445 is the modern direct hosting approach', True),
            ('NetBIOS is for printing while SMB is for file sharing only', False),
            ('SMB port 445 only works on Linux while NetBIOS is Windows-only', False),
        ]
    },

    # ── SDN ───────────────────────────────────────────────────────────────────

    {
        'text': 'What is Software-Defined Networking (SDN)?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'SDN separates the control plane (decisions about where traffic goes) from the data plane (actual packet forwarding). A centralised software controller manages network behaviour rather than individual device configurations.',
        'choices': [
            ('A type of network cable made from software-coated copper', False),
            ('An approach that separates network control from hardware allowing centralised software management of network behaviour', True),
            ('A wireless networking standard faster than Wi-Fi 6', False),
            ('Software installed on PCs to replace physical network adapters', False),
        ]
    },
    {
        'text': 'What is the main advantage of Software-Defined Networking (SDN) over traditional networking?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'SDN allows network administrators to manage and configure the entire network from a central software controller rather than configuring each device individually. This makes networks more flexible and easier to manage.',
        'choices': [
            ('SDN eliminates the need for any physical network hardware', False),
            ('Centralised management allowing the entire network to be configured from one software controller', True),
            ('SDN automatically repairs physical cable faults', False),
            ('SDN provides faster speeds than any hardware-based solution', False),
        ]
    },

    # ── HUB ───────────────────────────────────────────────────────────────────

    {
        'text': 'What is a network hub and how does it differ from a switch?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A hub broadcasts all received data to every connected port regardless of the destination. A switch intelligently forwards data only to the specific port where the destination device is connected making switches far more efficient.',
        'choices': [
            ('A hub is faster than a switch because it uses less processing power', False),
            ('A hub broadcasts data to all ports while a switch forwards data only to the correct destination port', True),
            ('A hub and switch are identical — hub is just an older name', False),
            ('A hub provides wireless connectivity while a switch is wired only', False),
        ]
    },
    {
        'text': 'Why are hubs no longer used in modern networks?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Hubs create excessive network congestion because all traffic is broadcast to all ports creating collisions and wasting bandwidth. Switches replaced hubs by forwarding data only to the intended recipient.',
        'choices': [
            ('Hubs only support 10 Mbps speeds', False),
            ('Hubs broadcast all traffic to all ports causing collisions and wasting bandwidth — switches replaced them', True),
            ('Hubs are too expensive compared to switches', False),
            ('Hubs cannot connect to routers', False),
        ]
    },

    # ── PoE SWITCH ────────────────────────────────────────────────────────────

    {
        'text': 'What is a PoE switch and how does it differ from a PoE injector?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A PoE switch has PoE built into every port delivering power and data through all ports simultaneously. A PoE injector is an inline device that adds power to a single cable between a non-PoE switch and one PoE device.',
        'choices': [
            ('A PoE switch is portable while a PoE injector is rack-mounted', False),
            ('A PoE switch has PoE on all ports while a PoE injector adds PoE to a single cable from a non-PoE switch', True),
            ('They are identical — PoE switch is just the newer name for a PoE injector', False),
            ('A PoE switch only works with wireless access points', False),
        ]
    },

    # ── 802.11 WIRELESS STANDARDS ─────────────────────────────────────────────

    {
        'text': 'What frequency and maximum speed does 802.11a support?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '802.11a operates on the 5 GHz band and supports a maximum speed of 54 Mbps. It was released alongside 802.11b in 1999 but was less common due to shorter range at 5 GHz.',
        'choices': [
            ('2.4 GHz — 11 Mbps', False),
            ('5 GHz — 54 Mbps', True),
            ('2.4 GHz — 54 Mbps', False),
            ('5 GHz — 600 Mbps', False),
        ]
    },
    {
        'text': 'What frequency and maximum speed does 802.11b support?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '802.11b operates on the 2.4 GHz band and supports a maximum speed of 11 Mbps. It was the first widely adopted Wi-Fi standard but is now obsolete.',
        'choices': [
            ('5 GHz — 54 Mbps', False),
            ('2.4 GHz — 11 Mbps', True),
            ('2.4 GHz — 54 Mbps', False),
            ('5 GHz — 11 Mbps', False),
        ]
    },
    {
        'text': 'What frequency and maximum speed does 802.11g support?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '802.11g operates on the 2.4 GHz band and supports up to 54 Mbps. It improved on 802.11b\'s 11 Mbps while remaining backward compatible with 802.11b devices.',
        'choices': [
            ('5 GHz — 54 Mbps', False),
            ('2.4 GHz — 54 Mbps', True),
            ('2.4 GHz — 600 Mbps', False),
            ('5 GHz — 150 Mbps', False),
        ]
    },
    {
        'text': 'What frequencies and maximum speed does 802.11n (Wi-Fi 4) support?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '802.11n (Wi-Fi 4) introduced dual-band support operating on both 2.4 GHz and 5 GHz. It uses MIMO (multiple antennas) to achieve speeds up to 600 Mbps.',
        'choices': [
            ('2.4 GHz only — up to 54 Mbps', False),
            ('Both 2.4 GHz and 5 GHz — up to 600 Mbps using MIMO', True),
            ('5 GHz only — up to 1.3 Gbps', False),
            ('2.4 GHz and 5 GHz — up to 9.6 Gbps', False),
        ]
    },
    {
        'text': 'What is 802.11ac (Wi-Fi 5) and what improvement did it bring over 802.11n?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '802.11ac (Wi-Fi 5) operates exclusively on the 5 GHz band and introduced MU-MIMO (multi-user MIMO) and wider channels to achieve speeds up to 3.5 Gbps — significantly faster than 802.11n.',
        'choices': [
            ('Wi-Fi 5 — 2.4 GHz only — up to 600 Mbps', False),
            ('Wi-Fi 5 — 5 GHz — up to 3.5 Gbps with MU-MIMO and wider channels', True),
            ('Wi-Fi 5 — 2.4 GHz and 5 GHz — up to 9.6 Gbps', False),
            ('Wi-Fi 5 — 6 GHz — up to 10 Gbps', False),
        ]
    },
    {
        'text': 'What is 802.11ax (Wi-Fi 6) and what are its key improvements?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '802.11ax (Wi-Fi 6) operates on 2.4 GHz and 5 GHz (Wi-Fi 6E adds 6 GHz) and achieves up to 9.6 Gbps. Key improvements include OFDMA for better multi-device efficiency lower latency and improved performance in crowded environments.',
        'choices': [
            ('Wi-Fi 6 — 5 GHz only — 3.5 Gbps — same as Wi-Fi 5 but more reliable', False),
            ('Wi-Fi 6 — 2.4/5 GHz — up to 9.6 Gbps with OFDMA for better performance in crowded environments', True),
            ('Wi-Fi 6 — 6 GHz only — up to 40 Gbps', False),
            ('Wi-Fi 6 — all frequencies — uses cellular towers for backhaul', False),
        ]
    },
    {
        'text': 'Which TWO 802.11 standards operate ONLY on the 5 GHz band? (Select TWO)',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': True,
        'explanation': '802.11a and 802.11ac (Wi-Fi 5) operate exclusively on 5 GHz. 802.11b and 802.11g are 2.4 GHz only. 802.11n and 802.11ax are dual-band.',
        'choices': [
            ('802.11a', True),
            ('802.11b', False),
            ('802.11g', False),
            ('802.11ac (Wi-Fi 5)', True),
        ]
    },
    {
        'text': 'Arrange the 802.11 standards in order from slowest to fastest maximum speed.',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Speeds: 802.11b (11 Mbps) → 802.11a/g (54 Mbps) → 802.11n (600 Mbps) → 802.11ac (3.5 Gbps) → 802.11ax (9.6 Gbps). Each generation brought significant speed improvements.',
        'choices': [
            ('b → g → a → n → ac → ax', False),
            ('b → a/g → n → ac → ax', True),
            ('a → b → g → ac → n → ax', False),
            ('g → b → a → n → ax → ac', False),
        ]
    },

    # ── WIRELESS CHANNELS ─────────────────────────────────────────────────────

    {
        'text': 'Why does 2.4 GHz Wi-Fi experience more interference than 5 GHz?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '2.4 GHz has only 3 non-overlapping channels (1 6 11) and is shared by many devices including microwaves Bluetooth and baby monitors. 5 GHz has many more non-overlapping channels and fewer competing devices.',
        'choices': [
            ('2.4 GHz transmits more data causing more collisions', False),
            ('2.4 GHz has only 3 non-overlapping channels and is shared by many other wireless devices', True),
            ('2.4 GHz uses older encryption that attracts more attackers', False),
            ('2.4 GHz is regulated more strictly limiting available power', False),
        ]
    },
    {
        'text': 'How many non-overlapping channels does the 2.4 GHz band have in the US?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'The 2.4 GHz band has only 3 non-overlapping channels in the US: channels 1 6 and 11. Using overlapping channels causes interference between nearby access points.',
        'choices': [
            ('1 non-overlapping channel', False),
            ('3 non-overlapping channels (1 6 and 11)', True),
            ('11 non-overlapping channels', False),
            ('23 non-overlapping channels', False),
        ]
    },

    # ── RFID ─────────────────────────────────────────────────────────────────

    {
        'text': 'What is RFID and how does it work?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'RFID (Radio-Frequency Identification) uses electromagnetic fields to automatically identify and track tags attached to objects. A reader emits radio waves that power passive tags and read their stored data without line of sight.',
        'choices': [
            ('Remote File ID — a protocol for identifying files on a network server', False),
            ('Radio-Frequency Identification — uses radio waves to identify and track tagged objects without line of sight', True),
            ('Rapid Frequency Interface Device — a type of wireless network adapter', False),
            ('Real-time Frequency Identification — GPS-based tracking system', False),
        ]
    },
    {
        'text': 'What is a common use case for RFID in a business environment?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'RFID is commonly used for asset tracking inventory management access control (key fobs building entry) and supply chain management. Unlike barcodes RFID does not require line of sight to scan.',
        'choices': [
            ('Streaming video to display screens throughout a building', False),
            ('Asset tracking inventory management and access control without requiring line of sight', True),
            ('Providing wireless internet access to devices', False),
            ('Encrypting data transmitted over a network', False),
        ]
    },

    # ── LONG-RANGE FIXED WIRELESS ─────────────────────────────────────────────

    {
        'text': 'What is long-range fixed wireless internet and when is it used?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Long-range fixed wireless uses directional antennas to transmit internet signals over distances of several kilometres. It is used to provide broadband connectivity to rural areas where fibre or cable is unavailable.',
        'choices': [
            ('A Wi-Fi extender that boosts signal within a building', False),
            ('Directional antenna systems that transmit internet over several kilometres — used in rural areas lacking cable or fibre', True),
            ('A cellular network that covers an entire city', False),
            ('A satellite dish that receives signals from orbit', False),
        ]
    },
    {
        'text': 'What is the difference between licensed and unlicensed fixed wireless frequencies?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Licensed frequencies are purchased from the government guaranteeing exclusive use and protection from interference. Unlicensed frequencies (like 2.4 GHz and 5 GHz) are free to use but shared with other devices and more prone to interference.',
        'choices': [
            ('Licensed is faster while unlicensed is slower', False),
            ('Licensed frequencies are purchased for exclusive use while unlicensed are shared and may have interference', True),
            ('Licensed is for government use only while unlicensed is for businesses', False),
            ('There is no practical difference between licensed and unlicensed frequencies', False),
        ]
    },

    # ── DNS RECORDS ───────────────────────────────────────────────────────────

    {
        'text': 'What is a DNS A record used for?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A DNS A record maps a hostname to an IPv4 address. For example www.example.com → 93.184.216.34. It is the most basic and common type of DNS record.',
        'choices': [
            ('Maps a hostname to an IPv6 address', False),
            ('Maps a hostname to an IPv4 address', True),
            ('Identifies which mail server handles email for a domain', False),
            ('Stores arbitrary text information for a domain', False),
        ]
    },
    {
        'text': 'What is a DNS AAAA record used for?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A DNS AAAA record maps a hostname to an IPv6 address. The name comes from IPv6 being four times the size of IPv4 (4 × A). Example: www.example.com → 2606:2800:220:1:248:1893:25c8:1946.',
        'choices': [
            ('Maps a hostname to an IPv4 address', False),
            ('Maps a hostname to an IPv6 address', True),
            ('An advanced A record with encryption', False),
            ('Identifies authoritative DNS servers for a domain', False),
        ]
    },
    {
        'text': 'What is a DNS MX record used for?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A DNS MX (Mail Exchanger) record specifies which mail server is responsible for accepting email for a domain. Without correct MX records email sent to that domain will not be delivered.',
        'choices': [
            ('Maps a hostname to an IP address for web traffic', False),
            ('Specifies which mail server handles email for a domain', True),
            ('Stores security policies for a domain', False),
            ('Identifies the primary DNS server for a domain', False),
        ]
    },
    {
        'text': 'What is a DNS TXT record and what is it commonly used for?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A DNS TXT record stores arbitrary text information for a domain. It is commonly used for email security (SPF DKIM DMARC records) domain ownership verification and other service configurations.',
        'choices': [
            ('A record that stores the website\'s text content for faster loading', False),
            ('Stores arbitrary text — commonly used for SPF DKIM DMARC email security and domain verification', True),
            ('A record that maps text domain names to numeric IP addresses', False),
            ('Stores encrypted certificates for HTTPS websites', False),
        ]
    },

    # ── DKIM / SPF / DMARC ────────────────────────────────────────────────────

    {
        'text': 'What is DKIM (DomainKeys Identified Mail) and what problem does it solve?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'DKIM adds a digital signature to outgoing emails allowing receiving servers to verify the email actually came from the claimed domain and has not been altered in transit. It prevents email spoofing and tampering.',
        'choices': [
            ('A spam filter that blocks emails from unknown senders', False),
            ('Adds a digital signature to emails allowing receiving servers to verify authenticity and detect tampering', True),
            ('Encrypts the full email body so only the recipient can read it', False),
            ('A blacklist of known spam domains', False),
        ]
    },
    {
        'text': 'What is SPF (Sender Policy Framework)?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'SPF is a DNS TXT record that lists the mail servers authorised to send email on behalf of a domain. Receiving servers check this record to verify the sender — if the sending server is not listed the email may be marked as spam.',
        'choices': [
            ('A firewall rule that blocks spam at the network perimeter', False),
            ('A DNS TXT record listing authorised mail servers for a domain — receiving servers verify senders against this list', True),
            ('An encryption standard for securing email content', False),
            ('A blacklist service that blocks known spam IP addresses', False),
        ]
    },
    {
        'text': 'What is DMARC and how does it work with SPF and DKIM?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'DMARC (Domain-based Message Authentication Reporting and Conformance) builds on SPF and DKIM by telling receiving servers what to do when emails fail those checks — reject quarantine or allow — and provides reporting to domain owners.',
        'choices': [
            ('DMARC replaces SPF and DKIM with a single unified standard', False),
            ('DMARC tells receiving servers what to do when SPF/DKIM checks fail and provides reporting to domain owners', True),
            ('DMARC encrypts email in transit between servers', False),
            ('DMARC is a blacklist of known phishing domains', False),
        ]
    },

    # ── DHCP CONCEPTS ─────────────────────────────────────────────────────────

    {
        'text': 'What is a DHCP lease?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A DHCP lease is the period of time a client is allowed to use an IP address assigned by a DHCP server. When the lease expires the client must renew it or request a new address.',
        'choices': [
            ('A permanent IP address assignment that never expires', False),
            ('The time period a client is allowed to use a DHCP-assigned IP address', True),
            ('The process of a DHCP server requesting an address from the router', False),
            ('A security certificate used to authenticate DHCP clients', False),
        ]
    },
    {
        'text': 'What is a DHCP reservation?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A DHCP reservation assigns a specific IP address to a specific device based on its MAC address. The device always gets the same IP address from DHCP while still being managed centrally — combining benefits of static and dynamic addressing.',
        'choices': [
            ('Blocking a specific IP address so no device can use it', False),
            ('Assigning a specific IP address to a specific device by MAC address so it always gets the same address', True),
            ('Reserving a range of IPs for future use', False),
            ('A backup DHCP server that activates when the primary fails', False),
        ]
    },
    {
        'text': 'What is a DHCP scope?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A DHCP scope is the range of IP addresses that the DHCP server is configured to assign to clients. For example a scope might be 192.168.1.100 to 192.168.1.200 meaning only those 101 addresses can be leased.',
        'choices': [
            ('The physical range of the DHCP server signal', False),
            ('The range of IP addresses the DHCP server is configured to assign to clients', True),
            ('The maximum number of devices a DHCP server can support', False),
            ('The security policy applied to all DHCP clients', False),
        ]
    },

    # ── SERVER ROLES ──────────────────────────────────────────────────────────

    {
        'text': 'What is a DNS server\'s role in a network?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A DNS server resolves human-readable domain names to IP addresses. Without DNS users would need to memorise IP addresses to visit websites or connect to network resources.',
        'choices': [
            ('Assigns IP addresses automatically to devices on the network', False),
            ('Resolves domain names to IP addresses allowing users to use names instead of IP addresses', True),
            ('Stores and shares files across the network', False),
            ('Authenticates users before granting network access', False),
        ]
    },
    {
        'text': 'What is a DHCP server\'s role in a network?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A DHCP server automatically assigns IP addresses subnet masks default gateways and DNS server addresses to client devices when they join the network eliminating the need for manual IP configuration.',
        'choices': [
            ('Resolves domain names to IP addresses', False),
            ('Automatically assigns IP addresses and network configuration to client devices', True),
            ('Controls user access to network resources', False),
            ('Stores shared files for network users', False),
        ]
    },
    {
        'text': 'What does a syslog server do?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A syslog server collects and stores log messages from network devices like routers switches firewalls and servers. Centralising logs makes monitoring troubleshooting and security analysis much easier.',
        'choices': [
            ('Manages system software updates across the network', False),
            ('Collects and stores log messages from network devices in a central location for monitoring and analysis', True),
            ('Monitors employee computer usage and productivity', False),
            ('Backs up system files from all network computers', False),
        ]
    },
    {
        'text': 'What is AAA in networking and what does each letter stand for?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'AAA stands for Authentication Authorization and Accounting. Authentication verifies who you are. Authorization determines what you can access. Accounting tracks what you do. RADIUS is a common AAA protocol.',
        'choices': [
            ('Antivirus Automation Architecture — security framework for networks', False),
            ('Authentication Authorization and Accounting — verifies identity controls access and tracks usage', True),
            ('Advanced Access Administration — enterprise user management', False),
            ('Automatic Address Assignment — IP address management', False),
        ]
    },
    {
        'text': 'What is a print server and what problem does it solve?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A print server manages print jobs from multiple users and sends them to one or more printers. It allows many computers to share a single printer without each needing a direct connection.',
        'choices': [
            ('A server that prints its own configuration for backup purposes', False),
            ('Manages print jobs from multiple users allowing shared access to one or more printers', True),
            ('A high-speed printer with a built-in CPU', False),
            ('A server that scans and digitises physical documents', False),
        ]
    },
    {
        'text': 'What is the role of a web server?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A web server hosts websites and serves web content (HTML CSS images) to clients over HTTP/HTTPS. When you visit a website your browser connects to the web server hosting that site.',
        'choices': [
            ('Stores and shares files across the local network only', False),
            ('Hosts websites and serves web content to clients over HTTP and HTTPS', True),
            ('Manages user accounts and passwords across the organisation', False),
            ('Processes email sent to the organisation', False),
        ]
    },

    # ── INTERNET APPLIANCES ───────────────────────────────────────────────────

    {
        'text': 'What is a spam gateway and how does it protect an organisation?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A spam gateway sits between the internet and the mail server filtering out spam phishing emails and malware before they reach users. It reduces inbox clutter and protects against email-based threats.',
        'choices': [
            ('A router that blocks all email from outside the network', False),
            ('Filters incoming email to remove spam phishing and malware before it reaches users', True),
            ('A device that limits how many emails users can send per day', False),
            ('An encrypted email relay between two organisations', False),
        ]
    },
    {
        'text': 'What is a UTM (Unified Threat Management) appliance?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A UTM is a single network security device that combines multiple security functions — firewall intrusion detection/prevention antivirus VPN content filtering and more — into one appliance simplifying security management.',
        'choices': [
            ('A device that manages user accounts and passwords', False),
            ('A single appliance combining firewall intrusion detection antivirus VPN and content filtering', True),
            ('A unified threat database shared between organisations', False),
            ('A monitoring tool that detects network performance issues', False),
        ]
    },
    {
        'text': 'What is a load balancer and why is it used?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A load balancer distributes incoming network traffic across multiple servers to prevent any single server from being overwhelmed. This improves performance reliability and availability of services.',
        'choices': [
            ('A device that balances power consumption across server racks', False),
            ('Distributes network traffic across multiple servers to prevent overload and improve availability', True),
            ('A UPS that distributes power evenly to network devices', False),
            ('Software that balances CPU usage across processor cores', False),
        ]
    },
    {
        'text': 'What is a proxy server and what are its benefits?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A proxy server acts as an intermediary between clients and the internet. Benefits include caching web content for faster access filtering content to enforce policies providing anonymity and improving security.',
        'choices': [
            ('A server that stores backup copies of all network data', False),
            ('An intermediary server between clients and internet — provides caching content filtering anonymity and security', True),
            ('A server that proxies authentication requests to Active Directory', False),
            ('A temporary server used when the primary server is down', False),
        ]
    },

    # ── APIPA ─────────────────────────────────────────────────────────────────

    {
        'text': 'What is APIPA and when does a device use it?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'APIPA (Automatic Private IP Addressing) assigns an address in the 169.254.0.1–169.254.255.254 range when a device cannot reach a DHCP server. An APIPA address means the device has failed to get a proper IP and cannot access the internet.',
        'choices': [
            ('A static IP address manually assigned by an administrator', False),
            ('Self-assigned address in the 169.254.x.x range when no DHCP server is reachable', True),
            ('An IPv6 address automatically generated from a MAC address', False),
            ('A public IP address assigned by the ISP', False),
        ]
    },
    {
        'text': 'A technician sees a computer with IP address 169.254.45.12. What does this indicate?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '169.254.x.x is an APIPA address meaning the computer could not reach the DHCP server to get a proper IP address. The technician should check network connectivity and DHCP server availability.',
        'choices': [
            ('The computer has been assigned a valid static IP address', False),
            ('The computer could not reach the DHCP server and assigned itself an APIPA address', True),
            ('The computer is connected to an IPv6-only network', False),
            ('The computer has a public IP address from the ISP', False),
        ]
    },

    # ── IPv6 ──────────────────────────────────────────────────────────────────

    {
        'text': 'How many bits are in an IPv6 address and how is it written?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'IPv6 addresses are 128 bits long written as eight groups of four hexadecimal digits separated by colons. Example: 2001:0db8:85a3:0000:0000:8a2e:0370:7334.',
        'choices': [
            ('32 bits — written as four decimal numbers separated by dots', False),
            ('128 bits — written as eight groups of four hexadecimal digits separated by colons', True),
            ('64 bits — written as four hexadecimal groups', False),
            ('256 bits — written as a long hexadecimal string', False),
        ]
    },
    {
        'text': 'Why was IPv6 developed to replace IPv4?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'IPv4 only supports about 4.3 billion addresses which have been exhausted by the growth of internet-connected devices. IPv6 supports 340 undecillion addresses (3.4 × 10^38) providing effectively unlimited addresses.',
        'choices': [
            ('IPv6 is faster than IPv4 because it uses shorter addresses', False),
            ('IPv4 addresses were exhausted — IPv6 provides 340 undecillion addresses for unlimited growth', True),
            ('IPv6 was required to support wireless networks', False),
            ('IPv4 lacked encryption which IPv6 builds in by default', False),
        ]
    },

    # ── INTERNET CONNECTION TYPES ─────────────────────────────────────────────

    {
        'text': 'What is satellite internet and what is its main disadvantage?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Satellite internet uses orbiting satellites to provide internet access anywhere on Earth. Its main disadvantage is high latency (delay) because signals must travel to space and back — typically 500–700ms for traditional geostationary satellites.',
        'choices': [
            ('Uses radio towers — disadvantage is limited to urban areas only', False),
            ('Uses orbiting satellites — main disadvantage is high latency due to signal travel distance', True),
            ('Uses underground cables — disadvantage is susceptibility to flooding', False),
            ('Uses laser beams — disadvantage is only works at night', False),
        ]
    },
    {
        'text': 'What is a WISP (Wireless Internet Service Provider)?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A WISP provides internet access using wireless technology (typically fixed wireless) rather than cables. WISPs are common in rural areas where fibre or cable infrastructure is not available.',
        'choices': [
            ('A company that provides Wi-Fi hotspots in coffee shops and airports', False),
            ('An ISP that delivers internet access using wireless technology — common in rural areas without cable infrastructure', True),
            ('A wireless security company that protects ISP networks', False),
            ('An internet provider that uses only 5G cellular towers', False),
        ]
    },

    # ── NETWORK TYPES ─────────────────────────────────────────────────────────

    {
        'text': 'What is a MAN (Metropolitan Area Network)?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A MAN covers a city or metropolitan area — larger than a LAN but smaller than a WAN. It might connect multiple buildings of a university or company branches across a city.',
        'choices': [
            ('A network connecting devices within a single room', False),
            ('A network covering a city or metropolitan area — larger than LAN but smaller than WAN', True),
            ('A network connecting continents via undersea cables', False),
            ('A mobile ad-hoc network used by emergency services', False),
        ]
    },
    {
        'text': 'What is a SAN (Storage Area Network)?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A SAN is a dedicated high-speed network that provides shared access to storage devices like disk arrays. Servers connect to the SAN to access storage as if it were locally attached enabling centralised high-performance storage.',
        'choices': [
            ('A network that only allows read-only access to files', False),
            ('A dedicated high-speed network providing shared access to storage devices for multiple servers', True),
            ('A wireless network for scanning documents', False),
            ('A secure network that encrypts all stored data', False),
        ]
    },

    # ── NETWORKING TOOLS ──────────────────────────────────────────────────────

    {
        'text': 'What is a cable crimper used for?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A cable crimper attaches RJ45 or RJ11 connectors to the ends of Ethernet or telephone cables. It mechanically presses the connector onto the cable creating a secure electrical connection.',
        'choices': [
            ('Testing whether a network cable has any breaks', False),
            ('Attaching RJ45 or RJ11 connectors to the ends of network cables', True),
            ('Tracing a cable from a wall jack back to a patch panel', False),
            ('Removing the outer jacket from a cable to expose the wires', False),
        ]
    },
    {
        'text': 'What is a cable stripper used for in network installations?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A cable stripper removes the outer plastic jacket from a network cable to expose the inner wire pairs. This must be done before terminating cables with connectors or punch-down blocks.',
        'choices': [
            ('Tests the cable for electrical continuity', False),
            ('Removes the outer jacket from a cable to expose the inner wire pairs', True),
            ('Attaches connectors to cable ends', False),
            ('Traces a cable path through walls', False),
        ]
    },
    {
        'text': 'What is a Wi-Fi analyser used for?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A Wi-Fi analyser scans the wireless spectrum showing nearby networks their signal strength channels and frequencies. It helps identify interference troubleshoot connectivity issues and choose the best channel for an access point.',
        'choices': [
            ('Tests whether a Wi-Fi password is correct', False),
            ('Scans the wireless spectrum to show networks signal strength channels and interference', True),
            ('Boosts Wi-Fi signal strength in weak areas', False),
            ('Measures the physical distance of a Wi-Fi connection', False),
        ]
    },
    {
        'text': 'What is a punchdown tool used for?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A punchdown tool terminates individual wires from a network cable into a punchdown block (like a keystone jack or patch panel). It pushes each wire into the correct slot and cuts off excess wire in one motion.',
        'choices': [
            ('Crimping RJ45 connectors onto cable ends', False),
            ('Terminating individual wires into a keystone jack or patch panel punchdown block', True),
            ('Testing cable continuity and wiremap', False),
            ('Removing staples that hold cables to walls', False),
        ]
    },
    {
        'text': 'What is a cable tester used for?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A cable tester checks whether a network cable is properly wired by verifying continuity and the correct pinout (wiremap) on both ends. It can detect open circuits short circuits and crossed or miswired pairs.',
        'choices': [
            ('Measures the maximum speed a cable can support', False),
            ('Verifies cable continuity and correct pinout detecting open circuits shorts and miswired pairs', True),
            ('Tests whether a cable can carry PoE power', False),
            ('Identifies which network a cable is connected to', False),
        ]
    },
    {
        'text': 'What is a loopback plug used for in network troubleshooting?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A loopback plug connects the transmit pins to the receive pins of a port. When a loopback test is run any data sent out immediately returns as received data — confirming the port hardware is functional.',
        'choices': [
            ('Connects two network switches together for testing', False),
            ('Connects transmit to receive pins to test whether a port can send and receive data', True),
            ('Blocks a network port to prevent unauthorised connections', False),
            ('Tests maximum cable length by looping the signal back', False),
        ]
    },
    {
        'text': 'What is a network tap and how is it used?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A network tap is a passive hardware device inserted into a network cable that passively copies all traffic passing through it to a monitoring port. It allows traffic analysis without affecting the live network flow.',
        'choices': [
            ('A device that physically cuts a network connection to isolate a segment', False),
            ('A passive device that copies all network traffic to a monitoring port without affecting the live connection', True),
            ('A tool for testing whether a cable is properly tapped into a wall', False),
            ('A wireless device that intercepts Wi-Fi traffic', False),
        ]
    },

    # ── MULTI-SELECT NETWORKING ────────────────────────────────────────────────

    {
        'text': 'Which TWO of the following are connectionless protocols that use UDP? (Select TWO)',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'DHCP uses UDP because clients do not have an IP address yet and cannot establish TCP connections. TFTP uses UDP for simplicity in transferring configuration files.',
        'choices': [
            ('DHCP', True),
            ('HTTPS', False),
            ('TFTP', True),
            ('SSH', False),
        ]
    },
    {
        'text': 'Which TWO of the following are connection-oriented protocols that use TCP? (Select TWO)',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'HTTPS and SSH both use TCP because they require reliable ordered delivery. HTTPS needs every byte of a web page to arrive correctly. SSH needs every command and response to be delivered reliably.',
        'choices': [
            ('DHCP', False),
            ('HTTPS', True),
            ('TFTP', False),
            ('SSH', True),
        ]
    },
    {
        'text': 'Which THREE of the following are email authentication standards stored as DNS TXT records? (Select THREE)',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'DKIM SPF and DMARC are all email authentication standards stored as DNS TXT records. Together they prevent email spoofing and help legitimate email reach inboxes.',
        'choices': [
            ('DKIM', True),
            ('DHCP', False),
            ('SPF', True),
            ('SNMP', False),
            ('DMARC', True),
        ]
    },
    {
        'text': 'Which TWO tools would a technician use when terminating a new Ethernet cable run? (Select TWO)',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'A cable stripper removes the outer jacket to expose wires. A punchdown tool terminates those wires into a keystone jack or patch panel. A crimper would be used for RJ45 connectors not punch-down terminations.',
        'choices': [
            ('Cable stripper', True),
            ('Loopback plug', False),
            ('Punchdown tool', True),
            ('Network tap', False),
        ]
    },
    {
        'text': 'Which TWO are server roles that handle name and address resolution on a network? (Select TWO)',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'DNS resolves domain names to IP addresses. DHCP automatically assigns IP addresses to devices. Both are fundamental network infrastructure roles.',
        'choices': [
            ('DNS server', True),
            ('Print server', False),
            ('DHCP server', True),
            ('Syslog server', False),
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
    print(f'Networking domain: {networking} | Core 1: {core1} | Overall: {total}')