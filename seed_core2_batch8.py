from app import app, db
from models import Question, Choice

questions_data = [

    # ── OPERATING SYSTEMS ─────────────────────────────────────────────────────

    {
        'text': 'What is the purpose of the Windows "Disk Cleanup" tool?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Physically cleans dust from the hard drive', False),
            ('Removes unnecessary files such as temporary files recycle bin contents and Windows Update cache to free up disk space', True),
            ('Defragments the hard drive to improve performance', False),
            ('Checks the hard drive for errors and bad sectors', False),
        ]
    },
    {
        'text': 'What is the Windows "Libraries" feature?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A collection of installed applications', False),
            ('Virtual folders that aggregate content from multiple locations on the computer making it easier to access related files regardless of where they are stored', True),
            ('A built-in book reading application', False),
            ('A feature for organizing installed fonts', False),
        ]
    },
    {
        'text': 'What does the Windows command "assoc" do?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Associates a user account with a computer on the domain', False),
            ('Displays or modifies file extension associations showing which program opens each file type', True),
            ('Lists all associated network drives', False),
            ('Shows associated hardware devices for each driver', False),
        ]
    },
    {
        'text': 'What is the purpose of the Windows "Indexing Service"?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Creates an index of all installed software for faster installation', False),
            ('Builds and maintains an index of files and their contents enabling fast Windows Search results', True),
            ('Tracks which files have been accessed and by whom', False),
            ('Creates backup copies of recently modified files', False),
        ]
    },
    {
        'text': 'What is "Windows Hello" and what authentication methods does it support?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A greeting application that launches at Windows startup', False),
            ('A biometric authentication system that supports facial recognition fingerprint and PIN as alternatives to passwords', True),
            ('A welcome screen customization tool', False),
            ('A voice assistant built into Windows', False),
        ]
    },
    {
        'text': 'What is the Windows "Snipping Tool" used for?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Removing unwanted files from the system', False),
            ('Capturing screenshots of the entire screen a specific window or a custom area', True),
            ('Cutting and trimming video files', False),
            ('Removing background processes from memory', False),
        ]
    },
    {
        'text': 'What is the difference between "sleep" and "hibernate" and "hybrid sleep"?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('They all do the same thing with different names', False),
            ('Sleep keeps data in RAM using power — Hibernate saves to disk using no power — Hybrid Sleep saves to disk AND keeps RAM powered for fastest resume', True),
            ('Sleep saves to disk — Hibernate keeps in RAM — Hybrid does neither', False),
            ('Hibernate is faster than sleep to resume', False),
        ]
    },
    {
        'text': 'What is the purpose of "Windows Subsystem for Android" (WSA)?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A tool for developing Android applications on Windows', False),
            ('Allows running Android applications natively on Windows 11 without a separate emulator', True),
            ('A synchronization tool between Android phones and Windows', False),
            ('A backup solution for Android device content', False),
        ]
    },
    {
        'text': 'What does "RunAs" allow in Windows?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Runs applications as fast as possible using maximum CPU', False),
            ('Allows running an application under a different user account without logging out — useful for running admin tools as a standard user', True),
            ('Runs multiple instances of the same application', False),
            ('Automatically runs applications at startup', False),
        ]
    },
    {
        'text': 'What is "Windows Presentation Foundation" (WPF)?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A tool for creating PowerPoint presentations in Windows', False),
            ('A UI framework for building Windows desktop applications with rich graphical interfaces', True),
            ('A built-in presentation mode that disables notifications', False),
            ('A display calibration tool for Windows monitors', False),
        ]
    },

    # ── OPERATING SYSTEMS — Multi Select ──────────────────────────────────────

    {
        'text': 'Which TWO of the following are true about Windows Defender? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Windows Defender provides real-time protection against malware', True),
            ('Windows Defender automatically disables when third-party antivirus is installed', True),
            ('Windows Defender requires a separate paid subscription', False),
            ('Windows Defender cannot detect ransomware', False),
        ]
    },
    {
        'text': 'Which TWO of the following are methods to access the Windows Advanced Startup Options? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Hold Shift while clicking Restart in the Start menu', True),
            ('Press F8 repeatedly during boot on modern Windows systems', False),
            ('Boot from Windows installation media and select Repair your computer', True),
            ('Type advanced in the Windows search bar', False),
        ]
    },
    {
        'text': 'Which TWO are correct statements about Windows file permissions inheritance? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Files and subfolders inherit permissions from their parent folder by default', True),
            ('Inherited permissions cannot be overridden on individual files', False),
            ('Explicitly set permissions on a file override inherited permissions', True),
            ('Permissions are always inherited from the drive root only', False),
        ]
    },
    {
        'text': 'Which TWO of the following describe the Windows pagefile? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('The pagefile extends available memory by using hard drive space as virtual RAM', True),
            ('The pagefile is stored in RAM for fastest access', False),
            ('Accessing the pagefile is slower than accessing physical RAM', True),
            ('The pagefile replaces the need for physical RAM', False),
        ]
    },

    # ── SECURITY ──────────────────────────────────────────────────────────────

    {
        'text': 'What is "vishing" and how does it differ from regular phishing?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Vishing uses video calls while phishing uses email — they are otherwise identical', False),
            ('Vishing is voice-based phishing conducted over phone calls — attackers impersonate banks IT support or government agencies to extract information', True),
            ('Vishing targets executives while phishing targets regular employees', False),
            ('Vishing uses text messages while phishing uses emails', False),
        ]
    },
    {
        'text': 'What is an "Advanced Persistent Threat" (APT)?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A type of antivirus software that provides advanced persistent protection', False),
            ('A sophisticated long-term cyberattack where an attacker gains unauthorized access and remains undetected for an extended period to steal data or monitor activity', True),
            ('A severe vulnerability that has no available patch', False),
            ('A type of malware that permanently damages hardware', False),
        ]
    },
    {
        'text': 'What is "security awareness training" and why is it important?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Technical training for IT security staff only', False),
            ('Training all employees to recognize and respond to security threats because humans are often the weakest link in security — most breaches involve human error', True),
            ('Training employees to use security software', False),
            ('Annual compliance training required by law only', False),
        ]
    },
    {
        'text': 'What is "whaling" in cybersecurity?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A large-scale phishing attack targeting thousands of users', False),
            ('A targeted spear phishing attack specifically aimed at senior executives or high-value individuals within an organization', True),
            ('An attack that uses very large malicious files to overwhelm systems', False),
            ('A social engineering technique involving physical mail', False),
        ]
    },
    {
        'text': 'What is "DNS poisoning" (DNS cache poisoning)?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Overloading a DNS server with too many requests', False),
            ('Corrupting a DNS resolver\'s cache with false records to redirect users to malicious websites without their knowledge', True),
            ('Blocking DNS queries to prevent internet access', False),
            ('Stealing DNS server credentials to take control', False),
        ]
    },
    {
        'text': 'What is "MAC address spoofing" and why would an attacker use it?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Physically replacing the MAC address chip on a network card', False),
            ('Changing a device\'s MAC address in software to impersonate another device bypass MAC filtering or hide network activity', True),
            ('Stealing another device\'s MAC address permanently', False),
            ('A technique for improving network performance by optimizing MAC addresses', False),
        ]
    },
    {
        'text': 'What is the purpose of "email authentication protocols" like SPF DKIM and DMARC?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('To encrypt email content so only the recipient can read it', False),
            ('To verify that emails are sent from legitimate servers and have not been tampered with helping prevent email spoofing and phishing', True),
            ('To compress email attachments for faster delivery', False),
            ('To authenticate users before they can send emails', False),
        ]
    },
    {
        'text': 'What is "insider threat" in cybersecurity?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('An attack that originates from inside a firewall', False),
            ('A security threat that comes from people within the organization such as employees contractors or business partners who misuse their authorized access', True),
            ('A threat that bypasses perimeter security from within the network', False),
            ('Malware that hides inside legitimate software', False),
        ]
    },
    {
        'text': 'What is "security through obscurity" and why is it insufficient alone?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Using dark colors in security interfaces to make them hard to read', False),
            ('Hiding security details hoping attackers won\'t find them — insufficient because determined attackers will eventually discover the hidden information and there is no real security control in place', True),
            ('Encrypting security logs so only administrators can read them', False),
            ('Using obscure file names to hide sensitive data', False),
        ]
    },
    {
        'text': 'What is the purpose of "vulnerability scanning"?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Scanning employees for security policy violations', False),
            ('Automatically identifying known security weaknesses misconfigurations and missing patches in systems and applications', True),
            ('Testing whether users will fall for phishing emails', False),
            ('Scanning network traffic for malware signatures', False),
        ]
    },

    # ── SECURITY — Multi Select ────────────────────────────────────────────────

    {
        'text': 'Which TWO of the following are true about encryption keys? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Longer encryption keys generally provide stronger security', True),
            ('Losing an encryption key means encrypted data may be permanently inaccessible', True),
            ('Encryption keys can be recovered by the hardware manufacturer', False),
            ('All encryption algorithms use the same key length', False),
        ]
    },
    {
        'text': 'Which TWO of the following are true about phishing attacks? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Phishing emails often create urgency to pressure victims into acting quickly', True),
            ('Phishing attacks can only be delivered via email', False),
            ('Hovering over links before clicking can reveal suspicious URLs', True),
            ('Antivirus software provides complete protection against all phishing attacks', False),
        ]
    },
    {
        'text': 'Which TWO are effective countermeasures against social engineering attacks? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Regular security awareness training for all staff', True),
            ('Installing faster network switches', False),
            ('Implementing verification procedures before sharing sensitive information', True),
            ('Using a more complex file naming convention', False),
        ]
    },
    {
        'text': 'Which TWO of the following are true about physical security? (Select TWO)',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Physical security is the first line of defense — if an attacker has physical access they can bypass most digital controls', True),
            ('Physical security only applies to server rooms not regular offices', False),
            ('Visitor logs and escorted access help prevent unauthorized physical access', True),
            ('Physical security is less important than network security', False),
        ]
    },

    # ── SOFTWARE TROUBLESHOOTING ───────────────────────────────────────────────

    {
        'text': 'A user reports Windows keeps asking them to activate even though they already activated. What could cause this?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Windows activation expires every 30 days', False),
            ('Significant hardware changes especially motherboard replacement can trigger reactivation because the license is tied to hardware fingerprint', True),
            ('Windows Update reset the activation', False),
            ('The user needs to purchase a new license annually', False),
        ]
    },
    {
        'text': 'A user cannot connect to a specific website but all other websites work fine. What should be checked?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Reinstall the browser', False),
            ('Check the hosts file for a manual override flush DNS cache and check if the site is blocked by firewall or parental controls', True),
            ('Replace the network adapter', False),
            ('The website is permanently down', False),
        ]
    },
    {
        'text': 'A Windows computer shows "No boot device found" after moving it to a new location. What should be checked first?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The operating system needs reinstalling', False),
            ('The hard drive cable may have become loose during transport — check SATA and power connections', True),
            ('The motherboard has failed', False),
            ('The monitor cable is disconnected', False),
        ]
    },
    {
        'text': 'A user reports that ctrl+alt+del no longer opens the security screen on their domain computer. What might have changed?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The keyboard has failed', False),
            ('A Group Policy may have been applied that disables or redirects this shortcut or a remote access tool is intercepting it', True),
            ('Windows needs to be reinstalled', False),
            ('The Ctrl key driver is corrupted', False),
        ]
    },
    {
        'text': 'A user\'s application displays garbled text with strange characters instead of normal text. What is the likely cause?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The monitor is failing', False),
            ('A font or character encoding issue — the required font may be missing or the wrong language/locale is set', True),
            ('The RAM has failed', False),
            ('The hard drive has bad sectors affecting the application', False),
        ]
    },
    {
        'text': 'A technician finds that Windows Defender is disabled and cannot be re-enabled. What is the most likely cause?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Windows Defender requires a subscription to remain active', False),
            ('Malware has disabled Windows Defender to avoid detection — this is a common malware behavior requiring a full malware removal procedure', True),
            ('Windows Defender was removed by Windows Update', False),
            ('The user accidentally uninstalled Windows Defender', False),
        ]
    },
    {
        'text': 'A user reports their laptop overheats and shuts down only when running on battery. On AC power it works fine. What could cause this?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The battery is causing physical heat', False),
            ('The power plan may switch to a higher performance mode on battery causing more heat or the battery is failing and generating excess heat under load', True),
            ('The cooling fan only works when plugged in', False),
            ('The thermal paste only works with AC power', False),
        ]
    },
    {
        'text': 'After enabling BitLocker a computer no longer boots and asks for a recovery key. What happened?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('BitLocker corrupted the hard drive', False),
            ('A hardware change or BIOS update changed the TPM measurement causing BitLocker to require the recovery key as a security measure', True),
            ('The BitLocker license has expired', False),
            ('Windows Update disabled BitLocker', False),
        ]
    },
    {
        'text': 'A user reports that their Outlook calendar is not syncing with their phone. What should be investigated?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Replace the phone immediately', False),
            ('Check account sync settings on both devices verify the account is correctly configured and check if airplane mode or battery saver is blocking sync', True),
            ('Reinstall Windows', False),
            ('The email server is offline', False),
        ]
    },
    {
        'text': 'A user cannot print to a shared printer on another computer. The printer works locally on the host computer. What should be checked?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Replace the printer', False),
            ('Verify file and printer sharing is enabled on the host check firewall rules allow printer sharing and ensure the user has permission to use the shared printer', True),
            ('Reinstall Windows on both computers', False),
            ('The network cable on the printer needs replacing', False),
        ]
    },

    # ── SOFTWARE TROUBLESHOOTING — Multi Select ───────────────────────────────

    {
        'text': 'Which TWO are valid steps when Windows will not start and shows a black screen? (Select TWO)',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Boot into Windows Recovery Environment and attempt Startup Repair', True),
            ('Immediately format the drive and reinstall Windows', False),
            ('Try booting into Safe Mode to determine if a driver is causing the issue', True),
            ('Replace the RAM before any other troubleshooting', False),
        ]
    },
    {
        'text': 'Which TWO should be checked when a user cannot log into their domain account? (Select TWO)',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Verify the computer can reach the domain controller over the network', True),
            ('Replace the keyboard immediately', False),
            ('Check if the account is locked out or expired in Active Directory', True),
            ('Reinstall Windows on the domain computer', False),
        ]
    },
    {
        'text': 'Which TWO are common symptoms of a failing Windows user profile? (Select TWO)',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('User logs in to a temporary profile with a warning message', True),
            ('The computer fails to POST', False),
            ('Desktop settings applications and documents are missing or reset after login', True),
            ('The network adapter stops working', False),
        ]
    },

    # ── OPERATIONAL PROCEDURES ────────────────────────────────────────────────

    {
        'text': 'What is a "maintenance window" in IT operations?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A physical window in the server room for ventilation', False),
            ('A scheduled period of time designated for performing system maintenance updates and changes with minimal impact on users', True),
            ('The time period during which IT support is available', False),
            ('A window opened in the management console for monitoring', False),
        ]
    },
    {
        'text': 'What is the purpose of "configuration baselines" in IT management?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A minimum hardware specification for company computers', False),
            ('Documented standard configurations for systems that serve as a reference point for detecting unauthorized changes and ensuring compliance', True),
            ('The baseline performance metrics of a new system', False),
            ('Default settings applied when a system is reset to factory', False),
        ]
    },
    {
        'text': 'What does "root cause analysis" mean in IT incident management?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Analyzing the root directory of a server for malware', False),
            ('Investigating an incident to identify the underlying cause rather than just fixing the immediate symptom so the problem does not recur', True),
            ('Finding which administrator caused a system failure', False),
            ('Analyzing the root access logs after a security breach', False),
        ]
    },
    {
        'text': 'What is an "escalation path" in IT support?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The career progression path for IT technicians', False),
            ('A predefined process for routing unresolved issues to higher levels of expertise or management when they cannot be resolved at the current level', True),
            ('A physical path for routing network cables through a building', False),
            ('The process for escalating costs on large IT projects', False),
        ]
    },
    {
        'text': 'What is "ITAM" (IT Asset Management)?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A programming framework for IT applications', False),
            ('The process of tracking and managing all IT hardware and software assets throughout their lifecycle from procurement to disposal', True),
            ('An automatic threat assessment module for security', False),
            ('An integrated tool for application monitoring', False),
        ]
    },
    {
        'text': 'What is the purpose of "patch testing" before deployment?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Patches should always be deployed immediately without testing', False),
            ('Testing patches in a non-production environment first to verify they do not break existing systems or applications before rolling out organization-wide', True),
            ('Testing whether the patch has been correctly downloaded', False),
            ('Checking that the patch matches its documented file size', False),
        ]
    },
    {
        'text': 'What is "environmental monitoring" in a data center context?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Monitoring employee environmental awareness', False),
            ('Continuously monitoring physical conditions such as temperature humidity power and water detection to prevent environmental damage to equipment', True),
            ('Monitoring the environmental impact of IT operations', False),
            ('Checking air quality for employee comfort', False),
        ]
    },
    {
        'text': 'What is "knowledge transfer" in IT operations?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Transferring files between computers on the network', False),
            ('The process of sharing expertise documentation and institutional knowledge between team members to ensure continuity when staff changes occur', True),
            ('Uploading company data to a cloud knowledge base', False),
            ('Training users on new software applications', False),
        ]
    },
    {
        'text': 'What is the purpose of an "audit trail" in IT systems?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A trail of breadcrumbs left by IT auditors during inspections', False),
            ('A chronological record of system activities and user actions that provides evidence for security investigations compliance verification and troubleshooting', True),
            ('A financial audit of IT expenditures', False),
            ('A record of software audit licenses', False),
        ]
    },
    {
        'text': 'What is "right to erasure" (right to be forgotten) in data privacy?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('The right of IT staff to erase data from failed drives', False),
            ('A legal right under privacy regulations like GDPR allowing individuals to request that their personal data be deleted from an organization\'s systems', True),
            ('The right to erase backup data after a set period', False),
            ('An employee\'s right to delete their own work files', False),
        ]
    },

    # ── OPERATIONAL PROCEDURES — Multi Select ─────────────────────────────────

    {
        'text': 'Which TWO are true about disaster recovery testing? (Select TWO)',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('A disaster recovery plan that has never been tested cannot be relied upon during an actual disaster', True),
            ('Testing disaster recovery always requires a full system outage', False),
            ('Tabletop exercises are a low-risk way to test disaster recovery procedures', True),
            ('Disaster recovery only needs to be tested once after creation', False),
        ]
    },
    {
        'text': 'Which TWO are examples of preventative maintenance tasks in IT? (Select TWO)',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Regularly applying security patches before vulnerabilities are exploited', True),
            ('Replacing hardware only after it fails completely', False),
            ('Cleaning dust from servers and workstations to prevent overheating', True),
            ('Waiting for users to report problems before investigating', False),
        ]
    },
    {
        'text': 'Which TWO of the following are correct regarding software licensing? (Select TWO)',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Volume licensing allows organizations to purchase multiple licenses at a reduced cost', True),
            ('Open source software can always be used commercially without any restrictions', False),
            ('Subscription-based licenses require ongoing payment and expire if not renewed', True),
            ('Freeware and free software mean the same thing legally', False),
        ]
    },
    {
        'text': 'Which TWO are responsibilities of an IT technician regarding user privacy? (Select TWO)',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('Only access user data that is necessary to complete the support task', True),
            ('Read user emails to check for security threats without permission', False),
            ('Maintain confidentiality about information observed during support work', True),
            ('Share interesting findings from user computers with colleagues', False),
        ]
    },

    # ── ADDITIONAL MIXED ──────────────────────────────────────────────────────

    {
        'text': 'What is "application compatibility shim" in Windows?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A physical adapter for connecting older application hardware', False),
            ('A compatibility layer that intercepts API calls from older applications and translates them to work with newer versions of Windows', True),
            ('A tool for removing incompatible applications from Windows', False),
            ('A security feature that prevents old applications from running', False),
        ]
    },
    {
        'text': 'What is "network bonding" or "NIC teaming"?',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Physically bonding network cables together with cable ties', False),
            ('Combining multiple network adapters into a single logical interface for increased bandwidth or redundancy', True),
            ('Bonding a computer permanently to a specific network', False),
            ('A security technique that bonds MAC addresses to IP addresses', False),
        ]
    },
    {
        'text': 'What is "multi-factor authentication fatigue attack"?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('When MFA causes users to become tired and disable it', False),
            ('Repeatedly sending MFA push notifications to a target hoping they will eventually approve one out of frustration or confusion', True),
            ('A brute force attack against MFA codes', False),
            ('When MFA systems become overloaded and fail', False),
        ]
    },
    {
        'text': 'What is "air gap" security and what is its main limitation?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A gap in firewall rules that allows authorized traffic — limitation is it can be accidentally widened', False),
            ('Physical isolation of a computer from all networks — the main limitation is that it requires physical access for all data transfers which can introduce risk through USB drives or other physical media', True),
            ('A cooling gap between servers — limitation is increased heat', False),
            ('An empty security policy with no rules — limitation is it allows all traffic', False),
        ]
    },
    {
        'text': 'What is "living off the land" (LotL) in cybersecurity attacks?',
        'domain': 'Security',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('A physical security attack conducted outdoors to avoid detection', False),
            ('Using legitimate built-in system tools like PowerShell WMI or certutil to conduct attacks making them harder to detect since no malware is installed', True),
            ('Attackers who work from rural areas to avoid jurisdiction', False),
            ('Using open source tools for penetration testing', False),
        ]
    },
    {
        'text': 'What is the purpose of "WHOIS" lookup?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'multi_select': False,
        'choices': [
            ('Identifies who is currently logged into a system', False),
            ('Queries a database to find registration information about a domain name including the owner registrar and registration dates', True),
            ('Checks who has accessed a specific file', False),
            ('Identifies which user last modified a registry key', False),
        ]
    },
    {
        'text': 'Which TWO of the following are true about Windows System Restore? (Select TWO)',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('System Restore does not affect personal files like documents and photos', True),
            ('System Restore can undo driver and application installations', True),
            ('System Restore requires a complete Windows reinstallation to use', False),
            ('System Restore backs up all user data automatically', False),
        ]
    },
    {
        'text': 'Which TWO are correct regarding Windows Event Log types? (Select TWO)',
        'domain': 'Operating Systems',
        'exam': 'core2',
        'multi_select': True,
        'choices': [
            ('The Security log records successful and failed login attempts', True),
            ('The Application log records hardware failure events', False),
            ('The System log records events from Windows system components and drivers', True),
            ('The Setup log records daily user activity', False),
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