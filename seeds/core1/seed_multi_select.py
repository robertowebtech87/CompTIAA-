import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app import app, db
from models import Question, Choice

questions_data = [

    # ── HARDWARE - Select TWO ─────────────────────────────────────────────────

    {
        'text': 'Which TWO of the following are advantages of an SSD over an HDD? (Select TWO)',
        'domain': 'Hardware',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'SSDs have no moving parts making them more durable and faster than HDDs. They also use less power.',
        'choices': [
            ('Faster data access speeds', True),
            ('Higher storage capacity per dollar', False),
            ('No moving parts making it more durable', True),
            ('Cheaper cost per gigabyte', False),
        ]
    },
    {
        'text': 'Which TWO form factors are commonly used for SSDs? (Select TWO)',
        'domain': 'Hardware',
        'exam': 'core1',
        'multi_select': True,
        'explanation': '2.5-inch SATA and M.2 are the two most common SSD form factors. M.2 can use either SATA or NVMe interface.',
        'choices': [
            ('2.5-inch SATA', True),
            ('3.5-inch SATA', False),
            ('M.2', True),
            ('5.25-inch bay', False),
        ]
    },
    {
        'text': 'A technician needs to install additional RAM in a desktop. Which TWO things must be verified before purchasing? (Select TWO)',
        'domain': 'Hardware',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'You must check the RAM type (DDR4, DDR5 etc.) that the motherboard supports and the maximum RAM the motherboard can handle.',
        'choices': [
            ('The RAM type and speed supported by the motherboard', True),
            ('The brand of the existing RAM modules', False),
            ('The maximum RAM capacity the motherboard supports', True),
            ('The color of the RAM heatspreader', False),
        ]
    },
    {
        'text': 'Which TWO of the following components are found on a motherboard? (Select TWO)',
        'domain': 'Hardware',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'The CPU socket and PCIe slots are both found directly on the motherboard.',
        'choices': [
            ('CPU socket', True),
            ('Power supply unit', False),
            ('PCIe expansion slots', True),
            ('Hard drive platters', False),
        ]
    },
    {
        'text': 'Which TWO statements about NVMe SSDs are correct? (Select TWO)',
        'domain': 'Hardware',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'NVMe SSDs use the PCIe interface for much faster speeds than SATA and physically plug directly into the M.2 slot on the motherboard.',
        'choices': [
            ('They use the PCIe interface for much faster speeds than SATA', True),
            ('They connect using the same SATA cable as HDDs', False),
            ('They plug directly into an M.2 slot on the motherboard with no cables', True),
            ('They require an external power connector from the PSU', False),
        ]
    },
    {
        'text': 'Which TWO of the following are input devices? (Select TWO)',
        'domain': 'Hardware',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Keyboards and barcode scanners are input devices — they send data into the computer. Monitors and speakers are output devices.',
        'choices': [
            ('Monitor', False),
            ('Keyboard', True),
            ('Barcode scanner', True),
            ('Speakers', False),
        ]
    },
    {
        'text': 'Which TWO of the following are output devices? (Select TWO)',
        'domain': 'Hardware',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Monitors and printers are output devices — they receive data from the computer and present it to the user.',
        'choices': [
            ('Webcam', False),
            ('Monitor', True),
            ('Microphone', False),
            ('Printer', True),
        ]
    },
    {
        'text': 'A user needs to connect their laptop to an external display. Which TWO ports on the laptop could be used for video output? (Select TWO)',
        'domain': 'Hardware',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'HDMI and DisplayPort are both video output ports commonly found on laptops. USB-A and RJ45 are not used for video output.',
        'choices': [
            ('HDMI', True),
            ('USB-A', False),
            ('DisplayPort', True),
            ('RJ45', False),
        ]
    },
    {
        'text': 'Which TWO of the following PSU ratings should a technician check when replacing a power supply? (Select TWO)',
        'domain': 'Hardware',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Wattage ensures the PSU can power all components. The form factor (ATX, SFX etc.) must match the case.',
        'choices': [
            ('Wattage to ensure it can power all components', True),
            ('The color of the PSU cables', False),
            ('The form factor to ensure it fits the case', True),
            ('The manufacturing date', False),
        ]
    },
    {
        'text': 'Which TWO of the following correctly describe the purpose of thermal paste? (Select TWO)',
        'domain': 'Hardware',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Thermal paste fills microscopic gaps between the CPU and cooler and improves heat transfer efficiency.',
        'choices': [
            ('It fills microscopic gaps between the CPU and the cooler surface', True),
            ('It acts as an electrical insulator for the CPU pins', False),
            ('It improves heat transfer from the CPU to the cooler', True),
            ('It lubricates the CPU fan bearings', False),
        ]
    },

    # ── NETWORKING - Select TWO ───────────────────────────────────────────────

    {
        'text': 'Which TWO of the following are private IP address ranges as defined by RFC 1918? (Select TWO)',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': True,
        'explanation': '10.0.0.0/8 and 192.168.0.0/16 are both RFC 1918 private ranges. The third is 172.16.0.0/12.',
        'choices': [
            ('10.0.0.0/8', True),
            ('8.8.8.0/24', False),
            ('192.168.0.0/16', True),
            ('204.79.197.0/24', False),
        ]
    },
    {
        'text': 'A technician needs to verify network connectivity on a Windows computer. Which TWO commands would be most useful? (Select TWO)',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'ping tests connectivity to a remote host and ipconfig displays the current IP configuration of the computer.',
        'choices': [
            ('ping', True),
            ('format', False),
            ('ipconfig', True),
            ('chkdsk', False),
        ]
    },
    {
        'text': 'Which TWO of the following are characteristics of TCP? (Select TWO)',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'TCP provides reliable ordered delivery and uses acknowledgements to confirm data was received.',
        'choices': [
            ('Provides reliable ordered delivery of data', True),
            ('Does not guarantee delivery of packets', False),
            ('Uses acknowledgements to confirm data receipt', True),
            ('Is faster than UDP because it has less overhead', False),
        ]
    },
    {
        'text': 'Which TWO wireless security protocols should be avoided as they are considered insecure? (Select TWO)',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'WEP and WPA (original) are both considered insecure due to known vulnerabilities. WPA2 and WPA3 are currently recommended.',
        'choices': [
            ('WEP', True),
            ('WPA2', False),
            ('WPA (original)', True),
            ('WPA3', False),
        ]
    },
    {
        'text': 'Which TWO of the following are true about a network switch? (Select TWO)',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'A switch operates at Layer 2 of the OSI model and forwards traffic based on MAC addresses, unlike a hub which broadcasts to all ports.',
        'choices': [
            ('It operates at Layer 2 of the OSI model', True),
            ('It broadcasts all traffic to every connected port', False),
            ('It forwards frames based on MAC addresses', True),
            ('It assigns IP addresses to connected devices', False),
        ]
    },
    {
        'text': 'A technician is setting up a small office network. Which TWO devices are needed to provide both wired and wireless connectivity and internet access? (Select TWO)',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'A router provides internet access and a wireless access point provides Wi-Fi connectivity. Many SOHO routers combine both.',
        'choices': [
            ('Router', True),
            ('Network hub', False),
            ('Wireless access point', True),
            ('KVM switch', False),
        ]
    },
    {
        'text': 'Which TWO of the following statements about IPv6 are correct? (Select TWO)',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'IPv6 uses 128-bit addresses written in hexadecimal and was developed to address the exhaustion of IPv4 addresses.',
        'choices': [
            ('IPv6 uses 128-bit addresses', True),
            ('IPv6 uses dotted decimal notation like IPv4', False),
            ('IPv6 was developed to address the exhaustion of IPv4 addresses', True),
            ('IPv6 supports fewer devices than IPv4', False),
        ]
    },
    {
        'text': 'Which TWO cable types are used for Ethernet networking? (Select TWO)',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Cat5e and Cat6 are both common Ethernet cable types. Coaxial is used for cable TV and older networks, not standard Ethernet.',
        'choices': [
            ('Cat5e', True),
            ('Coaxial RG-6', False),
            ('Cat6', True),
            ('Fiber optic ST connector for desktop Ethernet', False),
        ]
    },

    # ── MOBILE DEVICES - Select TWO ───────────────────────────────────────────

    {
        'text': 'Which TWO of the following are common symptoms of a failing laptop battery? (Select TWO)',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Swelling and significantly reduced battery life are both signs of battery degradation or failure.',
        'choices': [
            ('The battery charges faster than it used to', False),
            ('The battery swells and bulges', True),
            ('Significantly reduced battery life per charge', True),
            ('The laptop runs faster when on battery', False),
        ]
    },
    {
        'text': 'A user wants to connect their laptop to multiple external monitors. Which TWO ports would support video output? (Select TWO)',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'USB-C (with DisplayPort Alt Mode or Thunderbolt) and HDMI both support video output for connecting external monitors.',
        'choices': [
            ('USB-C / Thunderbolt', True),
            ('USB-A', False),
            ('HDMI', True),
            ('3.5mm audio jack', False),
        ]
    },
    {
        'text': 'Which TWO of the following are best practices for extending laptop battery lifespan? (Select TWO)',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Keeping the battery between 20-80% charge and avoiding heat exposure both help extend battery lifespan significantly.',
        'choices': [
            ('Keep the battery charge between 20% and 80%', True),
            ('Always charge to 100% before using the laptop', False),
            ('Avoid exposing the laptop to excessive heat', True),
            ('Discharge to 0% monthly to calibrate the battery', False),
        ]
    },
    {
        'text': 'Which TWO of the following are types of touchscreen technology? (Select TWO)',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Capacitive and resistive are two of the three primary touchscreen technologies. Capacitive is used in most modern smartphones.',
        'choices': [
            ('Capacitive', True),
            ('Electromagnetic pulse', False),
            ('Resistive', True),
            ('Inductive charging', False),
        ]
    },
    {
        'text': 'A technician is troubleshooting a laptop with no display output. Which TWO things should be checked first? (Select TWO)',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Checking brightness settings and connecting an external monitor are both quick first steps to determine if the issue is the display itself or something else.',
        'choices': [
            ('Check brightness settings — it may be turned all the way down', True),
            ('Replace the motherboard', False),
            ('Connect an external monitor to test if video output works', True),
            ('Reinstall the operating system', False),
        ]
    },

    # ── TROUBLESHOOTING - Select TWO ──────────────────────────────────────────

    {
        'text': 'A computer fails to POST and emits beep codes. Which TWO components should the technician check first? (Select TWO)',
        'domain': 'Troubleshooting',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'RAM and GPU failures are the most common causes of POST beep codes. The meaning of beep codes varies by BIOS manufacturer.',
        'choices': [
            ('RAM modules — reseat or test individually', True),
            ('The hard drive — check SATA cables', False),
            ('GPU — reseat or test with integrated graphics', True),
            ('The operating system — reinstall Windows', False),
        ]
    },
    {
        'text': 'A user reports their computer randomly restarts and runs hot. Which TWO actions should the technician take? (Select TWO)',
        'domain': 'Troubleshooting',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Cleaning dust from cooling components and checking/replacing thermal paste are the two most effective steps for overheating issues.',
        'choices': [
            ('Clean dust from fans and heatsinks', True),
            ('Replace the RAM modules', False),
            ('Check and reapply thermal paste on the CPU', True),
            ('Reinstall the operating system', False),
        ]
    },
    {
        'text': 'Which TWO of the following tools would a technician use to troubleshoot a suspected network cable problem? (Select TWO)',
        'domain': 'Troubleshooting',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'A cable tester verifies the cable is properly wired and has continuity. A toner probe traces the cable path to identify which port it connects to.',
        'choices': [
            ('Cable tester', True),
            ('Multimeter set to AC voltage', False),
            ('Toner probe', True),
            ('MemTest86', False),
        ]
    },
    {
        'text': 'A laser printer is producing poor quality output with faded areas and streaks. Which TWO components are most likely causing this? (Select TWO)',
        'domain': 'Troubleshooting',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'A low or defective toner cartridge and a worn drum unit are the two most common causes of poor print quality in laser printers.',
        'choices': [
            ('Low or defective toner cartridge', True),
            ('Incorrect paper size setting', False),
            ('Worn drum unit', True),
            ('Outdated printer driver', False),
        ]
    },
    {
        'text': 'A technician responds to a computer that will not boot. Which TWO initial steps are most appropriate? (Select TWO)',
        'domain': 'Troubleshooting',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Checking POST messages and verifying power connections are both quick non-destructive first steps in the troubleshooting process.',
        'choices': [
            ('Check POST messages and beep codes for clues', True),
            ('Immediately format the hard drive', False),
            ('Verify all power cables are properly connected', True),
            ('Replace the CPU', False),
        ]
    },
    {
        'text': 'Which TWO of the following should be done BEFORE replacing a suspected faulty component? (Select TWO)',
        'domain': 'Troubleshooting',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Backing up data protects against data loss during repair. Testing with a known-good replacement confirms the component is actually faulty before purchasing a new one.',
        'choices': [
            ('Back up user data in case something goes wrong', True),
            ('Order a replacement part immediately without further testing', False),
            ('Test with a known-good spare part to confirm the component is faulty', True),
            ('Reinstall the operating system first', False),
        ]
    },

    # ── SAFETY & MAINTENANCE - Select TWO ────────────────────────────────────

    {
        'text': 'Which TWO of the following are correct procedures when working inside a desktop computer? (Select TWO)',
        'domain': 'Safety & Best Practices',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Wearing an anti-static wrist strap prevents ESD damage and unplugging the computer ensures no live voltage is present while working.',
        'choices': [
            ('Wear an anti-static wrist strap to prevent ESD damage', True),
            ('Keep the computer powered on so you can test components as you go', False),
            ('Unplug the computer from the power outlet before opening', True),
            ('Work on a carpeted surface to cushion components', False),
        ]
    },
    {
        'text': 'Which TWO of the following are appropriate cleaning tools for computer components? (Select TWO)',
        'domain': 'Safety & Best Practices',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Compressed air removes dust effectively and isopropyl alcohol (90%+) cleans contacts and removes thermal paste without leaving moisture.',
        'choices': [
            ('Compressed air', True),
            ('Paper towels with water', False),
            ('Isopropyl alcohol (90% or higher)', True),
            ('Window cleaning spray', False),
        ]
    },
    {
        'text': 'A technician is about to handle a CPU and RAM. Which TWO precautions should be taken? (Select TWO)',
        'domain': 'Safety & Best Practices',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Touching a grounded metal surface discharges static electricity and handling components by their edges avoids touching sensitive circuits and contacts.',
        'choices': [
            ('Touch a grounded metal surface first to discharge static electricity', True),
            ('Hold the CPU by its pins for the most secure grip', False),
            ('Handle components by their edges avoiding contact with circuits and pins', True),
            ('Work in a warm humid room to prevent static buildup', False),
        ]
    },

    # ── VIRTUALIZATION & CLOUD - Select TWO ──────────────────────────────────

    {
        'text': 'Which TWO of the following are benefits of server virtualization? (Select TWO)',
        'domain': 'Virtualization & Cloud',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Virtualization reduces hardware costs by running multiple servers on one physical machine and allows faster deployment of new servers using templates.',
        'choices': [
            ('Reduces hardware costs by running multiple VMs on one physical server', True),
            ('Eliminates the need for backups', False),
            ('Allows faster deployment of new servers using VM templates', True),
            ('Makes servers immune to hardware failures', False),
        ]
    },
    {
        'text': 'Which TWO of the following are examples of SaaS (Software as a Service)? (Select TWO)',
        'domain': 'Virtualization & Cloud',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Microsoft 365 and Google Workspace are both SaaS applications — software delivered over the internet on a subscription basis.',
        'choices': [
            ('Microsoft 365 (Office online)', True),
            ('A physical server rack in a data center', False),
            ('Google Workspace (Gmail, Docs)', True),
            ('A VMware ESXi hypervisor installation', False),
        ]
    },
    {
        'text': 'Which TWO of the following are characteristics of cloud computing? (Select TWO)',
        'domain': 'Virtualization & Cloud',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Cloud computing offers on-demand self-service where resources can be provisioned without human interaction, and broad network access from any device.',
        'choices': [
            ('On-demand self-service — resources can be provisioned without human interaction', True),
            ('Resources are always physically located in the same building as the user', False),
            ('Broad network access from any internet-connected device', True),
            ('Cloud services always cost more than on-premises solutions', False),
        ]
    },

    # ── PRINTERS - Select TWO ─────────────────────────────────────────────────

    {
        'text': 'Which TWO of the following are steps in the laser printing process? (Select TWO)',
        'domain': 'Printers',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Charging the drum and fusing the toner to the paper with heat are both steps in the six-step laser printing process.',
        'choices': [
            ('Charging the photosensitive drum', True),
            ('Spraying ink through microscopic nozzles', False),
            ('Fusing toner to the paper with heat', True),
            ('Burning the image with a thermal print head', False),
        ]
    },
    {
        'text': 'A network printer suddenly stops working for all users. Which TWO items should the technician check first? (Select TWO)',
        'domain': 'Printers',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Checking the printer power and status and verifying network connectivity are both quick first steps before more complex troubleshooting.',
        'choices': [
            ('Check the printer power and display status panel', True),
            ('Reinstall printer drivers on all computers immediately', False),
            ('Verify the printer has network connectivity — check link lights', True),
            ('Replace the toner cartridge', False),
        ]
    },
    {
        'text': 'Which TWO of the following statements about inkjet printers are correct? (Select TWO)',
        'domain': 'Printers',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Inkjet printers spray liquid ink and require regular print head cleaning to prevent clogged nozzles.',
        'choices': [
            ('They spray liquid ink through microscopic nozzles onto paper', True),
            ('They use a laser to create a static charge on a drum', False),
            ('Print heads can become clogged if the printer is not used regularly', True),
            ('They use toner powder that is fused with heat', False),
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
            exam=qd.get('exam', 'core1'),
            explanation=qd.get('explanation', ''),
            multi_select=qd.get('multi_select', False),
            active=True
        )
        db.session.add(q)
        db.session.flush()
        for choice_text, is_correct in qd['choices']:
            c = Choice(question_id=q.id, text=choice_text, is_correct=is_correct)
            db.session.add(c)
        added += 1
    db.session.commit()
    total = Question.query.count()
    multi = Question.query.filter_by(multi_select=True).count()
    print(f'Added {added} questions. Skipped {skipped} duplicates.')
    print(f'Total questions: {total} | Multi-select questions: {multi}')