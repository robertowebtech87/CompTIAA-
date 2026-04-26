from app import app, db
from models import Question, Choice

questions_data = [

    # ── OPERATING SYSTEMS ─────────────────────────────────────────────────────

    {
        'text': 'What is the Windows "Problem Steps Recorder" (PSR) used for?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A tool for recording audio problems on the system', False),
            ('Records screen activity and user actions with screenshots to help document and reproduce technical problems for support', True),
            ('A performance recording tool for benchmarking', False),
            ('A tool for recording BSOD crash events', False),
        ]
    },
    {
        'text': 'What is the purpose of the Windows "Resource Monitor"?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Monitors electrical power consumption of components', False),
            ('Provides detailed real-time information about CPU memory disk and network usage by individual processes', True),
            ('Manages system restore points and resources', False),
            ('Monitors hardware temperatures and fan speeds', False),
        ]
    },
    {
        'text': 'What does the Windows command "ipconfig /flushdns" do?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Resets the network adapter to factory settings', False),
            ('Clears the local DNS resolver cache forcing the computer to look up fresh DNS records', True),
            ('Flushes all network traffic and resets connections', False),
            ('Releases and renews the IP address from DHCP', False),
        ]
    },
    {
        'text': 'What is a "mandatory user profile" in a Windows domain?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A profile that forces the user to change their password', False),
            ('A read-only roaming profile where changes are discarded at logoff — used to enforce a consistent desktop environment', True),
            ('A profile that cannot be deleted by administrators', False),
            ('A profile that requires biometric authentication', False),
        ]
    },
    {
        'text': 'What is the purpose of the "net share" command in Windows?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Shares internet connection with other devices', False),
            ('Displays creates or deletes shared folders on a Windows computer from the command line', True),
            ('Tests connectivity to network shares', False),
            ('Configures network share permissions', False),
        ]
    },
    {
        'text': 'What is Windows "DirectX" and why is it important?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A security framework for encrypting files', False),
            ('A collection of APIs that handle multimedia tasks especially gaming and video — applications require specific versions to run properly', True),
            ('A direct connection protocol for network shares', False),
            ('A file system used for external drives', False),
        ]
    },
    {
        'text': 'What is the Windows "Component Services" console used for?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Managing physical hardware components', False),
            ('Configuring and managing COM and DCOM components distributed transactions and event services', True),
            ('Installing and removing Windows features', False),
            ('Managing printer components and drivers', False),
        ]
    },
    {
        'text': 'What does the error "The trust relationship between this workstation and the primary domain failed" mean?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The user has entered the wrong password too many times', False),
            ('The computer account in Active Directory has lost its secure channel with the domain controller and needs to be rejoined to the domain', True),
            ('The domain controller is offline', False),
            ('The user account has been disabled', False),
        ]
    },
    {
        'text': 'What is the purpose of the Windows "Performance Monitor" (perfmon)?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A tool exclusively for monitoring GPU performance', False),
            ('Tracks and logs system performance data over time allowing analysis of CPU memory disk and network metrics to identify bottlenecks', True),
            ('Monitors employee productivity metrics', False),
            ('A real-time process viewer similar to Task Manager', False),
        ]
    },
    {
        'text': 'What is "Windows To Go" and in which editions was it available?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A portable version of Windows that runs from a USB drive — available in Windows 10 Enterprise and Education', True),
            ('A cloud version of Windows that runs in a browser', False),
            ('Windows installed on a tablet for mobile use', False),
            ('A lightweight Windows version for older hardware', False),
        ]
    },

    # ── OPERATING SYSTEMS — Multi Select ──────────────────────────────────────

    {
        'text': 'Which TWO of the following are true about Windows PowerShell? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('PowerShell can automate administrative tasks using scripts', True),
            ('PowerShell only works on Windows and not on other operating systems', False),
            ('PowerShell uses cmdlets which are more powerful than basic command prompt commands', True),
            ('PowerShell replaces all functionality of Command Prompt and they cannot run the same commands', False),
        ]
    },
    {
        'text': 'Which TWO Windows editions include the ability to host Remote Desktop connections? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Windows 10/11 Pro', True),
            ('Windows 10/11 Home', False),
            ('Windows 10/11 Enterprise', True),
            ('Windows 10/11 S Mode', False),
        ]
    },
    {
        'text': 'Which TWO are valid Windows startup modes accessible from the Advanced Boot Options? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Safe Mode with Networking', True),
            ('Turbo Boot Mode', False),
            ('Enable Boot Logging', True),
            ('Express Boot Mode', False),
        ]
    },
    {
        'text': 'Which TWO of the following are correct about the Windows Registry structure? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('HKEY_LOCAL_MACHINE contains settings that apply to all users on the computer', True),
            ('The Registry can only be edited using the regedit graphical tool', False),
            ('HKEY_CURRENT_USER contains settings specific to the currently logged-in user', True),
            ('Deleting a registry key has no effect on system behavior', False),
        ]
    },

    # ── SECURITY ──────────────────────────────────────────────────────────────

    {
        'text': 'What is "on-path attack" (formerly known as man-in-the-middle)?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('An attacker blocking all traffic on a network path', False),
            ('An attacker positioning themselves between two communicating parties to intercept or alter their communication without either party knowing', True),
            ('An attack that targets the network routing path', False),
            ('An attack using the shortest network path to reach a target', False),
        ]
    },
    {
        'text': 'What is "session hijacking"?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Physically stealing a user\'s computer during an active session', False),
            ('Stealing or forging a session token to take over an authenticated user\'s active session without needing their credentials', True),
            ('Crashing an application to terminate user sessions', False),
            ('Intercepting a video conference session', False),
        ]
    },
    {
        'text': 'What is "cross-site scripting" (XSS)?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Copying scripts from one website to another', False),
            ('A web attack where malicious scripts are injected into trusted websites and executed in victims\' browsers to steal data or hijack sessions', True),
            ('A technique for running scripts across multiple servers simultaneously', False),
            ('A method of testing websites for scripting errors', False),
        ]
    },
    {
        'text': 'What is "typosquatting"?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Squatting in a physical location to access a company\'s Wi-Fi', False),
            ('Registering domain names that are common misspellings of legitimate websites to trick users who make typos into visiting malicious sites', True),
            ('Using autocorrect to change typed URLs to malicious ones', False),
            ('A brute force technique that tries common typing patterns', False),
        ]
    },
    {
        'text': 'What is a "supply chain attack"?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('An attack targeting retail supply chain management systems', False),
            ('Compromising a software vendor or hardware manufacturer to distribute malware through legitimate updates or products to their customers', True),
            ('Disrupting the delivery of physical IT equipment', False),
            ('Attacking a company through its internet service provider', False),
        ]
    },
    {
        'text': 'What is the purpose of "content filtering" in a network security context?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Compressing web content to improve network speed', False),
            ('Inspecting and blocking network traffic based on content type URL categories or keywords to enforce acceptable use policies and block malicious content', True),
            ('Filtering out duplicate network packets', False),
            ('Prioritizing network traffic based on content type', False),
        ]
    },
    {
        'text': 'What is "endpoint detection and response" (EDR)?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A basic antivirus solution for endpoints', False),
            ('A security solution that continuously monitors endpoints for threats provides real-time detection and enables rapid investigation and response to incidents', True),
            ('A tool for managing endpoint device configurations', False),
            ('Software that detects when endpoints connect to the network', False),
        ]
    },
    {
        'text': 'What is "steganography" in cybersecurity?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A type of strong encryption algorithm', False),
            ('The practice of hiding secret information within ordinary non-secret files like images or audio to conceal the existence of the message', True),
            ('A technique for securing network stenography protocols', False),
            ('A method of writing security policies', False),
        ]
    },
    {
        'text': 'What is "role-based access control" (RBAC)?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Controlling access based on the user\'s physical role in the building', False),
            ('A method of restricting system access where permissions are assigned to roles and users are assigned to those roles rather than assigning permissions directly to individuals', True),
            ('An access control system based on the time of day', False),
            ('Granting access based on the user\'s seniority level', False),
        ]
    },
    {
        'text': 'What is a "false positive" in security scanning?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A security threat that was successfully blocked', False),
            ('When a security tool incorrectly identifies legitimate activity or a safe file as malicious', True),
            ('A positive security scan result that confirms no threats', False),
            ('When a threat bypasses security detection undetected', False),
        ]
    },

    # ── SECURITY — Multi Select ────────────────────────────────────────────────

    {
        'text': 'Which TWO of the following are true about HTTPS? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('HTTPS encrypts data transmitted between the browser and web server', True),
            ('HTTPS guarantees that a website is legitimate and not a phishing site', False),
            ('HTTPS uses SSL/TLS certificates to establish encrypted connections', True),
            ('HTTPS makes websites load faster than HTTP', False),
        ]
    },
    {
        'text': 'Which TWO of the following describe good password policy practices? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Require a minimum password length of at least 8 characters', True),
            ('Require users to change passwords every 30 days for maximum security', False),
            ('Implement account lockout after multiple failed login attempts', True),
            ('Allow users to reuse their last 20 passwords for convenience', False),
        ]
    },
    {
        'text': 'Which TWO of the following are examples of data at rest encryption? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('BitLocker encrypting the entire hard drive', True),
            ('HTTPS encrypting web traffic', False),
            ('EFS encrypting individual files on an NTFS volume', True),
            ('VPN encrypting network tunnel traffic', False),
        ]
    },
    {
        'text': 'Which TWO actions should be taken when an employee leaves the company? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Immediately disable or delete their user accounts', True),
            ('Leave their accounts active for 90 days in case they return', False),
            ('Revoke their access to all systems and physical premises', True),
            ('Keep their passwords on file for data recovery purposes', False),
        ]
    },
    {
        'text': 'Which TWO are true about wireless security protocols? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('WPA3 is currently the most secure widely available Wi-Fi security protocol', True),
            ('WEP provides equivalent security to WPA2', False),
            ('WPA2 uses AES encryption which is significantly more secure than WEP', True),
            ('All wireless security protocols provide the same level of protection', False),
        ]
    },

    # ── SOFTWARE TROUBLESHOOTING ───────────────────────────────────────────────

    {
        'text': 'A user reports that Windows shows the correct time but keeps reverting to the wrong time zone after restart. What should be checked?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Replace the CMOS battery', False),
            ('Check if Group Policy is enforcing a specific time zone or if Windows location services are incorrectly detecting the time zone', True),
            ('The network adapter needs updating', False),
            ('Windows needs to be reinstalled', False),
        ]
    },
    {
        'text': 'A user reports their computer freezes every time they play video. Other tasks work fine. What is the most likely cause?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The RAM is failing', False),
            ('The GPU or its driver is struggling with video decode — try updating the graphics driver or checking GPU temperatures', True),
            ('The hard drive is failing', False),
            ('The monitor is incompatible', False),
        ]
    },
    {
        'text': 'A technician runs SFC and it reports "Windows Resource Protection found corrupt files but was unable to fix some of them." What should be done next?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Reinstall Windows immediately', False),
            ('Run DISM /Online /Cleanup-Image /RestoreHealth first to repair the component store then run SFC again', True),
            ('Replace the hard drive', False),
            ('Run chkdsk only', False),
        ]
    },
    {
        'text': 'A user\'s laptop screen goes black after exactly 2 minutes of inactivity even though power settings say never. What should be checked?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The screen is failing', False),
            ('Check if a screensaver or Group Policy is overriding the local power settings', True),
            ('Update the display driver', False),
            ('Replace the battery', False),
        ]
    },
    {
        'text': 'A user reports that their microphone works in some apps but not others after a Windows update. What is the likely cause?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The microphone hardware is failing selectively', False),
            ('Windows privacy settings are blocking microphone access for specific apps — check Settings > Privacy > Microphone', True),
            ('The audio driver needs reinstalling', False),
            ('The microphone is incompatible with the updated Windows version', False),
        ]
    },
    {
        'text': 'What does it mean when Device Manager shows a yellow exclamation mark next to a device?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The device is working perfectly and is highlighted', False),
            ('The device has a problem — usually a missing corrupted or incompatible driver', True),
            ('The device needs a firmware update', False),
            ('The device is disabled by the administrator', False),
        ]
    },
    {
        'text': 'A user installed antivirus software and now their computer is extremely slow. What should the technician investigate?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The antivirus is incompatible with the CPU', False),
            ('The antivirus may be doing a full initial scan conflicting with Windows Defender or the real-time protection settings need adjusting', True),
            ('The hard drive needs replacing', False),
            ('The RAM needs upgrading', False),
        ]
    },
    {
        'text': 'A user cannot open any PDF files. They double-click and nothing happens. What should be checked first?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The PDF files are corrupted', False),
            ('Check if a PDF reader is installed and set as the default application for PDF files in Windows settings', True),
            ('Reinstall Windows', False),
            ('The hard drive has bad sectors affecting PDF files', False),
        ]
    },
    {
        'text': 'What does it mean when Windows shows "not enough disk space" during an update even though the drive has free space?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The disk space indicator is wrong — ignore the error', False),
            ('Windows Update requires a specific amount of free space on the system partition — run Disk Cleanup and clear Windows Update cache', True),
            ('The file system is corrupted', False),
            ('The hard drive needs to be replaced', False),
        ]
    },
    {
        'text': 'A user reports that after joining a domain they can no longer access local shares they could before. What is most likely happening?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Domain computers cannot access local shares', False),
            ('Domain Group Policy may have changed the network profile to Domain which has different firewall rules blocking local sharing', True),
            ('The hard drive failed during domain join', False),
            ('Local accounts are automatically deleted when joining a domain', False),
        ]
    },

    # ── SOFTWARE TROUBLESHOOTING — Multi Select ───────────────────────────────

    {
        'text': 'Which TWO are common causes of Windows not recognizing a newly installed internal drive? (Select TWO)',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('The drive has not been initialized and partitioned in Disk Management', True),
            ('The drive brand is not supported by Windows', False),
            ('The SATA or power cable is not properly connected', True),
            ('The drive needs to be registered with Microsoft', False),
        ]
    },
    {
        'text': 'Which TWO steps help resolve a "Windows could not connect to the Group Policy Client service" error? (Select TWO)',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Check and repair the Group Policy Client service registry permissions', True),
            ('Replace the network adapter', False),
            ('Use System File Checker to repair corrupted system files', True),
            ('Reinstall the printer drivers', False),
        ]
    },
    {
        'text': 'Which TWO tools help identify what is causing high memory usage in Windows? (Select TWO)',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Task Manager sorted by Memory column', True),
            ('Disk Defragmenter', False),
            ('Resource Monitor — Memory tab showing per-process usage', True),
            ('Windows Update', False),
        ]
    },

    # ── OPERATIONAL PROCEDURES ────────────────────────────────────────────────

    {
        'text': 'What is "vendor management" in IT operations?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Managing the physical vendors that come to the office', False),
            ('The process of selecting evaluating and managing relationships with third-party technology vendors to ensure they meet contractual obligations and security standards', True),
            ('Managing the inventory of vendor-supplied equipment', False),
            ('Negotiating prices with hardware suppliers', False),
        ]
    },
    {
        'text': 'What is a "playbook" in cybersecurity incident response?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A book of security certifications and their requirements', False),
            ('A documented set of predefined steps and procedures for responding to specific types of security incidents', True),
            ('A training manual for new security analysts', False),
            ('A list of approved security tools', False),
        ]
    },
    {
        'text': 'What is "technical debt" in IT?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The financial cost of IT equipment purchases', False),
            ('The accumulated cost of shortcuts and outdated systems that need to be fixed later — taking the easy solution now creates more work and risk in the future', True),
            ('Money owed to technology vendors', False),
            ('The cost of cybersecurity incidents', False),
        ]
    },
    {
        'text': 'What is "business continuity planning" (BCP)?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Planning the company\'s annual IT budget', False),
            ('A strategy for ensuring critical business functions continue to operate during and after a disaster or major disruption', True),
            ('A plan for business growth and expansion', False),
            ('Planning regular business reviews and audits', False),
        ]
    },
    {
        'text': 'What is "first call resolution" (FCR) in IT support?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The policy of always calling the user before working on their ticket', False),
            ('Resolving a support issue during the first contact without requiring follow-up calls or escalation — a key metric of support quality', True),
            ('The first phone call made when setting up a new IT system', False),
            ('Calling the vendor first before troubleshooting any issue', False),
        ]
    },
    {
        'text': 'What is the purpose of "hardening" an operating system?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Upgrading to a faster CPU for better performance', False),
            ('Reducing the attack surface by disabling unnecessary services removing default accounts applying patches and enforcing security policies', True),
            ('Installing a physical case to protect the computer', False),
            ('Configuring the system for maximum performance', False),
        ]
    },
    {
        'text': 'What is a "golden image" in IT deployment?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A high-resolution company logo used in presentations', False),
            ('A pre-configured master system image used to rapidly deploy identical standardized computers across an organization', True),
            ('A backup image of the most important server', False),
            ('An award-winning IT infrastructure design', False),
        ]
    },
    {
        'text': 'What is the principle of "need to know" in information security?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Users should know all company policies', False),
            ('Access to information should only be granted to individuals who need it to perform their specific job function', True),
            ('IT staff need to know all user passwords for support purposes', False),
            ('Management needs to know all employee activities', False),
        ]
    },
    {
        'text': 'What is a "hot site" in disaster recovery?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A server room that runs at high temperatures for efficiency', False),
            ('A fully equipped backup facility with running systems ready for immediate failover with minimal downtime', True),
            ('A temporary office space set up after a disaster', False),
            ('A cloud server that activates when the primary server gets too hot', False),
        ]
    },
    {
        'text': 'What is the difference between a "hot site" cold site" and "warm site" in disaster recovery?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('They refer to the temperature of the server room', False),
            ('Hot site is fully operational and ready immediately — warm site has infrastructure but needs setup — cold site has only the physical space and power', True),
            ('Hot site is for summer disasters warm site for spring and cold site for winter', False),
            ('They are identical concepts with different names used by different vendors', False),
        ]
    },

    # ── OPERATIONAL PROCEDURES — Multi Select ─────────────────────────────────

    {
        'text': 'Which TWO of the following are true about change management? (Select TWO)',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Emergency changes can bypass normal approval when business critical but must still be documented afterward', True),
            ('All changes no matter how small must go through a six-week approval process', False),
            ('Change management reduces the risk of unintended consequences from system modifications', True),
            ('Change management only applies to software changes not hardware', False),
        ]
    },
    {
        'text': 'Which TWO are best practices for remote support sessions? (Select TWO)',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Always get explicit permission from the user before accessing their computer remotely', True),
            ('Keep the remote session open indefinitely for future use', False),
            ('Inform the user of everything you are doing during the session', True),
            ('Save the user\'s credentials for faster future access', False),
        ]
    },
    {
        'text': 'Which TWO of the following are true about IT documentation? (Select TWO)',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Good documentation reduces resolution time for recurring issues', True),
            ('Documentation should only be created for major outages', False),
            ('Network diagrams are an important part of IT documentation', True),
            ('Documentation is unnecessary if the same technician always handles issues', False),
        ]
    },
    {
        'text': 'Which TWO are examples of environmental controls in a data center? (Select TWO)',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('HVAC systems maintaining proper temperature and humidity', True),
            ('Antivirus software protecting servers', False),
            ('Fire suppression systems protecting against fire damage', True),
            ('Firewalls protecting against network attacks', False),
        ]
    },

    # ── MIXED — Additional questions ──────────────────────────────────────────

    {
        'text': 'What is "application virtualization" and give an example?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Running applications on a virtual machine — for example VMware', False),
            ('Packaging an application with all its dependencies so it runs in an isolated environment without being installed traditionally — for example Microsoft App-V or Docker containers', True),
            ('Creating a virtual copy of an application for backup', False),
            ('Running multiple instances of the same application simultaneously', False),
        ]
    },
    {
        'text': 'What is "bring your own technology" (BYOT) policy?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A policy allowing employees to purchase company technology', False),
            ('A broader policy than BYOD that allows employees to use any personal technology including devices wearables and software for work purposes', True),
            ('A policy for employees to build their own computers', False),
            ('A technology sharing program between departments', False),
        ]
    },
    {
        'text': 'What is "threat intelligence" in cybersecurity?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The ability of antivirus software to detect new threats automatically', False),
            ('Evidence-based knowledge about existing or emerging threats that helps organizations make informed decisions about their security posture', True),
            ('Intelligence gathered by physically monitoring suspicious individuals', False),
            ('Automated threat detection using artificial intelligence', False),
        ]
    },
    {
        'text': 'What is a "security baseline"?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The minimum security requirements an organization must meet', False),
            ('A documented set of minimum security configurations that all systems must meet before being deployed in the production environment', True),
            ('The base level of encryption used across the organization', False),
            ('A network monitoring threshold that triggers alerts', False),
        ]
    },
    {
        'text': 'What is the purpose of "network address translation" (NAT)?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Translates network names to IP addresses like DNS', False),
            ('Allows multiple devices on a private network to share a single public IP address by translating private addresses to the public address and back', True),
            ('Encrypts network traffic for security', False),
            ('Converts IPv4 addresses to IPv6 format', False),
        ]
    },
    {
        'text': 'What is a "next-generation firewall" (NGFW)?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A firewall that will be available in the next generation of hardware', False),
            ('An advanced firewall that goes beyond port and protocol filtering to include application awareness deep packet inspection intrusion prevention and threat intelligence', True),
            ('A firewall designed specifically for IPv6 networks', False),
            ('A wireless firewall for protecting Wi-Fi networks', False),
        ]
    },
    {
        'text': 'Which TWO of the following are true about incident response? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('The first phase of incident response is preparation — having a plan before an incident occurs', True),
            ('Incidents should be resolved as quickly as possible without documenting anything to save time', False),
            ('Lessons learned from incidents should be used to improve future security posture', True),
            ('Only large organizations need an incident response plan', False),
        ]
    },
    {
        'text': 'Which TWO of the following correctly describe the concept of "least privilege"? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Users should only have the minimum permissions necessary to do their job', True),
            ('Administrators should have standard user rights for daily tasks and only use admin accounts when needed', True),
            ('All users should have equal access to all systems for fairness', False),
            ('Least privilege only applies to network access not file permissions', False),
        ]
    },
    {
        'text': 'What is the purpose of "log retention policies"?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Automatically deleting all logs after 24 hours to save storage', False),
            ('Defining how long different types of logs must be kept to meet legal compliance and forensic investigation requirements', True),
            ('Retaining only error logs and deleting informational logs', False),
            ('A policy for retaining only the logs of administrator actions', False),
        ]
    },
    {
        'text': 'What is "shadow IT"?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('IT systems used only at night to avoid peak hours', False),
            ('Technology systems applications or services used within an organization without explicit IT department approval or knowledge', True),
            ('A backup IT system that operates in parallel with the primary system', False),
            ('Outsourced IT services managed by a third party', False),
        ]
    },
    {
        'text': 'What does "due care" mean in IT security and operations?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Caring about the due date for security audits', False),
            ('Taking reasonable steps to implement and maintain security controls — showing that an organization actively works to protect its systems and data', True),
            ('Caring for physical IT equipment to prevent damage', False),
            ('The care taken when writing IT documentation', False),
        ]
    },
    {
        'text': 'What is a "tabletop exercise" used for in disaster recovery planning?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Testing physical server hardware on a table in the lab', False),
            ('A discussion-based exercise where key personnel walk through a simulated disaster scenario to test and improve the disaster recovery plan without actually executing it', True),
            ('A meeting to discuss the layout of server room tables and racks', False),
            ('A hands-on technical exercise for junior IT staff', False),
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