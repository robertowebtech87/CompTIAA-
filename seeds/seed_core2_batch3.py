from app import app, db
from models import Question, Choice

questions_data = [

    # ── SECURITY — Malware Types ──────────────────────────────────────────────

    {
        'text': 'What is a virus in the context of malware?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('Any type of malicious software', False),
            ('Malware that attaches itself to legitimate files and spreads when those files are executed', True),
            ('Software that displays unwanted advertisements', False),
            ('A program that encrypts files and demands payment', False),
        ]
    },
    {
        'text': 'What is a worm and how does it differ from a virus?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('A worm requires user interaction to spread while a virus spreads automatically', False),
            ('A worm self-replicates and spreads across networks without needing to attach to a host file, unlike a virus which requires a host', True),
            ('They are identical — worm is just an older term for virus', False),
            ('A worm targets mobile devices while a virus targets desktops', False),
        ]
    },
    {
        'text': 'What is a Trojan horse in cybersecurity?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('A virus that destroys the boot sector', False),
            ('Malware disguised as legitimate software that tricks users into installing it while performing malicious actions in the background', True),
            ('A type of ransomware that targets Greek websites', False),
            ('A network attack that floods servers with traffic', False),
        ]
    },
    {
        'text': 'What is ransomware?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('Software that steals and sells user data', False),
            ('Malware that encrypts the victim\'s files and demands payment for the decryption key', True),
            ('A type of spyware that monitors keystrokes', False),
            ('Malware that deletes all files on a system', False),
        ]
    },
    {
        'text': 'What is spyware?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('Software that blocks internet access', False),
            ('Malware that secretly monitors user activity and collects personal information without the user\'s knowledge', True),
            ('A program that displays pop-up advertisements', False),
            ('Software that slows down the computer intentionally', False),
        ]
    },
    {
        'text': 'What is adware?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('Software used by advertisers to target specific users legitimately', False),
            ('Unwanted software that displays advertisements, often redirecting browsers or injecting ads into web pages', True),
            ('A tool for blocking online advertisements', False),
            ('Malware that steals credit card information', False),
        ]
    },
    {
        'text': 'What is a keylogger?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('Software that manages keyboard shortcuts', False),
            ('Malware that records keystrokes and sends them to an attacker allowing capture of passwords and sensitive information', True),
            ('A program that locks the keyboard remotely', False),
            ('Hardware used to test keyboard functionality', False),
        ]
    },
    {
        'text': 'What is a botnet?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('A network of security cameras', False),
            ('A network of infected computers controlled by an attacker used to perform coordinated attacks or send spam', True),
            ('An automated customer service system', False),
            ('A group of servers running automated tasks', False),
        ]
    },
    {
        'text': 'What is a zero-day vulnerability?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('A vulnerability that has been patched for zero days', False),
            ('A vulnerability that is unknown to the software vendor and has no available patch — attackers can exploit it before it is fixed', True),
            ('A vulnerability that only affects systems with zero updates installed', False),
            ('A security flaw found on the first day of a software release', False),
        ]
    },
    {
        'text': 'What is cryptomining malware?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('Malware that encrypts user files', False),
            ('Malware that hijacks the victim\'s CPU and GPU resources to mine cryptocurrency for the attacker without the user\'s knowledge', True),
            ('Software used to secure cryptocurrency wallets', False),
            ('A type of ransomware that demands payment in cryptocurrency', False),
        ]
    },

    # ── SECURITY — Social Engineering ─────────────────────────────────────────

    {
        'text': 'What is phishing?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('A network scanning technique used by administrators', False),
            ('A social engineering attack using fraudulent emails or websites that appear legitimate to trick users into revealing credentials or downloading malware', True),
            ('A type of denial of service attack', False),
            ('A method of testing password strength', False),
        ]
    },
    {
        'text': 'What is spear phishing and how does it differ from regular phishing?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('Spear phishing targets mobile devices while phishing targets desktops', False),
            ('Spear phishing is a highly targeted attack aimed at a specific individual or organization using personalized information to appear more convincing', True),
            ('Spear phishing uses phone calls while phishing uses email', False),
            ('They are identical attacks with different names', False),
        ]
    },
    {
        'text': 'What is vishing?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('A phishing attack using video calls', False),
            ('Voice phishing — a social engineering attack conducted over the phone where attackers impersonate legitimate organizations to extract information', True),
            ('A type of malware that affects voice over IP systems', False),
            ('Visual phishing using fake images', False),
        ]
    },
    {
        'text': 'What is tailgating in physical security?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('Following someone too closely while driving', False),
            ('An attacker physically following an authorized person through a secure door or entry point without using their own credentials', True),
            ('Monitoring another user\'s network traffic', False),
            ('Copying data from a USB drive left on a desk', False),
        ]
    },
    {
        'text': 'What is pretexting in social engineering?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('Sending text messages with malicious links', False),
            ('Creating a fabricated scenario or false identity to manipulate someone into providing information or access', True),
            ('Using pre-written scripts for phishing emails', False),
            ('Testing security before an attack', False),
        ]
    },
    {
        'text': 'What is a man-in-the-middle (MITM) attack?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('An attack where the attacker stands physically between two computers', False),
            ('An attack where the attacker secretly intercepts and potentially alters communication between two parties who believe they are communicating directly', True),
            ('A social engineering attack involving two attackers', False),
            ('An attack that requires two separate vulnerabilities to be exploited', False),
        ]
    },
    {
        'text': 'What is a denial of service (DoS) attack?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('An attack that denies the attacker service from a company', False),
            ('An attack that overwhelms a system or network with traffic making it unavailable to legitimate users', True),
            ('Refusing to provide IT services to a user', False),
            ('Blocking a user account after too many failed logins', False),
        ]
    },
    {
        'text': 'What is SQL injection?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('A hardware attack on database servers', False),
            ('An attack where malicious SQL code is inserted into input fields to manipulate a database, potentially exposing or destroying data', True),
            ('A method of backing up SQL databases', False),
            ('Injecting updates into a SQL server remotely', False),
        ]
    },
    {
        'text': 'What is the purpose of multi-factor authentication (MFA)?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('To make login faster by remembering multiple passwords', False),
            ('To require two or more forms of verification making it much harder for attackers to gain access even if they have the password', True),
            ('To allow multiple users to share one account', False),
            ('To automatically rotate passwords every 30 days', False),
        ]
    },
    {
        'text': 'What are the three factors of authentication?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('Username, password, and security question', False),
            ('Something you know (password), something you have (token/phone), and something you are (biometric)', True),
            ('Something you know, something you remember, and something you type', False),
            ('Password, PIN, and backup code', False),
        ]
    },

    # ── SECURITY — Windows Security Features ──────────────────────────────────

    {
        'text': 'What is Windows Defender Antivirus and is it sufficient protection on its own?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('A firewall — not sufficient as it does not scan for viruses', False),
            ('A built-in antivirus and anti-malware tool that provides good baseline protection and is sufficient for most home users when kept updated', True),
            ('An enterprise-only security tool not available on Windows Home', False),
            ('A VPN service built into Windows', False),
        ]
    },
    {
        'text': 'What is the Windows Security Center and what does it monitor?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('A remote monitoring tool for IT administrators', False),
            ('A central dashboard that monitors the status of antivirus, firewall, Windows Update, and other security features providing alerts when action is needed', True),
            ('A tool for monitoring network security only', False),
            ('A password manager built into Windows', False),
        ]
    },
    {
        'text': 'What does enabling Secure Boot in UEFI/BIOS protect against?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('Protects against viruses in downloaded files', False),
            ('Prevents unauthorized operating systems and bootloaders from loading during startup protecting against bootkits and rootkits', True),
            ('Encrypts the hard drive during startup', False),
            ('Requires a password before Windows loads', False),
        ]
    },
    {
        'text': 'What is the principle of least privilege?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('Giving users the minimum amount of storage space needed', False),
            ('Granting users only the permissions they need to perform their job and nothing more', True),
            ('Restricting internet access for all users equally', False),
            ('Requiring the least complex password possible', False),
        ]
    },
    {
        'text': 'What should an IT technician do before working on a customer\'s computer to protect against data theft accusations?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('Ask the customer to leave the room', False),
            ('Document the existing condition of the device and get the customer to acknowledge what work will be performed', True),
            ('Disable the internet connection first', False),
            ('Install monitoring software to prove nothing was stolen', False),
        ]
    },
    {
        'text': 'What is the purpose of an account lockout policy?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('Automatically locks inactive user accounts after 90 days', False),
            ('Locks a user account after a specified number of failed login attempts to prevent brute force attacks', True),
            ('Forces users to change their password after a set time', False),
            ('Prevents users from logging in after business hours', False),
        ]
    },
    {
        'text': 'What is patch management?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('Physically repairing damaged network cables', False),
            ('The process of regularly identifying, testing, and applying software updates and security patches to keep systems protected', True),
            ('Managing software licenses across an organization', False),
            ('Backing up systems before making changes', False),
        ]
    },
    {
        'text': 'What is the risk of using end-of-life (EOL) software?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('The software runs more slowly over time', False),
            ('The vendor no longer provides security patches leaving the software vulnerable to known and future exploits', True),
            ('The license expires and the software stops working', False),
            ('End-of-life software is more prone to crashing', False),
        ]
    },
    {
        'text': 'What is data loss prevention (DLP)?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('A backup solution that prevents data from being lost in a disaster', False),
            ('A set of tools and policies designed to prevent sensitive data from being accidentally or intentionally leaked outside the organization', True),
            ('Antivirus software that prevents malware from destroying files', False),
            ('A RAID configuration that prevents data loss from drive failure', False),
        ]
    },
    {
        'text': 'What is the purpose of a DMZ (Demilitarized Zone) in network security?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('A zone where no security rules apply', False),
            ('A network segment that sits between the public internet and the internal network hosting publicly accessible services like web servers while keeping the internal network protected', True),
            ('A geographic area with no network coverage', False),
            ('A portion of the network reserved for guest users', False),
        ]
    },

    # ── SECURITY — Physical Security ──────────────────────────────────────────

    {
        'text': 'What is the purpose of a privacy screen on a laptop or monitor?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('To reduce eye strain from blue light', False),
            ('To prevent shoulder surfing by limiting the viewing angle so only the person directly in front can see the screen', True),
            ('To protect the screen from scratches', False),
            ('To reduce glare from overhead lighting', False),
        ]
    },
    {
        'text': 'What is a cable lock used for on a laptop?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('Securing network cables to prevent them being unplugged', False),
            ('Physically securing the laptop to a desk or fixture to prevent theft', True),
            ('Locking the laptop keyboard to prevent unauthorized use', False),
            ('Preventing cables from being damaged', False),
        ]
    },
    {
        'text': 'What is a smart card used for in enterprise security?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('Storing large amounts of data for backup', False),
            ('A physical authentication token containing a chip that stores credentials used for secure login and physical access control', True),
            ('A wireless payment card for purchasing equipment', False),
            ('A card that monitors employee internet usage', False),
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
            exam=qd.get('exam', 'core2'),
            explanation=qd.get('explanation', ''),
            active=True
        )
        db.session.add(q)
        db.session.flush()
        for choice_text, is_correct in qd['choices']:
            db.session.add(Choice(question_id=q.id, text=choice_text, is_correct=is_correct))
        added += 1
    db.session.commit()
    total = Question.query.count()
    core2 = Question.query.filter_by(exam='core2').count()
    print(f'Added {added} questions. Skipped {skipped}.')
    print(f'Core 2 total: {core2} | Overall: {total}')