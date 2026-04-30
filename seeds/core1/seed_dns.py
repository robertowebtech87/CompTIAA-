import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app import app, db
from models import Question, Choice

questions_data = [

    # ── WHAT IS DNS ───────────────────────────────────────────────────────────

    {
        'text': 'What is the primary purpose of DNS?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'DNS (Domain Name System) translates human-readable domain names like www.google.com into IP addresses like 142.250.80.46. Without DNS users would need to memorise IP addresses to visit websites.',
        'choices': [
            ('To assign IP addresses automatically to network devices', False),
            ('To translate domain names into IP addresses', True),
            ('To encrypt web traffic between client and server', False),
            ('To route packets between different networks', False),
        ]
    },
    {
        'text': 'What port does DNS use and which transport protocol does it primarily use?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'DNS uses port 53 and primarily uses UDP for standard queries because speed matters more than reliability for small DNS packets. TCP port 53 is used for larger operations like zone transfers.',
        'choices': [
            ('Port 53 — TCP only', False),
            ('Port 53 — primarily UDP with TCP for large transfers', True),
            ('Port 80 — HTTP', False),
            ('Port 443 — HTTPS', False),
        ]
    },
    {
        'text': 'What does DNS stand for?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'DNS stands for Domain Name System. It is a distributed hierarchical database that maps domain names to IP addresses and provides other network resource information.',
        'choices': [
            ('Dynamic Network Service', False),
            ('Domain Name System', True),
            ('Data Network Standard', False),
            ('Distributed Name Server', False),
        ]
    },

    # ── DNS HIERARCHY ─────────────────────────────────────────────────────────

    {
        'text': 'How many root server clusters exist at the top of the DNS hierarchy?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'There are 13 root server clusters at the top of the DNS hierarchy. In reality these clusters consist of over 1,000 physical servers worldwide. They are the starting point for resolving any domain name on the internet.',
        'choices': [
            ('1', False),
            ('13', True),
            ('256', False),
            ('1000', False),
        ]
    },
    {
        'text': 'What are top-level domains (TLDs) in the DNS hierarchy?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Top-level domains are the highest level of domain names after the root. Generic TLDs include .com .org .net while country code TLDs include .uk .us .ca. There are about 275 country code TLDs.',
        'choices': [
            ('The IP addresses of root DNS servers', False),
            ('The highest level domain extensions like .com .org .net and country codes like .uk', True),
            ('The DNS servers managed by your ISP', False),
            ('The subdomain prefixes like www or mail', False),
        ]
    },
    {
        'text': 'What is a fully qualified domain name (FQDN)?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A fully qualified domain name (FQDN) is the complete domain name specifying its exact location in the DNS hierarchy. For example www.professormesser.com is an FQDN — it includes the hostname subdomain domain and TLD.',
        'choices': [
            ('Just the top-level domain like .com or .org', False),
            ('The complete domain name including all levels like www.professormesser.com', True),
            ('The IP address returned by a DNS query', False),
            ('The DNS server address configured on a device', False),
        ]
    },

    # ── DNS RECORD TYPES ──────────────────────────────────────────────────────

    {
        'text': 'What does a DNS A record do?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A DNS A record maps a hostname to an IPv4 address. For example www.example.com → 93.184.216.34. It is the most basic and common DNS record type.',
        'choices': [
            ('Maps a hostname to an IPv6 address', False),
            ('Maps a hostname to an IPv4 address', True),
            ('Identifies the mail server for a domain', False),
            ('Creates an alias pointing to another hostname', False),
        ]
    },
    {
        'text': 'What does a DNS AAAA record do?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A DNS AAAA (quad-A) record maps a hostname to an IPv6 address. The name comes from IPv6 being four times the size of IPv4 (4 × A). Example: www.example.com → 2606:2800:220:1:248:1893:25c8:1946.',
        'choices': [
            ('Maps a hostname to an IPv4 address', False),
            ('Maps a hostname to an IPv6 address', True),
            ('An advanced A record with built-in encryption', False),
            ('Identifies authoritative DNS servers for a domain', False),
        ]
    },
    {
        'text': 'What is a CNAME record used for?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A CNAME (Canonical Name) record creates an alias that points to another hostname. For example ftp.example.com and www.example.com could both be CNAMEs pointing to mail.example.com. Change the A record once and all aliases update automatically.',
        'choices': [
            ('Maps a hostname directly to an IP address', False),
            ('Creates an alias that points to another hostname', True),
            ('Identifies which mail server handles email for the domain', False),
            ('Stores arbitrary text information for a domain', False),
        ]
    },
    {
        'text': 'What is a DNS MX record and why is it critical?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'An MX (Mail Exchanger) record specifies which mail server is responsible for accepting email for a domain. Without correct MX records email sent to that domain will not be delivered. Every email domain must have at least one MX record.',
        'choices': [
            ('Maps a hostname to an IP address for web traffic', False),
            ('Specifies which mail server handles email for a domain', True),
            ('Creates a mirror copy of the DNS zone', False),
            ('Stores security policies for the domain', False),
        ]
    },
    {
        'text': 'What is a DNS TXT record commonly used for?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'DNS TXT records store arbitrary text information for a domain. They are commonly used for email security (SPF DKIM DMARC) domain ownership verification and other service configurations.',
        'choices': [
            ('Storing the full text content of a website for faster loading', False),
            ('Storing arbitrary text — commonly used for SPF DKIM DMARC and domain verification', True),
            ('Mapping text domain names to numeric IP addresses', False),
            ('Storing encrypted certificates for HTTPS', False),
        ]
    },
    {
        'text': 'What is a DNS SOA record?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'SOA (Start of Authority) is the first record in a DNS zone. It contains administrative information about the zone including the primary nameserver contact email serial number and timing parameters like refresh intervals.',
        'choices': [
            ('Secondary Object Address — identifies backup DNS servers', False),
            ('Start of Authority — first record in a DNS zone with admin information and timing parameters', True),
            ('Secure Origin Authentication — verifies the DNS server identity', False),
            ('Source of Address — identifies which IPs can query the server', False),
        ]
    },
    {
        'text': 'What is TTL in DNS and what happens when it expires?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'TTL (Time to Live) defines how long a DNS record is cached before the resolver must re-query the authoritative server. When TTL expires the cached record is discarded and a fresh lookup is performed. Short TTL means faster propagation of changes.',
        'choices': [
            ('Total Transfer Limit — the maximum file size DNS can resolve', False),
            ('Time to Live — how long a record is cached before the resolver must refresh it', True),
            ('Time to Load — how fast a webpage loads after DNS resolution', False),
            ('Transfer Time Limit — maximum time allowed for a DNS query response', False),
        ]
    },

    # ── EMAIL SECURITY RECORDS ────────────────────────────────────────────────

    {
        'text': 'What is DKIM and how does it protect email?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'DKIM (DomainKeys Identified Mail) adds a digital signature to outgoing emails. The private key signs the email on the server. The public key is stored as a DNS TXT record. Receiving servers verify the signature using the public key confirming the email is authentic and unaltered.',
        'choices': [
            ('A spam filter that blocks emails from unknown senders', False),
            ('Adds a digital signature to emails — private key on server signs it public key in DNS verifies it', True),
            ('Encrypts the full email body so only the recipient can read it', False),
            ('A blacklist of known spam IP addresses stored in DNS', False),
        ]
    },
    {
        'text': 'Where is the DKIM public key stored?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'The DKIM public key is stored as a TXT record in the DNS server — anyone can retrieve it to verify email signatures. The private key is kept securely on the email server and is used to sign outgoing messages.',
        'choices': [
            ('On the email server alongside the private key', False),
            ('As a TXT record in the DNS server', True),
            ('In the email header of every outgoing message', False),
            ('In the DMARC record in DNS', False),
        ]
    },
    {
        'text': 'What is SPF (Sender Policy Framework)?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'SPF is a DNS TXT record that lists all mail servers authorised to send email on behalf of a domain. Receiving servers check this list to verify the sender — if the sending server is not listed the email may be marked as spam or rejected.',
        'choices': [
            ('A firewall rule blocking spam at the network perimeter', False),
            ('A DNS TXT record listing all authorised mail servers for a domain', True),
            ('An encryption standard for securing email content', False),
            ('A blacklist service blocking known spam IP addresses', False),
        ]
    },
    {
        'text': 'What is DMARC and what does it add on top of SPF and DKIM?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'DMARC (Domain-based Message Authentication Reporting and Conformance) builds on SPF and DKIM by defining what to do when those checks fail — none (allow) quarantine or reject. It also provides reporting so domain owners can see who is sending email pretending to be them.',
        'choices': [
            ('DMARC replaces both SPF and DKIM with a single unified record', False),
            ('Tells receiving servers what to do when SPF or DKIM checks fail and provides reporting to domain owners', True),
            ('DMARC encrypts email in transit between mail servers', False),
            ('DMARC is a blacklist of known phishing domains stored in DNS', False),
        ]
    },
    {
        'text': 'Which THREE are email authentication/security standards stored as DNS TXT records? (Select THREE)',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'DKIM SPF and DMARC are all email security standards stored as DNS TXT records. Together they prevent email spoofing verify sender identity and define policies for failed checks.',
        'choices': [
            ('DKIM — DomainKeys Identified Mail', True),
            ('DHCP — Dynamic Host Configuration Protocol', False),
            ('SPF — Sender Policy Framework', True),
            ('SNMP — Simple Network Management Protocol', False),
            ('DMARC — Domain-based Message Authentication Reporting and Conformance', True),
        ]
    },

    # ── DNS TOOLS ─────────────────────────────────────────────────────────────

    {
        'text': 'What command-line tool is used to query DNS records on Windows?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'nslookup is the standard DNS query tool on Windows. It can look up A records AAAA records MX records TXT records and more. For example: nslookup google.com returns the IP addresses for google.com.',
        'choices': [
            ('ipconfig', False),
            ('nslookup', True),
            ('netstat', False),
            ('tracert', False),
        ]
    },
    {
        'text': 'What command is commonly used to query DNS records on Linux and macOS?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'dig (Domain Information Groper) is the primary DNS query tool on Linux and macOS. It provides detailed output including the question answer and authority sections. Example: dig www.google.com returns the IP addresses and TTL values.',
        'choices': [
            ('nslookup', False),
            ('dig', True),
            ('ifconfig', False),
            ('ping', False),
        ]
    },
    {
        'text': 'A technician types nslookup google.com and gets back three IP addresses. What does this indicate?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Multiple IP addresses returned by DNS indicates redundancy. The domain has multiple servers and DNS round-robin load balancing distributes requests across them. If one server fails requests can use the other IP addresses.',
        'choices': [
            ('The DNS server is misconfigured and has duplicate records', False),
            ('The domain has multiple servers for redundancy and load balancing', True),
            ('The computer has three network interfaces', False),
            ('DNS is returning cached results from three different queries', False),
        ]
    },

    # ── DNS SCENARIOS ─────────────────────────────────────────────────────────

    {
        'text': 'A user can ping a server by IP address but cannot reach it by hostname. What is the most likely cause?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'If a device can be reached by IP but not by hostname the problem is DNS resolution. The DNS server may be unreachable incorrect or missing the record for that hostname. The network itself is working since ping by IP succeeds.',
        'choices': [
            ('The server is offline', False),
            ('DNS resolution is failing — the DNS server is unreachable or missing the record', True),
            ('The network cable is faulty', False),
            ('The firewall is blocking all traffic', False),
        ]
    },
    {
        'text': 'A company changes its web server IP address. Users still reach the old server for several hours after the change. What causes this?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'DNS caching and TTL cause this. When users queried DNS earlier they cached the old IP address. Until the TTL expires they continue using the cached record. Lowering the TTL before making changes reduces this delay.',
        'choices': [
            ('The old server is still running and intercepting traffic', False),
            ('DNS caching — users have the old IP cached and the TTL has not yet expired', True),
            ('The new server has the wrong IP address configured', False),
            ('The ISP has not updated their routing tables', False),
        ]
    },
    {
        'text': 'What DNS record type would you check if users are not receiving email sent to your domain?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'MX (Mail Exchanger) records tell other mail servers where to deliver email for your domain. If MX records are missing or incorrect incoming email will fail. This is the first record to check when email delivery problems occur.',
        'choices': [
            ('A record', False),
            ('MX record', True),
            ('TXT record', False),
            ('CNAME record', False),
        ]
    },
    {
        'text': 'What happens when a device cannot reach its DNS server?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Without DNS the device cannot resolve domain names to IP addresses. Web browsing by name will fail even if the internet connection itself is working. The device can still communicate using direct IP addresses.',
        'choices': [
            ('The device loses all network connectivity including ping', False),
            ('Domain name resolution fails but direct IP communication still works', True),
            ('The device automatically uses a backup DNS server from the internet', False),
            ('All network traffic is blocked by the OS until DNS is restored', False),
        ]
    },
    {
        'text': 'A user reports that email from your company keeps ending up in recipients spam folders. Which DNS records should you verify? (Select TWO)',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'SPF and DKIM are the primary DNS email authentication records that affect spam filtering. SPF verifies the sending server is authorised. DKIM provides a digital signature. Missing or incorrect records cause legitimate email to be marked as spam.',
        'choices': [
            ('SPF record — verifies authorised sending servers', True),
            ('A record — maps hostname to IP', False),
            ('DKIM record — provides digital signature verification', True),
            ('CNAME record — hostname alias', False),
        ]
    },
    {
        'text': 'What is the difference between a DNS A record and a CNAME record?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'An A record maps a hostname directly to an IP address. A CNAME record creates an alias that points to another hostname (not an IP). CNAMEs are useful when multiple names should resolve to the same server — change the A record once and all CNAMEs follow.',
        'choices': [
            ('A records are for IPv6 while CNAME records are for IPv4', False),
            ('A records map directly to IP addresses while CNAME records create aliases pointing to other hostnames', True),
            ('A records are temporary while CNAME records are permanent', False),
            ('They are identical — CNAME is just the newer name for A record', False),
        ]
    },
    {
        'text': 'Which DNS record would you add to verify domain ownership to a third-party service like Google?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'TXT records are used for domain ownership verification. Third-party services like Google provide a unique text string that you add as a TXT record. They then query your DNS to verify you control the domain.',
        'choices': [
            ('MX record', False),
            ('A record', False),
            ('TXT record', True),
            ('CNAME record', False),
        ]
    },
    {
        'text': 'In the DNS hierarchy what is the correct order from top to bottom?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'The DNS hierarchy goes from top to bottom: Root servers → Top-level domains (.com .org .net) → Second-level domains (google professormesser) → Subdomains (www mail ftp). Queries start at the root and work downward.',
        'choices': [
            ('Subdomains → Second-level domains → TLDs → Root', False),
            ('Root → Top-level domains → Second-level domains → Subdomains', True),
            ('TLDs → Root → Second-level domains → Subdomains', False),
            ('Second-level domains → TLDs → Subdomains → Root', False),
        ]
    },
    {
        'text': 'A web server called mail.example.com also hosts FTP and web services. A CNAME record is created for ftp.example.com pointing to mail.example.com. What happens when the IP of mail.example.com changes?',
        'domain': 'DNS',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Only the A record for mail.example.com needs to be updated. The CNAME for ftp.example.com points to mail.example.com — not directly to an IP. So it automatically resolves to the new IP without any changes to the CNAME record.',
        'choices': [
            ('The CNAME record for ftp.example.com must also be manually updated', False),
            ('Only the A record for mail.example.com needs updating — the CNAME follows automatically', True),
            ('Both the A record and CNAME must be deleted and recreated', False),
            ('The CNAME stops working until manually re-pointed to the new IP', False),
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
    dns = Question.query.filter_by(exam='core1', domain='DNS').count()
    print(f'Added {added} questions. Skipped {skipped} duplicates.')
    print(f'DNS: {dns} | Core 1: {core1} | Overall: {total}')