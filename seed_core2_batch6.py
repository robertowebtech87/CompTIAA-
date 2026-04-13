from app import app, db
from models import Question, Choice

questions_data = [

    # ── OPERATING SYSTEMS — Windows Administration ────────────────────────────

    {
        'text': 'What is the purpose of the Windows "Computer Management" console?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A tool exclusively for managing hardware drivers', False),
            ('A centralized console that combines Device Manager, Disk Management, Event Viewer, Local Users and Groups, and other management tools in one place', True),
            ('A remote management tool for connecting to other computers', False),
            ('A tool for monitoring network performance', False),
        ]
    },
    {
        'text': 'What does the Windows command "gpresult /r" do?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Resets all Group Policy settings to default', False),
            ('Displays the Group Policy settings currently applied to the user and computer', True),
            ('Forces an immediate Group Policy update', False),
            ('Lists all available Group Policy templates', False),
        ]
    },
    {
        'text': 'What is the Windows "Credential Manager" used for?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Managing BitLocker encryption keys', False),
            ('Storing and managing saved usernames and passwords for websites and network resources', True),
            ('Managing digital certificates', False),
            ('Storing VPN credentials only', False),
        ]
    },
    {
        'text': 'What is a Windows "HomeGroup" and why was it removed?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A parental control feature removed due to privacy concerns', False),
            ('A simple home network sharing feature removed in Windows 10 version 1803 because it was rarely used and caused confusion', True),
            ('A home edition feature upgraded to WorkGroup in Windows 11', False),
            ('A feature replaced by OneDrive for file sharing', False),
        ]
    },
    {
        'text': 'What is the purpose of the "net localgroup administrators" command?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Lists all users on the local network', False),
            ('Displays or modifies the local Administrators group membership on a Windows computer', True),
            ('Creates a new local administrator group', False),
            ('Resets the administrator password', False),
        ]
    },
    {
        'text': 'What is Windows "Storage Spaces" used for?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Managing cloud storage quotas', False),
            ('Combining multiple physical drives into a single logical storage pool with optional redundancy', True),
            ('Compressing files to save disk space', False),
            ('Creating virtual hard disk files', False),
        ]
    },
    {
        'text': 'What command in Windows shows all running processes from the command line?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('proclist', False),
            ('tasklist', True),
            ('pslist', False),
            ('runlist', False),
        ]
    },
    {
        'text': 'What is the purpose of "Windows Sandbox"?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A backup environment that activates when Windows becomes corrupted', False),
            ('A lightweight isolated VM built into Windows Pro and Enterprise for safely running untrusted software', True),
            ('A secure area of memory for critical system processes', False),
            ('A testing environment for Windows updates before they are installed', False),
        ]
    },
    {
        'text': 'What does the acronym BSOD stand for and what causes it?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Boot System Operational Delay — caused by slow hard drives', False),
            ('Blue Screen of Death — a critical system error caused by hardware failure, driver issues, or corrupted system files that forces Windows to stop', True),
            ('Basic System Override Diagnostic — a planned diagnostic mode', False),
            ('Blue Screen of Data — caused by database corruption', False),
        ]
    },
    {
        'text': 'What is "Fast Startup" in Windows and what problem can it cause?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A feature that speeds up login — can cause incorrect passwords to be accepted', False),
            ('A hybrid shutdown that saves the kernel session to disk for faster boot — can cause issues with dual boot systems and some driver updates not applying', True),
            ('An SSD optimization feature — can cause HDD wear', False),
            ('A network feature that preloads frequently used apps — can use too much RAM', False),
        ]
    },

    # ── OPERATING SYSTEMS — Multi Select ──────────────────────────────────────

    {
        'text': 'Which TWO of the following are correct ways to access the Windows Recovery Environment (WinRE)? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Hold Shift and click Restart from the Start menu', True),
            ('Press F2 during POST to enter WinRE', False),
            ('Boot from Windows installation media and select Repair your computer', True),
            ('Type winre in the Run dialog', False),
        ]
    },
    {
        'text': 'Which TWO of the following are true about Windows 11 hardware requirements? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Requires a TPM 2.0 chip', True),
            ('Requires at least 2GB of RAM', False),
            ('Requires Secure Boot capable UEFI firmware', True),
            ('Requires a dedicated GPU', False),
        ]
    },
    {
        'text': 'Which TWO of the following are advantages of using NTFS over FAT32? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('NTFS supports file permissions and encryption', True),
            ('FAT32 is slower than NTFS on all operations', False),
            ('NTFS supports files larger than 4GB', True),
            ('NTFS works on all operating systems without drivers', False),
        ]
    },
    {
        'text': 'Which TWO are correct statements about Windows User Account Control (UAC)? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('UAC prompts standard users to enter admin credentials for elevated tasks', True),
            ('UAC can be completely disabled without any security risk', False),
            ('UAC helps prevent unauthorized changes to the operating system', True),
            ('UAC only affects administrator accounts', False),
        ]
    },
    {
        'text': 'Which TWO Windows tools can be used to manage startup programs? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Task Manager — Startup tab', True),
            ('Device Manager', False),
            ('msconfig — Startup tab (Windows 8 and earlier)', True),
            ('Disk Management', False),
        ]
    },

    # ── SECURITY — Single Select ───────────────────────────────────────────────

    {
        'text': 'What is "smishing"?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A phishing attack using social media messages', False),
            ('SMS phishing — fraudulent text messages designed to trick recipients into clicking malicious links or revealing information', True),
            ('A phishing attack that targets small businesses', False),
            ('A type of malware that spreads via Bluetooth', False),
        ]
    },
    {
        'text': 'What is a "logic bomb"?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A physical device used to destroy server hardware', False),
            ('Malicious code hidden in software that activates when a specific condition is met such as a date or a user action', True),
            ('A type of DDoS attack that overwhelms servers with logical operations', False),
            ('A password cracking technique using logical patterns', False),
        ]
    },
    {
        'text': 'What is "pharming"?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A large-scale phishing campaign targeting many users simultaneously', False),
            ('Redirecting users from legitimate websites to fraudulent ones by corrupting DNS or modifying the hosts file', True),
            ('Growing a botnet by infecting many computers at once', False),
            ('A social engineering technique used in agricultural businesses', False),
        ]
    },
    {
        'text': 'What is the purpose of a "honeypot" in cybersecurity?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A secure vault for storing encryption keys', False),
            ('A decoy system designed to attract attackers, detect intrusion attempts, and study attack methods without risking real systems', True),
            ('A password manager for storing credentials securely', False),
            ('A type of firewall that traps malicious traffic', False),
        ]
    },
    {
        'text': 'What is "credential stuffing"?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Adding extra characters to passwords to make them stronger', False),
            ('Using lists of username and password combinations stolen from data breaches to attempt login on other services', True),
            ('Stuffing too many credentials into a single password manager', False),
            ('A physical attack where printed credentials are hidden in the office', False),
        ]
    },
    {
        'text': 'What does "security through obscurity" mean and why is it not recommended as a primary security strategy?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Hiding servers in secure locations — not recommended because servers can be physically stolen', False),
            ('Relying on secrecy of design or implementation rather than proper security controls — not recommended because once discovered the system has no real protection', True),
            ('Encrypting data so it appears as random noise — not recommended because encryption is slow', False),
            ('Using obscure programming languages for better security — not recommended because developers are harder to find', False),
        ]
    },
    {
        'text': 'What is "ransomware as a service" (RaaS)?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A legitimate security service that tests ransomware defenses', False),
            ('A criminal business model where ransomware developers rent their tools to other criminals in exchange for a share of the ransom payments', True),
            ('A cloud service for backing up data against ransomware', False),
            ('A government service for recovering ransomware-encrypted files', False),
        ]
    },
    {
        'text': 'What is the purpose of a "security token" in authentication?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Stores all the user\'s passwords securely', False),
            ('A physical or software device that generates a time-based one-time code used as a second factor in MFA', True),
            ('A digital signature that verifies software integrity', False),
            ('A hardware key that replaces the need for a password entirely', False),
        ]
    },
    {
        'text': 'What is "shoulder surfing" and how can it be prevented?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Stealing data from shared network drives — prevented by proper permissions', False),
            ('Observing someone\'s screen or keyboard to steal credentials — prevented by privacy screens and awareness', True),
            ('Intercepting wireless traffic — prevented by using WPA3', False),
            ('Installing malware via USB — prevented by disabling USB ports', False),
        ]
    },
    {
        'text': 'What is "data exfiltration"?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Deleting sensitive data from company servers', False),
            ('The unauthorized transfer of data from an organization to an external location controlled by an attacker', True),
            ('Encrypting data for secure external transmission', False),
            ('Removing old data from systems to comply with retention policies', False),
        ]
    },

    # ── SECURITY — Multi Select ────────────────────────────────────────────────

    {
        'text': 'Which TWO of the following are true about ransomware attacks? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Paying the ransom does not guarantee file recovery', True),
            ('Ransomware can only spread through email attachments', False),
            ('Regular offline backups are the most effective defense against ransomware', True),
            ('Ransomware only targets large enterprises', False),
        ]
    },
    {
        'text': 'Which TWO of the following are physical security controls? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Mantrap or access control vestibule', True),
            ('Firewall rules', False),
            ('Security cameras and badge access systems', True),
            ('Password complexity requirements', False),
        ]
    },
    {
        'text': 'Which TWO are true about encryption? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Encryption protects data confidentiality', True),
            ('Encrypted data cannot be decrypted even with the correct key', False),
            ('Encryption does not protect data if the encryption key is compromised', True),
            ('Encryption automatically verifies data integrity', False),
        ]
    },
    {
        'text': 'Which TWO of the following help protect against man-in-the-middle attacks? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Using HTTPS with valid SSL certificates', True),
            ('Using a faster internet connection', False),
            ('Using a VPN to encrypt traffic', True),
            ('Using a longer password', False),
        ]
    },
    {
        'text': 'Which TWO are indicators that a computer may be infected with malware? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Unusual network activity and connections to unknown IP addresses', True),
            ('The computer starts faster than usual', False),
            ('Antivirus software has been disabled without user action', True),
            ('Windows Update completes successfully', False),
        ]
    },

    # ── SOFTWARE TROUBLESHOOTING — Single Select ──────────────────────────────

    {
        'text': 'A user reports their computer shows "Operating System not found" on boot. What should be checked first?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Replace the RAM immediately', False),
            ('Check the BIOS boot order and verify the drive is detected — the OS drive may not be set as first boot device', True),
            ('Reinstall Windows immediately', False),
            ('Replace the motherboard', False),
        ]
    },
    {
        'text': 'A user reports that Windows Explorer keeps crashing and restarting. What should the technician try?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Replace the hard drive', False),
            ('Run sfc /scannow to check for corrupted system files and check for conflicting shell extensions', True),
            ('Add more RAM', False),
            ('Reinstall the graphics driver', False),
        ]
    },
    {
        'text': 'A user receives "This app can\'t run on your PC" when trying to install software. What is the most likely cause?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The hard drive is failing', False),
            ('The application is designed for a different processor architecture — for example a 64-bit only app on a 32-bit OS', True),
            ('The user does not have internet access', False),
            ('The monitor resolution is too low', False),
        ]
    },
    {
        'text': 'What does the Windows error "The application was unable to start correctly 0xc000007b" typically indicate?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The hard drive has bad sectors', False),
            ('A 32-bit application is trying to load a 64-bit DLL or a required runtime component is missing or corrupted', True),
            ('The user account does not have permission to run the app', False),
            ('Windows needs to be activated', False),
        ]
    },
    {
        'text': 'A user reports Windows takes 15 minutes to shut down. What is the most likely cause?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The hard drive is too full', False),
            ('A service or process is not responding to the shutdown signal — check Event Viewer for timeout entries', True),
            ('The RAM needs to be upgraded', False),
            ('Windows Update is downloading during shutdown', False),
        ]
    },
    {
        'text': 'A user reports that their microphone does not work in video calls but does work in the Sound settings test. What is the issue?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The microphone hardware has failed', False),
            ('The video call application does not have permission to access the microphone — check app permissions in Windows Settings', True),
            ('The audio driver needs to be reinstalled', False),
            ('The USB port is faulty', False),
        ]
    },
    {
        'text': 'After a Windows update a user\'s mapped network drives no longer connect at login. What is the likely cause?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The network switch has failed', False),
            ('The update changed network settings or a Group Policy that handles drive mapping needs to be refreshed', True),
            ('The file server is offline', False),
            ('The user password has expired', False),
        ]
    },
    {
        'text': 'A user reports that the on-screen keyboard appears automatically even though they have not enabled it. What should the technician check?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The physical keyboard has failed', False),
            ('Accessibility settings — the on-screen keyboard may have been accidentally enabled via Ease of Access or a sticky keys shortcut', True),
            ('A virus has infected the keyboard driver', False),
            ('The touchscreen driver is interfering', False),
        ]
    },
    {
        'text': 'A user\'s Windows Search is not finding files that definitely exist on the drive. What should the technician do?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Replace the hard drive', False),
            ('Rebuild the Windows Search index from Indexing Options in Control Panel', True),
            ('Reinstall Windows', False),
            ('Run chkdsk to repair file system errors', False),
        ]
    },
    {
        'text': 'A user reports that their computer displays the correct time but the wrong date after every restart. What component needs replacing?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The operating system needs reinstalling', False),
            ('The CMOS battery on the motherboard — it maintains BIOS settings including date and time when powered off', True),
            ('The RAM is losing configuration data', False),
            ('The hard drive is failing', False),
        ]
    },

    # ── SOFTWARE TROUBLESHOOTING — Multi Select ───────────────────────────────

    {
        'text': 'Which TWO are common symptoms of insufficient RAM in Windows? (Select TWO)',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Constant high disk usage as Windows uses the pagefile heavily', True),
            ('The monitor displays incorrect colors', False),
            ('Applications crash or respond slowly especially when multiple are open', True),
            ('The computer runs faster than expected', False),
        ]
    },
    {
        'text': 'Which TWO of the following Windows tools help identify which application is causing high CPU usage? (Select TWO)',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Task Manager — Processes tab sorted by CPU', True),
            ('chkdsk', False),
            ('Resource Monitor — CPU tab showing per-process usage', True),
            ('Disk Defragmenter', False),
        ]
    },
    {
        'text': 'Which TWO steps should be taken when a Windows application crashes and generates an error report? (Select TWO)',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Check Event Viewer Application log for the specific error details', True),
            ('Immediately reinstall Windows', False),
            ('Check if an application update is available that fixes the crash', True),
            ('Replace the hard drive', False),
        ]
    },

    # ── OPERATIONAL PROCEDURES — Single Select ────────────────────────────────

    {
        'text': 'What is "social engineering" in the context of security?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Building relationships with colleagues to get promoted', False),
            ('Manipulating people psychologically to bypass security controls or reveal confidential information', True),
            ('Engineering secure social media platforms', False),
            ('Using social media to recruit IT professionals', False),
        ]
    },
    {
        'text': 'What is a "tabletop exercise" in IT security?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Testing physical security by attempting to break into a facility', False),
            ('A discussion-based simulation where team members talk through their responses to a hypothetical security incident without actually executing anything', True),
            ('A physical exercise where IT equipment is set up on tables for testing', False),
            ('A training exercise for setting up network equipment', False),
        ]
    },
    {
        'text': 'What is "mean time between failures" (MTBF)?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The average time it takes to repair a failed system', False),
            ('The average time a device or system is expected to operate between failures — a measure of reliability', True),
            ('The maximum time allowed before a backup must be performed', False),
            ('The average time between security incidents', False),
        ]
    },
    {
        'text': 'What is "mean time to repair" (MTTR)?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The average time between equipment failures', False),
            ('The average time required to restore a failed system back to normal operation', True),
            ('The maximum time allowed to resolve a support ticket', False),
            ('The minimum time needed between system restarts', False),
        ]
    },
    {
        'text': 'What is the purpose of a "post-mortem" or "lessons learned" review after an IT incident?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('To assign blame to the technician who caused the incident', False),
            ('To analyze what happened, why it happened, and how to prevent similar incidents in the future', True),
            ('To calculate the financial cost of the incident for insurance', False),
            ('To document the incident for legal proceedings', False),
        ]
    },
    {
        'text': 'What is "configuration management" in IT?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Managing email configuration for all users', False),
            ('Tracking and controlling changes to system configurations to maintain integrity and support troubleshooting', True),
            ('Configuring new hardware when it arrives', False),
            ('Managing network switch port configurations', False),
        ]
    },
    {
        'text': 'A technician is asked to set up a new employee\'s computer. What should be done before handing it over?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Just install Windows and give it to the employee', False),
            ('Install and configure the OS, apply all updates, install required software, join the domain, configure security settings, and verify everything works', True),
            ('Give the employee the Windows disk and let them set it up', False),
            ('Copy settings from another employee\'s computer without customization', False),
        ]
    },
    {
        'text': 'What is "two-person integrity" (TPI) in IT operations?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Requiring two IT technicians to be physically present for sensitive or high-risk operations to prevent fraud or error', True),
            ('A password policy requiring two different passwords per account', False),
            ('A backup policy requiring two copies of all data', False),
            ('Having two administrators approve all IT purchases', False),
        ]
    },
    {
        'text': 'What should a technician do if they find unlicensed software installed on a company computer?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Ignore it as it is not an IT concern', False),
            ('Report it to management and follow the company\'s software compliance policy — do not simply delete it without authorization', True),
            ('Delete it immediately without telling anyone', False),
            ('Purchase a license for the user without approval', False),
        ]
    },
    {
        'text': 'What is the correct response when a user asks a technician to access another employee\'s email?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Access it if the requesting user is a manager', False),
            ('Decline and explain that accessing another employee\'s email requires proper authorization and must follow company policy and legal requirements', True),
            ('Access it and report what you find to HR', False),
            ('Grant the request if the employee is absent', False),
        ]
    },

    # ── OPERATIONAL PROCEDURES — Multi Select ─────────────────────────────────

    {
        'text': 'Which TWO are examples of proper data handling practices? (Select TWO)',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Encrypting sensitive data both in transit and at rest', True),
            ('Storing customer passwords in plain text for easy access', False),
            ('Using role-based access control to limit who can access sensitive data', True),
            ('Sharing customer data freely within the organization for efficiency', False),
        ]
    },
    {
        'text': 'Which TWO are correct statements about incident response? (Select TWO)',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Containment should happen before eradication to prevent further damage', True),
            ('All incidents should be resolved without documentation to save time', False),
            ('Post-incident review helps prevent recurrence of similar incidents', True),
            ('Minor incidents do not need to be documented', False),
        ]
    },
    {
        'text': 'Which TWO of the following are best practices for IT asset disposal? (Select TWO)',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Sanitizing storage drives before disposal to prevent data recovery', True),
            ('Throwing old computers in regular trash to save disposal costs', False),
            ('Using a certified e-waste recycler for electronic components', True),
            ('Donating computers with data still on the drives', False),
        ]
    },
    {
        'text': 'Which TWO behaviors could result in a data breach that a technician should be aware of? (Select TWO)',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Leaving a laptop with sensitive data unattended in a public place', True),
            ('Using a VPN when working remotely', False),
            ('Sending unencrypted sensitive data via regular email', True),
            ('Locking the computer screen when stepping away', False),
        ]
    },

    # ── MIXED — Additional Core 2 Questions ───────────────────────────────────

    {
        'text': 'What is the difference between a virus scanner and an anti-malware tool?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('They are identical tools with different names', False),
            ('A virus scanner focuses on traditional viruses while anti-malware covers a broader range of threats including spyware, ransomware, and adware — modern tools usually combine both', True),
            ('Anti-malware is only used for Mac systems', False),
            ('Virus scanners work in real time while anti-malware only works on demand', False),
        ]
    },
    {
        'text': 'What is "fileless malware"?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Malware that deletes all files on the system', False),
            ('Malware that operates entirely in memory without writing files to disk making it harder to detect with traditional antivirus', True),
            ('A type of virus that hides inside legitimate files', False),
            ('Malware that only affects empty storage drives', False),
        ]
    },
    {
        'text': 'What is a "pass the hash" attack?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A brute force attack on hashed passwords', False),
            ('Using a captured password hash to authenticate to a system without knowing the actual password', True),
            ('Passing malware between systems using hash values', False),
            ('A technique for cracking MD5 password hashes', False),
        ]
    },
    {
        'text': 'What Windows feature logs all failed and successful login attempts?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Task Manager', False),
            ('Windows Security Event Log', True),
            ('Windows Defender', False),
            ('System Information', False),
        ]
    },
    {
        'text': 'What is "port knocking" in network security?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Physically testing network ports for connectivity', False),
            ('A method of opening firewall ports by sending connection attempts to a sequence of closed ports as a secret knock', True),
            ('Scanning all ports on a network to find open ones', False),
            ('A technique for forwarding traffic between ports', False),
        ]
    },
    {
        'text': 'What is the Windows "Local Security Policy" used for?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Managing firewall rules for individual applications', False),
            ('Configuring security settings on a standalone Windows computer including password policies account lockout and audit policies', True),
            ('Managing Windows Defender scan schedules', False),
            ('Configuring BitLocker encryption settings', False),
        ]
    },
    {
        'text': 'A company wants to prevent employees from copying data to USB drives. What is the best way to enforce this?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Ask employees not to use USB drives', False),
            ('Use Group Policy or endpoint security software to disable USB storage devices on company computers', True),
            ('Remove USB ports physically from all computers', False),
            ('Monitor USB usage and discipline violators', False),
        ]
    },
    {
        'text': 'What is "zero trust" security architecture?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A network with no firewall or security rules', False),
            ('A security model that assumes no user or device should be trusted by default even inside the network requiring verification for every access request', True),
            ('A policy of trusting no external vendors', False),
            ('A security approach that uses no encryption', False),
        ]
    },
    {
        'text': 'Which TWO of the following are examples of technical security controls? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Firewall rules blocking unauthorized traffic', True),
            ('Security awareness training for employees', False),
            ('Antivirus software monitoring for malware', True),
            ('Physical locks on server room doors', False),
        ]
    },
    {
        'text': 'Which TWO of the following are true about VPNs? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('VPNs encrypt traffic between the client and the VPN server', True),
            ('VPNs make the user completely anonymous online', False),
            ('VPNs allow remote workers to securely access internal company resources', True),
            ('VPNs protect against malware on the local device', False),
        ]
    },
    {
        'text': 'What is the purpose of "input validation" in application security?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Validating that keyboard input is registered correctly', False),
            ('Ensuring that data entered into an application meets expected criteria to prevent injection attacks and unexpected behavior', True),
            ('Verifying that user login credentials are correct', False),
            ('Checking that form fields are not left empty', False),
        ]
    },
    {
        'text': 'What is the correct action when a security certificate warning appears in a browser?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Always click through and proceed — warnings are just formalities', False),
            ('Do not proceed — investigate the warning as the certificate may be expired, self-signed, or the site may be spoofed', True),
            ('Refresh the page to clear the warning', False),
            ('Disable HTTPS for the site to avoid the warning', False),
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