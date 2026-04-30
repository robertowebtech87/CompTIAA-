import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app import app, db
from models import Question, Choice

questions_data = [

    # ── SOFTWARE TROUBLESHOOTING ──────────────────────────────────────────────

    {
        'text': 'A user reports that Windows boots to a black screen with a cursor but no desktop. What should the technician try first?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('Reinstall Windows immediately', False),
            ('Press Ctrl+Alt+Del, open Task Manager, and run explorer.exe as a new task', True),
            ('Replace the hard drive', False),
            ('Run MemTest86', False),
        ]
    },
    {
        'text': 'A user receives a "Windows cannot find the Microsoft .NET Framework" error when launching an application. What should be done?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('Reinstall Windows', False),
            ('Download and install the required version of the .NET Framework from Microsoft', True),
            ('Replace the RAM', False),
            ('Run chkdsk on the drive', False),
        ]
    },
    {
        'text': 'A technician needs to find which process is using a specific port on a Windows computer. What command should be used?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('ipconfig /all', False),
            ('netstat -ano', True),
            ('ping localhost', False),
            ('tasklist', False),
        ]
    },
    {
        'text': 'A user reports that their computer is slow. Task Manager shows 95% disk usage constantly. What is the most likely cause?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('The monitor needs replacing', False),
            ('Windows Search or Windows Update is indexing or updating in the background, or the drive is failing', True),
            ('Too many monitors are connected', False),
            ('The GPU needs a driver update', False),
        ]
    },
    {
        'text': 'A user installs a program and immediately gets a BSOD. What should the technician do?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('Replace the hard drive', False),
            ('Uninstall the program, check the BSOD stop code in Event Viewer, and look for a driver conflict or incompatible software', True),
            ('Reinstall Windows', False),
            ('Upgrade the RAM', False),
        ]
    },
    {
        'text': 'What does the Windows error "NTLDR is missing" or "Bootmgr is missing" indicate?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('The network adapter driver is missing', False),
            ('The boot manager file is corrupted or missing, or the system is trying to boot from the wrong device', True),
            ('The user profile is corrupted', False),
            ('The RAM has failed', False),
        ]
        },
    {
        'text': 'A user reports that their default browser keeps changing back to Internet Explorer after every restart. What is likely happening?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('Windows Update is resetting the browser', False),
            ('A program or malware is changing the default browser setting — scan for malware and check startup programs', True),
            ('The user does not have permission to change defaults', False),
            ('Internet Explorer cannot be uninstalled', False),
        ]
    },
    {
        'text': 'An application works on Windows 10 but fails to run on Windows 11. What should the technician try first?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('Downgrade to Windows 10', False),
            ('Right-click the application, go to Properties, Compatibility tab, and enable compatibility mode for Windows 10', True),
            ('Reinstall the application', False),
            ('Update the GPU driver', False),
        ]
    },
    {
        'text': 'What is the Windows command to end a running process from the command prompt?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('kill processname', False),
            ('taskkill /IM processname.exe /F', True),
            ('stop processname', False),
            ('end /process processname', False),
        ]
    },
    {
        'text': 'A user reports that after a Windows Update their second monitor stopped working. What should be tried first?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('Replace the monitor', False),
            ('Roll back the display driver in Device Manager to the version before the update', True),
            ('Reinstall Windows', False),
            ('Replace the GPU', False),
        ]
    },
    {
        'text': 'A user reports that their printer prints a test page fine but jobs from specific applications fail. What is the most likely cause?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('The printer is broken', False),
            ('The application has incorrect printer settings or needs to be repaired or reinstalled', True),
            ('The printer driver needs replacing', False),
            ('The toner is low', False),
        ]
    },
    {
        'text': 'What does it mean when Windows shows a "low virtual memory" warning?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('The hard drive is almost full', False),
            ('The system is running low on both physical RAM and pagefile space — close applications or increase pagefile size', True),
            ('The GPU has insufficient memory', False),
            ('The network bandwidth is low', False),
        ]
    },
    {
        'text': 'A technician suspects a startup program is causing Windows to crash. What is the safest way to test this?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('Reinstall Windows clean', False),
            ('Use msconfig to perform a selective startup disabling startup programs one at a time to identify the culprit', True),
            ('Delete the startup folder entirely', False),
            ('Disable all services using services.msc', False),
        ]
    },
    {
        'text': 'What is the Windows Reliability Monitor and how is it useful for troubleshooting?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('A real-time performance monitor for CPU and RAM', False),
            ('A timeline showing application crashes, hardware failures, and system changes helping identify what changed before problems started', True),
            ('A tool that automatically fixes stability issues', False),
            ('A log of all user login and logout times', False),
        ]
    },
    {
        'text': 'A user\'s Outlook keeps crashing on startup. What should the technician try first?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('Reinstall Windows', False),
            ('Start Outlook in safe mode using outlook /safe to rule out add-in conflicts', True),
            ('Replace the hard drive', False),
            ('Upgrade the RAM', False),
        ]
    },
    {
        'text': 'What does the error "side-by-side configuration is incorrect" typically mean in Windows?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('Two monitors are configured incorrectly', False),
            ('A required runtime library (Visual C++ redistributable) is missing or corrupted — reinstalling it usually fixes the error', True),
            ('The RAM modules are in the wrong slots', False),
            ('The application was installed on the wrong drive', False),
        ]
    },
    {
        'text': 'A user reports that file associations are broken — double-clicking a PDF opens Notepad instead of a PDF reader. How is this fixed?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('Reinstall Windows', False),
            ('Go to Settings → Apps → Default Apps and set the correct application for PDF files', True),
            ('Delete and reinstall Notepad', False),
            ('Run sfc /scannow', False),
        ]
    },
    {
        'text': 'What is the first step when troubleshooting any software issue according to the CompTIA troubleshooting methodology?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('Apply a solution immediately', False),
            ('Identify the problem — gather information, ask the user what changed, and reproduce the issue if possible', True),
            ('Reinstall the operating system', False),
            ('Back up the data first', False),
        ]
    },
    {
        'text': 'A Windows application stops responding every time a specific file is opened. What does this suggest?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('The hard drive is failing', False),
            ('The specific file is corrupted or contains content the application cannot handle — try opening a different file to confirm', True),
            ('The application needs to be updated', False),
            ('The RAM is insufficient', False),
        ]
    },
    {
        'text': 'After removing malware a user\'s browser still redirects to unwanted websites. What should the technician check?',
        'domain': 'Software Troubleshooting',
        'exam': 'core2',
        'choices': [
            ('Reinstall Windows', False),
            ('Check browser extensions, homepage settings, DNS settings, and the hosts file as the malware may have modified these', True),
            ('Replace the network adapter', False),
            ('Run chkdsk on the drive', False),
        ]
    },

    # ── OPERATIONAL PROCEDURES ────────────────────────────────────────────────

    {
        'text': 'What is the correct order of the CompTIA troubleshooting methodology?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('Fix it, document it, test it, identify it', False),
            ('Identify, establish theory, test theory, establish plan, implement solution, verify, document', True),
            ('Identify, fix immediately, document afterward', False),
            ('Test all solutions simultaneously then document the one that worked', False),
        ]
    },
    {
        'text': 'What does "establishing a theory of probable cause" mean in IT troubleshooting?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('Guessing the most expensive fix and trying it first', False),
            ('Forming a logical hypothesis about what is causing the problem based on the symptoms and information gathered', True),
            ('Documenting the problem for later review', False),
            ('Escalating to a senior technician', False),
        ]
    },
    {
        'text': 'Why is documentation important after resolving an IT issue?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('It is only required for billing purposes', False),
            ('It creates a knowledge base that helps resolve similar issues faster in the future and provides accountability', True),
            ('Documentation is only needed for major outages', False),
            ('It is only required by law for medical organizations', False),
        ]
    },
    {
        'text': 'What is a knowledge base in IT support?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('A database of employee contact information', False),
            ('A searchable repository of documented solutions, procedures, and known issues that technicians can reference to resolve problems quickly', True),
            ('A list of all software licenses owned by the company', False),
            ('A record of all hardware assets in the organization', False),
        ]
    },
    {
        'text': 'What is the purpose of an asset inventory or asset management system?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('Tracking employee attendance', False),
            ('Maintaining a record of all hardware and software assets including location, specifications, owner, and warranty status', True),
            ('Managing the IT budget', False),
            ('Monitoring network bandwidth usage', False),
        ]
    },
    {
        'text': 'What is a regulated data type that requires special handling and compliance?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('General business emails and memos', False),
            ('PII (Personally Identifiable Information), PHI (Protected Health Information), and PCI data (credit card data)', True),
            ('Public marketing materials', False),
            ('Open source software documentation', False),
        ]
    },
    {
        'text': 'What is the proper way to handle a data breach according to incident response procedures?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('Fix the breach quietly without reporting it', False),
            ('Contain the breach, assess the damage, notify affected parties and authorities as required, document everything, and implement measures to prevent recurrence', True),
            ('Simply change all passwords and consider it resolved', False),
            ('Blame the affected user and close the ticket', False),
        ]
    },
    {
        'text': 'What is an RTO (Recovery Time Objective)?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('The maximum age of restored data that is acceptable', False),
            ('The maximum acceptable length of time that a system can be offline after a failure before it must be restored', True),
            ('The time it takes to run a full backup', False),
            ('The required response time for support tickets', False),
        ]
    },
    {
        'text': 'What is the purpose of a disaster recovery plan?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('A plan for handling difficult customers', False),
            ('A documented strategy for restoring IT systems and data after a major disaster such as a fire, flood, or cyberattack', True),
            ('A plan for replacing broken hardware', False),
            ('Insurance documentation for equipment', False),
        ]
    },
    {
        'text': 'What should a technician do if they are unable to resolve an issue within their skill level?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('Keep trying indefinitely without telling anyone', False),
            ('Escalate the ticket to a more experienced technician or specialist and document what has already been tried', True),
            ('Close the ticket and hope the problem resolves itself', False),
            ('Ask the user to fix it themselves', False),
        ]
    },
    {
        'text': 'What is the correct environmental disposal method for old CRT monitors and batteries?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('Throw them in the regular trash', False),
            ('Take them to a certified e-waste recycling facility as they contain hazardous materials like lead and mercury', True),
            ('Bury them as they decompose naturally', False),
            ('Donate them to a landfill site', False),
        ]
    },
    {
        'text': 'What is the purpose of licensing compliance in an organization?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('To get discounts on software purchases', False),
            ('To ensure the organization is legally authorized to use the software it has installed avoiding fines and legal action', True),
            ('To prevent employees from installing personal software', False),
            ('To track which employees use each application', False),
        ]
    },
    {
        'text': 'What is a standard operating procedure (SOP)?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('The minimum required qualifications for an IT job', False),
            ('A documented set of step-by-step instructions for performing routine tasks consistently and correctly', True),
            ('A list of approved vendors for purchasing equipment', False),
            ('The standard working hours for IT staff', False),
        ]
    },
    {
        'text': 'A technician is about to perform maintenance on a server during business hours. What must be done first?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('Begin work immediately to minimize downtime', False),
            ('Submit and get approval for a change request, notify affected users, schedule a maintenance window, and prepare a rollback plan', True),
            ('Back up the server and start immediately', False),
            ('Call the server manufacturer for guidance', False),
        ]
    },
    {
        'text': 'What is the purpose of multifactor authentication from an operational standpoint?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('To make login more complicated for users', False),
            ('To significantly reduce the risk of unauthorized access even if a password is compromised by requiring a second form of verification', True),
            ('To replace passwords entirely', False),
            ('To allow multiple users to share one account securely', False),
        ]
    },
    {
        'text': 'What does it mean to "harden" a system?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('Upgrading to faster hardware components', False),
            ('Reducing the attack surface by disabling unnecessary services, applying updates, enforcing strong passwords, and configuring security settings', True),
            ('Installing a physical case to protect from drops', False),
            ('Increasing RAM for better performance', False),
        ]
    },
    {
        'text': 'What is the correct professional response when a user asks a technician to bypass a company security policy?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('Do it if the user is a senior manager', False),
            ('Politely decline, explain the reason for the policy, and escalate if the user insists', True),
            ('Agree and do it quietly without documenting', False),
            ('Immediately report the user to HR without explanation', False),
        ]
    },
    {
        'text': 'What is the purpose of a network baseline?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('The minimum network speed required for video conferencing', False),
            ('A recorded snapshot of normal network performance metrics used to identify anomalies and troubleshoot performance issues', True),
            ('The base level of network security required by law', False),
            ('The default router configuration settings', False),
        ]
    },
    {
        'text': 'A technician finishes a repair and the user is happy. What is the last step before fully closing the ticket?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('Leave immediately to the next job', False),
            ('Verify full functionality with the user, document the solution, and ensure the user understands what was done', True),
            ('Send an invoice', False),
            ('Remove all tools and leave without saying anything', False),
        ]
    },
    {
        'text': 'What is the purpose of screensavers and automatic screen lock policies in a workplace?',
        'domain': 'Operational Procedures',
        'exam': 'core2',
        'choices': [
            ('To extend monitor life by reducing static images', False),
            ('To automatically lock unattended computers preventing unauthorized access to sensitive information', True),
            ('To display company branding and marketing materials', False),
            ('To save power when computers are not in use', False),
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