import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app import app, db
from models import Question, Choice

questions_data = [

    # ── TROUBLESHOOTING (more) ────────────────────────────────────────────────

    {
        'text': 'A user reports their monitor displays a "No Signal" message. What should you check first?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Replace the monitor immediately', False),
            ('Check that the video cable is securely connected to both the monitor and the graphics card, and that the correct input source is selected', True),
            ('Reinstall the graphics driver', False),
            ('Replace the graphics card', False),
        ]
    },
    {
        'text': 'A computer takes a very long time to boot. What are the most likely causes?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The monitor resolution is set too high', False),
            ('Too many startup programs, a fragmented or failing hard drive, or insufficient RAM', True),
            ('The keyboard is causing a delay in the boot process', False),
            ('The network adapter is slowing the boot sequence', False),
        ]
    },
    {
        'text': 'A user hears clicking sounds coming from their computer. What does this most likely indicate?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The CPU fan needs lubrication', False),
            ('The RAM is loose in its slot', False),
            ('A failing hard disk drive — clicking is a common sign of mechanical failure', True),
            ('The power supply fan is running at maximum speed', False),
        ]
    },
    {
        'text': 'What should you do immediately if you suspect an HDD is failing?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Defragment the drive to repair bad sectors', False),
            ('Back up all data immediately before the drive fails completely', True),
            ('Run chkdsk to fix all errors and continue using the drive', False),
            ('Reformat the drive and reinstall the OS', False),
        ]
    },
    {
        'text': 'A user cannot print to a network printer even though other users can. What should you check on the user\'s computer?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Replace the printer cartridge', False),
            ('Restart the printer', False),
            ('Check that the correct printer is set as default, the printer driver is installed, and the user has permission to use the printer', True),
            ('Replace the network cable on the printer', False),
        ]
    },
    {
        'text': 'A laptop battery drains much faster than it used to. What is the most likely cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The charger is not providing enough voltage', False),
            ('Battery degradation due to charge cycles reducing its capacity over time', True),
            ('The operating system has a bug affecting power management', False),
            ('The screen brightness is too low, causing extra battery drain', False),
        ]
    },
    {
        'text': 'A user reports that their computer shuts down without warning, especially during heavy use. What is the most likely cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The hard drive is running out of space', False),
            ('Overheating — the thermal protection is shutting the system down to prevent damage', True),
            ('The RAM has too many applications loaded', False),
            ('The network connection is causing instability', False),
        ]
    },
    {
        'text': 'What tool would you use to test if a network cable is properly crimped and has continuity?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Multimeter', False),
            ('Loopback plug', False),
            ('Cable tester', True),
            ('Toner probe', False),
        ]
    },
    {
        'text': 'A user\'s keyboard types the wrong characters. What should you check?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Replace the keyboard immediately', False),
            ('Check the keyboard language and layout settings in the operating system', True),
            ('Reinstall the operating system', False),
            ('Clean the keyboard with compressed air', False),
        ]
    },
    {
        'text': 'What does it mean when a Windows computer displays "Bootmgr is missing"?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The RAM has failed and cannot load Windows', False),
            ('The Windows Boot Manager file is corrupted or the system is trying to boot from the wrong device', True),
            ('The graphics driver is missing and needs to be reinstalled', False),
            ('The hard drive is full and cannot load system files', False),
        ]
    },
    {
        'text': 'A user reports that their internet works but they cannot access any websites by name, only by IP address. What is the problem?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The firewall is blocking all web traffic', False),
            ('DNS resolution is not working — the DNS server may be unreachable or incorrectly configured', True),
            ('The web browser needs to be reinstalled', False),
            ('The network adapter driver is outdated', False),
        ]
    },
    {
        'text': 'When should you try the simplest solution first when troubleshooting?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Only when dealing with software problems', False),
            ('Always — starting with the simplest and most common causes before moving to complex solutions saves time', True),
            ('Only when the user is a beginner', False),
            ('Only when the problem has occurred before', False),
        ]
    },
    {
        'text': 'A user reports that their external hard drive is not showing up in Windows Explorer. What should you check?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Replace the external hard drive', False),
            ('Check Disk Management to see if the drive is detected but needs a drive letter assigned or needs to be initialized', True),
            ('Reinstall Windows to fix the USB subsystem', False),
            ('Update the BIOS firmware', False),
        ]
    },
    {
        'text': 'What is the purpose of using a known-good spare part when troubleshooting hardware?',
        'domain': 'Troubleshooting',
        'choices': [
            ('To permanently replace the faulty component', False),
            ('To confirm whether the original component is causing the problem by swapping it with a working one', True),
            ('To test the spare part before selling it', False),
            ('To avoid buying new parts unnecessarily', False),
        ]
    },
    {
        'text': 'A user receives a "Low Disk Space" warning on Windows. What should you do?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Defragment the drive to recover space', False),
            ('Run Disk Cleanup, uninstall unused programs, and move large files to external storage or the cloud', True),
            ('Reinstall Windows to free up space', False),
            ('Add more RAM to compensate for low disk space', False),
        ]
    },

    # ── VIRTUALIZATION & CLOUD (more) ─────────────────────────────────────────

    {
        'text': 'What is the purpose of a virtual switch in a virtualized environment?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('To physically connect servers in a data center', False),
            ('To provide network connectivity between virtual machines and the physical network', True),
            ('To encrypt traffic between virtual machines', False),
            ('To balance CPU load across multiple virtual machines', False),
        ]
    },
    {
        'text': 'What does "elasticity" mean in cloud computing?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('The ability of cloud systems to withstand hardware failures', False),
            ('The ability to automatically scale resources up or down based on demand', True),
            ('The flexibility to choose between different cloud providers', False),
            ('The durability of data stored in the cloud', False),
        ]
    },
    {
        'text': 'What is the main advantage of cloud storage over local storage?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('Cloud storage is always faster than local storage', False),
            ('Cloud storage is accessible from anywhere with an internet connection and provides redundancy', True),
            ('Cloud storage never requires a subscription fee', False),
            ('Cloud storage uses less bandwidth than local storage', False),
        ]
    },
    {
        'text': 'What does "on-premises" mean in the context of IT infrastructure?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('Software that is only available online', False),
            ('Hardware and software that is physically located and managed within the organization\'s own facilities', True),
            ('A type of cloud service managed by a third party', False),
            ('Servers that are located in a co-location data center', False),
        ]
    },
    {
        'text': 'What is the purpose of a VM template?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('To create a backup of a running virtual machine', False),
            ('A pre-configured virtual machine image used to rapidly deploy new VMs with a consistent configuration', True),
            ('To update the hypervisor software', False),
            ('To migrate VMs between different cloud providers', False),
        ]
    },
    {
        'text': 'What is high availability (HA) in virtualization?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('A feature that maximizes VM performance by allocating more CPU resources', False),
            ('A feature that automatically restarts virtual machines on another host if the original host fails', True),
            ('A security feature that isolates VMs from each other', False),
            ('A backup feature that creates daily snapshots of all VMs', False),
        ]
    },
    {
        'text': 'What is the difference between cloud backup and cloud storage?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('There is no difference — they are the same service', False),
            ('Cloud backup is specifically designed to restore data after a failure while cloud storage is for active file access and sharing', True),
            ('Cloud backup is free while cloud storage requires a subscription', False),
            ('Cloud storage provides better security than cloud backup', False),
        ]
    },
    {
        'text': 'What does multi-tenancy mean in cloud computing?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('A cloud service that requires multiple administrators', False),
            ('Multiple customers sharing the same physical infrastructure while their data and applications remain isolated from each other', True),
            ('A cloud service that operates across multiple geographic regions', False),
            ('A billing model where multiple departments share one cloud account', False),
        ]
    },
    {
        'text': 'What is a hyperconverged infrastructure (HCI)?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('A network infrastructure that combines wired and wireless connections', False),
            ('A software-defined IT infrastructure that combines compute, storage, and networking into a single system managed by a hypervisor', True),
            ('A type of cloud service that combines IaaS and SaaS', False),
            ('A server architecture that uses multiple CPUs for maximum performance', False),
        ]
    },
    {
        'text': 'What is the purpose of resource allocation in virtualization?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('To permanently assign physical hardware to specific virtual machines', False),
            ('To distribute CPU, memory, and storage resources among virtual machines based on their needs and priorities', True),
            ('To encrypt resources to prevent unauthorized VM access', False),
            ('To monitor network traffic between virtual machines', False),
        ]
    },

    # ── NETWORKING (more) ─────────────────────────────────────────────────────

    {
        'text': 'What is the purpose of a DHCP reservation?',
        'domain': 'Networking',
        'choices': [
            ('To block a specific device from getting an IP address', False),
            ('To ensure a specific device always receives the same IP address from the DHCP server based on its MAC address', True),
            ('To reserve a range of IP addresses for future use', False),
            ('To prevent IP address conflicts on the network', False),
        ]
    },
    {
        'text': 'What does the term "bandwidth" refer to in networking?',
        'domain': 'Networking',
        'choices': [
            ('The physical width of a network cable', False),
            ('The maximum rate at which data can be transferred over a network connection', True),
            ('The number of devices that can connect to a network simultaneously', False),
            ('The distance a wireless signal can travel', False),
        ]
    },
    {
        'text': 'What is a network bridge?',
        'domain': 'Networking',
        'choices': [
            ('A device that connects two different types of networks such as wired and wireless', False),
            ('A device that connects two network segments and forwards traffic between them based on MAC addresses', True),
            ('A device that translates between IPv4 and IPv6 addresses', False),
            ('A cable that connects two switches together', False),
        ]
    },
    {
        'text': 'What is the purpose of a network repeater?',
        'domain': 'Networking',
        'choices': [
            ('To filter and block unwanted network traffic', False),
            ('To regenerate and amplify a network signal to extend the range of a network', True),
            ('To convert between different network protocols', False),
            ('To assign IP addresses to devices on the network', False),
        ]
    },
    {
        'text': 'What does the acronym SSID stand for?',
        'domain': 'Networking',
        'choices': [
            ('Subnet Service Identifier', False),
            ('Service Set Identifier — the name broadcast by a wireless access point to identify a Wi-Fi network', True),
            ('Secure System Internet Device', False),
            ('Static Station IP Designation', False),
        ]
    },
    {
        'text': 'What is a rogue access point?',
        'domain': 'Networking',
        'choices': [
            ('An access point that has lost its configuration settings', False),
            ('An unauthorized wireless access point connected to the network that can be used to intercept traffic or bypass security', True),
            ('An access point that broadcasts on an unauthorized frequency', False),
            ('A wireless access point with a weak signal', False),
        ]
    },
    {
        'text': 'What does latency mean in networking?',
        'domain': 'Networking',
        'choices': [
            ('The total amount of data transmitted per second', False),
            ('The delay between sending a request and receiving a response — measured in milliseconds', True),
            ('The number of packets lost during transmission', False),
            ('The physical distance between two network devices', False),
        ]
    },
    {
        'text': 'What is packet loss and what can cause it?',
        'domain': 'Networking',
        'choices': [
            ('Data that is encrypted before transmission and cannot be read', False),
            ('When data packets fail to reach their destination, caused by network congestion, faulty hardware, or poor wireless signal', True),
            ('When a packet is duplicated and arrives twice at the destination', False),
            ('When packets arrive out of order at their destination', False),
        ]
    },
    {
        'text': 'What is the purpose of port forwarding on a router?',
        'domain': 'Networking',
        'choices': [
            ('To speed up internet traffic by prioritizing certain ports', False),
            ('To redirect incoming traffic on a specific port to a specific device on the local network', True),
            ('To block incoming traffic on dangerous ports', False),
            ('To assign static IP addresses to devices based on their port usage', False),
        ]
    },
    {
        'text': 'What is an IP address conflict and what causes it?',
        'domain': 'Networking',
        'choices': [
            ('When two devices try to access the same website simultaneously', False),
            ('When two devices on the same network are assigned the same IP address, causing connectivity issues for both', True),
            ('When a device tries to connect to a network it is not authorized to use', False),
            ('When a router runs out of IP addresses to assign', False),
        ]
    },
    {
        'text': 'What is the function of a wireless access point?',
        'domain': 'Networking',
        'choices': [
            ('To assign IP addresses to wireless devices', False),
            ('To connect wireless devices to a wired network by transmitting and receiving Wi-Fi signals', True),
            ('To encrypt wireless traffic between devices', False),
            ('To extend the range of a wired network using fiber optic cable', False),
        ]
    },

    # ── SECURITY (more) ───────────────────────────────────────────────────────

    {
        'text': 'What is a security audit?',
        'domain': 'Security',
        'choices': [
            ('A scan for viruses on a single computer', False),
            ('A systematic evaluation of an organization\'s information security to identify vulnerabilities and verify compliance with policies', True),
            ('A review of user passwords to ensure they are strong enough', False),
            ('A physical inspection of server hardware for damage', False),
        ]
    },
    {
        'text': 'What is the purpose of a honeypot in network security?',
        'domain': 'Security',
        'choices': [
            ('To store encrypted backup data securely', False),
            ('A decoy system designed to attract attackers and gather information about their methods while keeping real systems safe', True),
            ('To filter malicious traffic before it reaches the network', False),
            ('To provide secure remote access for authorized users', False),
        ]
    },
    {
        'text': 'What is two-factor authentication (2FA)?',
        'domain': 'Security',
        'choices': [
            ('Using two different passwords for the same account', False),
            ('A security method requiring two separate forms of verification such as a password and a code sent to a phone', True),
            ('Logging in from two different devices simultaneously', False),
            ('A system that requires two administrators to approve access', False),
        ]
    },
    {
        'text': 'What is the difference between authentication and authorization?',
        'domain': 'Security',
        'choices': [
            ('They are the same thing — both verify who you are', False),
            ('Authentication verifies who you are while authorization determines what you are allowed to do', True),
            ('Authentication is for users and authorization is for devices', False),
            ('Authorization happens before authentication in the security process', False),
        ]
    },
    {
        'text': 'What is a security token?',
        'domain': 'Security',
        'choices': [
            ('A password that changes every login', False),
            ('A physical or digital device that generates a one-time code used as part of multi-factor authentication', True),
            ('A certificate that verifies a website is legitimate', False),
            ('An encrypted file that stores user credentials', False),
        ]
    },
    {
        'text': 'What does the acronym CIA stand for in information security?',
        'domain': 'Security',
        'choices': [
            ('Computer Intrusion Analysis', False),
            ('Confidentiality, Integrity, and Availability — the three core principles of information security', True),
            ('Certified Internet Administrator', False),
            ('Cyber Intelligence Agency', False),
        ]
    },
    {
        'text': 'What is data integrity in the context of security?',
        'domain': 'Security',
        'choices': [
            ('The encryption of data during transmission', False),
            ('Ensuring that data is accurate, complete, and has not been tampered with or altered', True),
            ('The process of backing up data to prevent loss', False),
            ('The availability of data to authorized users at all times', False),
        ]
    },
    {
        'text': 'What is a security patch?',
        'domain': 'Security',
        'choices': [
            ('A physical device that protects network ports from unauthorized access', False),
            ('A software update specifically designed to fix a security vulnerability in an operating system or application', True),
            ('A configuration change that strengthens firewall rules', False),
            ('An antivirus definition update that adds new malware signatures', False),
        ]
    },
    {
        'text': 'What is the purpose of a CAPTCHA?',
        'domain': 'Security',
        'choices': [
            ('To encrypt data submitted through web forms', False),
            ('To distinguish between human users and automated bots by presenting a challenge that is easy for humans but difficult for machines', True),
            ('To verify that a website uses HTTPS', False),
            ('To scan uploaded files for malware', False),
        ]
    },
    {
        'text': 'What is shoulder surfing?',
        'domain': 'Security',
        'choices': [
            ('A type of network attack that intercepts wireless signals', False),
            ('A social engineering technique where an attacker observes someone entering sensitive information such as a PIN or password', True),
            ('An attack that uses reflections in windows or mirrors to read screen content', False),
            ('A physical attack on server hardware in a data center', False),
        ]
    },

    # ── OPERATING SYSTEMS (more) ──────────────────────────────────────────────

    {
        'text': 'What is the Windows command to display the contents of a directory?',
        'domain': 'Operating Systems',
        'choices': [
            ('ls', False),
            ('dir', True),
            ('show', False),
            ('list', False),
        ]
    },
    {
        'text': 'What does the Windows command "shutdown /r /t 0" do?',
        'domain': 'Operating Systems',
        'choices': [
            ('Shuts down the computer immediately without restarting', False),
            ('Restarts the computer immediately with no delay', True),
            ('Schedules a restart in 0 minutes from midnight', False),
            ('Resets the system clock to zero', False),
        ]
    },
    {
        'text': 'What is the purpose of the Windows services.msc snap-in?',
        'domain': 'Operating Systems',
        'choices': [
            ('To manage installed applications and programs', False),
            ('To view, start, stop, and configure Windows background services', True),
            ('To monitor CPU and memory performance in real time', False),
            ('To manage network adapter settings and drivers', False),
        ]
    },
    {
        'text': 'What is a swap file in Linux?',
        'domain': 'Operating Systems',
        'choices': [
            ('A file used to exchange data between two users', False),
            ('A file on the hard drive used as virtual memory when physical RAM is full, similar to the Windows pagefile', True),
            ('A log file that records all user commands', False),
            ('A configuration file for network settings', False),
        ]
    },
    {
        'text': 'What is the purpose of the Windows Environment Variables?',
        'domain': 'Operating Systems',
        'choices': [
            ('To store the current weather and location data', False),
            ('To store system-wide and user-specific settings and paths that applications and the OS use to locate resources', True),
            ('To configure display settings and resolution', False),
            ('To manage network connection profiles', False),
        ]
    },
    {
        'text': 'What does the acronym NTFS stand for?',
        'domain': 'Operating Systems',
        'choices': [
            ('Network Transfer File System', False),
            ('New Technology File System', True),
            ('Node Terminal File Service', False),
            ('Native Transfer Format Standard', False),
        ]
    },
    {
        'text': 'What is the Windows command to copy files and folders including subdirectories?',
        'domain': 'Operating Systems',
        'choices': [
            ('copy /s', False),
            ('xcopy', True),
            ('move', False),
            ('robocopy /basic', False),
        ]
    },
    {
        'text': 'What is the purpose of the Windows Performance Monitor?',
        'domain': 'Operating Systems',
        'choices': [
            ('To monitor and display real-time and historical performance data for system resources like CPU, memory, disk, and network', True),
            ('To manage and update installed applications', False),
            ('To test network speed and latency', False),
            ('To configure power management settings', False),
        ]
    },
    {
        'text': 'What does the Linux command "chmod" do?',
        'domain': 'Operating Systems',
        'choices': [
            ('Changes the owner of a file or directory', False),
            ('Changes the read, write, and execute permissions of a file or directory', True),
            ('Changes the name of a file or directory', False),
            ('Changes the location of a file or directory', False),
        ]
    },
    {
        'text': 'What is the purpose of the PATH environment variable in Windows and Linux?',
        'domain': 'Operating Systems',
        'choices': [
            ('To store the current user\'s home directory location', False),
            ('To tell the operating system which directories to search when a command is entered without a full file path', True),
            ('To define the default save location for downloaded files', False),
            ('To specify the location of system log files', False),
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
        q = Question(text=qd['text'], domain=qd['domain'], active=True)
        db.session.add(q)
        db.session.flush()
        for choice_text, is_correct in qd['choices']:
            c = Choice(question_id=q.id, text=choice_text, is_correct=is_correct)
            db.session.add(c)
        added += 1
    db.session.commit()
    total = Question.query.count()
    print(f'Added {added} new questions. Skipped {skipped} duplicates. Total in DB: {total}')