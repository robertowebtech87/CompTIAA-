import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app import app, db
from models import Question, Choice

questions_data = [

    # ── OPERATING SYSTEMS — Windows Deep Dive ─────────────────────────────────

    {
        'text': 'What is the purpose of the Windows "Sysprep" tool?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A system repair tool for corrupted Windows installations', False),
            ('Prepares a Windows installation for cloning or deployment by generalizing it and removing machine-specific information like SID and computer name', True),
            ('A tool for creating system restore points', False),
            ('A performance optimization tool', False),
        ]
    },
    {
        'text': 'What does "joining a domain" mean for a Windows computer?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Connecting the computer to the internet', False),
            ('Registering the computer with an Active Directory server so it can be centrally managed and users can log in with domain credentials', True),
            ('Adding the computer to a homegroup', False),
            ('Connecting to a workgroup network', False),
        ]
    },
    {
        'text': 'What is Active Directory and what is its primary purpose?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A file sharing service for Windows networks', False),
            ('A Microsoft directory service that centralizes management of users computers groups and policies across a Windows domain network', True),
            ('A database for storing application settings', False),
            ('A backup service for Windows servers', False),
        ]
    },
    {
        'text': 'What is the Windows "Print Management" console used for?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Managing print credits and billing', False),
            ('Centrally managing printers and print servers across a network from one interface', True),
            ('Monitoring ink and toner levels remotely', False),
            ('Scheduling print jobs for off-peak hours', False),
        ]
    },
    {
        'text': 'What is the difference between "Sleep" and "Hibernate" in Windows power management?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('They are identical functions with different names', False),
            ('Sleep saves the session to RAM and uses a small amount of power while Hibernate saves the session to disk and uses no power', True),
            ('Hibernate saves to RAM while Sleep saves to disk', False),
            ('Sleep shuts down the computer completely while Hibernate keeps it running slowly', False),
        ]
    },
    {
        'text': 'What is the Windows "Remote Server Administration Tools" (RSAT) used for?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Remotely controlling user desktops', False),
            ('Managing Windows Server roles and features from a Windows client computer without needing to be at the server', True),
            ('A VPN tool for remote server access', False),
            ('Monitoring server performance remotely', False),
        ]
    },
    {
        'text': 'What is a "roaming profile" in a Windows domain?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A profile that works without a network connection', False),
            ('A user profile stored on a server that follows the user so their settings and files are available on any domain computer they log into', True),
            ('A profile for users who work remotely via VPN', False),
            ('A mobile device management profile', False),
        ]
    },
    {
        'text': 'What does the Windows command "whoami" display?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The computer name only', False),
            ('The currently logged-in user account name and domain', True),
            ('All user accounts on the system', False),
            ('The Windows version and build number', False),
        ]
    },
    {
        'text': 'What is the purpose of Windows "Offline Files"?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Files that are deleted but not yet removed from the recycle bin', False),
            ('A feature that caches network files locally so they are accessible when the network connection is unavailable', True),
            ('Files that are hidden from regular users', False),
            ('Temporary files stored while downloads are in progress', False),
        ]
    },
    {
        'text': 'What is the Windows "Encrypting File System" (EFS) recovery agent used for?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Recovering deleted files from an encrypted drive', False),
            ('A designated account that can decrypt EFS-encrypted files when the original user\'s certificate is unavailable', True),
            ('A tool for recovering BitLocker-encrypted drives', False),
            ('An administrator account that bypasses all file permissions', False),
        ]
    },
    {
        'text': 'What Windows tool is used to create a complete image backup of the operating system drive?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('File History', False),
            ('Windows Backup and Restore — Create a system image', True),
            ('System Restore', False),
            ('Reset This PC', False),
        ]
    },
    {
        'text': 'What is the purpose of the "robocopy" command in Windows?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A robot automation tool for Windows scripts', False),
            ('A robust file copy utility that supports mirroring directories resumable transfers and copying file permissions', True),
            ('A remote backup tool for copying files over the network', False),
            ('A tool for copying system files during Windows setup', False),
        ]
    },
    {
        'text': 'What is the Windows "Deployment Image Servicing and Management" (DISM) primarily used for?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Deploying new computers over the network', False),
            ('Servicing Windows images — adding or removing features updating drivers and repairing the Windows component store', True),
            ('A disk imaging tool for creating backups', False),
            ('Managing Windows Update delivery', False),
        ]
    },
    {
        'text': 'What does the error "0xC0000428 - Windows cannot verify the digital signature" indicate during boot?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The hard drive is failing', False),
            ('A driver or boot file has a digital signature that cannot be verified — often caused by unsigned drivers or Secure Boot conflicts', True),
            ('The Windows license is invalid', False),
            ('The RAM has failed', False),
        ]
    },
    {
        'text': 'What is the purpose of the "bcdedit" command in Windows?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Backs up and deletes temporary files', False),
            ('Edits the Windows Boot Configuration Data store controlling how Windows boots', True),
            ('Manages BitLocker drive encryption settings', False),
            ('A disk check and edit tool', False),
        ]
    },

    # ── OPERATING SYSTEMS — macOS and Linux ───────────────────────────────────

    {
        'text': 'What is the macOS "Keychain" used for?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Managing FileVault disk encryption', False),
            ('A password manager built into macOS that securely stores passwords certificates and keys', True),
            ('Managing installed applications and their permissions', False),
            ('A tool for backing up macOS to iCloud', False),
        ]
    },
    {
        'text': 'What is "FileVault" on macOS?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A secure cloud storage service for Mac users', False),
            ('Full-disk encryption built into macOS that protects data if the Mac is lost or stolen', True),
            ('A file versioning system similar to Windows File History', False),
            ('A vault for storing important documents on iCloud', False),
        ]
    },
    {
        'text': 'What is the macOS "Terminal" used for?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A flight booking application', False),
            ('A command-line interface for macOS allowing direct access to the Unix-based operating system', True),
            ('A remote desktop tool for Mac', False),
            ('An application for managing network connections', False),
        ]
    },
    {
        'text': 'What is the Linux "root" account equivalent to in Windows?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A standard user account', False),
            ('The built-in Administrator account with full system privileges', True),
            ('A guest account with limited access', False),
            ('A service account used only by applications', False),
        ]
    },
    {
        'text': 'What does the Linux command "grep" do?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Copies files from one location to another', False),
            ('Searches for a specified pattern within files or command output and displays matching lines', True),
            ('Removes files and directories', False),
            ('Displays disk usage statistics', False),
        ]
    },
    {
        'text': 'What is the purpose of the Linux "/var/log" directory?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Stores variable-length application data', False),
            ('Contains system and application log files', True),
            ('Stores user home directories', False),
            ('Contains variable environment settings', False),
        ]
    },
    {
        'text': 'What Linux command displays disk space usage for file systems?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('ls -l', False),
            ('df -h', True),
            ('du -s', False),
            ('free -m', False),
        ]
    },
    {
        'text': 'What is the macOS equivalent of Windows Device Manager?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Finder', False),
            ('System Information — Hardware section', True),
            ('Activity Monitor', False),
            ('Console', False),
        ]
    },
    {
        'text': 'What does the Linux "top" command display?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The top 10 largest files on the system', False),
            ('A real-time view of running processes and system resource usage similar to Windows Task Manager', True),
            ('The most recently modified files', False),
            ('The top network connections by bandwidth', False),
        ]
    },
    {
        'text': 'What is a "shell script" in Linux?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A script that runs inside a web browser shell', False),
            ('A text file containing a series of shell commands that can be executed as a program to automate tasks', True),
            ('A script for configuring the Linux graphical shell', False),
            ('A remote script that runs on a server', False),
        ]
    },

    # ── OPERATING SYSTEMS — Multi Select ──────────────────────────────────────

    {
        'text': 'Which TWO of the following are true about macOS compared to Windows? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('macOS is built on a Unix foundation', True),
            ('macOS supports the same software as Windows without any compatibility issues', False),
            ('macOS uses Time Machine for built-in backup functionality', True),
            ('macOS uses the NTFS file system by default', False),
        ]
    },
    {
        'text': 'Which TWO Linux commands are used for file and directory management? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('mkdir — creates a new directory', True),
            ('netstat — displays network connections', False),
            ('rm — removes files and directories', True),
            ('top — shows running processes', False),
        ]
    },
    {
        'text': 'Which TWO are true about Windows domain environments? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Users can log into any domain computer with their domain credentials', True),
            ('Domain environments require Windows Home edition', False),
            ('Group Policy can enforce settings across all domain computers', True),
            ('Domain computers cannot connect to the internet', False),
        ]
    },
    {
        'text': 'Which TWO are valid partition styles used in Windows? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('MBR (Master Boot Record)', True),
            ('FAT (File Allocation Table)', False),
            ('GPT (GUID Partition Table)', True),
            ('NTFS (New Technology File System)', False),
        ]
    },

    # ── SECURITY — Advanced Topics ────────────────────────────────────────────

    {
        'text': 'What is "defense in depth" and give an example?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Using one very strong security measure — for example a 256-bit firewall', False),
            ('Using multiple layers of security so if one fails others protect the system — for example firewall plus antivirus plus MFA plus encryption', True),
            ('Deeply understanding security threats — for example studying hacker techniques', False),
            ('Physical security measures only — for example locks and cameras', False),
        ]
    },
    {
        'text': 'What is "privilege escalation" in cybersecurity?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Promoting a user account to administrator through HR', False),
            ('When an attacker gains higher-level permissions than they should have — either by exploiting a vulnerability or through social engineering', True),
            ('Increasing the security privileges of a legitimate administrator', False),
            ('Escalating a security incident to a senior analyst', False),
        ]
    },
    {
        'text': 'What is the purpose of "network access control" (NAC)?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Controls how much network bandwidth each user can use', False),
            ('Ensures only compliant and authorized devices can connect to the network by checking security posture before granting access', True),
            ('Controls which websites employees can visit', False),
            ('Manages network switch port assignments', False),
        ]
    },
    {
        'text': 'What is "PKI" (Public Key Infrastructure)?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A set of physical keys for securing server rooms', False),
            ('A framework of hardware software policies and procedures for creating managing distributing and revoking digital certificates', True),
            ('A protocol for key exchange over the internet', False),
            ('A type of encryption algorithm', False),
        ]
    },
    {
        'text': 'What is an "intrusion detection system" (IDS)?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A system that blocks all unauthorized network traffic', False),
            ('A system that monitors network traffic or system activity for suspicious behavior and generates alerts but does not block traffic', True),
            ('A physical security system for detecting unauthorized building entry', False),
            ('A tool for detecting malware on endpoints', False),
        ]
    },
    {
        'text': 'What is the difference between an IDS and an IPS?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('They are identical — IPS is just a newer version of IDS', False),
            ('An IDS only detects and alerts on suspicious activity while an IPS actively blocks or prevents the suspicious traffic', True),
            ('An IDS blocks traffic while an IPS only monitors', False),
            ('An IDS is hardware-based while an IPS is software-based', False),
        ]
    },
    {
        'text': 'What is "hashing" in security?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Encrypting data so it can be decrypted later', False),
            ('A one-way function that converts data into a fixed-length string used to verify data integrity — the same input always produces the same output but cannot be reversed', True),
            ('A method of compressing files for storage', False),
            ('Converting data into binary format', False),
        ]
    },
    {
        'text': 'What is "salting" in the context of password storage?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Adding special characters to a password to make it stronger', False),
            ('Adding random data to a password before hashing it so identical passwords produce different hash values preventing rainbow table attacks', True),
            ('Encrypting passwords with a secret key', False),
            ('Storing passwords in multiple databases for redundancy', False),
        ]
    },
    {
        'text': 'What is a "rainbow table" attack?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('An attack using colorful social engineering tactics', False),
            ('Using a pre-computed table of hash values to reverse password hashes and recover original passwords', True),
            ('A multi-colored phishing campaign targeting different user groups', False),
            ('An attack that uses multiple simultaneous network connections', False),
        ]
    },
    {
        'text': 'What is "SSAE 18 SOC 2" compliance?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A hardware security standard for servers', False),
            ('An auditing standard for service organizations that evaluates controls related to security availability processing integrity confidentiality and privacy', True),
            ('A software coding standard for secure applications', False),
            ('A networking protocol for secure communications', False),
        ]
    },

    # ── SECURITY — Multi Select ────────────────────────────────────────────────

    {
        'text': 'Which TWO of the following are true about multi-factor authentication? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('MFA significantly reduces account compromise risk even if a password is stolen', True),
            ('MFA requires three or more factors by definition', False),
            ('MFA combines two or more different types of authentication factors', True),
            ('MFA makes accounts completely immune to all attacks', False),
        ]
    },
    {
        'text': 'Which TWO of the following are examples of administrative security controls? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Security awareness training policy', True),
            ('Firewall blocking unauthorized ports', False),
            ('Acceptable use policy for company devices', True),
            ('Antivirus software on all workstations', False),
        ]
    },
    {
        'text': 'Which TWO statements about biometric authentication are correct? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Biometrics use physical characteristics like fingerprints or facial recognition', True),
            ('Biometrics are always more secure than passwords', False),
            ('Biometrics are an example of "something you are" authentication factor', True),
            ('Biometrics can be easily changed if compromised like a password', False),
        ]
    },
    {
        'text': 'Which TWO of the following are true about firewalls? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Firewalls can filter traffic based on port numbers and IP addresses', True),
            ('A firewall protects against all types of cyberattacks', False),
            ('Firewalls can be hardware-based software-based or both', True),
            ('A firewall eliminates the need for antivirus software', False),
        ]
    },

    # ── SOFTWARE TROUBLESHOOTING — Advanced ───────────────────────────────────

    {
        'text': 'A user reports that after changing their Windows password they can no longer access EFS-encrypted files. Why?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('EFS encryption is linked to the user\'s certificate which may have been lost if the password was reset by an administrator rather than changed by the user', True),
            ('Changing passwords always removes access to encrypted files', False),
            ('EFS requires the old password to decrypt files', False),
            ('The files were automatically deleted when the password changed', False),
        ]
    },
    {
        'text': 'A computer consistently fails to complete Windows updates with error 0x80070005. What does this indicate?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The hard drive is full', False),
            ('An access denied error — a third-party security software or permissions issue is preventing Windows Update from accessing required files', True),
            ('The internet connection is too slow', False),
            ('The Windows license needs to be renewed', False),
        ]
    },
    {
        'text': 'A user\'s Outlook keeps prompting for a password repeatedly even after entering the correct credentials. What should be checked?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Reinstall Windows', False),
            ('Check the Windows Credential Manager for outdated Outlook credentials and remove them so they can be re-entered fresh', True),
            ('Replace the network adapter', False),
            ('The email account has been hacked', False),
        ]
    },
    {
        'text': 'A user reports that their computer shows "Your PC ran into a problem and needs to restart" (BSOD) every day at the same time. What does the timing suggest?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The power supply is failing at a specific voltage', False),
            ('A scheduled task or backup job running at that time is triggering the crash — check Task Scheduler and Event Viewer', True),
            ('The computer needs to be restarted at that time', False),
            ('The RAM degrades at the same time each day', False),
        ]
    },
    {
        'text': 'What is the purpose of "Windows Memory Diagnostics" tool?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Monitors memory usage in real time', False),
            ('Tests RAM for errors by running memory tests during restart — a simpler alternative to MemTest86 that is built into Windows', True),
            ('Clears cached memory to improve performance', False),
            ('Manages virtual memory pagefile settings', False),
        ]
    },
    {
        'text': 'A user reports that Windows activates correctly but one specific program shows as unlicensed. What should be checked?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Reinstall Windows', False),
            ('Verify the software license key is valid and entered correctly or contact the software vendor for license recovery', True),
            ('Windows activation and software licenses are linked — reactivate Windows', False),
            ('The hard drive needs to be replaced', False),
        ]
    },
    {
        'text': 'A user upgraded from Windows 10 to Windows 11 and now their fingerprint reader no longer works. What is the most likely cause?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Windows 11 does not support fingerprint readers', False),
            ('The fingerprint reader driver is not compatible with Windows 11 — check manufacturer website for a Windows 11 driver', True),
            ('The fingerprint reader hardware has failed from the upgrade', False),
            ('Windows Hello must be disabled and re-enabled', False),
        ]
    },
    {
        'text': 'What does a "memory leak" in an application cause over time?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The application deletes files from RAM', False),
            ('The application gradually consumes more and more RAM without releasing it eventually causing slowness crashes or out-of-memory errors', True),
            ('RAM physically leaks data to the hard drive', False),
            ('The application becomes permanently corrupted', False),
        ]
    },
    {
        'text': 'A user reports their computer clock is always wrong even after being set correctly. The CMOS battery is new. What else could cause this?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The CPU is faulty', False),
            ('The Windows Time service is disabled or misconfigured preventing automatic time synchronization', True),
            ('The RAM is insufficient', False),
            ('The monitor is affecting the system time', False),
        ]
    },
    {
        'text': 'What should be done if a Windows application installer fails with "Windows Installer service could not be accessed"?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Reinstall Windows immediately', False),
            ('Start the Windows Installer service via services.msc or re-register it using msiexec /unregister then msiexec /regserver', True),
            ('Replace the hard drive', False),
            ('Disable Windows Defender and try again', False),
        ]
    },

    # ── SOFTWARE TROUBLESHOOTING — Multi Select ───────────────────────────────

    {
        'text': 'Which TWO are correct troubleshooting steps when an application fails to install? (Select TWO)',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Check Event Viewer for specific error codes during the failed installation', True),
            ('Immediately replace the hard drive', False),
            ('Try running the installer with administrator privileges', True),
            ('Reinstall Windows before attempting installation again', False),
        ]
    },
    {
        'text': 'Which TWO Windows logs in Event Viewer are most useful for diagnosing application crashes? (Select TWO)',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Application log — contains errors from installed applications', True),
            ('Hardware log', False),
            ('System log — contains OS and driver errors that may affect applications', True),
            ('Internet log', False),
        ]
    },
    {
        'text': 'Which TWO are valid methods for removing stubborn malware that standard antivirus cannot remove? (Select TWO)',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Boot from a rescue disk and scan outside of Windows where the malware cannot run', True),
            ('Simply restart the computer multiple times', False),
            ('Use a second-opinion scanner from a different vendor', True),
            ('Increase the screen resolution to detect hidden malware', False),
        ]
    },
    {
        'text': 'Which TWO of the following can cause Windows to go into an activation loop? (Select TWO)',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Significant hardware changes such as replacing the motherboard', True),
            ('Installing new software applications', False),
            ('Moving a volume-licensed computer outside its managed environment', True),
            ('Updating Windows Defender definitions', False),
        ]
    },

    # ── OPERATIONAL PROCEDURES — Advanced ─────────────────────────────────────

    {
        'text': 'What is "separation of duties" in IT operations?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Separating IT staff into different departments', False),
            ('Dividing critical tasks among multiple people so no single person has complete control reducing the risk of fraud or error', True),
            ('Keeping development and production environments separate', False),
            ('Having separate IT teams for hardware and software', False),
        ]
    },
    {
        'text': 'What is a "service level agreement" (SLA) and what happens if it is not met?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A list of services offered — no consequence if not met', False),
            ('A contract specifying minimum service standards — failure to meet it typically results in financial penalties or contract renegotiation', True),
            ('An internal policy for IT staff — violations result in disciplinary action', False),
            ('A training agreement for new IT staff — failure means more training', False),
        ]
    },
    {
        'text': 'What is the purpose of "version control" in IT?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Tracking which version of Windows is installed', False),
            ('Tracking changes to files or code over time allowing previous versions to be restored and changes to be reviewed', True),
            ('Managing software license versions', False),
            ('Controlling which users can update files', False),
        ]
    },
    {
        'text': 'What should an IT technician do when they discover evidence of illegal activity on a user\'s computer during a repair?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Delete the evidence to protect the user', False),
            ('Stop working immediately do not alter any data and report the discovery to management and follow legal chain of custody procedures', True),
            ('Continue the repair and mention it to HR later', False),
            ('Copy the evidence and report anonymously', False),
        ]
    },
    {
        'text': 'What is "informed consent" in IT support?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Making sure users are informed about company IT policies', False),
            ('Ensuring the user understands and agrees to what work will be performed on their device before the technician begins', True),
            ('Informing users of security vulnerabilities', False),
            ('Getting consent from management before working on executive computers', False),
        ]
    },
    {
        'text': 'What is the purpose of a "runbook" in IT operations?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A log of how far IT technicians ran during fire drills', False),
            ('A documented set of procedures and operations for running and managing IT systems including routine tasks and incident responses', True),
            ('A book of approved software that can be run on company computers', False),
            ('A training manual for new IT staff', False),
        ]
    },
    {
        'text': 'What is "ITIL" and how does it relate to IT support?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('IT Infrastructure Library — a set of best practices for delivering IT services and support', True),
            ('International Technology Integration Language — a programming standard', False),
            ('IT Investment and Licensing — a financial framework', False),
            ('Integrated Technology Infrastructure Layer — a network model', False),
        ]
    },
    {
        'text': 'What is "capacity planning" in IT?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Planning how many IT staff are needed in each department', False),
            ('Forecasting future IT resource needs (storage compute network) to ensure systems can handle anticipated demand', True),
            ('Managing the storage capacity of individual hard drives', False),
            ('Planning for disaster recovery scenarios', False),
        ]
    },
    {
        'text': 'What does "due diligence" mean in IT security?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Completing tasks on time and within budget', False),
            ('Taking reasonable steps to investigate understand and address security risks before they become problems', True),
            ('Following up on all support tickets within 24 hours', False),
            ('Conducting annual performance reviews of IT staff', False),
        ]
    },
    {
        'text': 'What is the purpose of "end of life" (EOL) planning for IT equipment?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Planning memorial services for deceased IT staff', False),
            ('Planning the replacement of equipment before it becomes unsupported to avoid security vulnerabilities and operational issues', True),
            ('Scheduling equipment disposal to minimize environmental impact', False),
            ('Documenting which equipment needs to be repaired', False),
        ]
    },

    # ── OPERATIONAL PROCEDURES — Multi Select ─────────────────────────────────

    {
        'text': 'Which TWO are correct steps in the CompTIA troubleshooting methodology? (Select TWO)',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Establish a theory of probable cause before testing solutions', True),
            ('Apply the most expensive solution first to save time', False),
            ('Document findings actions and outcomes after resolving the issue', True),
            ('Always reinstall the OS as the first troubleshooting step', False),
        ]
    },
    {
        'text': 'Which TWO of the following are important when documenting an IT support ticket? (Select TWO)',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Recording all troubleshooting steps taken even unsuccessful ones', True),
            ('Only documenting the final solution to keep records brief', False),
            ('Including the date time and technician name for accountability', True),
            ('Omitting user information to protect privacy', False),
        ]
    },
    {
        'text': 'Which TWO behaviors demonstrate poor professional conduct in IT support? (Select TWO)',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Browsing the user\'s personal files out of curiosity during a repair', True),
            ('Explaining what was done after completing a repair', False),
            ('Dismissing a user\'s complaint without investigating', True),
            ('Escalating a ticket when it exceeds your expertise', False),
        ]
    },
    {
        'text': 'Which TWO of the following are included in a comprehensive disaster recovery plan? (Select TWO)',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Defined roles and responsibilities during a disaster', True),
            ('A list of all employees\' personal contact information', False),
            ('Recovery time objectives and recovery point objectives', True),
            ('The IT department\'s vacation schedule', False),
        ]
    },

    # ── ADDITIONAL MIXED CORE 2 ────────────────────────────────────────────────

    {
        'text': 'What is "application whitelisting"?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A list of applications approved for purchase', False),
            ('A security approach that only allows pre-approved applications to run blocking everything else by default', True),
            ('Marking safe emails as not spam', False),
            ('A list of trusted websites in browser settings', False),
        ]
    },
    {
        'text': 'What is the purpose of "log aggregation" in security operations?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Compressing log files to save storage space', False),
            ('Collecting logs from multiple systems into a central location for unified monitoring correlation and analysis', True),
            ('Deleting old log files automatically', False),
            ('Encrypting log files for compliance', False),
        ]
    },
    {
        'text': 'What is a "SIEM" (Security Information and Event Management) system?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A simple firewall management tool', False),
            ('A platform that collects and analyzes security data from across the organization in real time to detect and respond to threats', True),
            ('A security awareness training platform', False),
            ('A patch management system', False),
        ]
    },
    {
        'text': 'What is "threat hunting" in cybersecurity?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Automatically blocking threats detected by antivirus', False),
            ('Proactively searching through systems and networks to detect advanced threats that may have evaded automated security tools', True),
            ('Hunting for vulnerabilities in competitor systems', False),
            ('Monitoring social media for security threats', False),
        ]
    },
    {
        'text': 'What is the purpose of "two-factor authentication" specifically using SMS codes?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The most secure form of 2FA available', False),
            ('Sends a one-time code to a phone number as a second verification step — considered weaker than app-based 2FA because SMS can be intercepted via SIM swapping', True),
            ('A method that replaces passwords with phone numbers', False),
            ('A way to share login credentials securely', False),
        ]
    },
    {
        'text': 'What is "data sovereignty"?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The right of individuals to own their personal data', False),
            ('The concept that data is subject to the laws of the country where it is stored — relevant when using cloud services in different countries', True),
            ('A company\'s exclusive ownership of customer data', False),
            ('Government control over all digital communications', False),
        ]
    },
    {
        'text': 'What is a "bring your own device" (BYOD) policy designed to address?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Encouraging employees to purchase company-approved devices', False),
            ('Defining rules for how personal devices can be used for work including security requirements data separation and what happens when an employee leaves', True),
            ('Allowing employees to bring food and drinks to the office', False),
            ('A policy allowing employees to build their own computers', False),
        ]
    },
    {
        'text': 'What is the purpose of "data classification" in an organization?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Organizing files alphabetically on servers', False),
            ('Categorizing data by sensitivity level (public internal confidential secret) so appropriate security controls can be applied to each category', True),
            ('Classifying employees by their data access needs', False),
            ('Sorting data by date for archive purposes', False),
        ]
    },
    {
        'text': 'Which TWO of the following are true about Windows Group Policy? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Group Policy can enforce password complexity requirements across all domain computers', True),
            ('Group Policy only applies to user accounts not computer configurations', False),
            ('Group Policy can be used to push software installations to domain computers', True),
            ('Group Policy requires Windows Home edition to function', False),
        ]
    },
    {
        'text': 'Which TWO are correct statements about cloud computing models? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('SaaS (Software as a Service) delivers applications over the internet without local installation', True),
            ('IaaS gives the customer full control including the operating system', True),
            ('PaaS gives the customer full hardware and OS control', False),
            ('SaaS requires the customer to manage the underlying infrastructure', False),
        ]
    },
    {
        'text': 'What is the Windows "Startup Repair" tool used for?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Repairing corrupted application files', False),
            ('Automatically diagnosing and fixing problems that prevent Windows from starting such as corrupted boot files', True),
            ('A tool for optimizing startup programs', False),
            ('Repairing hardware driver issues at startup', False),
        ]
    },
    {
        'text': 'What does the acronym PII stand for and why does it need protection?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Personal Internet Information — needs protection from hackers', False),
            ('Personally Identifiable Information — any data that can be used to identify a specific individual which must be protected to prevent identity theft and comply with privacy laws', True),
            ('Private Industry Information — trade secrets that must be kept confidential', False),
            ('Public Internet Identity — usernames that need to be kept private', False),
        ]
    },
    {
        'text': 'What is the purpose of "application sandboxing" on mobile devices?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Limiting how much storage each app can use', False),
            ('Isolating each app in its own environment so it cannot access data from other apps or the OS without explicit permission', True),
            ('Preventing apps from using the internet without permission', False),
            ('Creating a backup of app data in the cloud', False),
        ]
    },
    {
        'text': 'What is "containerization" as it relates to mobile device management?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Packaging applications for deployment using Docker', False),
            ('Separating corporate apps and data from personal apps and data on a BYOD device using a secure container', True),
            ('Storing mobile devices in secure physical containers', False),
            ('Compressing app data to save storage space', False),
        ]
    },
    {
        'text': 'What is the purpose of "remote wipe" on a mobile device?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Cleaning the screen remotely using software', False),
            ('Erasing all data on a lost or stolen device remotely to prevent unauthorized access to company or personal data', True),
            ('Updating the device remotely without user interaction', False),
            ('Removing malware from a device over the network', False),
        ]
    },
    {
        'text': 'Which TWO of the following are features of mobile device management (MDM)? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Enforcing passcode and encryption policies on enrolled devices', True),
            ('Physically tracking the location of lost devices in real time', False),
            ('Remotely wiping data from lost or stolen devices', True),
            ('Increasing the battery life of enrolled devices', False),
        ]
    },
    {
        'text': 'What is "digital forensics" in IT?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Designing digital artwork for forensic science departments', False),
            ('The process of collecting preserving and analyzing digital evidence from computers and devices in a legally admissible way', True),
            ('Recovering deleted files from failed hard drives', False),
            ('Testing software for security vulnerabilities', False),
        ]
    },
    {
        'text': 'What is the "order of volatility" in digital forensics?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The order in which hardware components fail during an incident', False),
            ('The sequence in which evidence should be collected starting with the most volatile data (RAM) that will be lost first if the system is powered off', True),
            ('The order in which files are deleted during a cyberattack', False),
            ('The priority order for restoring systems after an incident', False),
        ]
    },
    {
        'text': 'Which TWO of the following must be preserved when collecting digital evidence? (Select TWO)',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Chain of custody documentation showing who handled the evidence', True),
            ('The original evidence must remain unaltered — work on forensic copies', True),
            ('The suspect must be present when evidence is collected', False),
            ('All evidence must be collected within 24 hours', False),
        ]
    },
    {
        'text': 'What is "virtualization security" and why is it important?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Security for virtual reality applications', False),
            ('Securing the hypervisor and virtual machines because if the hypervisor is compromised all VMs running on it are potentially compromised', True),
            ('Using virtual machines to test security tools safely', False),
            ('Encrypting virtual machine files at rest', False),
        ]
    },
    {
        'text': 'What is "patch Tuesday" and why is it significant?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The day when IT staff must complete all outstanding tickets', False),
            ('Microsoft\'s regular monthly schedule for releasing security patches and updates — typically the second Tuesday of each month', True),
            ('A weekly day for applying patches to avoid Friday outages', False),
            ('A CompTIA exam day recommendation for applying updates', False),
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