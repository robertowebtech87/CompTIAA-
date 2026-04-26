from app import app, db
from models import Question, Choice

questions_data = [

    # ── OPERATING SYSTEMS — Windows Features & Tools ─────────────────────────

    {
        'text': 'What is the purpose of the Windows Registry?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('A database that stores low-level settings for the OS, hardware, and installed applications', True),
            ('A backup of all user files and documents', False),
            ('A list of all installed Windows updates', False),
            ('A log of all user login and logout events', False),
        ]
    },
    {
        'text': 'What command opens the Windows Registry Editor?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('msconfig', False),
            ('regedit', True),
            ('gpedit.msc', False),
            ('services.msc', False),
        ]
    },
    {
        'text': 'What is the purpose of msconfig in Windows?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('To edit the Windows Registry', False),
            ('To configure system startup options, boot settings, and which services start at boot', True),
            ('To manage user accounts and passwords', False),
            ('To configure Windows Firewall rules', False),
        ]
    },
    {
        'text': 'What is the Windows Event Viewer used for?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Monitoring real-time CPU and RAM usage', False),
            ('Viewing logs of system events, application errors, security events, and warnings', True),
            ('Managing startup programs', False),
            ('Configuring network adapter settings', False),
        ]
    },
    {
        'text': 'What are the three main log categories in Windows Event Viewer?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Startup, Runtime, and Shutdown', False),
            ('Application, Security, and System', True),
            ('Hardware, Software, and Network', False),
            ('Error, Warning, and Information only', False),
        ]
    },
    {
        'text': 'What is the purpose of the Windows pagefile?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('A file that stores browser history and cached web pages', False),
            ('Virtual memory — a space on the hard drive used as an extension of RAM when physical RAM is full', True),
            ('A backup of the Windows system files', False),
            ('A temporary file used during Windows updates', False),
        ]
    },
    {
        'text': 'What does the acronym UAC stand for in Windows and what is its purpose?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Universal Application Control — manages which apps can run', False),
            ('User Account Control — prompts for admin approval before allowing changes that could affect the system', True),
            ('Unified Access Configuration — controls network access', False),
            ('User Authentication Certificate — verifies user identity', False),
        ]
    },
    {
        'text': 'What is the difference between a local user account and a Microsoft account in Windows?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Local accounts have more permissions than Microsoft accounts', False),
            ('A local account is tied only to that device while a Microsoft account syncs settings and files across multiple devices via the cloud', True),
            ('Microsoft accounts cannot access local files', False),
            ('Local accounts require internet access to log in', False),
        ]
    },
    {
        'text': 'What Windows feature allows you to return the system to a previous working state without affecting personal files?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Windows Backup', False),
            ('System Restore', True),
            ('Reset This PC', False),
            ('File History', False),
        ]
    },
    {
        'text': 'What is the difference between System Restore and Reset This PC in Windows?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('They are identical features with different names', False),
            ('System Restore rolls back system settings to a restore point without removing files, while Reset This PC reinstalls Windows and optionally removes all files', True),
            ('System Restore removes all files while Reset This PC keeps them', False),
            ('Reset This PC only works on laptops', False),
        ]
    },
    {
        'text': 'What is the Windows Task Scheduler used for?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Managing running processes and CPU priority', False),
            ('Automating tasks by running programs or scripts at specified times or triggered by specific events', True),
            ('Scheduling Windows updates during off hours only', False),
            ('Managing employee work schedules', False),
        ]
    },
    {
        'text': 'What is the purpose of the Disk Management tool in Windows?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Scanning drives for malware', False),
            ('Creating, deleting, formatting, and assigning drive letters to partitions on storage drives', True),
            ('Defragmenting hard drives', False),
            ('Checking drive health and SMART status', False),
        ]
    },
    {
        'text': 'What file system is required for drives larger than 32GB on modern Windows systems?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('FAT16', False),
            ('FAT32', False),
            ('NTFS', True),
            ('exFAT', False),
        ]
    },
    {
        'text': 'What is exFAT and when is it typically used?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('An older file system used only on Windows XP', False),
            ('A file system optimized for flash drives and memory cards that works across both Windows and macOS without the limitations of FAT32', True),
            ('A file system used exclusively on Linux systems', False),
            ('A compressed file system used for system backups', False),
        ]
    },
    {
        'text': 'What is the maximum individual file size supported by FAT32?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('1 GB', False),
            ('4 GB', True),
            ('16 GB', False),
            ('Unlimited', False),
        ]
    },
    {
        'text': 'What is the Windows command to check and repair file system errors on a drive?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('sfc /scannow', False),
            ('defrag', False),
            ('chkdsk', True),
            ('diskpart', False),
        ]
    },
    {
        'text': 'What does the Windows command "sfc /scannow" do?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Scans the hard drive for bad sectors', False),
            ('Scans and repairs corrupted or missing Windows system files', True),
            ('Scans for malware and viruses', False),
            ('Checks network connectivity', False),
        ]
    },
    {
        'text': 'What is the DISM command used for in Windows?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Disk imaging and sector mapping', False),
            ('Deployment Image Servicing and Management — repairs the Windows component store which sfc relies on', True),
            ('Displaying information about system memory', False),
            ('Direct interface for storage management', False),
        ]
    },
    {
        'text': 'A user needs to quickly switch between multiple open applications using only the keyboard. What shortcut do they use?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Windows key + D', False),
            ('Alt + Tab', True),
            ('Ctrl + Alt + Del', False),
            ('Windows key + Tab', False),
        ]
    },
    {
        'text': 'What is the purpose of Windows Defender Credential Guard?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Stores and manages saved website passwords', False),
            ('Protects login credentials by isolating them in a secure virtualized environment to prevent credential theft attacks', True),
            ('Monitors failed login attempts', False),
            ('Encrypts user password hints', False),
        ]
    },

    # ── OPERATING SYSTEMS — macOS & Linux basics ──────────────────────────────

    {
        'text': 'What is the macOS equivalent of Windows Task Manager?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('System Preferences', False),
            ('Activity Monitor', True),
            ('Console', False),
            ('Finder', False),
        ]
    },
    {
        'text': 'Where are system-wide application settings and preferences stored on macOS?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Finder', False),
            ('System Preferences / System Settings', True),
            ('Activity Monitor', False),
            ('Terminal', False),
        ]
    },
    {
        'text': 'What is the macOS equivalent of Windows Control Panel?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Finder', False),
            ('System Preferences (macOS Monterey and earlier) / System Settings (macOS Ventura and later)', True),
            ('App Store', False),
            ('Spotlight', False),
        ]
    },
    {
        'text': 'What Linux command is used to list the contents of a directory?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('dir', False),
            ('ls', True),
            ('list', False),
            ('show', False),
        ]
    },
    {
        'text': 'What Linux command changes the current working directory?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('mv', False),
            ('dir', False),
            ('cd', True),
            ('ls', False),
        ]
    },
    {
        'text': 'What does the Linux command "sudo" do?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Shuts down the system', False),
            ('Executes a command with elevated superuser (root) privileges', True),
            ('Lists files in a directory', False),
            ('Copies files to another location', False),
        ]
    },
    {
        'text': 'What is the Linux command to display the current directory path?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('cd', False),
            ('dir', False),
            ('pwd', True),
            ('path', False),
        ]
    },
    {
        'text': 'What is the purpose of the /etc directory in Linux?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Stores user home directories', False),
            ('Contains system-wide configuration files', True),
            ('Stores temporary files', False),
            ('Contains executable program files', False),
        ]
    },
    {
        'text': 'What Linux command is used to update package lists and install updates on Debian/Ubuntu systems?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('yum update', False),
            ('apt update && apt upgrade', True),
            ('pacman -Syu', False),
            ('rpm -update', False),
        ]
    },
    {
        'text': 'What is the macOS Time Machine used for?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Scheduling automated tasks', False),
            ('A built-in backup feature that automatically backs up the entire Mac to an external drive', True),
            ('Tracking application usage over time', False),
            ('Rolling back macOS to a previous version', False),
        ]
    },

    # ── OPERATING SYSTEMS — Windows Networking & Remote Access ───────────────

    {
        'text': 'What is the default port number for Remote Desktop Protocol (RDP)?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('22', False),
            ('80', False),
            ('3389', True),
            ('443', False),
        ]
    },
    {
        'text': 'What Windows tool allows you to map a network folder as a drive letter?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Disk Management', False),
            ('Map Network Drive in File Explorer', True),
            ('Device Manager', False),
            ('Network and Sharing Center', False),
        ]
    },
    {
        'text': 'What is a VPN and why would a remote worker use one?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('A faster internet connection for streaming', False),
            ('A Virtual Private Network that creates an encrypted tunnel allowing remote workers to securely access company resources as if on the local network', True),
            ('A tool for blocking advertisements', False),
            ('A backup service for remote workers', False),
        ]
    },
    {
        'text': 'What is the UNC path format used to access shared network resources in Windows?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('http://servername/sharename', False),
            ('\\\\servername\\sharename', True),
            ('ftp://servername/sharename', False),
            ('servername:/sharename', False),
        ]
    },
    {
        'text': 'What Windows feature allows administrators to apply settings and restrictions across domain computers centrally?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Local Security Policy', False),
            ('Group Policy', True),
            ('Windows Defender', False),
            ('Task Scheduler', False),
        ]
    },
    {
        'text': 'What is the difference between a workgroup and a domain in Windows networking?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('A workgroup supports more users than a domain', False),
            ('A workgroup is a peer-to-peer network where each computer manages its own security, while a domain uses a central server (Active Directory) to manage all users and computers', True),
            ('Domains are only used on Linux networks', False),
            ('A workgroup requires a server while a domain does not', False),
        ]
    },
    {
        'text': 'What does NTFS compression do and what is its main limitation?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Encrypts files for security — cannot be used with BitLocker', False),
            ('Reduces file size on disk but increases CPU usage when reading and writing compressed files', True),
            ('Creates a ZIP archive of selected files', False),
            ('Removes duplicate files from the drive', False),
        ]
    },
    {
        'text': 'What is Windows BitLocker and which drives can it encrypt?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Antivirus software that encrypts malware before removal', False),
            ('A full drive encryption feature that can encrypt the OS drive, fixed drives, and removable drives', True),
            ('A file-level encryption tool for individual files only', False),
            ('A cloud backup encryption service', False),
        ]
    },
    {
        'text': 'What is EFS (Encrypting File System) in Windows and how does it differ from BitLocker?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('EFS and BitLocker are identical features', False),
            ('EFS encrypts individual files and folders using the logged-in user\'s credentials, while BitLocker encrypts the entire drive', True),
            ('EFS encrypts the entire drive while BitLocker encrypts individual files', False),
            ('EFS is only available on Windows Server', False),
        ]
    },
    {
        'text': 'What Windows command displays all active network connections and listening ports?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('ipconfig /all', False),
            ('ping', False),
            ('netstat', True),
            ('tracert', False),
        ]
    },

    # ── OPERATING SYSTEMS — Windows Installation & Upgrades ──────────────────

    {
        'text': 'What is the minimum CPU speed requirement for Windows 11?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('1 GHz single core', False),
            ('1 GHz or faster with 2 or more cores on a compatible 64-bit processor', True),
            ('2 GHz quad core', False),
            ('Any CPU that ran Windows 10', False),
        ]
    },
    {
        'text': 'What does a clean installation of Windows mean compared to an upgrade?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('A clean install is faster than an upgrade', False),
            ('A clean install wipes the drive and installs Windows fresh with no existing files or settings, while an upgrade preserves files and settings', True),
            ('A clean install preserves all files while an upgrade deletes them', False),
            ('They are the same process with different names', False),
        ]
    },
    {
        'text': 'What tool does Microsoft provide to create bootable Windows installation media on a USB drive?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Windows Deployment Services', False),
            ('Media Creation Tool', True),
            ('DISM', False),
            ('Rufus', False),
        ]
    },
    {
        'text': 'After a Windows upgrade a user finds that their scanner no longer works. What is the most likely cause?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('The scanner hardware has failed', False),
            ('The scanner driver is incompatible with the new version of Windows and needs an updated driver', True),
            ('Windows upgrades always remove peripheral devices', False),
            ('The USB port was disabled during the upgrade', False),
        ]
    },
    {
        'text': 'What is PXE boot and when would it be used?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Booting from an external USB drive', False),
            ('Pre-boot Execution Environment — booting a computer from the network to deploy an OS image without physical installation media', True),
            ('A fast boot mode that skips hardware checks', False),
            ('Booting into safe mode over a network connection', False),
        ]
    },
    {
        'text': 'What Windows edition is required to join a computer to a domain?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Windows Home', False),
            ('Windows Pro, Enterprise, or Education', True),
            ('Any Windows edition supports domain joining', False),
            ('Only Windows Enterprise supports domain joining', False),
        ]
    },
    {
        'text': 'What is the purpose of Windows Update in terms of security?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('It backs up user data before installing updates', False),
            ('It delivers security patches that fix vulnerabilities before attackers can exploit them keeping the system protected', True),
            ('It updates antivirus definitions', False),
            ('It scans for and removes malware', False),
        ]
    },
    {
        'text': 'What is the Windows command to force a Group Policy update immediately?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('gpedit.msc /refresh', False),
            ('gpupdate /force', True),
            ('gpresult /update', False),
            ('msconfig /gp', False),
        ]
    },
    {
        'text': 'What is the purpose of the Windows "Compatibility Mode" for older applications?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Runs the application faster by allocating more CPU', False),
            ('Emulates an older version of Windows so legacy applications that were not designed for newer OS versions can run', True),
            ('Automatically updates old applications to newer versions', False),
            ('Allows 32-bit apps to use 64-bit memory', False),
        ]
    },
    {
        'text': 'What is the Windows "Safe Mode" and when should it be used?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('A mode for children that restricts access to adult content', False),
            ('A diagnostic startup mode that loads only essential drivers and services — used to troubleshoot driver issues, malware, and startup problems', True),
            ('A power-saving mode that reduces CPU speed', False),
            ('A backup mode that automatically saves open documents', False),
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