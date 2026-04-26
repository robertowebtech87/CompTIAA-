from app import app, db
from models import Question, Choice

questions_data = [

    # ── OPERATING SYSTEMS - Windows Deep Dive ────────────────────────────────

    {
        'text': 'What are the minimum RAM requirements for Windows 11?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('1 GB', False),
            ('2 GB', False),
            ('4 GB', True),
            ('8 GB', False),
        ]
    },
    {
        'text': 'What is the difference between Windows 10 Home and Windows 10 Pro?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Pro supports more RAM and has faster performance', False),
            ('Pro includes features like BitLocker, Remote Desktop, and the ability to join a domain that Home does not have', True),
            ('Home includes more built-in applications than Pro', False),
            ('Pro can only be installed on business computers', False),
        ]
    },
    {
        'text': 'What is the Windows domain and why would a business use it?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('A domain is a type of internet connection for businesses', False),
            ('A domain is a centralized network managed by Active Directory that allows administrators to manage users, computers, and policies from one place', True),
            ('A domain is a security certificate that encrypts all network traffic', False),
            ('A domain is a premium Windows feature that improves gaming performance', False),
        ]
    },
    {
        'text': 'What is the purpose of Group Policy in Windows?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('To manage printer settings for a single user', False),
            ('To centrally configure and enforce settings and restrictions across multiple computers and users in a domain', True),
            ('To group applications together on the taskbar', False),
            ('To manage user group memberships on a local computer', False),
        ]
    },
    {
        'text': 'What command opens the Local Group Policy Editor in Windows?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('regedit', False),
            ('msconfig', False),
            ('gpedit.msc', True),
            ('secpol.msc', False),
        ]
    },
    {
        'text': 'What is the Windows Task Scheduler used for?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('To monitor CPU and memory usage in real time', False),
            ('To automate tasks by running programs or scripts at specified times or in response to specific events', True),
            ('To schedule Windows Update installations', False),
            ('To manage startup programs and services', False),
        ]
    },
    {
        'text': 'What is the purpose of the Windows Control Panel?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('To manage running processes and system performance', False),
            ('A centralized interface for configuring system settings such as hardware, user accounts, network, and appearance', True),
            ('To view and manage installed Windows updates', False),
            ('To access command line tools and utilities', False),
        ]
    },
    {
        'text': 'What is the Windows upgrade path from Windows 10 Home to Windows 10 Pro?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('You must perform a clean install — upgrading in place is not possible', False),
            ('You can upgrade in place by purchasing and entering a Windows 10 Pro product key in Settings', True),
            ('You must contact Microsoft support to upgrade between editions', False),
            ('Windows 10 Home automatically upgrades to Pro after one year', False),
        ]
    },
    {
        'text': 'What does the Windows Reliability Monitor show?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('Real-time CPU and memory usage statistics', False),
            ('A timeline of system stability showing application crashes, hardware failures, and Windows updates that may have affected reliability', True),
            ('The current network speed and connection quality', False),
            ('A list of all installed programs and their last run date', False),
        ]
    },
    {
        'text': 'What is the purpose of Windows Remote Desktop?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('To share files between two computers on the same network', False),
            ('To allow a user to remotely access and control another Windows computer over a network as if sitting in front of it', True),
            ('To broadcast your screen to multiple viewers simultaneously', False),
            ('To remotely install Windows on another computer', False),
        ]
    },
    {
        'text': 'Which Windows editions support being the host for an incoming Remote Desktop connection?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('All Windows editions including Home', False),
            ('Windows Pro, Enterprise, and Education — Windows Home can connect to but cannot host RDP sessions', True),
            ('Only Windows Server editions', False),
            ('Only Windows Enterprise', False),
        ]
    },
    {
        'text': 'What is the purpose of the Windows hosts file located at C:\\Windows\\System32\\drivers\\etc\\hosts?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('It stores the login credentials for network shares', False),
            ('It maps hostnames to IP addresses and is checked before DNS, allowing manual overrides of DNS resolution', True),
            ('It contains a list of blocked websites for parental controls', False),
            ('It stores the network adapter configuration settings', False),
        ]
    },
    {
        'text': 'What is the Windows Recovery Environment (WinRE) used for?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('A separate recovery partition used to diagnose and repair Windows startup and system problems', True),
            ('A cloud-based backup service for Windows files', False),
            ('A tool for creating Windows installation media', False),
            ('A feature that automatically reinstalls Windows every 30 days', False),
        ]
    },
    {
        'text': 'What does the net user command do in Windows?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('It displays current network connections', False),
            ('It manages local user accounts — creating, deleting, and modifying users from the command line', True),
            ('It tests network connectivity to a remote host', False),
            ('It displays network adapter configuration', False),
        ]
    },
    {
        'text': 'What is the purpose of Windows Sandbox?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'choices': [
            ('A tool for testing network security configurations', False),
            ('A lightweight isolated virtual environment for safely running untrusted applications without affecting the host system', True),
            ('A protected area of memory for critical Windows processes', False),
            ('A backup environment that activates when Windows becomes corrupted', False),
        ]
    },

    # ── SECURITY - Core 2 Topics ──────────────────────────────────────────────

    {
        'text': 'What are the steps in the malware removal process?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('Delete all files, reinstall Windows, restore from backup', False),
            ('Investigate and identify, quarantine, disable System Restore, remediate, schedule scans, enable System Restore, educate the user', True),
            ('Run antivirus, restart computer, update drivers', False),
            ('Format the drive, reinstall OS, restore user files', False),
        ]
    },
    {
        'text': 'Why should System Restore be disabled when removing malware?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('System Restore uses too many resources during malware removal', False),
            ('Malware can hide in System Restore points and reinfect the system if a restore is performed after removal', True),
            ('System Restore conflicts with antivirus software', False),
            ('Disabling System Restore speeds up the malware scan', False),
        ]
    },
    {
        'text': 'What is the first step when you suspect a computer is infected with malware?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('Immediately format the hard drive', False),
            ('Disconnect the computer from the network to prevent the malware from spreading or communicating with command and control servers', True),
            ('Run a full antivirus scan while connected to the internet', False),
            ('Restore the computer from a backup', False),
        ]
    },
    {
        'text': 'What is Windows Defender Firewall and what does it do?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('An antivirus program that scans files for malware', False),
            ('A built-in Windows firewall that monitors and controls incoming and outgoing network traffic based on security rules', True),
            ('A VPN service built into Windows', False),
            ('A parental control feature that blocks inappropriate websites', False),
        ]
    },
    {
        'text': 'What is the purpose of NTFS permissions?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('To encrypt files stored on an NTFS volume', False),
            ('To control which users and groups can access files and folders and what actions they can perform on them', True),
            ('To set the compression level for files on the drive', False),
            ('To prevent files from being deleted when the drive is full', False),
        ]
    },
    {
        'text': 'What is the difference between NTFS permissions and share permissions?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('They are identical and one overrides the other', False),
            ('NTFS permissions apply locally and over the network while share permissions only apply when accessing a resource over the network — when both apply the most restrictive wins', True),
            ('Share permissions are more secure than NTFS permissions', False),
            ('NTFS permissions only apply to administrators', False),
        ]
    },
    {
        'text': 'What is a rootkit?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('A program that displays unwanted pop-up advertisements', False),
            ('Malware that hides deep in the operating system to conceal its presence and the presence of other malware, making it very difficult to detect and remove', True),
            ('A virus that targets the root directory of a hard drive', False),
            ('A tool used by administrators to access the root account', False),
        ]
    },
    {
        'text': 'What is the purpose of an access control list (ACL)?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('A list of approved software that can be installed on company computers', False),
            ('A set of rules that specifies which users or systems are granted or denied access to a particular resource', True),
            ('A log of all access attempts to a secure system', False),
            ('A list of IP addresses that are allowed to connect to a network', False),
        ]
    },
    {
        'text': 'What is credential harvesting?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('The process of collecting strong passwords for future use', False),
            ('A cyberattack technique that steals usernames and passwords through phishing, keyloggers, or fake login pages', True),
            ('A backup method for storing user login information securely', False),
            ('The process of creating new user credentials in bulk', False),
        ]
    },
    {
        'text': 'What is the purpose of end-user security awareness training?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('To teach users how to repair their own computers', False),
            ('To educate users about security threats and best practices so they can recognize and avoid social engineering, phishing, and other attacks', True),
            ('To train users to perform security audits on the network', False),
            ('To certify users in cybersecurity practices', False),
        ]
    },
    {
        'text': 'What is the purpose of file encryption on a Windows system?',
        'domain': 'Security',
        'exam': 'core2',
        'choices': [
            ('To compress files to save disk space', False),
            ('To protect sensitive files by converting them into unreadable format so only authorized users with the correct key can access them', True),
            ('To prevent files from being modified by other users', False),
            ('To hide files from appearing in Windows Explorer', False),
        ]
    },

    # ── SOFTWARE TROUBLESHOOTING ──────────────────────────────────────────────

    {
        'text': 'A user reports that an application crashes immediately after opening. What should the technician check first?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('Replace the computer immediately', False),
            ('Check the Event Viewer for error codes, verify the application is compatible with the OS version, and try reinstalling the application', True),
            ('Reinstall Windows', False),
            ('Add more RAM to the system', False),
        ]
    },
    {
        'text': 'What does a "missing DLL" error when launching an application typically indicate?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('The hard drive is failing', False),
            ('A required Dynamic Link Library file is missing or corrupt — reinstalling the application or installing the required runtime may fix it', True),
            ('The application is not compatible with the CPU', False),
            ('The user does not have permission to run the application', False),
        ]
    },
    {
        'text': 'A user reports that their computer is very slow after installing a new application. What should the technician do?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('Replace the CPU', False),
            ('Check Task Manager to see if the new application is consuming excessive resources, and consider uninstalling it', True),
            ('Reinstall Windows', False),
            ('Increase the screen resolution', False),
        ]
    },
    {
        'text': 'What is an application becoming "unresponsive" or "not responding" in Windows typically caused by?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('The monitor is incompatible with the application', False),
            ('The application is waiting for a resource that is unavailable, has encountered a bug, or is consuming more resources than available', True),
            ('The keyboard driver has failed', False),
            ('The application needs to be updated', False),
        ]
    },
    {
        'text': 'A user cannot install a new application and receives an "insufficient permissions" error. What should the technician do?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('Reinstall Windows', False),
            ('Run the installer as an administrator by right-clicking and selecting "Run as administrator"', True),
            ('Disable Windows Defender', False),
            ('Increase the user\'s storage quota', False),
        ]
    },
    {
        'text': 'What is the purpose of compatibility mode in Windows?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('To run applications faster by optimizing system resources', False),
            ('To run older applications that were designed for a previous version of Windows by emulating that OS environment', True),
            ('To run applications with administrator privileges automatically', False),
            ('To prevent applications from accessing the internet', False),
        ]
    },
    {
        'text': 'A user reports that Windows Update keeps failing. What should the technician try?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('Reinstall Windows immediately', False),
            ('Run the Windows Update troubleshooter, clear the Windows Update cache, and check the Event Viewer for specific error codes', True),
            ('Disable Windows Update permanently', False),
            ('Replace the hard drive', False),
        ]
    },
    {
        'text': 'What should you do if a Windows PC has a profile that is corrupted and the user cannot log in properly?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('Reinstall Windows', False),
            ('Create a new user profile, copy the user\'s data to the new profile, and delete the corrupted profile', True),
            ('Reset the user\'s password', False),
            ('Run SFC /scannow to repair the profile', False),
        ]
    },
    {
        'text': 'A user reports that their browser homepage keeps changing and they see unwanted toolbars. What is the most likely cause?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('The browser needs to be updated', False),
            ('The computer is infected with a browser hijacker — a type of malware that modifies browser settings', True),
            ('Windows Update changed the browser settings', False),
            ('The user accidentally changed the settings', False),
        ]
    },
    {
        'text': 'What is the purpose of System File Checker (SFC) in Windows?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('To check the hard drive for bad sectors', False),
            ('To scan and repair corrupted or missing Windows system files', True),
            ('To remove temporary files and free up disk space', False),
            ('To verify that all installed drivers are up to date', False),
        ]
    },

    # ── OPERATIONAL PROCEDURES ────────────────────────────────────────────────

    {
        'text': 'What is a ticketing system used for in IT support?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('To purchase hardware and software licenses', False),
            ('To track, manage, and document IT support requests and incidents from creation to resolution', True),
            ('To schedule employee shifts and work assignments', False),
            ('To monitor network performance and uptime', False),
        ]
    },
    {
        'text': 'What should always be included when documenting a resolved IT support ticket?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('Only the final solution applied', False),
            ('The problem description, steps taken to diagnose, the solution applied, and any follow-up actions required', True),
            ('The user\'s personal information and login credentials', False),
            ('A list of all software installed on the computer', False),
        ]
    },
    {
        'text': 'What is change management in IT?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('The process of training employees on new software', False),
            ('A structured process for requesting, reviewing, approving, and implementing changes to IT systems to minimize risk and disruption', True),
            ('The process of replacing outdated hardware', False),
            ('Managing the IT budget and expenses', False),
        ]
    },
    {
        'text': 'What is the purpose of a rollback plan in change management?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('To plan for future hardware upgrades', False),
            ('A documented procedure to reverse a change and restore the system to its previous state if the change causes problems', True),
            ('A plan for rolling out new software to all users', False),
            ('A schedule for regular system maintenance', False),
        ]
    },
    {
        'text': 'What is the 3-2-1 backup rule?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('Back up 3 times per day, keep 2 weeks of backups, store 1 offsite copy', False),
            ('Keep 3 copies of data on 2 different media types with 1 copy stored offsite', True),
            ('Test backups 3 times, use 2 backup solutions, perform 1 full backup per week', False),
            ('Keep data for 3 years, 2 formats, 1 cloud copy', False),
        ]
    },
    {
        'text': 'What is the difference between a full backup and an incremental backup?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('Full backups are faster than incremental backups', False),
            ('A full backup copies all data every time while an incremental backup only copies data that has changed since the last backup', True),
            ('Incremental backups include all data while full backups only include changes', False),
            ('There is no practical difference between them', False),
        ]
    },
    {
        'text': 'What is the purpose of proper cable management in a professional environment?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('To reduce the cost of cables', False),
            ('To improve airflow, reduce tripping hazards, make troubleshooting easier, and maintain a professional appearance', True),
            ('To prevent data theft through physical cable tapping', False),
            ('To increase network speed by reducing cable length', False),
        ]
    },
    {
        'text': 'What is the proper way to dispose of old hard drives containing sensitive data?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('Delete all files and empty the Recycle Bin', False),
            ('Format the drive before disposal', False),
            ('Physically destroy the drive through shredding or degaussing, or use certified data destruction software with multiple overwrite passes', True),
            ('Donate the drive to a recycling center without any special preparation', False),
        ]
    },
    {
        'text': 'What is an SLA (Service Level Agreement)?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('A contract that specifies the minimum level of service a provider must deliver, including response times and uptime guarantees', True),
            ('A software license agreement for enterprise applications', False),
            ('A security policy that defines acceptable use of company resources', False),
            ('An agreement between two companies to share IT resources', False),
        ]
    },
    {
        'text': 'What is the purpose of an Acceptable Use Policy (AUP)?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('To define what hardware employees are allowed to use', False),
            ('A document that defines the acceptable ways in which employees may use company IT resources including computers, internet, and email', True),
            ('To specify the minimum security requirements for company devices', False),
            ('A policy that determines how long data must be retained', False),
        ]
    },
    {
        'text': 'What is the correct way to handle personally identifiable information (PII)?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('Store it in a shared folder for easy access by all staff', False),
            ('Collect, store, and process it only as necessary, keep it secure, and comply with relevant privacy regulations', True),
            ('Always back it up to a public cloud service', False),
            ('Share it freely within the organization as needed', False),
        ]
    },
    {
        'text': 'What is the purpose of a network diagram in IT documentation?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('To show the company organizational chart', False),
            ('A visual representation of the network topology showing how devices are connected, making it easier to troubleshoot and plan changes', True),
            ('To document software licenses and renewal dates', False),
            ('To show the physical layout of server hardware', False),
        ]
    },
    {
        'text': 'What does BYOD stand for and what security concern does it raise?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('Build Your Own Device — a program where employees assemble their own computers', False),
            ('Bring Your Own Device — a policy allowing employees to use personal devices for work, raising concerns about data security and malware introduction', True),
            ('Buy Your Own Device — a policy where employees purchase company-approved devices', False),
            ('Backup Your Own Data — a data protection policy', False),
        ]
    },
    {
        'text': 'What is the purpose of an incident response plan?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('A plan for managing employee workplace accidents', False),
            ('A documented set of procedures for detecting, responding to, and recovering from security incidents in an organized and effective manner', True),
            ('A plan for responding to hardware failures in the server room', False),
            ('A schedule for regular security audits', False),
        ]
    },
    {
        'text': 'What is the purpose of a chain of custody in IT forensics?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('A procedure for chaining network devices together for redundancy', False),
            ('A documented record of who collected, handled, and had access to evidence to ensure its integrity and admissibility in legal proceedings', True),
            ('A process for securely transferring data between two companies', False),
            ('A method for linking user accounts across multiple systems', False),
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
        q = Question(text=qd['text'], domain=qd['domain'],
                     exam=qd.get('exam', 'core2'), active=True)
        db.session.add(q)
        db.session.flush()
        for choice_text, is_correct in qd['choices']:
            c = Choice(question_id=q.id, text=choice_text, is_correct=is_correct)
            db.session.add(c)
        added += 1
    db.session.commit()
    total = Question.query.count()
    core2_total = Question.query.filter_by(exam='core2').count()
    print(f'Added {added} new Core 2 questions. Skipped {skipped} duplicates.')
    print(f'Core 2 total: {core2_total} | Overall total: {total}')