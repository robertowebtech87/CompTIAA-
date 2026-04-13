from app import app, db
from models import Question, Choice

questions_data = [

    # ── OPERATING SYSTEMS — Single Select ─────────────────────────────────────

    {
        'text': 'What is the purpose of the Windows hosts file?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Maps hostnames to IP addresses locally overriding DNS resolution', True),
            ('Stores all DNS cache entries', False),
            ('Configures DHCP settings for the computer', False),
            ('Lists all computers on the local network', False),
        ]
    },
    {
        'text': 'What Windows tool shows which programs are set to run at startup?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Device Manager', False),
            ('Task Manager — Startup tab', True),
            ('Services.msc', False),
            ('Disk Management', False),
        ]
    },
    {
        'text': 'What is the purpose of the Windows "Print Spooler" service?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Manages the printer hardware drivers', False),
            ('Queues print jobs and sends them to the printer in order', True),
            ('Converts documents to PDF format', False),
            ('Monitors ink and toner levels', False),
        ]
    },
    {
        'text': 'A technician needs to see detailed hardware information about a Windows PC including driver versions. What tool should they use?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Task Manager', False),
            ('System Information (msinfo32)', True),
            ('Disk Management', False),
            ('Event Viewer', False),
        ]
    },
    {
        'text': 'What is the Windows command to display the routing table?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('ipconfig /route', False),
            ('route print', True),
            ('netstat /route', False),
            ('tracert /table', False),
        ]
    },
    {
        'text': 'What does the Windows command "net use" do?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Tests network connectivity', False),
            ('Maps a network share to a drive letter from the command line', True),
            ('Displays current network adapter settings', False),
            ('Resets the network stack', False),
        ]
    },
    {
        'text': 'What is the purpose of Windows Hyper-V?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A built-in antivirus solution', False),
            ('A built-in hypervisor that allows creating and running virtual machines on Windows', True),
            ('A backup and recovery solution', False),
            ('A remote desktop tool', False),
        ]
    },
    {
        'text': 'What is the difference between 32-bit and 64-bit versions of Windows?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('32-bit Windows is newer and more secure', False),
            ('64-bit Windows can address more RAM (over 4GB) and run both 32-bit and 64-bit applications, while 32-bit is limited to 4GB RAM and cannot run 64-bit apps', True),
            ('64-bit Windows only runs on Intel processors', False),
            ('32-bit and 64-bit Windows have identical performance', False),
        ]
    },
    {
        'text': 'What is Windows Subsystem for Linux (WSL)?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A virtual machine running Linux on Windows', False),
            ('A compatibility layer that allows running Linux command-line tools natively on Windows without a VM', True),
            ('A Linux emulator that converts Windows apps to Linux', False),
            ('A dual boot configuration tool', False),
        ]
    },
    {
        'text': 'What is the purpose of the Windows "netsh" command?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Tests network connectivity like ping', False),
            ('A command-line utility for configuring and displaying network settings including IP, firewall, and wireless', True),
            ('Displays the network routing table', False),
            ('Resets the TCP/IP stack', False),
        ]
    },

    # ── OPERATING SYSTEMS — Multi Select ──────────────────────────────────────

    {
        'text': 'Which TWO of the following are features available in Windows Pro but NOT in Windows Home? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('BitLocker Drive Encryption', True),
            ('Windows Defender Antivirus', False),
            ('Ability to join a domain', True),
            ('Windows Update', False),
        ]
    },
    {
        'text': 'Which TWO commands would help a technician diagnose a DNS resolution problem on Windows? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('nslookup', True),
            ('chkdsk', False),
            ('ipconfig /flushdns', True),
            ('defrag', False),
        ]
    },
    {
        'text': 'Which TWO of the following are true about NTFS permissions? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('NTFS permissions apply both locally and over the network', True),
            ('NTFS permissions only apply when accessing files over the network', False),
            ('When a user belongs to multiple groups permissions are cumulative', True),
            ('Deny permissions are always overridden by Allow permissions', False),
        ]
    },
    {
        'text': 'Which TWO of the following are valid Windows file systems? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('NTFS', True),
            ('APFS', False),
            ('exFAT', True),
            ('HFS+', False),
        ]
    },
    {
        'text': 'A technician needs to repair Windows system files. Which TWO commands should be used in order? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('DISM /Online /Cleanup-Image /RestoreHealth', True),
            ('chkdsk /f', False),
            ('sfc /scannow', True),
            ('defrag /c', False),
        ]
    },

    # ── SECURITY — Single Select ───────────────────────────────────────────────

    {
        'text': 'What is the purpose of a password manager?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Automatically resets passwords every 30 days', False),
            ('Securely stores and generates strong unique passwords for each account so users only need to remember one master password', True),
            ('Monitors login attempts across all websites', False),
            ('Shares passwords between team members', False),
        ]
    },
    {
        'text': 'What is an evil twin attack?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A malware that creates a copy of itself', False),
            ('A rogue wireless access point that mimics a legitimate network to intercept traffic from users who connect to it', True),
            ('An attack where two hackers work together', False),
            ('Malware that creates a duplicate user account', False),
        ]
    },
    {
        'text': 'What is the difference between symmetric and asymmetric encryption?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Symmetric is stronger than asymmetric encryption', False),
            ('Symmetric encryption uses the same key to encrypt and decrypt, while asymmetric uses a public key to encrypt and a private key to decrypt', True),
            ('Asymmetric encryption uses the same key for both operations', False),
            ('Symmetric encryption uses two different keys', False),
        ]
    },
    {
        'text': 'What does HTTPS provide that HTTP does not?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Faster web page loading speeds', False),
            ('Encryption of data transmitted between the browser and web server protecting it from interception', True),
            ('Automatic malware scanning of downloaded files', False),
            ('Two-factor authentication for all websites', False),
        ]
    },
    {
        'text': 'What is a digital certificate used for?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Storing encrypted user passwords', False),
            ('Verifying the identity of a website or entity and enabling encrypted communications', True),
            ('A physical token for multi-factor authentication', False),
            ('A license key for software products', False),
        ]
    },
    {
        'text': 'What is a brute force attack?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A physical attack on server hardware', False),
            ('Systematically trying every possible password combination until the correct one is found', True),
            ('Flooding a server with requests to take it offline', False),
            ('Intercepting network traffic to steal credentials', False),
        ]
    },
    {
        'text': 'What is a dictionary attack?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Using a list of common words and passwords to attempt login rather than trying every possible combination', True),
            ('An attack using stolen dictionary definitions to answer security questions', False),
            ('A DoS attack using large data files', False),
            ('Reading confidential files stored on public network shares', False),
        ]
    },
    {
        'text': 'What is the purpose of a CAPTCHA on a website?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('To encrypt form submissions', False),
            ('To distinguish human users from automated bots by presenting a challenge easy for humans but difficult for machines', True),
            ('To verify the user has a valid email address', False),
            ('To check if a browser supports JavaScript', False),
        ]
    },
    {
        'text': 'What is a watering hole attack?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('An attack that floods a network with traffic', False),
            ('Compromising a website frequently visited by the target group to infect visitors with malware', True),
            ('An attack that targets water treatment facilities', False),
            ('Intercepting communications at a coffee shop Wi-Fi', False),
        ]
    },
    {
        'text': 'What is the purpose of network segmentation from a security perspective?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('To improve network speed by splitting traffic', False),
            ('To limit the spread of malware and contain breaches by dividing the network into separate zones with controlled access between them', True),
            ('To reduce the number of IP addresses needed', False),
            ('To separate wired and wireless networks physically', False),
        ]
    },

    # ── SECURITY — Multi Select ────────────────────────────────────────────────

    {
        'text': 'Which TWO of the following are examples of social engineering attacks? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Phishing email asking for login credentials', True),
            ('SQL injection on a web form', False),
            ('Tailgating through a secure door', True),
            ('Port scanning a network', False),
        ]
    },
    {
        'text': 'Which TWO of the following best protect against phishing attacks? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('User security awareness training', True),
            ('Defragmenting hard drives regularly', False),
            ('Email filtering and anti-phishing tools', True),
            ('Increasing RAM on workstations', False),
        ]
    },
    {
        'text': 'Which TWO of the following are authentication factors used in multi-factor authentication? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Something you know — a password or PIN', True),
            ('Something you bought — a paid subscription', False),
            ('Something you are — a fingerprint or face scan', True),
            ('Something you read — a privacy policy', False),
        ]
    },
    {
        'text': 'Which TWO actions should be taken immediately when malware is discovered on a workstation? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Disconnect the computer from the network to prevent spreading', True),
            ('Continue using the computer normally while scanning', False),
            ('Back up critical user data before making changes', True),
            ('Immediately reinstall Windows without backing up', False),
        ]
    },
    {
        'text': 'Which TWO of the following are characteristics of a strong password? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('At least 12 characters long', True),
            ('Uses only lowercase letters for simplicity', False),
            ('Contains a mix of uppercase, lowercase, numbers, and symbols', True),
            ('Uses the user\'s name and birth year', False),
        ]
    },

    # ── SOFTWARE TROUBLESHOOTING — Single Select ──────────────────────────────

    {
        'text': 'A user reports that Windows Update is stuck at 0% and will not progress. What should the technician try first?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Reinstall Windows', False),
            ('Restart the Windows Update service and clear the update cache from C:\\Windows\\SoftwareDistribution', True),
            ('Disable Windows Update permanently', False),
            ('Replace the hard drive', False),
        ]
    },
    {
        'text': 'A user receives a "your clock is behind" error when visiting HTTPS websites. What is the cause?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The internet connection is too slow', False),
            ('The system date and time is incorrect causing SSL certificate validation to fail', True),
            ('The browser needs updating', False),
            ('The website certificate has expired', False),
        ]
    },
    {
        'text': 'An application displays "access denied" when a standard user tries to run it. What is the quickest fix?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Create a new user account', False),
            ('Right-click the application and select "Run as administrator"', True),
            ('Reinstall the application', False),
            ('Disable UAC', False),
        ]
    },
    {
        'text': 'A user reports their computer randomly plays audio but no visible application is open. What should be investigated?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Replace the speakers', False),
            ('Check background browser tabs, notifications, malware, and the system tray for hidden running applications', True),
            ('Update the audio driver', False),
            ('The sound card has failed', False),
        ]
    },
    {
        'text': 'A user reports that copy and paste stops working after using the computer for a few hours. What is the likely cause?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The keyboard has failed', False),
            ('A conflicting application or memory leak is interfering with the Windows clipboard service — restarting the rdpclip or explorer process usually fixes it', True),
            ('The hard drive is failing', False),
            ('Windows needs to be reinstalled', False),
        ]
    },
    {
        'text': 'A user cannot open any .exe files after a malware infection was removed. What likely happened?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The hard drive is corrupted', False),
            ('The malware changed the .exe file association in the registry — it needs to be restored', True),
            ('All .exe files were deleted by the antivirus', False),
            ('Windows needs to be reinstalled', False),
        ]
    },
    {
        'text': 'What does the Windows error code 0x80070002 typically indicate during Windows Update?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The hard drive is full', False),
            ('A required file was not found — often fixed by clearing the Windows Update cache', True),
            ('The internet connection is too slow', False),
            ('The Windows license has expired', False),
        ]
    },
    {
        'text': 'A user\'s computer takes 10 minutes to log in. Once logged in it runs normally. What is most likely causing the slow login?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The hard drive is failing', False),
            ('Too many startup programs or a Group Policy script is running at login — check startup items and login scripts', True),
            ('The monitor takes time to warm up', False),
            ('The RAM is insufficient', False),
        ]
    },
    {
        'text': 'A user installed a Windows update and now their VPN client no longer connects. What is the first thing to try?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Uninstall Windows', False),
            ('Check for an updated VPN client compatible with the new Windows version or roll back the update', True),
            ('Replace the network adapter', False),
            ('Reinstall the operating system', False),
        ]
    },
    {
        'text': 'What tool in Windows allows you to see exactly which DLL files a program is loading and which might be missing?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Task Manager', False),
            ('Process Monitor or Dependency Walker', True),
            ('Device Manager', False),
            ('Event Viewer', False),
        ]
    },

    # ── SOFTWARE TROUBLESHOOTING — Multi Select ───────────────────────────────

    {
        'text': 'Which TWO tools are most useful for diagnosing a Windows startup crash? (Select TWO)',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Event Viewer — check System and Application logs for errors', True),
            ('Disk Defragmenter', False),
            ('Windows Reliability Monitor — shows timeline of crashes and changes', True),
            ('Disk Cleanup', False),
        ]
    },
    {
        'text': 'Which TWO of the following are valid steps when an application fails to install? (Select TWO)',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Run the installer as administrator', True),
            ('Replace the CPU', False),
            ('Check that the system meets the minimum requirements for the application', True),
            ('Format the drive and reinstall Windows immediately', False),
        ]
    },
    {
        'text': 'A user\'s computer is running slowly. Which TWO tools should the technician use first to diagnose the issue? (Select TWO)',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Task Manager — check CPU, memory, and disk usage', True),
            ('MemTest86', False),
            ('Resource Monitor — see which processes are consuming the most resources', True),
            ('chkdsk /r', False),
        ]
    },
    {
        'text': 'Which TWO are common causes of the Windows Blue Screen of Death (BSOD)? (Select TWO)',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Faulty or incompatible drivers', True),
            ('Too many browser tabs open', False),
            ('Failing hardware such as bad RAM or a failing drive', True),
            ('Using the wrong screen resolution', False),
        ]
    },

    # ── OPERATIONAL PROCEDURES — Single Select ────────────────────────────────

    {
        'text': 'What is the purpose of a privacy policy in an organization?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('To prevent employees from using social media at work', False),
            ('To define how the organization collects, uses, stores, and protects personal data of customers and employees', True),
            ('To block access to private websites', False),
            ('To set rules for private office conversations', False),
        ]
    },
    {
        'text': 'What does GDPR stand for and who does it affect?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('General Data Protection Regulation — affects any organization that handles personal data of EU residents', True),
            ('General Device Privacy Rules — affects hardware manufacturers only', False),
            ('Global Data Processing Regulation — applies only to cloud providers', False),
            ('Government Data Privacy Requirement — applies only to government agencies', False),
        ]
    },
    {
        'text': 'What is the purpose of a clean desk policy?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('To improve employee productivity through organization', False),
            ('To ensure sensitive documents and credentials are not left visible when a workstation is unattended preventing unauthorized access', True),
            ('To maintain a tidy office for customer visits', False),
            ('To reduce clutter around computer equipment for fire safety', False),
        ]
    },
    {
        'text': 'What is the correct method for disposing of confidential paper documents?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Throw them in the recycling bin', False),
            ('Shred them using a cross-cut shredder before disposal', True),
            ('Tear them in half and place in general waste', False),
            ('Store them in a locked cabinet permanently', False),
        ]
    },
    {
        'text': 'What is an air-gapped computer?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A computer with extra cooling fans for heat management', False),
            ('A computer that is physically isolated from all unsecured networks including the internet making it very difficult to attack remotely', True),
            ('A laptop without a battery that runs only on AC power', False),
            ('A computer stored in a secure server room', False),
        ]
    },
    {
        'text': 'What does it mean to sanitize a hard drive before disposal?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Cleaning the drive physically with isopropyl alcohol', False),
            ('Overwriting all data multiple times or physically destroying the drive so that data cannot be recovered', True),
            ('Formatting the drive and reinstalling Windows', False),
            ('Deleting all files and emptying the recycle bin', False),
        ]
    },
    {
        'text': 'What is the purpose of a Non-Disclosure Agreement (NDA) in IT work?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Prevents technicians from working for competitors', False),
            ('Legally binds a technician or employee to keep confidential information private and not disclose it to unauthorized parties', True),
            ('Prevents customers from sharing negative reviews', False),
            ('A contract that limits IT support to specific tasks', False),
        ]
    },
    {
        'text': 'What is the first thing a technician should do when arriving at a user\'s desk for a support call?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Immediately start troubleshooting', False),
            ('Introduce yourself, confirm the reported issue with the user, and ask clarifying questions to understand the problem', True),
            ('Ask for the user\'s password', False),
            ('Reboot the computer before doing anything else', False),
        ]
    },
    {
        'text': 'What is meant by "scope creep" in IT project management?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A security vulnerability that grows over time', False),
            ('The gradual expansion of a project beyond its original objectives without proper change control authorization', True),
            ('When a technician works outside their designated area', False),
            ('A virus that slowly spreads through a network', False),
        ]
    },
    {
        'text': 'What is the purpose of an end-user license agreement (EULA)?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A warranty for hardware products', False),
            ('A legal contract between the software publisher and the user defining how the software may be used', True),
            ('A subscription agreement for cloud services', False),
            ('A training certificate for software applications', False),
        ]
    },
    {
        'text': 'What is the proper response if a technician accidentally breaks something while repairing a customer\'s device?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Hide it and hope the customer does not notice', False),
            ('Immediately inform the customer, document what happened, and arrange for repair or replacement', True),
            ('Blame the damage on a pre-existing issue', False),
            ('Complete the repair and only mention it if asked', False),
        ]
    },
    {
        'text': 'What is the risk of installing unlicensed or pirated software on a company computer?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The software will run slightly slower', False),
            ('Legal liability for the organization, potential fines, and security risks as pirated software often contains malware', True),
            ('The software will only work for 30 days', False),
            ('It uses more RAM than licensed software', False),
        ]
    },

    # ── OPERATIONAL PROCEDURES — Multi Select ─────────────────────────────────

    {
        'text': 'Which TWO are examples of regulated data that require special handling? (Select TWO)',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('PHI — Protected Health Information', True),
            ('Public marketing brochures', False),
            ('PII — Personally Identifiable Information', True),
            ('Open source software documentation', False),
        ]
    },
    {
        'text': 'Which TWO of the following should be included in a change management request? (Select TWO)',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Description of the change and its purpose', True),
            ('The technician\'s personal opinion about the change', False),
            ('A rollback plan in case the change causes problems', True),
            ('A list of all other tickets the technician has open', False),
        ]
    },
    {
        'text': 'Which TWO of the following are proper methods for physically destroying a hard drive that contains sensitive data? (Select TWO)',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Degaussing — exposing it to a powerful magnetic field', True),
            ('Formatting the drive with a quick format', False),
            ('Shredding the drive in a certified e-waste shredder', True),
            ('Deleting all files and emptying the Recycle Bin', False),
        ]
    },
    {
        'text': 'Which TWO behaviors demonstrate professional conduct when working at a customer site? (Select TWO)',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Maintaining confidentiality about what you observe on the customer\'s screens', True),
            ('Sharing details of the customer\'s setup with coworkers after the visit', False),
            ('Communicating clearly with the user about what work is being performed', True),
            ('Accessing files unrelated to the support task out of curiosity', False),
        ]
    },

    # ── MIXED DOMAINS — Additional questions ──────────────────────────────────

    {
        'text': 'What is the purpose of the Windows "Remote Assistance" feature?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Allows a technician to fully control a remote computer without the user\'s knowledge', False),
            ('Allows a user to invite a trusted person to view or control their desktop to provide help while the user watches', True),
            ('A tool for remotely installing Windows on another computer', False),
            ('Remote Assistance and Remote Desktop are identical features', False),
        ]
    },
    {
        'text': 'What is a TPM chip and why is it required for Windows 11?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Thermal Protection Module — prevents overheating', False),
            ('Trusted Platform Module — a hardware chip that stores cryptographic keys used for BitLocker and secure boot required for Windows 11 security features', True),
            ('Total Power Management chip — manages battery life', False),
            ('Transfer Protocol Manager — manages network security', False),
        ]
    },
    {
        'text': 'What does the acronym BYOD mean and what is a key policy concern?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Build Your Own Device — employees assemble company computers', False),
            ('Bring Your Own Device — employees use personal devices for work raising concerns about data security, malware, and data separation', True),
            ('Buy Your Own Device — employees purchase approved company devices', False),
            ('Back Up Your Own Data — employees manage their own backups', False),
        ]
    },
    {
        'text': 'What is the purpose of Mobile Device Management (MDM) software?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Managing mobile phone bills for employees', False),
            ('Centrally managing, monitoring, and securing mobile devices used in an organization including enforcing policies and remotely wiping lost devices', True),
            ('Repairing damaged mobile device screens', False),
            ('Tracking employee location via their phones', False),
        ]
    },
    {
        'text': 'What is a sandbox in cybersecurity?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A secure location for storing backup data', False),
            ('An isolated environment used to run and analyze suspicious software safely without risking the host system', True),
            ('A type of firewall that separates networks', False),
            ('A test environment for new employee devices', False),
        ]
    },
    {
        'text': 'What is the purpose of log monitoring in a security context?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Storing application error messages for developers', False),
            ('Detecting suspicious activity, unauthorized access attempts, and security incidents by analyzing system and security event logs', True),
            ('Tracking user productivity', False),
            ('Monitoring internet bandwidth usage', False),
        ]
    },
    {
        'text': 'Which TWO of the following are signs that a computer may be infected with cryptomining malware? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('CPU or GPU usage is very high with no obvious applications running', True),
            ('The computer runs faster than usual', False),
            ('The computer runs hot and fans run at maximum speed constantly', True),
            ('The screen brightness keeps changing', False),
        ]
    },
    {
        'text': 'Which TWO of the following describe a rootkit? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('It hides deep in the operating system making it very difficult to detect', True),
            ('It encrypts the user\'s files and demands a ransom', False),
            ('It may hide other malware from antivirus software', True),
            ('It always displays pop-up advertisements', False),
        ]
    },
    {
        'text': 'What is meant by the term "defense in depth"?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Using a very strong firewall as the only security measure', False),
            ('Implementing multiple layers of security so that if one layer fails others still protect the system', True),
            ('Burying network cables underground for physical protection', False),
            ('Having a deep understanding of cybersecurity principles', False),
        ]
    },
    {
        'text': 'What is the purpose of a certificate authority (CA)?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('To issue employee ID cards', False),
            ('A trusted entity that issues and signs digital certificates verifying the identity of websites and organizations', True),
            ('To manage SSL certificate renewals automatically', False),
            ('To block connections to untrusted websites', False),
        ]
    },
    {
        'text': 'What type of malware disguises itself as a useful application but opens a backdoor for attackers?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Worm', False),
            ('Trojan horse', True),
            ('Adware', False),
            ('Spyware', False),
        ]
    },
    {
        'text': 'A company wants to allow employees to work from home and access internal file servers. What is the most secure solution?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Make the file server publicly accessible on the internet', False),
            ('Implement a VPN so remote employees connect through an encrypted tunnel to the internal network', True),
            ('Share files via personal email', False),
            ('Use a free cloud storage service', False),
        ]
    },
    {
        'text': 'What is the purpose of penetration testing?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Testing network cable connections for continuity', False),
            ('Authorized simulated attacks on a system to identify security vulnerabilities before malicious attackers can exploit them', True),
            ('Testing printer throughput speed', False),
            ('Checking if server racks are properly secured', False),
        ]
    },
    {
        'text': 'Which TWO of the following are best practices for securing a wireless network? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Use WPA2 or WPA3 encryption', True),
            ('Leave the network open for easy guest access', False),
            ('Change the default router admin credentials', True),
            ('Use WEP encryption for compatibility', False),
        ]
    },
    {
        'text': 'Which TWO of the following are true about the principle of least privilege? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Users should only have the permissions needed to perform their job', True),
            ('All users should have administrator rights for efficiency', False),
            ('It reduces the damage that can be done if an account is compromised', True),
            ('Only applies to server accounts not workstation accounts', False),
        ]
    },
    {
        'text': 'What is the Windows "Action Center" (Security and Maintenance)?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A tool for managing Windows action shortcuts', False),
            ('A central dashboard that monitors security status, maintenance issues, and displays alerts when Windows needs attention', True),
            ('A task automation tool similar to Task Scheduler', False),
            ('The Windows Store for downloading applications', False),
        ]
    },
    {
        'text': 'What is the purpose of a recovery partition on a Windows computer?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Stores backup copies of user documents', False),
            ('Contains a factory image of Windows used to restore the computer to its original state without installation media', True),
            ('Stores Windows Update files for offline installation', False),
            ('A hidden partition that stores the BitLocker encryption key', False),
        ]
    },
    {
        'text': 'What happens to local user account data when a Windows computer is joined to a domain?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Local accounts are automatically deleted', False),
            ('Local accounts remain but users log in with domain credentials — local accounts are typically used only for emergency access', True),
            ('All user data is automatically migrated to the domain controller', False),
            ('Local accounts are converted to domain accounts automatically', False),
        ]
    },
    {
        'text': 'What is the purpose of Windows "Device Encryption" on consumer devices?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Prevents unauthorized software from being installed', False),
            ('A simplified version of BitLocker that automatically encrypts the system drive on compatible devices to protect data if the device is lost or stolen', True),
            ('Encrypts individual files selected by the user', False),
            ('Manages which devices are allowed to connect via USB', False),
        ]
    },
    {
        'text': 'Which TWO of the following would be found in a Windows Security event log? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Failed login attempts', True),
            ('Hard drive temperature readings', False),
            ('Successful user logons and logoffs', True),
            ('Application crash reports', False),
        ]
    },
    {
        'text': 'Which TWO of the following are valid reasons to roll back a device driver in Windows? (Select TWO)',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('A new driver update caused the device to stop working', True),
            ('The device is too old to have drivers', False),
            ('A driver update is causing system instability or BSODs', True),
            ('The device manager shows a yellow exclamation mark', False),
        ]
    },
    {
        'text': 'What is the primary purpose of Windows File History?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Tracks changes made to Windows system files', False),
            ('Automatically backs up personal files to an external drive or network location allowing previous versions to be restored', True),
            ('Logs all file access and modification events', False),
            ('Compresses old files to save disk space', False),
        ]
    },
    {
        'text': 'What is the risk of disabling User Account Control (UAC) in Windows?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Windows will run slower without UAC', False),
            ('Malware and unauthorized programs can make system changes without any prompt or approval significantly increasing security risk', True),
            ('Standard users will no longer be able to log in', False),
            ('BitLocker will automatically disable', False),
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
    core2 = Question.query.filter_by(exam='core2').count()
    multi = Question.query.filter_by(exam='core2', multi_select=True).count()
    print(f'Added {added} questions. Skipped {skipped}.')
    print(f'Core 2 total: {core2} | Multi-select Core 2: {multi} | Overall: {total}')