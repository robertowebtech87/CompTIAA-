from app import app, db
from models import Question, Choice

questions_data = [

    # ── PORT IDENTIFICATION ────────────────────────────────────────────────────

    {
        'text': 'What port does HTTP use?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'HTTP (HyperText Transfer Protocol) uses port 80. It is the foundation of web communication but transmits data in plain text. HTTPS (port 443) is the secure version.',
        'choices': [('Port 21', False), ('Port 80', True), ('Port 443', False), ('Port 8080', False)]
    },
    {
        'text': 'What port does SSH use?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'SSH (Secure Shell) uses port 22. It provides encrypted remote access replacing the insecure Telnet (port 23).',
        'choices': [('Port 20', False), ('Port 22', True), ('Port 23', False), ('Port 25', False)]
    },
    {
        'text': 'What port does SMTP use?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'SMTP (Simple Mail Transfer Protocol) uses port 25. It is used for sending email between mail servers.',
        'choices': [('Port 21', False), ('Port 25', True), ('Port 53', False), ('Port 110', False)]
    },
    {
        'text': 'What port does DNS use?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'DNS (Domain Name System) uses port 53. It resolves human-readable domain names like www.google.com to IP addresses.',
        'choices': [('Port 25', False), ('Port 53', True), ('Port 67', False), ('Port 80', False)]
    },
    {
        'text': 'What port does FTP use for control commands?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'FTP uses port 21 for control (sending commands) and port 20 for actual data transfer. Port 21 establishes the command channel.',
        'choices': [('Port 20', False), ('Port 21', True), ('Port 22', False), ('Port 23', False)]
    },
    {
        'text': 'What port does FTP use for data transfer?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'FTP uses port 20 for data transfer and port 21 for control commands. Both ports must be available for FTP to function correctly.',
        'choices': [('Port 20', True), ('Port 21', False), ('Port 22', False), ('Port 69', False)]
    },
    {
        'text': 'What port does RDP use?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'RDP (Remote Desktop Protocol) uses port 3389. It allows remote graphical access to Windows computers over a network.',
        'choices': [('Port 22', False), ('Port 443', False), ('Port 3389', True), ('Port 5900', False)]
    },
    {
        'text': 'What port does POP3 use?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'POP3 (Post Office Protocol 3) uses port 110. It downloads email from a server to a single device.',
        'choices': [('Port 25', False), ('Port 110', True), ('Port 143', False), ('Port 993', False)]
    },
    {
        'text': 'What port does IMAP use?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'IMAP (Internet Message Access Protocol) uses port 143. It syncs email across multiple devices keeping messages on the server.',
        'choices': [('Port 110', False), ('Port 143', True), ('Port 443', False), ('Port 993', False)]
    },
    {
        'text': 'What port does HTTPS use?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'HTTPS uses port 443. It is HTTP with TLS/SSL encryption protecting data in transit.',
        'choices': [('Port 80', False), ('Port 443', True), ('Port 8080', False), ('Port 993', False)]
    },
    {
        'text': 'What port does LDAP use?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'LDAP (Lightweight Directory Access Protocol) uses port 389 for directory services like Active Directory.',
        'choices': [('Port 143', False), ('Port 389', True), ('Port 443', False), ('Port 636', False)]
    },
    {
        'text': 'What port does LDAPS use?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'LDAPS (Secure LDAP) uses port 636. It is LDAP with TLS/SSL encryption protecting directory service communications.',
        'choices': [('Port 389', False), ('Port 443', False), ('Port 636', True), ('Port 993', False)]
    },
    {
        'text': 'What port does IMAPS use?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'IMAPS (Secure IMAP) uses port 993. It is IMAP with SSL/TLS encryption for secure email synchronisation.',
        'choices': [('Port 143', False), ('Port 465', False), ('Port 993', True), ('Port 995', False)]
    },
    {
        'text': 'What port does POP3S use?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'POP3S (Secure POP3) uses port 995. It is POP3 with SSL/TLS encryption for secure email downloading.',
        'choices': [('Port 110', False), ('Port 993', False), ('Port 995', True), ('Port 3389', False)]
    },
    {
        'text': 'What port does SMTPS use?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'SMTPS (Secure SMTP) uses port 465. It is SMTP with SSL/TLS encryption for secure email sending.',
        'choices': [('Port 25', False), ('Port 443', False), ('Port 465', True), ('Port 587', False)]
    },
    {
        'text': 'What port does SNMP use for queries?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'SNMP uses port 161 for queries (polling network devices) and port 162 for traps (alerts sent from devices to the management system).',
        'choices': [('Port 69', False), ('Port 161', True), ('Port 162', False), ('Port 389', False)]
    },
    {
        'text': 'What port does SNMP use for traps (alerts)?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'SNMP uses port 162 for traps — alerts automatically sent from network devices to the management system when something notable happens.',
        'choices': [('Port 161', False), ('Port 162', True), ('Port 389', False), ('Port 443', False)]
    },
    {
        'text': 'What port does TFTP use?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'TFTP (Trivial File Transfer Protocol) uses port 69. It uses UDP and is commonly used for transferring firmware and config files to network devices.',
        'choices': [('Port 21', False), ('Port 67', False), ('Port 69', True), ('Port 80', False)]
    },
    {
        'text': 'What ports does DHCP use?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'DHCP uses port 67 (server receiving requests) and port 68 (client receiving responses). It automatically assigns IP addresses to network devices.',
        'choices': [('Ports 20 and 21', False), ('Ports 53 and 54', False), ('Ports 67 and 68', True), ('Ports 80 and 443', False)]
    },
    {
        'text': 'What port does Telnet use?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Telnet uses port 23. It provides unencrypted remote access and should be avoided in favour of SSH (port 22) which is encrypted.',
        'choices': [('Port 21', False), ('Port 22', False), ('Port 23', True), ('Port 25', False)]
    },
    {
        'text': 'What port does SFTP use?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'SFTP (SSH File Transfer Protocol) uses port 22 — the same as SSH since it runs over the SSH protocol. It provides encrypted file transfer.',
        'choices': [('Port 20', False), ('Port 21', False), ('Port 22', True), ('Port 69', False)]
    },

    # ── IDENTIFY PROTOCOL FROM PORT ────────────────────────────────────────────

    {
        'text': 'Which protocol uses port 80?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 80 is used by HTTP (HyperText Transfer Protocol) for standard unencrypted web traffic.',
        'choices': [('FTP', False), ('HTTP', True), ('HTTPS', False), ('SMTP', False)]
    },
    {
        'text': 'Which protocol uses port 443?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 443 is used by HTTPS — secure web browsing using TLS/SSL encryption.',
        'choices': [('HTTP', False), ('LDAP', False), ('HTTPS', True), ('IMAPS', False)]
    },
    {
        'text': 'Which protocol uses port 22?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 22 is used by SSH (Secure Shell) for encrypted remote access. SFTP also uses port 22 since it runs over SSH.',
        'choices': [('Telnet', False), ('FTP', False), ('SSH', True), ('SMTP', False)]
    },
    {
        'text': 'Which protocol uses port 53?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 53 is used by DNS (Domain Name System) for resolving domain names to IP addresses.',
        'choices': [('DHCP', False), ('DNS', True), ('HTTP', False), ('SMTP', False)]
    },
    {
        'text': 'Which protocol uses port 25?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 25 is used by SMTP (Simple Mail Transfer Protocol) for sending email between mail servers.',
        'choices': [('FTP', False), ('SSH', False), ('SMTP', True), ('DNS', False)]
    },
    {
        'text': 'Which protocol uses port 3389?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 3389 is used by RDP (Remote Desktop Protocol) for remote graphical access to Windows machines.',
        'choices': [('SSH', False), ('VNC', False), ('RDP', True), ('LDAP', False)]
    },
    {
        'text': 'Which protocol uses port 110?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 110 is used by POP3 (Post Office Protocol 3) for downloading email from a server to a local device.',
        'choices': [('SMTP', False), ('POP3', True), ('IMAP', False), ('DNS', False)]
    },
    {
        'text': 'Which protocol uses port 143?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 143 is used by IMAP (Internet Message Access Protocol) for syncing email across multiple devices.',
        'choices': [('POP3', False), ('IMAP', True), ('SMTP', False), ('LDAP', False)]
    },
    {
        'text': 'Which protocol uses port 389?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 389 is used by LDAP (Lightweight Directory Access Protocol) for accessing directory services like Microsoft Active Directory.',
        'choices': [('IMAP', False), ('SNMP', False), ('LDAP', True), ('HTTPS', False)]
    },
    {
        'text': 'Which protocol uses port 636?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 636 is used by LDAPS — the secure encrypted version of LDAP using SSL/TLS.',
        'choices': [('LDAP', False), ('LDAPS', True), ('SMTPS', False), ('IMAPS', False)]
    },
    {
        'text': 'Which protocol uses port 993?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 993 is used by IMAPS — secure IMAP with SSL/TLS encryption for syncing email across devices.',
        'choices': [('IMAP', False), ('POP3S', False), ('IMAPS', True), ('SMTPS', False)]
    },
    {
        'text': 'Which protocol uses port 995?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 995 is used by POP3S — secure POP3 with SSL/TLS encryption.',
        'choices': [('IMAPS', False), ('POP3S', True), ('SMTPS', False), ('LDAPS', False)]
    },
    {
        'text': 'Which protocol uses port 465?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 465 is used by SMTPS — secure SMTP with SSL/TLS encryption for sending email.',
        'choices': [('SMTP', False), ('SMTPS', True), ('IMAPS', False), ('HTTPS', False)]
    },
    {
        'text': 'Which protocol uses port 161?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 161 is used by SNMP (Simple Network Management Protocol) for polling and querying network devices.',
        'choices': [('LDAP', False), ('SNMP', True), ('TFTP', False), ('DHCP', False)]
    },
    {
        'text': 'Which protocol uses port 69?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 69 is used by TFTP (Trivial File Transfer Protocol). It uses UDP and is used for simple file transfers like firmware updates to network devices.',
        'choices': [('FTP', False), ('TFTP', True), ('DHCP', False), ('SSH', False)]
    },
    {
        'text': 'Which protocol uses ports 67 and 68?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Ports 67 and 68 are used by DHCP. Port 67 receives requests at the server and port 68 receives responses at the client.',
        'choices': [('DNS', False), ('DHCP', True), ('SNMP', False), ('TFTP', False)]
    },

    # ── SCENARIO / APPLIED QUESTIONS ──────────────────────────────────────────

    {
        'text': 'A technician needs to allow secure email synchronisation across multiple devices through a firewall. Which port must be opened?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'IMAPS (port 993) provides secure IMAP email sync with SSL/TLS encryption. This allows email to be synchronised across multiple devices securely.',
        'choices': [('Port 110', False), ('Port 143', False), ('Port 465', False), ('Port 993', True)]
    },
    {
        'text': 'A network administrator wants to allow devices to automatically receive IP addresses. Which port(s) must not be blocked?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'DHCP uses ports 67 and 68. If these ports are blocked devices will not receive automatic IP addresses and will be unable to connect to the network.',
        'choices': [('Port 53', False), ('Ports 67 and 68', True), ('Port 80', False), ('Port 443', False)]
    },
    {
        'text': 'A user reports they can browse HTTP websites but cannot access HTTPS sites. Which port is likely blocked?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'If HTTP (port 80) works but HTTPS does not then port 443 is blocked. Most modern websites require HTTPS so this would prevent access to the majority of sites.',
        'choices': [('Port 80', False), ('Port 443', True), ('Port 53', False), ('Port 8080', False)]
    },
    {
        'text': 'An IT administrator needs to monitor router and switch performance remotely. Which protocol and port should be configured?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'SNMP (Simple Network Management Protocol) on port 161 is used to monitor and manage network devices like routers and switches remotely.',
        'choices': [('SSH port 22', False), ('HTTP port 80', False), ('SNMP port 161', True), ('RDP port 3389', False)]
    },
    {
        'text': 'A company uses Active Directory for user authentication. Which port must be open for clients to query the directory?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'LDAP uses port 389 for directory queries like Active Directory lookups. LDAPS (port 636) would be used for encrypted directory access.',
        'choices': [('Port 25', False), ('Port 389', True), ('Port 443', False), ('Port 3389', False)]
    },
    {
        'text': 'An admin needs to transfer a router configuration file to a new device. The network team uses TFTP. Which port must be open?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'TFTP uses port 69 and UDP. It is commonly used in networking for transferring configuration files and firmware to devices.',
        'choices': [('Port 21', False), ('Port 22', False), ('Port 69', True), ('Port 80', False)]
    },

    # ── MULTI-SELECT ADVANCED ──────────────────────────────────────────────────

    {
        'text': 'Which THREE of the following protocols use TCP? (Select THREE)',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'HTTP HTTPS and FTP all use TCP because they require reliable ordered delivery. DNS primarily uses UDP and DHCP uses UDP.',
        'choices': [
            ('HTTP (port 80)', True),
            ('DNS (port 53)', False),
            ('HTTPS (port 443)', True),
            ('DHCP (ports 67/68)', False),
            ('FTP (ports 20/21)', True),
        ]
    },
    {
        'text': 'Which TWO of the following are secure replacements for insecure protocols? (Select TWO)',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'SFTP (port 22) replaces FTP (ports 20/21) with encryption over SSH. HTTPS (port 443) replaces HTTP (port 80) with TLS/SSL encryption.',
        'choices': [
            ('SFTP replacing FTP', True),
            ('Telnet replacing SSH', False),
            ('HTTPS replacing HTTP', True),
            ('DHCP replacing DNS', False),
        ]
    },
    {
        'text': 'Which TWO protocols would you use specifically for RECEIVING email? (Select TWO)',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'POP3 (port 110) and IMAP (port 143) are both used for receiving email. SMTP (port 25) is for sending email not receiving.',
        'choices': [
            ('SMTP (port 25)', False),
            ('POP3 (port 110)', True),
            ('IMAP (port 143)', True),
            ('DNS (port 53)', False),
        ]
    },
    {
        'text': 'Which THREE port numbers are associated with email protocols of any kind? (Select THREE)',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Port 25 (SMTP sending) port 110 (POP3 receiving) and port 143 (IMAP syncing) are all standard email ports. Ports 53 and 80 are DNS and HTTP.',
        'choices': [
            ('Port 25', True),
            ('Port 53', False),
            ('Port 80', False),
            ('Port 110', True),
            ('Port 143', True),
        ]
    },

    # ── ABBREVIATIONS DEEP DIVE ────────────────────────────────────────────────

    {
        'text': 'What does DHCP stand for?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'DHCP stands for Dynamic Host Configuration Protocol. It automatically assigns IP addresses subnet masks gateways and DNS server addresses to devices joining a network.',
        'choices': [
            ('Dynamic Host Configuration Protocol', True),
            ('Digital Host Control Protocol', False),
            ('Dynamic HTTP Connection Protocol', False),
            ('Distributed Host Communication Protocol', False),
        ]
    },
    {
        'text': 'What does SMTP stand for?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'SMTP stands for Simple Mail Transfer Protocol. It is the standard protocol used for sending email between mail servers and from email clients to servers.',
        'choices': [
            ('Secure Mail Transfer Protocol', False),
            ('Simple Mail Transfer Protocol', True),
            ('Standard Message Transfer Protocol', False),
            ('System Mail Transmission Protocol', False),
        ]
    },
    {
        'text': 'What does SNMP stand for?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'SNMP stands for Simple Network Management Protocol. It is used to monitor and manage network devices like routers switches printers and servers.',
        'choices': [
            ('Secure Network Monitoring Protocol', False),
            ('Simple Node Management Protocol', False),
            ('Simple Network Management Protocol', True),
            ('Standard Network Monitoring Protocol', False),
        ]
    },
    {
        'text': 'What does TFTP stand for and how does it differ from FTP?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'TFTP stands for Trivial File Transfer Protocol. Unlike FTP it uses UDP instead of TCP has no authentication and is designed for simple transfers like firmware and config files to network devices.',
        'choices': [
            ('Total File Transfer Protocol — faster version of FTP using TCP', False),
            ('Trivial File Transfer Protocol — uses UDP no authentication simpler than FTP', True),
            ('Trusted File Transfer Protocol — more secure version of FTP', False),
            ('Transfer Format Protocol — used for web file transfers', False),
        ]
    },
    {
        'text': 'What does LDAP stand for and what is it used for?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'LDAP stands for Lightweight Directory Access Protocol. It is used to access and query directory services like Microsoft Active Directory for user authentication and resource management.',
        'choices': [
            ('Local Data Access Protocol — accesses local databases', False),
            ('Lightweight Directory Access Protocol — queries directory services like Active Directory', True),
            ('Layered Domain Authentication Protocol — manages domain logins', False),
            ('Link Data Application Protocol — transfers application data', False),
        ]
    },
    {
        'text': 'What does ARP stand for and when is it used?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'ARP stands for Address Resolution Protocol. It is used when a device knows a target\'s IP address but needs to find the corresponding MAC address for local network communication.',
        'choices': [
            ('Automatic Routing Protocol — finds paths between networks', False),
            ('Address Resolution Protocol — finds MAC addresses from known IP addresses', True),
            ('Application Request Protocol — handles app communication', False),
            ('Advanced Relay Protocol — forwards network packets', False),
        ]
    },
    {
        'text': 'What does ICMP stand for and what is ping based on?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'ICMP stands for Internet Control Message Protocol. The ping tool uses ICMP echo requests and replies to test connectivity and measure latency between devices.',
        'choices': [
            ('Internet Connection Monitoring Protocol — used for network speed tests', False),
            ('Internet Control Message Protocol — ping uses ICMP echo requests and replies', True),
            ('Internal Communication Management Protocol — used for LAN messaging', False),
            ('Integrated Control Messaging Protocol — used by routers only', False),
        ]
    },
    {
        'text': 'What does SSL/TLS stand for and what is its purpose?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'SSL stands for Secure Sockets Layer and TLS stands for Transport Layer Security. TLS is the modern successor to SSL. They encrypt data in transit protecting it from interception. HTTPS uses TLS.',
        'choices': [
            ('System Security Layer / Transport Link Security — physical network encryption', False),
            ('Secure Sockets Layer / Transport Layer Security — encrypts data in transit', True),
            ('Server Security License / Token Layer Standard — server authentication', False),
            ('Shared Security Link / Transfer Layer Standard — file sharing encryption', False),
        ]
    },
    {
        'text': 'What does DNS stand for and what problem does it solve?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'DNS stands for Domain Name System. It solves the problem of humans needing to remember IP addresses by translating human-readable domain names like www.google.com to IP addresses like 142.250.80.46.',
        'choices': [
            ('Data Network Standard — defines how data is formatted', False),
            ('Domain Name System — translates domain names to IP addresses', True),
            ('Dynamic Node Service — assigns IP addresses automatically', False),
            ('Distributed Network Security — protects network communications', False),
        ]
    },
    {
        'text': 'What does FTP stand for and what are its two ports?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'FTP stands for File Transfer Protocol. It uses port 21 for control (commands) and port 20 for data transfer. It is unencrypted — SFTP or FTPS should be used for secure transfers.',
        'choices': [
            ('Fast Transfer Protocol — ports 22 and 23', False),
            ('File Transfer Protocol — ports 20 and 21', True),
            ('File Transfer Protocol — ports 80 and 443', False),
            ('Forward Transfer Protocol — ports 25 and 26', False),
        ]
    },

    # ── QUICK RECALL (FLASHCARD STYLE) ────────────────────────────────────────

    {
        'text': 'Port 22 = ?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 22 is SSH (Secure Shell) — used for encrypted remote access. SFTP also runs on port 22 since it uses SSH as its transport.',
        'choices': [('FTP', False), ('Telnet', False), ('SSH / SFTP', True), ('SMTP', False)]
    },
    {
        'text': 'Port 23 = ?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 23 is Telnet — unencrypted remote access. It should be replaced with SSH (port 22) in all modern environments.',
        'choices': [('SSH', False), ('Telnet', True), ('FTP', False), ('SMTP', False)]
    },
    {
        'text': 'Port 443 = ?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 443 is HTTPS — secure web browsing using TLS/SSL encryption. It is the most widely used port on the internet.',
        'choices': [('HTTP', False), ('SMTPS', False), ('HTTPS', True), ('IMAPS', False)]
    },
    {
        'text': 'Port 993 = ?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 993 is IMAPS — secure IMAP for encrypted email synchronisation across multiple devices.',
        'choices': [('POP3S', False), ('IMAPS', True), ('SMTPS', False), ('LDAPS', False)]
    },
    {
        'text': 'Port 995 = ?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 995 is POP3S — secure POP3 for encrypted email downloading to a single device.',
        'choices': [('IMAPS', False), ('SMTPS', False), ('POP3S', True), ('HTTPS', False)]
    },
    {
        'text': 'Port 3389 = ?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 3389 is RDP (Remote Desktop Protocol) — used for remote graphical access to Windows computers.',
        'choices': [('SSH', False), ('VNC', False), ('RDP', True), ('LDAP', False)]
    },
    {
        'text': 'Port 53 = ?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 53 is DNS — Domain Name System. It resolves domain names to IP addresses using primarily UDP.',
        'choices': [('DHCP', False), ('TFTP', False), ('DNS', True), ('HTTP', False)]
    },
    {
        'text': 'Port 25 = ?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 25 is SMTP — Simple Mail Transfer Protocol for sending email between servers.',
        'choices': [('FTP', False), ('SMTP', True), ('SSH', False), ('DNS', False)]
    },
    {
        'text': 'Port 80 = ?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 80 is HTTP — standard unencrypted web traffic. Most modern websites redirect to HTTPS (port 443).',
        'choices': [('HTTPS', False), ('HTTP', True), ('SMTP', False), ('FTP', False)]
    },
    {
        'text': 'Port 110 = ?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 110 is POP3 — Post Office Protocol 3 for downloading email from a server to one device.',
        'choices': [('IMAP', False), ('SMTP', False), ('POP3', True), ('DNS', False)]
    },
    {
        'text': 'Port 143 = ?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 143 is IMAP — Internet Message Access Protocol for syncing email across multiple devices.',
        'choices': [('POP3', False), ('IMAP', True), ('LDAP', False), ('HTTPS', False)]
    },
    {
        'text': 'Port 389 = ?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 389 is LDAP — Lightweight Directory Access Protocol for querying directory services like Active Directory.',
        'choices': [('LDAPS', False), ('SNMP', False), ('LDAP', True), ('IMAP', False)]
    },
    {
        'text': 'Port 636 = ?',
        'domain': 'Ports & Protocols',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 636 is LDAPS — secure LDAP with SSL/TLS encryption for secure directory service access.',
        'choices': [('LDAP', False), ('LDAPS', True), ('IMAPS', False), ('SMTPS', False)]
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
    ports = Question.query.filter_by(exam='core1', domain='Ports & Protocols').count()
    print(f'Added {added} questions. Skipped {skipped} duplicates.')
    print(f'Ports & Protocols total: {ports} | Core 1: {core1} | Overall: {total}')