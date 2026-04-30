import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app import app, db
from models import Question, Choice

questions_data = [
    # ── Mobile Devices / Display & Antenna (PDF 1) ──────────────────────────
    {
        'text': 'What is a key consideration regarding repairing a damaged mobile device display?',
        'domain': 'Mobile Devices',
        'choices': [
            ('Mobile displays are always easy and cheap to repair', False),
            ('Mobile displays can never be repaired and must always be replaced', False),
            ('Repairs can be expensive and in some cases it may be more cost effective to replace the entire unit', True),
            ('Mobile displays are covered under all manufacturer warranties permanently', False),
        ]
    },
    {
        'text': 'On laptops, what physical factor has a significant bearing on how well the display holds up over time?',
        'domain': 'Mobile Devices',
        'choices': [
            ('The resolution of the screen', False),
            ('The refresh rate setting', False),
            ('The durability of the hinges and the overall build quality of the screen', True),
            ('The brightness level setting', False),
        ]
    },
    {
        'text': 'Is touch integration standard on all laptops?',
        'domain': 'Mobile Devices',
        'choices': [
            ('Yes, all modern laptops come with touchscreen as standard', False),
            ('No, laptops never support touchscreens', False),
            ('No, it is typically a feature you must specifically request, though some models do offer it as standard', True),
            ('Yes, but only on laptops running Windows 11', False),
        ]
    },
    {
        'text': 'What does a 60Hz refresh rate on a display mean?',
        'domain': 'Mobile Devices',
        'choices': [
            ('The display can show 60 different colors per second', False),
            ('The display processes 60 megabytes of data per second', False),
            ('The display refreshes or redraws the image 60 times per second', True),
            ('The display brightness adjusts itself 60 times per second', False),
        ]
    },
    {
        'text': 'Who would most benefit from a display with a higher refresh rate than 60Hz?',
        'domain': 'Mobile Devices',
        'choices': [
            ('Someone using a laptop for basic office work and browsing', False),
            ('Someone writing documents in a word processor', False),
            ('Someone doing 3D animation, intensive graphics work, or gaming', True),
            ('Someone using a laptop in a dimly lit room', False),
        ]
    },
    {
        'text': 'What is the most likely cause of a dim screen on a mobile device?',
        'domain': 'Mobile Devices',
        'choices': [
            ('A failing CPU', False),
            ('A damaged Wi-Fi antenna', False),
            ('Low brightness settings or a backlight issue', True),
            ('Outdated RAM', False),
        ]
    },
    {
        'text': 'What should you do first if a touchscreen becomes unresponsive?',
        'domain': 'Mobile Devices',
        'choices': [
            ('Replace the screen immediately', False),
            ('Perform a factory reset of the device', False),
            ('Update the drivers or recalibrate the digitizer in the display settings', True),
            ('Check the Wi-Fi connection settings', False),
        ]
    },
    {
        'text': 'What are dead pixels and how are they typically resolved?',
        'domain': 'Mobile Devices',
        'choices': [
            ('Pixels that flash rapidly — resolved by adjusting the refresh rate', False),
            ('Pixels with incorrect color — resolved by adjusting display color settings', False),
            ('Pixels that appear as small black spots on the screen — typically require screen replacement as there is little else that can be done', True),
            ('Pixels that are too bright — resolved by reducing screen brightness', False),
        ]
    },
    {
        'text': 'Lines appearing on a screen could indicate a problem with which components?',
        'domain': 'Mobile Devices',
        'choices': [
            ('The battery and the charging port', False),
            ('The RAM and the CPU', False),
            ('The GPU or the cable connections between the display and the motherboard', True),
            ('The Wi-Fi antenna or the SIM card', False),
        ]
    },
    {
        'text': 'What can cause a flickering screen on a laptop?',
        'domain': 'Mobile Devices',
        'choices': [
            ('Too many background applications running', False),
            ('An outdated operating system', False),
            ('A loose cable connection or a faulty inverter that provides the backlight', True),
            ('Insufficient RAM causing display errors', False),
        ]
    },
    {
        'text': 'What can cause color distortion on a display?',
        'domain': 'Mobile Devices',
        'choices': [
            ('An outdated GPU driver only', False),
            ('Excessive screen brightness settings', False),
            ('A faulty display connection', True),
            ('Low battery levels affecting screen output', False),
        ]
    },
    {
        'text': 'Where is the Wi-Fi antenna typically located in a laptop?',
        'domain': 'Mobile Devices',
        'choices': [
            ('Inside the base of the laptop near the keyboard', False),
            ('Next to the RAM slots on the motherboard', False),
            ('Embedded in the screen, typically around the outer edge of the display', True),
            ('Inside the battery compartment', False),
        ]
    },
    {
        'text': 'What is the typical maximum range of a Bluetooth connection?',
        'domain': 'Mobile Devices',
        'choices': [
            ('10 feet', False),
            ('100 feet', False),
            ('Around 30 feet', True),
            ('Around 300 feet', False),
        ]
    },
    {
        'text': 'A user is experiencing a weak Wi-Fi signal on their laptop. What is the most likely and simple cause?',
        'domain': 'Mobile Devices',
        'choices': [
            ('The SIM card is not inserted correctly', False),
            ('The display brightness is set too high', False),
            ('The laptop is too far from the Wi-Fi source or there may be physical obstructions blocking the signal', True),
            ('The Bluetooth antenna is interfering with Wi-Fi', False),
        ]
    },
    {
        'text': 'What should you check first if a mobile device has no cellular service?',
        'domain': 'Mobile Devices',
        'choices': [
            ('The Wi-Fi antenna connection', False),
            ('The display refresh rate settings', False),
            ('The SIM card and roaming settings', True),
            ('The Bluetooth driver version', False),
        ]
    },
    {
        'text': 'What is a digital SIM (eSIM)?',
        'domain': 'Mobile Devices',
        'choices': [
            ('A SIM card made from a different material for durability', False),
            ('A SIM card that stores data instead of identity credentials', False),
            ('A SIM that is no longer a physical hardware component but is built digitally into the device', True),
            ('A SIM card that works exclusively with Wi-Fi calling', False),
        ]
    },
    {
        'text': 'What is the correct way to clean a mobile device screen?',
        'domain': 'Mobile Devices',
        'choices': [
            ('Use a paper towel and water', False),
            ('Use an alcohol-soaked cotton ball', False),
            ('Use a microfiber cloth and a screen-safe cleaner', True),
            ('Use a dry tissue and rub firmly to remove smudges', False),
        ]
    },
    {
        'text': 'How does keeping screen brightness high affect the device?',
        'domain': 'Mobile Devices',
        'choices': [
            ('It improves GPU performance', False),
            ('It has no effect on battery life', False),
            ('It draws more power and reduces battery life', True),
            ('It increases the refresh rate automatically', False),
        ]
    },
    {
        'text': 'Which of the following is a best practice for maintaining wireless antenna performance?',
        'domain': 'Mobile Devices',
        'choices': [
            ('Disable Bluetooth when not in use to prevent antenna interference', False),
            ('Keep the device in airplane mode when at home', False),
            ('Keep device firmware updated for the latest wireless protocols and avoid obstructions that block signals', True),
            ('Reset network settings monthly to refresh antenna connections', False),
        ]
    },
    {
        'text': 'According to the material, when display and antenna issues DO occur, what are they most commonly caused by?',
        'domain': 'Mobile Devices',
        'choices': [
            ('Physical damage from drops or liquid exposure', False),
            ('Manufacturing defects in the components', False),
            ('Configuration and settings issues rather than actual hardware failures', True),
            ('Incompatible software updates breaking hardware drivers', False),
        ]
    },
    # ── Storage - HDD vs SSD ─────────────────────────────────────────────────
    {
        'text': 'How does a Hard Disk Drive (HDD) store data?',
        'domain': 'Storage',
        'choices': [
            ('Using flash-based memory chips with no moving parts', False),
            ('Using optical laser technology to burn data onto a disc', False),
            ('Using a spinning magnetic platter and an actuator arm with a read-write head', True),
            ('Using RAM chips that retain data when powered off', False),
        ]
    },
    {
        'text': 'What type of storage technology does an SSD use?',
        'domain': 'Storage',
        'choices': [
            ('Magnetic platters with an actuator arm', False),
            ('Optical disc technology', False),
            ('Flash-based storage with no moving parts', True),
            ('Rotating drum memory', False),
        ]
    },
    {
        'text': 'Which of the following is NOT an advantage of an SSD over an HDD?',
        'domain': 'Storage',
        'choices': [
            ('Faster data access speeds', False),
            ('More durable due to no moving parts', False),
            ('Higher storage capacity per dollar', True),
            ('Better power efficiency', False),
        ]
    },
    {
        'text': 'Why are HDDs less power efficient than SSDs?',
        'domain': 'Storage',
        'choices': [
            ('HDDs require more RAM to function', False),
            ('HDDs require a motor to spin the disk and move the actuator arm', True),
            ('HDDs generate more heat due to their flash memory', False),
            ('HDDs use PCIe interface which draws more power', False),
        ]
    },
    {
        'text': 'In terms of performance, how do SSDs compare to HDDs?',
        'domain': 'Storage',
        'choices': [
            ('Some high-end HDDs can match entry-level SSD speeds', False),
            ('HDDs outperform SSDs for sequential read tasks', False),
            ('SSDs entirely outperform HDDs — no HDD can reach the performance level of any SSD', True),
            ('SSDs and HDDs perform equally for everyday tasks', False),
        ]
    },
    {
        'text': 'What is the PRIMARY use case where HDDs are still preferred over SSDs?',
        'domain': 'Storage',
        'choices': [
            ('Gaming consoles requiring fast load times', False),
            ('Ultrabooks where physical size matters', False),
            ('Bulk storage, archiving, and backup where large capacity is the main concern', True),
            ('Operating system drives where speed is critical', False),
        ]
    },
    {
        'text': 'Which of the following is the best use case for an SSD?',
        'domain': 'Storage',
        'choices': [
            ('Long-term cold storage of rarely accessed archive data', False),
            ('A server storing massive amounts of backup files', False),
            ('An operating system drive, gaming, or high-performance computing', True),
            ('A NAS (Network Attached Storage) for bulk file storage', False),
        ]
    },
    {
        'text': 'What does NVMe stand for?',
        'domain': 'Storage',
        'choices': [
            ('New Virtual Memory Extension', False),
            ('Non-Volatile Memory Express', False),
            ('Non-Volatile Memory Express', True),
            ('Network Virtual Memory Expansion', False),
        ]
    },
    {
        'text': 'What interface does a 2.5-inch SATA SSD use to connect to the motherboard?',
        'domain': 'Storage',
        'choices': [
            ('PCIe interface', False),
            ('NVMe interface', False),
            ('Serial ATA (SATA) interface', True),
            ('Thunderbolt interface', False),
        ]
    },
    {
        'text': 'What interface does an NVMe SSD use to connect to the motherboard?',
        'domain': 'Storage',
        'choices': [
            ('Serial ATA (SATA)', False),
            ('USB 3.0', False),
            ('PCIe (Peripheral Component Interconnect Express)', True),
            ('HDMI', False),
        ]
    },
    {
        'text': 'Can a 2.5-inch SATA SSD and an NVMe SSD be used interchangeably in the same slot?',
        'domain': 'Storage',
        'choices': [
            ('Yes, they use the same connector', False),
            ('Yes, but only if the motherboard supports both', False),
            ('No, they use completely different interfaces and are not interchangeable', True),
            ('Yes, with the use of an adapter cable', False),
        ]
    },
    {
        'text': 'What does an NVMe SSD physically resemble?',
        'domain': 'Storage',
        'choices': [
            ('A traditional 3.5-inch hard disk drive', False),
            ('A USB flash drive', False),
            ('A RAM chip, but with a different physical connector', True),
            ('A 2.5-inch laptop hard drive', False),
        ]
    },
    {
        'text': 'Why are SSDs a better choice for mobile devices like ultrabooks?',
        'domain': 'Storage',
        'choices': [
            ('They are cheaper than HDDs', False),
            ('They have higher storage capacities', False),
            ('They come in smaller physical form factors making them ideal for compact devices', True),
            ('They generate more heat which keeps the device warm in cold environments', False),
        ]
    },
    {
        'text': 'Which of the following best explains why SSDs tend to have a longer lifespan than HDDs?',
        'domain': 'Storage',
        'choices': [
            ('SSDs use more advanced magnetic technology', False),
            ('SSDs are coated with a protective layer against dust', False),
            ('SSDs have no moving parts, so there is less mechanical wear and tear', True),
            ('SSDs run at lower temperatures due to their larger size', False),
        ]
    },
    {
        'text': 'A business needs to store years worth of archive data and rarely needs to access it quickly. Budget is a concern. What is the best storage choice?',
        'domain': 'Storage',
        'choices': [
            ('NVMe SSD for maximum speed', False),
            ('2.5-inch SATA SSD for reliability', False),
            ('HDD for the highest capacity at the lowest cost per gigabyte', True),
            ('Thunderbolt external SSD for portability', False),
        ]
    },
    {
        'text': 'Which of the following is a true statement about HDDs?',
        'domain': 'Storage',
        'choices': [
            ('HDDs are completely silent during operation', False),
            ('HDDs are faster than SSDs for random read and write operations', False),
            ('HDDs produce some noise during operation due to their spinning platters and moving parts', True),
            ('HDDs use flash memory to store data magnetically', False),
        ]
    },
    {
        'text': 'When upgrading the storage drive in an existing system, what is the most important thing to verify first?',
        'domain': 'Storage',
        'choices': [
            ('The color of the drive to match the system aesthetic', False),
            ('The brand of the drive for warranty purposes', False),
            ('The interface and form factor compatibility with the motherboard', True),
            ('Whether the drive supports Wi-Fi connectivity', False),
        ]
    },
    # ── Hardware Failure ─────────────────────────────────────────────────────
    {
        'text': 'What are the four main categories of hardware failure causes covered in this material?',
        'domain': 'Hardware Troubleshooting',
        'choices': [
            ('Physical damage, software conflicts, user error, and manufacturing defects', False),
            ('Power surges, overheating, dust buildup, and dropping components', False),
            ('Mechanical failures, electrical failures, environmental failures, and manufacturing defects or software-related failures', True),
            ('Wear and tear, short circuits, humidity, and firmware corruption', False),
        ]
    },
    {
        'text': 'Which computer components are most susceptible to mechanical wear and tear over time due to having moving parts?',
        'domain': 'Hardware Troubleshooting',
        'choices': [
            ('RAM modules and SSDs', False),
            ('Motherboards and CPUs', False),
            ('Traditional hard disk drives with spinning disks and cooling fans', True),
            ('Power supply units and graphics cards', False),
        ]
    },
    {
        'text': 'What is one of the best ways to reduce the risk of mechanical storage failures?',
        'domain': 'Hardware Troubleshooting',
        'choices': [
            ('Defragment hard drives regularly to reduce mechanical stress', False),
            ('Keep hard drives in a vertical position to reduce platter wear', False),
            ('Switch to solid-state drives which have no moving parts and are therefore less prone to mechanical failure', True),
            ('Replace hard drive cables every 6 months to prevent connection failures', False),
        ]
    },
    {
        'text': 'What can cause electrical failures in computer hardware?',
        'domain': 'Hardware Troubleshooting',
        'choices': [
            ('Using third-party cables and peripherals', False),
            ('Running too many applications simultaneously', False),
            ('Power surges or spikes, overheating, dust accumulation, and short circuits', True),
            ('Keeping the system powered on for extended periods', False),
        ]
    },
    {
        'text': 'What is the purpose of a surge protector?',
        'domain': 'Hardware Troubleshooting',
        'choices': [
            ('It provides backup power to the system during a power outage', False),
            ('It conditions the power supply to deliver a constant voltage to components', False),
            ('It has a built-in breaker that trips during a power spike to prevent the surge from reaching the system components', True),
            ('It filters dust from the power supply unit to prevent overheating', False),
        ]
    },
    {
        'text': 'What does UPS stand for and what is its purpose?',
        'domain': 'Hardware Troubleshooting',
        'choices': [
            ('Universal Power Supply — it replaces the internal power supply unit', False),
            ('Uninterrupted Power System — it boosts power delivery to components', False),
            ('Uninterruptible Power Supply — it conditions power to make it steadier as it flows through the system and provides backup power', True),
            ('Unified Protection System — it protects against both power surges and dust buildup', False),
        ]
    },
    {
        'text': 'How can you help prevent electrical failures caused by overheating?',
        'domain': 'Hardware Troubleshooting',
        'choices': [
            ('Reduce the CPU clock speed in the BIOS settings', False),
            ('Replace the power supply unit annually', False),
            ('Regularly clean dust from components to maintain better airflow and keep the system cool', True),
            ('Install additional RAM to reduce the load on the CPU', False),
        ]
    },
    {
        'text': 'What should you do to prevent electrical failures caused by moisture?',
        'domain': 'Hardware Troubleshooting',
        'choices': [
            ('Use a dehumidifier only in server room environments', False),
            ('Apply isopropyl alcohol to components monthly to repel moisture', False),
            ('Keep liquids away from electronic components and ensure the environment remains dry', True),
            ('Seal the computer case completely to prevent any moisture from entering', False),
        ]
    },
    {
        'text': 'What are the main environmental causes of hardware failure?',
        'domain': 'Hardware Troubleshooting',
        'choices': [
            ('Power surges, short circuits, and manufacturing defects', False),
            ('Improper installation, forced connections, and dropped components', False),
            ('Extreme temperatures, humidity and moisture, and dust and debris buildup', True),
            ('Software conflicts, driver failures, and firmware corruption', False),
        ]
    },
    {
        'text': 'What is the ideal environment to keep computer systems in to reduce environmental hardware failures?',
        'domain': 'Hardware Troubleshooting',
        'choices': [
            ('A warm environment with moderate humidity for component flexibility', False),
            ('A sealed environment with no airflow to prevent dust entry', False),
            ('A climate-controlled environment that is cool, dry, and as dust-free as possible', True),
            ('A cold environment with high humidity to prevent static buildup', False),
        ]
    },
    {
        'text': 'Why is there little that can be done to PREVENT manufacturing defects?',
        'domain': 'Hardware Troubleshooting',
        'choices': [
            ('Manufacturing defects only occur in low-cost components', False),
            ('Manufacturers deliberately limit warranty coverage to avoid responsibility', False),
            ('Manufacturing defects occur during the production process before the component reaches the user so there is no way to prevent them — they can only be detected and responded to', True),
            ('Manufacturing defects are too rare to warrant preventative measures', False),
        ]
    },
    {
        'text': 'What utility can help detect a possible hard drive manufacturing defect?',
        'domain': 'Hardware Troubleshooting',
        'choices': [
            ('Task Manager', False),
            ('MemTest86', False),
            ('Check Disk utility to determine the integrity of files on the drive', True),
            ('Device Manager', False),
        ]
    },
    {
        'text': 'How are manufacturing defects in hardware typically resolved?',
        'domain': 'Hardware Troubleshooting',
        'choices': [
            ('They can be repaired using firmware updates from the manufacturer', False),
            ('They can be fixed by reinstalling the operating system', False),
            ('The component can potentially be returned and replaced under warranty, or replaced by purchasing a new unit if not covered', True),
            ('They can be resolved by running the BIOS diagnostics utility', False),
        ]
    },
    {
        'text': 'How can software induce a hardware failure?',
        'domain': 'Hardware Troubleshooting',
        'choices': [
            ('Software can directly corrupt the firmware of hardware components', False),
            ('Malware can cause physical damage to storage drives', False),
            ('Monitoring software that is not functioning or configured correctly can fail to detect issues like CPU overheating, allowing hardware damage to occur', True),
            ('Software updates can change voltage settings that damage components', False),
        ]
    },
    {
        'text': 'What is an example of software-induced hardware failure mentioned in the material?',
        'domain': 'Hardware Troubleshooting',
        'choices': [
            ('A virus corrupting the hard drive partition table', False),
            ('A driver update causing a GPU to overheat', False),
            ('The CPU temperature monitoring feature in the BIOS not functioning properly, allowing the CPU to overheat without any warning', True),
            ('A Windows update disabling the cooling fan control software', False),
        ]
    },
    {
        'text': 'Why should you regularly monitor system logs even if the system appears to be running normally?',
        'domain': 'Hardware Troubleshooting',
        'choices': [
            ('System logs show which components are due for replacement based on age', False),
            ('System logs record backup schedules and alert you to missed backups', False),
            ('System logs generate entries that can be indicative of hardware errors even before visible symptoms appear, allowing early detection of problems', True),
            ('System logs track software license expiry dates that could affect hardware performance', False),
        ]
    },
    {
        'text': 'What should you do with aging components to help ensure system longevity?',
        'domain': 'Hardware Troubleshooting',
        'choices': [
            ('Overclock them to get maximum performance before they fail', False),
            ('Keep them running as long as possible to get the best return on investment', False),
            ('Replace aging components as you can and keep systems as up-to-date as possible', True),
            ('Reformat and reinstall the operating system on aging components to extend their life', False),
        ]
    },
    {
        'text': 'What is the recommended best practice for protecting data in the event of hardware failure?',
        'domain': 'Hardware Troubleshooting',
        'choices': [
            ('Store all data on a single high-quality SSD for reliability', False),
            ('Use RAID 0 to improve data read speeds and reliability', False),
            ('Perform regular backups and verify that the data can be successfully recovered', True),
            ('Keep duplicate copies of data in the same system on separate partitions', False),
        ]
    },
    {
        'text': 'Why might a system in a pet-friendly home environment require more frequent maintenance than one in a well-ventilated office?',
        'domain': 'Hardware Troubleshooting',
        'choices': [
            ('Pets generate more static electricity that damages components', False),
            ('Home systems are used more intensively than office systems', False),
            ('Pet hair accumulates inside the case more quickly than regular dust, increasing the risk of overheating and component failure', True),
            ('Home environments tend to have more power surges than office environments', False),
        ]
    },
    {
        'text': 'According to the material, what is the ultimate goal of all hardware maintenance and best practices?',
        'domain': 'Hardware Troubleshooting',
        'choices': [
            ('To eliminate all possibility of hardware failure entirely', False),
            ('To reduce the cost of component replacements over time', False),
            ('To do whatever possible to ensure that systems and their components last as long as possible, even though everything will eventually reach its end of life', True),
            ('To maintain the manufacturer warranty on all components', False),
        ]
    },
    # ── Maintenance Tools ─────────────────────────────────────────────────────
    {
        'text': 'What are the primary goals of performing regular system maintenance?',
        'domain': 'Maintenance',
        'choices': [
            ('To upgrade components and increase clock speeds', False),
            ('To reset the BIOS settings and clear cached data', False),
            ('To prevent hardware failures, maintain proper airflow and temperature regulation, and diagnose and resolve software and hardware problems', True),
            ('To reinstall the operating system and update all software', False),
        ]
    },
    {
        'text': 'What are the two primary types of screwdrivers used for computer maintenance?',
        'domain': 'Maintenance',
        'choices': [
            ('Torx and hex screwdrivers', False),
            ('Flathead and jeweler\'s screwdrivers', False),
            ('Phillips and flathead screwdrivers', True),
            ('Torx and Phillips screwdrivers', False),
        ]
    },
    {
        'text': 'What is the purpose of an anti-static wrist strap during system maintenance?',
        'domain': 'Maintenance',
        'choices': [
            ('To protect your wrist from sharp edges inside the case', False),
            ('To measure the voltage levels of components', False),
            ('To reduce the chance of electrostatic discharge damaging sensitive components', True),
            ('To ground the power supply before working on it', False),
        ]
    },
    {
        'text': 'What is the advantage of using an air compressor over individual compressed air cans for cleaning?',
        'domain': 'Maintenance',
        'choices': [
            ('An air compressor produces colder air which is better for cooling components', False),
            ('Compressed air cans are too powerful and can damage components', False),
            ('An air compressor means you do not have to keep purchasing individual cans repeatedly', True),
            ('An air compressor can also be used to apply thermal paste evenly', False),
        ]
    },
    {
        'text': 'What is thermal paste used for in computer maintenance?',
        'domain': 'Maintenance',
        'choices': [
            ('It seals gaps between the case panels to improve airflow', False),
            ('It lubricates CPU fan bearings to reduce noise', False),
            ('It improves heat transfer between the CPU and the cooler by ensuring better contact', True),
            ('It protects the motherboard from moisture and condensation', False),
        ]
    },
    {
        'text': 'What is a multimeter used for in computer maintenance?',
        'domain': 'Maintenance',
        'choices': [
            ('Testing RAM for memory errors', False),
            ('Measuring the refresh rate of displays', False),
            ('Checking connectivity and continuity between connections', True),
            ('Testing the speed of hard drives and SSDs', False),
        ]
    },
    {
        'text': 'What is a crimper used for in network maintenance?',
        'domain': 'Maintenance',
        'choices': [
            ('Tracing cable paths through walls and ceilings', False),
            ('Testing network cable connectivity end to end', False),
            ('Attaching connectors to the ends of network cables', True),
            ('Punching down wires at a network rack', False),
        ]
    },
    {
        'text': 'Why might a technician choose to make their own network cables rather than buying pre-made ones?',
        'domain': 'Maintenance',
        'choices': [
            ('Pre-made cables are always lower quality than hand-crimped cables', False),
            ('Hand-crimped cables support faster data transfer speeds', False),
            ('Buying cable and connectors in bulk and crimping them yourself saves a significant amount of money, and damaged cables can be repaired by crimping on a new connector', True),
            ('Pre-made cables are not available in the lengths required for most installations', False),
        ]
    },
    {
        'text': 'What is a toner probe used for?',
        'domain': 'Maintenance',
        'choices': [
            ('Testing whether a network cable is properly crimped', False),
            ('Measuring the voltage on a network switch port', False),
            ('Tracing cable paths to identify where a wall port connects to at the other end such as at a switch', True),
            ('Punching down wires at a patch panel', False),
        ]
    },
    {
        'text': 'What is a punchdown tool used for?',
        'domain': 'Maintenance',
        'choices': [
            ('Crimping RJ45 connectors onto network cables', False),
            ('Testing network port connectivity with a loopback signal', False),
            ('Wiring connections at a network rack or patch panel', True),
            ('Tracing cable runs through walls and ceilings', False),
        ]
    },
    {
        'text': 'What is a loopback plug used for?',
        'domain': 'Maintenance',
        'choices': [
            ('Connecting two network switches together for testing', False),
            ('Tracing the physical path of a network cable', False),
            ('Testing connectivity on a single network interface to verify it is functioning correctly', True),
            ('Measuring the signal strength of a Wi-Fi antenna', False),
        ]
    },
    {
        'text': 'Which of the following is a Windows-based software tool used to monitor system performance and running processes?',
        'domain': 'Maintenance',
        'choices': [
            ('MemTest86', False),
            ('Disk Clean-up', False),
            ('Task Manager', True),
            ('BIOS utility', False),
        ]
    },
    {
        'text': 'What is the purpose of the Disk Clean-up utility?',
        'domain': 'Maintenance',
        'choices': [
            ('It checks the physical health of the hard drive for errors', False),
            ('It defragments the hard drive to improve read speeds', False),
            ('It helps determine the state of the hard drive by cleaning up unnecessary files', True),
            ('It formats and repartitions the hard drive for optimal performance', False),
        ]
    },
    {
        'text': 'What is the Check Disk utility used for?',
        'domain': 'Maintenance',
        'choices': [
            ('Monitoring CPU and RAM usage in real time', False),
            ('Cleaning up temporary files and freeing disk space', False),
            ('Helping to determine the state and health of hard drives by checking for errors', True),
            ('Checking whether the correct drivers are installed for storage devices', False),
        ]
    },
    {
        'text': 'What is MemTest86 used for?',
        'domain': 'Maintenance',
        'choices': [
            ('Testing the read and write speed of SSDs and HDDs', False),
            ('Checking the GPU memory for rendering errors', False),
            ('Testing RAM for memory errors', True),
            ('Verifying that the BIOS settings are correctly configured', False),
        ]
    },
    {
        'text': 'Is MemTest86 included by default in Windows?',
        'domain': 'Maintenance',
        'choices': [
            ('Yes, it is built into Windows as a standard utility', False),
            ('Yes, but only in Windows Pro and Enterprise editions', False),
            ('No, it must be downloaded and installed separately', True),
            ('No, it is only available for Mac and Linux systems', False),
        ]
    },
    {
        'text': 'Why is it important to regularly check the system event log?',
        'domain': 'Maintenance',
        'choices': [
            ('The system log shows which applications are using the most storage', False),
            ('The system log displays the current CPU and RAM temperatures', False),
            ('The system log records all events including software errors, hardware issues, driver problems, and application failures, helping you stay on top of what is happening with the system', True),
            ('The system log shows which drivers need to be updated', False),
        ]
    },
    {
        'text': 'Why is it important to not only back up data but also test the recovery of that data?',
        'domain': 'Maintenance',
        'choices': [
            ('Testing recovery updates the backup file with the latest changes', False),
            ('Backups automatically delete themselves if not tested regularly', False),
            ('Simply having backups is not enough — you need to verify that all necessary data is included and that it can be successfully recovered when needed', True),
            ('Testing recovery ensures the backup drive is not infected with malware', False),
        ]
    },
    {
        'text': 'Why do desktop systems constantly accumulate dust inside the case?',
        'domain': 'Maintenance',
        'choices': [
            ('Desktop cases are not sealed properly during manufacturing', False),
            ('Dust is attracted to the magnetic fields generated by HDDs', False),
            ('The fans that evacuate hot air must also pull air into the system, and that incoming air carries dust with it', True),
            ('Desktop components generate static electricity that attracts dust particles', False),
        ]
    },
    {
        'text': 'According to the material, what is the single most important principle behind preventative maintenance?',
        'domain': 'Maintenance',
        'choices': [
            ('Always use the most expensive and professional grade tools available', False),
            ('Replace components on a fixed schedule regardless of their condition', False),
            ('Ensure that preventative maintenance is done consistently because the more you maintain something the better it will perform and the longer it will last', True),
            ('Focus maintenance efforts on software updates rather than hardware cleaning', False),
        ]
    },
    # ── ESD / Safety ─────────────────────────────────────────────────────────
    {
        'text': 'What does ESD stand for and why is it a concern when handling computer components?',
        'domain': 'Safety & Best Practices',
        'choices': [
            ('Electrical System Damage — it can permanently short circuit the motherboard', False),
            ('Electronic Static Discharge — it can overheat sensitive components', False),
            ('Electrostatic Discharge — even a small static shock can damage components that operate at microvolt levels', True),
            ('Electrical Surge Damage — it can cause power spikes that fry the CPU', False),
        ]
    },
    {
        'text': 'What is the purpose of an anti-static wrist strap?',
        'domain': 'Safety & Best Practices',
        'choices': [
            ('It protects your wrist from sharp edges inside the computer case', False),
            ('It measures the static electricity level in the room', False),
            ('It grounds you so that any static charge is discharged safely into the mat rather than into the component you are handling', True),
            ('It prevents electrical current from the power supply reaching your hands', False),
        ]
    },
    {
        'text': 'If you do not have an anti-static wrist strap available, what should you do before handling components?',
        'domain': 'Safety & Best Practices',
        'choices': [
            ('Wear rubber gloves to insulate yourself from static', False),
            ('Work as quickly as possible to minimize contact time with components', False),
            ('Touch something metal first to pre-discharge any built-up static electricity', True),
            ('Run cold water over your hands to reduce static charge', False),
        ]
    },
    {
        'text': 'What are anti-static bags used for?',
        'domain': 'Safety & Best Practices',
        'choices': [
            ('Storing food and drinks away from computer workstations', False),
            ('Keeping components cool during installation', False),
            ('Storing and transporting computer components to protect them from electrostatic discharge', True),
            ('Wrapping power cables to prevent electrical shorts', False),
        ]
    },
    {
        'text': 'What is the correct way to handle a motherboard?',
        'domain': 'Safety & Best Practices',
        'choices': [
            ('Hold it firmly in the center for maximum control', False),
            ('Place it face down on a flat surface before installing components', False),
            ('Hold it by its edges and avoid touching the circuitry and pins', True),
            ('Hold it by the CPU socket area for the most stable grip', False),
        ]
    },
    {
        'text': 'What is the correct way to handle a CPU?',
        'domain': 'Safety & Best Practices',
        'choices': [
            ('Hold it by the pins to avoid touching the processor surface', False),
            ('Apply firm pressure to seat it properly before installation', False),
            ('Handle it by the sides and avoid direct contact with the pins or connectors', True),
            ('Hold it by the heat spreader surface for the most secure grip', False),
        ]
    },
    {
        'text': 'When installing a RAM module, how much force should be required?',
        'domain': 'Safety & Best Practices',
        'choices': [
            ('Significant force is always needed to ensure a proper connection', False),
            ('No force at all — RAM modules float into place magnetically', False),
            ('RAM should be firmly inserted but should not require a lot of force — it should snap into place when properly aligned', True),
            ('Moderate force with a screwdriver is recommended to seat the contacts', False),
        ]
    },
    {
        'text': 'What precaution should you take specifically regarding hard drives and SSDs during handling?',
        'domain': 'Safety & Best Practices',
        'choices': [
            ('Always wear latex gloves when touching the circuit board', False),
            ('Store them vertically to prevent data loss during handling', False),
            ('Avoid dropping them or applying pressure on any sensitive components', True),
            ('Keep them in the anti-static bag until the very last moment of installation', False),
        ]
    },
    {
        'text': 'What should you always do before working on any internal computer components?',
        'domain': 'Safety & Best Practices',
        'choices': [
            ('Run a full virus scan to ensure the system is clean', False),
            ('Back up all data to an external drive', False),
            ('Unplug the power source completely before opening the case or touching any internal components', True),
            ('Enter the BIOS and disable all hardware components', False),
        ]
    },
    {
        'text': 'What should you do before handling power connectors?',
        'domain': 'Safety & Best Practices',
        'choices': [
            ('Apply thermal paste to ensure a good connection', False),
            ('Test the connector with a multimeter first', False),
            ('Make sure your hands are completely dry — never handle power connectors with wet or damp hands', True),
            ('Wear an anti-static wrist strap only — moisture is not a concern for power connectors', False),
        ]
    },
    {
        'text': 'Why is cable management important inside a computer case?',
        'domain': 'Safety & Best Practices',
        'choices': [
            ('It makes the system look more professional for clients', False),
            ('It reduces the overall weight of the system', False),
            ('It improves airflow to keep the system cool and reduces strain on cable connections', True),
            ('It prevents data corruption by keeping cables away from storage devices', False),
        ]
    },
    {
        'text': 'What tools are recommended for organizing cables inside a computer case?',
        'domain': 'Safety & Best Practices',
        'choices': [
            ('Zip ties only — velcro can cause static buildup', False),
            ('Electrical tape to bundle cables together', False),
            ('Cable ties or velcro straps for better organization', True),
            ('Adhesive clips mounted directly to components', False),
        ]
    },
    {
        'text': 'What surface should you always work on when handling computer components?',
        'domain': 'Safety & Best Practices',
        'choices': [
            ('A carpeted floor to cushion any accidental drops', False),
            ('A glass surface to prevent static buildup', False),
            ('A clean flat surface to prevent damage and ensure components are stable', True),
            ('An elevated surface with cushioning to protect components from vibration', False),
        ]
    },
    {
        'text': 'Why is it important to ensure components are properly seated before powering the system on?',
        'domain': 'Safety & Best Practices',
        'choices': [
            ('Improperly seated components will trigger a BIOS warning only', False),
            ('The system will automatically detect and fix unseated components on first boot', False),
            ('Powering on with improperly seated components such as RAM can cause system instability or failure to boot', True),
            ('Improperly seated components will only cause issues after several hours of use', False),
        ]
    },
    {
        'text': 'What environmental conditions should be maintained when working with computer components?',
        'domain': 'Safety & Best Practices',
        'choices': [
            ('High humidity to prevent static buildup and a warm room temperature', False),
            ('Very cold temperature and low lighting to protect sensitive components', False),
            ('Optimal room temperature, low humidity to prevent condensation and corrosion, and no food or drinks nearby', True),
            ('High temperature and moderate humidity for best component flexibility during installation', False),
        ]
    },
    {
        'text': 'What can happen if you ignore cooling considerations, for example starting a system with a non-functioning fan?',
        'domain': 'Safety & Best Practices',
        'choices': [
            ('The system will automatically throttle performance to compensate', False),
            ('The BIOS will shut down the system before any damage occurs', False),
            ('The system can easily overheat and cause damage to components', True),
            ('The system will run normally for a short period before displaying a warning message', False),
        ]
    },
    {
        'text': 'What is a common mistake people make when components do not seem to fit during installation?',
        'domain': 'Safety & Best Practices',
        'choices': [
            ('Using the wrong anti-static mat', False),
            ('Not reading the component manual before installation', False),
            ('Forcing parts into place which can cause damage especially to pins and connectors', True),
            ('Installing components without first checking cable management', False),
        ]
    },
    {
        'text': 'What does double-checking component orientation before insertion help prevent?',
        'domain': 'Safety & Best Practices',
        'choices': [
            ('ESD damage from improper grounding', False),
            ('Overheating during the first boot', False),
            ('Forcing a component in the wrong direction which can damage pins, connectors, or the component itself', True),
            ('Driver conflicts after the operating system loads', False),
        ]
    },
    {
        'text': 'What is a good organizational practice when working with computer components and screws?',
        'domain': 'Safety & Best Practices',
        'choices': [
            ('Place all screws in a single pile near the workspace for easy access', False),
            ('Tape screws directly to the component they came from', False),
            ('Keep spare screws and small components in labeled containers for optimal organization', True),
            ('Store all screws in the anti-static bag with the components', False),
        ]
    },
    {
        'text': 'According to the material, how delicate are computer components really?',
        'domain': 'Safety & Best Practices',
        'choices': [
            ('Extremely delicate — even gentle handling can cause microscopic damage', False),
            ('Very delicate — always use tools and never handle with bare hands', False),
            ('Not as delicate as people might think — they can be handled and manipulated normally as long as you exercise a reasonable level of extra caution', True),
            ('Completely robust — no special handling precautions are needed for modern components', False),
        ]
    },
    # ── Laptops - Hardware ────────────────────────────────────────────────────
    {
        'text': 'What is the ONE hardware component found in laptops that is NOT found in desktop computers?',
        'domain': 'Laptops',
        'choices': [
            ('CPU', False),
            ('Motherboard', False),
            ('Battery', True),
            ('Cooling system', False),
        ]
    },
    {
        'text': 'What does SODIMM stand for?',
        'domain': 'Laptops',
        'choices': [
            ('Standard Output Dual In-line Memory Module', False),
            ('Small Outline Dynamic Integrated Memory Module', False),
            ('Small Outline Dual In-line Memory Module', True),
            ('System Optimized Dual Integrated Memory Module', False),
        ]
    },
    {
        'text': 'What is the advantage of dual-channel RAM over single-channel RAM?',
        'domain': 'Laptops',
        'choices': [
            ('It doubles the total amount of RAM available', False),
            ('It reduces heat output from the memory chips', False),
            ('It provides two channels of communication to the processor, offering better performance', True),
            ('It allows RAM to be soldered directly onto the motherboard', False),
        ]
    },
    {
        'text': 'Why are SSDs more reliable than HDDs specifically in laptops?',
        'domain': 'Laptops',
        'choices': [
            ('SSDs are cheaper to manufacture', False),
            ('SSDs have a longer warranty period', False),
            ('SSDs have no moving parts, making them less susceptible to damage from being bumped around', True),
            ('SSDs consume more power which stabilizes performance', False),
        ]
    },
    {
        'text': 'Which display technology offers the best contrast and deepest blacks but is the most expensive?',
        'domain': 'Laptops',
        'choices': [
            ('LCD (Liquid Crystal Display)', False),
            ('IPS (In-Plane Switching)', False),
            ('OLED (Organic Light-Emitting Diode)', True),
            ('TFT (Thin Film Transistor)', False),
        ]
    },
    {
        'text': 'What is the key difference between an integrated GPU and a dedicated GPU in a laptop?',
        'domain': 'Laptops',
        'choices': [
            ('Integrated GPUs are always faster than dedicated GPUs', False),
            ('Dedicated GPUs are built into the CPU to save space', False),
            ('Integrated GPUs are built into the CPU, while dedicated GPUs are separate and used solely for graphics', True),
            ('Integrated GPUs are only found in gaming laptops', False),
        ]
    },
    {
        'text': 'What unit is laptop battery capacity typically measured in?',
        'domain': 'Laptops',
        'choices': [
            ('Milliamps (mA)', False),
            ('Volts (V)', False),
            ('Watt-hours (Wh)', True),
            ('Gigahertz (GHz)', False),
        ]
    },
    {
        'text': 'What are the two most common laptop battery types?',
        'domain': 'Laptops',
        'choices': [
            ('Nickel-cadmium and Nickel-metal hydride', False),
            ('Lithium-ion and Lithium polymer', True),
            ('Lithium-ion and Nickel-cadmium', False),
            ('Alkaline and Lithium polymer', False),
        ]
    },
    {
        'text': 'To maximize laptop battery lifespan, what charge level range should you try to keep it between?',
        'domain': 'Laptops',
        'choices': [
            ('0% and 100%', False),
            ('10% and 90%', False),
            ('20% and 80%', True),
            ('50% and 100%', False),
        ]
    },
    {
        'text': 'What is the RJ45 port on a laptop used for?',
        'domain': 'Laptops',
        'choices': [
            ('Connecting an external monitor', False),
            ('Connecting USB peripherals', False),
            ('Connecting an Ethernet cable for wired network access', True),
            ('Connecting audio devices', False),
        ]
    },
    {
        'text': 'Thunderbolt 3 and 4 connectors look identical to which other port type?',
        'domain': 'Laptops',
        'choices': [
            ('HDMI', False),
            ('DisplayPort', False),
            ('USB-C', True),
            ('RJ45', False),
        ]
    },
    {
        'text': 'What are the Wi-Fi standards that most modern laptops support?',
        'domain': 'Laptops',
        'choices': [
            ('Wi-Fi 4 (802.11n) and Wi-Fi 5 (802.11ac)', False),
            ('Wi-Fi 5 (802.11ac) and Wi-Fi 6 (802.11ax)', True),
            ('Wi-Fi 3 (802.11g) and Wi-Fi 4 (802.11n)', False),
            ('Wi-Fi 6 (802.11ax) and Wi-Fi 7 (802.11be)', False),
        ]
    },
    {
        'text': 'What is a passive cooling solution in a laptop?',
        'domain': 'Laptops',
        'choices': [
            ('A high-speed fan built into the CPU', False),
            ('A liquid cooling loop circulating through the chassis', False),
            ('Heat sinks or radiators that dissipate heat without using fans', True),
            ('A cooling pad connected via USB', False),
        ]
    },
    {
        'text': 'What is the most common cause of laptop overheating?',
        'domain': 'Laptops',
        'choices': [
            ('Running the laptop on battery instead of plugged in', False),
            ('Using dual-channel RAM', False),
            ('Dust accumulating on the vents blocking heat from escaping', True),
            ('Having a dedicated GPU installed', False),
        ]
    },
    {
        'text': 'Which of the following is the BEST recommended method to clean a laptop\'s vents for thermal maintenance?',
        'domain': 'Laptops',
        'choices': [
            ('Wiping the vents with a damp cloth', False),
            ('Using a hairdryer on low heat', False),
            ('Using compressed air or carefully vacuuming the vents', True),
            ('Disassembling the laptop and washing the fan blades', False),
        ]
    },
    {
        'text': 'IPS displays are preferred over standard LCD for which reason?',
        'domain': 'Laptops',
        'choices': [
            ('They are cheaper to produce', False),
            ('They consume less battery power', False),
            ('They offer better viewing angles and color accuracy', True),
            ('They are thinner and lighter', False),
        ]
    },
    {
        'text': 'A laptop CPU is sometimes soldered directly onto the motherboard. What does this mean for the user?',
        'domain': 'Laptops',
        'choices': [
            ('It improves cooling efficiency significantly', False),
            ('It allows for easier upgrades in the future', False),
            ('The CPU cannot be upgraded or replaced', True),
            ('It increases the clock speed of the processor', False),
        ]
    },
    {
        'text': 'Which of the following actions will help preserve laptop battery life?',
        'domain': 'Laptops',
        'choices': [
            ('Always charge the battery to 100% before use', False),
            ('Keep screen brightness at maximum for better visibility', False),
            ('Reduce screen brightness, disable unused hardware, and use power management settings', True),
            ('Keep all background applications running to avoid restart delays', False),
        ]
    },
    # ── Digitizer / Touchscreen ───────────────────────────────────────────────
    {
        'text': 'What is the primary function of a digitizer in a touchscreen device?',
        'domain': 'Mobile Devices',
        'choices': [
            ('It powers the backlight of the display', False),
            ('It controls the refresh rate of the screen', False),
            ('It converts analog touches or pen input into digital signals', True),
            ('It manages the color accuracy of the display panel', False),
        ]
    },
    {
        'text': 'In which of the following devices would you find a digitizer?',
        'domain': 'Mobile Devices',
        'choices': [
            ('Only in smartphones and tablets', False),
            ('Only in professional drawing tablets', False),
            ('In any device with a touchscreen, drawing tablets, and stylus-supported devices', True),
            ('Only in laptops with dedicated GPUs', False),
        ]
    },
    {
        'text': 'What are the three primary types of touchscreens?',
        'domain': 'Mobile Devices',
        'choices': [
            ('LCD, IPS, and OLED', False),
            ('Active, Passive, and EMR', False),
            ('Capacitive, Resistive, and Infrared/Surface Acoustic Wave (SAW)', True),
            ('Unidirectional, Omnidirectional, and Beamforming', False),
        ]
    },
    {
        'text': 'What type of touchscreen is most commonly found in modern smartphones, tablets, and premium laptops?',
        'domain': 'Mobile Devices',
        'choices': [
            ('Resistive touchscreen', False),
            ('Infrared touchscreen', False),
            ('Capacitive touchscreen', True),
            ('Surface Acoustic Wave (SAW) touchscreen', False),
        ]
    },
    {
        'text': 'How does a capacitive touchscreen detect input?',
        'domain': 'Mobile Devices',
        'choices': [
            ('It detects physical pressure applied to multiple layers', False),
            ('It uses infrared beams across the screen surface', False),
            ('It uses a layer of conductive material that reacts to touch', True),
            ('It uses electromagnetic resonance to detect finger position', False),
        ]
    },
    {
        'text': 'What is multi-touch input and which touchscreen type supports it?',
        'domain': 'Mobile Devices',
        'choices': [
            ('The ability to use any object to touch the screen — supported by resistive screens', False),
            ('The ability to touch the screen with gloves on — supported by SAW screens', False),
            ('The ability to register multiple simultaneous points of input such as pinch-to-zoom — supported by capacitive screens', True),
            ('The ability to use a stylus and finger at the same time — supported by resistive screens', False),
        ]
    },
    {
        'text': 'Which touchscreen type only supports single-touch input?',
        'domain': 'Mobile Devices',
        'choices': [
            ('Capacitive touchscreen', False),
            ('Infrared touchscreen', False),
            ('Resistive touchscreen', True),
            ('Surface Acoustic Wave touchscreen', False),
        ]
    },
    {
        'text': 'Why are resistive touchscreens commonly used in outdoor ATMs and industrial equipment?',
        'domain': 'Mobile Devices',
        'choices': [
            ('They support multi-touch gestures better than capacitive screens', False),
            ('They are more accurate and responsive than capacitive screens', False),
            ('They work with any object including gloved hands and are more durable against dust, moisture, and temperature fluctuations', True),
            ('They are newer technology and therefore more reliable', False),
        ]
    },
    {
        'text': 'Which touchscreen type is more cost effective and why?',
        'domain': 'Mobile Devices',
        'choices': [
            ('Capacitive, because it uses simpler conductive material', False),
            ('Infrared, because it requires no physical screen layers', False),
            ('Resistive, because it is an older technology that is cheaper to manufacture', True),
            ('SAW, because it requires no internal electronics', False),
        ]
    },
    {
        'text': 'What type of stylus contains internal electronics and supports pressure sensitivity, commonly used in digital art?',
        'domain': 'Mobile Devices',
        'choices': [
            ('Passive stylus', False),
            ('EMR stylus', False),
            ('Active stylus', True),
            ('Capacitive stylus', False),
        ]
    },
    {
        'text': 'What is a passive stylus and what is it typically used for?',
        'domain': 'Mobile Devices',
        'choices': [
            ('A stylus with pressure sensitivity used for professional drawing', False),
            ('A stylus that uses electromagnetic resonance for precision input', False),
            ('A stylus that functions like a finger touch with no pressure sensitivity, typically used for general navigation', True),
            ('A stylus that works exclusively with resistive touchscreens', False),
        ]
    },
    {
        'text': 'What does EMR stand for in relation to styluses?',
        'domain': 'Mobile Devices',
        'choices': [
            ('Extended Memory Response', False),
            ('Electronic Motion Recognition', False),
            ('Electromagnetic Resonance', True),
            ('Enhanced Micro Resolution', False),
        ]
    },
    {
        'text': 'What type of stylus is used in professional graphics tablets for enhanced accuracy?',
        'domain': 'Mobile Devices',
        'choices': [
            ('Active stylus', False),
            ('Passive stylus', False),
            ('EMR (Electromagnetic Resonance) stylus', True),
            ('Capacitive stylus', False),
        ]
    },
    {
        'text': 'What is the first recommended step when a touchscreen becomes unresponsive?',
        'domain': 'Mobile Devices',
        'choices': [
            ('Replace the digitizer immediately', False),
            ('Perform a full factory reset', False),
            ('Restart the device, clean the surface, update drivers, or recalibrate the touch settings', True),
            ('Disable and re-enable the touchscreen in device manager', False),
        ]
    },
    {
        'text': 'What are ghost touches on a touchscreen?',
        'domain': 'Mobile Devices',
        'choices': [
            ('A delay in screen response caused by outdated drivers', False),
            ('Dead pixels that appear as dark spots on the display', False),
            ('Screen reactions that occur when there is no actual touch, caused by screen damage or software issues', True),
            ('Incorrect color rendering caused by a faulty digitizer', False),
        ]
    },
    {
        'text': 'What should you check first if a stylus is not being recognized by the device?',
        'domain': 'Mobile Devices',
        'choices': [
            ('Replace the stylus immediately as it has likely failed', False),
            ('Recalibrate the touchscreen settings', False),
            ('Check the battery of the stylus, update the firmware, and verify driver installations', True),
            ('Perform a factory reset of the device', False),
        ]
    },
    {
        'text': 'What are possible causes of a delayed touchscreen response?',
        'domain': 'Mobile Devices',
        'choices': [
            ('Screen brightness set too high and low battery', False),
            ('Incorrect screen resolution and outdated display panel', False),
            ('Overheating, insufficient memory, software conflicts, or driver issues', True),
            ('Physical damage to the screen and a failing GPU', False),
        ]
    },
    {
        'text': 'Which touchscreen type would work best in an environment where the user may be wearing gloves?',
        'domain': 'Mobile Devices',
        'choices': [
            ('Capacitive touchscreen', False),
            ('Active digitizer panel', False),
            ('Resistive touchscreen', True),
            ('Infrared touchscreen', False),
        ]
    },
    {
        'text': 'What feature of capacitive touchscreens makes handwriting recognition possible?',
        'domain': 'Mobile Devices',
        'choices': [
            ('The ability to detect pressure levels from the finger', False),
            ('The use of electromagnetic resonance technology', False),
            ('Enhanced sensitivity that can detect fine and precise touch input', True),
            ('The multi-layer physical construction of the screen', False),
        ]
    },
    {
        'text': 'Which of the following best describes a Surface Acoustic Wave (SAW) touchscreen?',
        'domain': 'Mobile Devices',
        'choices': [
            ('The most common type found in all modern smartphones and laptops', False),
            ('A pressure-based screen used in older industrial devices', False),
            ('A specialized touchscreen type used for more specific applications alongside infrared touchscreens', True),
            ('A touchscreen that uses conductive material and supports multi-touch gestures', False),
        ]
    },
    # ── Motherboard / Hardware ────────────────────────────────────────────────
    {
        'text': 'What is the primary function of the motherboard?',
        'domain': 'Hardware',
        'choices': [
            ('Store data permanently', False),
            ('Execute software instructions', False),
            ('Facilitate communication between all system components', True),
            ('Convert electrical power for components', False),
        ]
    },
    {
        'text': 'Which motherboard form factor is NOT a real standard?',
        'domain': 'Hardware',
        'choices': [
            ('ATX', False),
            ('MicroATX', False),
            ('Mini-ITX', False),
            ('FlexATX Pro', True),
        ]
    },
    {
        'text': 'What does PCIe stand for?',
        'domain': 'Hardware',
        'choices': [
            ('Peripheral Component Interface Extended', False),
            ('Peripheral Component Interconnect eXtended', True),
            ('Processor Core Interface eXtended', False),
            ('Printed Circuit Interconnect Extended', False),
        ]
    },
    {
        'text': 'What does 1 GHz represent?',
        'domain': 'Hardware',
        'choices': [
            ('1 million cycles per second', False),
            ('1 billion bytes per second', False),
            ('1 billion cycles per second', True),
            ('1 million instructions per second', False),
        ]
    },
    {
        'text': 'What is cache memory in a CPU?',
        'domain': 'Hardware',
        'choices': [
            ('A type of long-term storage built into the processor', False),
            ('Small built-in memory that temporarily holds values during processing', True),
            ('Another name for RAM', False),
            ('The memory used to store the OS', False),
        ]
    },
    {
        'text': 'Why is RAM described as "volatile"?',
        'domain': 'Hardware',
        'choices': [
            ('It can overheat easily', False),
            ('Its data is erased when the computer loses power', True),
            ('It causes system instability', False),
            ('It degrades over time', False),
        ]
    },
    {
        'text': 'SODIMM RAM modules are specifically designed for:',
        'domain': 'Hardware',
        'choices': [
            ('Servers requiring ECC memory', False),
            ('Desktop workstations', False),
            ('Laptops, due to their smaller physical size', True),
            ('High-performance gaming PCs', False),
        ]
    },
    {
        'text': 'What is the main reason an HDD is slower than an SSD?',
        'domain': 'Hardware',
        'choices': [
            ('HDDs use older memory technology', False),
            ('HDDs have a spinning magnetic disk that must physically rotate to the correct location', True),
            ('HDDs connect via a slower USB interface', False),
            ('HDDs lack cache memory', False),
        ]
    },
    {
        'text': 'Which storage technology connects directly to the motherboard using the NVMe protocol for the highest speeds?',
        'domain': 'Hardware',
        'choices': [
            ('HDD (Hard Disk Drive)', False),
            ('SATA SSD', False),
            ('NVMe SSD', True),
            ('SODIMM', False),
        ]
    },
    {
        'text': 'A company needs to archive huge amounts of data that is rarely accessed. Best choice?',
        'domain': 'Hardware',
        'choices': [
            ('NVMe SSD for maximum speed', False),
            ('HDD for high capacity at lower cost per GB', True),
            ('SSD for durability', False),
            ('External USB RAM drives', False),
        ]
    },
    {
        'text': 'What does the Power Supply Unit (PSU) do?',
        'domain': 'Hardware',
        'choices': [
            ('Stores backup power for the system', False),
            ('Converts wall outlet power to usable voltage levels for components', True),
            ('Distributes RAM across the motherboard', False),
            ('Regulates CPU clock speed', False),
        ]
    },
    {
        'text': 'What is the purpose of thermal paste applied to a CPU?',
        'domain': 'Hardware',
        'choices': [
            ('It acts as an electrical conductor between CPU and RAM', False),
            ('It lubricates the CPU fan bearings', False),
            ('It improves heat transfer from the CPU to the cooler by ensuring better contact', True),
            ('It is a protective coating against moisture', False),
        ]
    },
    {
        'text': 'Adding more RAM to a system primarily does which of the following?',
        'domain': 'Hardware',
        'choices': [
            ('Directly increases CPU clock speed', False),
            ('Increases the GPU\'s rendering power', False),
            ('Allows the system to run at its maximum potential by preventing slowdowns from insufficient workspace', True),
            ('Increases storage read speeds', False),
        ]
    },
    {
        'text': 'Which of the following is an INPUT device?',
        'domain': 'Hardware',
        'choices': [
            ('Monitor', False),
            ('Printer', False),
            ('Keyboard', True),
            ('External hard drive', False),
        ]
    },
    {
        'text': 'A video editor wants to upgrade their GPU. What expansion slot would it use?',
        'domain': 'Hardware',
        'choices': [
            ('DIMM slot', False),
            ('SATA port', False),
            ('PCIe slot', True),
            ('NVMe M.2 slot', False),
        ]
    },
    # ── Docking Stations ──────────────────────────────────────────────────────
    {
        'text': 'What is the primary purpose of both a docking station and a port replicator?',
        'domain': 'Laptops',
        'choices': [
            ('To increase the processing speed of a laptop', False),
            ('To replace the laptop battery with a more powerful one', False),
            ('To extend the functionality and port availability of a laptop', True),
            ('To allow a laptop to run desktop operating systems', False),
        ]
    },
    {
        'text': 'What is the main difference between a docking station and a port replicator?',
        'domain': 'Laptops',
        'choices': [
            ('A docking station is portable while a port replicator stays on the desk', False),
            ('A port replicator provides power delivery while a docking station only adds ports', False),
            ('A docking station provides additional ports, power delivery, and extended functionality, while a port replicator is a simplified version that primarily just adds more ports', True),
            ('A docking station connects via USB while a port replicator mounts the laptop directly', False),
        ]
    },
    {
        'text': 'Why do laptops benefit from docking stations and port replicators?',
        'domain': 'Laptops',
        'choices': [
            ('Laptops run faster when connected to a docking station', False),
            ('Laptops cannot connect to external monitors without a docking station', False),
            ('Laptops sacrifice ports to remain compact and portable, so docking stations and port replicators restore that expanded connectivity', True),
            ('Laptops require docking stations to charge their batteries properly', False),
        ]
    },
    {
        'text': 'How does a port replicator typically connect to a laptop?',
        'domain': 'Laptops',
        'choices': [
            ('It mounts directly onto a proprietary connector on the laptop base', False),
            ('It connects via a Thunderbolt 4 cable only', False),
            ('It connects over a single USB connection', True),
            ('It connects via a proprietary docking connector specific to the laptop brand', False),
        ]
    },
    {
        'text': 'How does a docking station typically connect to a laptop?',
        'domain': 'Laptops',
        'choices': [
            ('Via a single USB cable connection', False),
            ('Via a Bluetooth wireless connection', False),
            ('The laptop is physically mounted directly into the docking station, usually via a proprietary connector', True),
            ('Via an HDMI cable connection', False),
        ]
    },
    {
        'text': 'Why do docking stations typically need to be proprietary?',
        'domain': 'Laptops',
        'choices': [
            ('Proprietary docking stations are cheaper to manufacture', False),
            ('Generic docking stations do not support USB connections', False),
            ('They connect directly to the laptop via a specific connector that is unique to the make and model of the laptop', True),
            ('Proprietary docking stations offer better wireless connectivity', False),
        ]
    },
    {
        'text': 'Which of the following is a key feature found on most docking stations?',
        'domain': 'Laptops',
        'choices': [
            ('Built-in SSD storage for additional capacity', False),
            ('A dedicated GPU for enhanced graphics performance', False),
            ('Multiple USB ports, video outputs, physical Ethernet connectivity, audio ports, and additional power delivery', True),
            ('A built-in cooling fan to keep the laptop temperature down', False),
        ]
    },
    {
        'text': 'What is one advantage a port replicator has over a docking station?',
        'domain': 'Laptops',
        'choices': [
            ('Port replicators support more devices than docking stations', False),
            ('Port replicators provide better power delivery than docking stations', False),
            ('Port replicators are smaller, lighter, easier to carry, and better suited for travel', True),
            ('Port replicators are always compatible with any laptop regardless of brand', False),
        ]
    },
    {
        'text': 'Can a port replicator be used with a desktop computer?',
        'domain': 'Laptops',
        'choices': [
            ('No, port replicators only work with laptops', False),
            ('No, desktop computers use a different USB standard', False),
            ('Yes, because a port replicator connects via a single USB connection and functions as a peripheral device', True),
            ('Yes, but only if the desktop has a Thunderbolt port', False),
        ]
    },
    {
        'text': 'Is there such a thing as a docking station for a desktop computer?',
        'domain': 'Laptops',
        'choices': [
            ('Yes, all desktop computers support proprietary docking stations', False),
            ('Yes, but only for high-performance workstations', False),
            ('No, docking stations are designed for laptops, and desktop systems already support far more ports natively', True),
            ('Yes, desktop docking stations are used to add extra USB ports', False),
        ]
    },
    {
        'text': 'What is a key productivity benefit of using a port replicator or docking station?',
        'domain': 'Laptops',
        'choices': [
            ('It speeds up the laptop CPU when connected', False),
            ('It automatically backs up data to an external drive', False),
            ('All peripherals remain permanently connected so you only need to connect or disconnect a single cable when using or removing the laptop', True),
            ('It allows multiple users to share the same laptop simultaneously', False),
        ]
    },
    {
        'text': 'Does connecting a device through a port replicator slow down data transfer speeds compared to connecting directly to the laptop?',
        'domain': 'Laptops',
        'choices': [
            ('Yes, all data is slowed by about 50% through a port replicator', False),
            ('Yes, but only for USB 2.0 devices', False),
            ('No, you get the same performance whether connected through the port replicator or directly to the laptop', True),
            ('Yes, but only for video output connections', False),
        ]
    },
    {
        'text': 'What is the first thing to check if a device connected to a docking station or port replicator is not being recognized?',
        'domain': 'Laptops',
        'choices': [
            ('Reinstall the operating system', False),
            ('Replace the docking station immediately', False),
            ('Check the physical connection and ensure the device has adequate power, then check for driver updates and firmware compatibility', True),
            ('Disable and re-enable the USB controller in device manager', False),
        ]
    },
    {
        'text': 'A user has an external monitor connected to their docking station but is getting no video output. What should they check?',
        'domain': 'Laptops',
        'choices': [
            ('Whether the docking station has enough USB ports available', False),
            ('Whether the Ethernet cable is properly connected', False),
            ('The cable connections and the laptop display settings to ensure the system is configured to send a video signal to the external monitor', True),
            ('Whether the laptop battery is fully charged', False),
        ]
    },
    {
        'text': 'What is the Windows keyboard shortcut to quickly access display output settings?',
        'domain': 'Laptops',
        'choices': [
            ('Windows key + D', False),
            ('Windows key + M', False),
            ('Windows key + P', True),
            ('Windows key + E', False),
        ]
    },
    {
        'text': 'A user connects their laptop to a docking station with an Ethernet cable but has no network connection. What is a likely cause?',
        'domain': 'Laptops',
        'choices': [
            ('The docking station does not support wired Ethernet', False),
            ('The Ethernet cable is the wrong category', False),
            ('The Ethernet network interface may be disabled in the network settings, especially if the laptop was previously using Wi-Fi', True),
            ('The laptop firewall is blocking the wired connection', False),
        ]
    },
    {
        'text': 'Which type of professional would most benefit from a docking station versus a port replicator?',
        'domain': 'Laptops',
        'choices': [
            ('A traveling sales professional who needs extra ports on the go', False),
            ('A student who occasionally needs an extra USB port', False),
            ('An office-based professional who needs multiple monitors, wired Ethernet, and multiple peripherals permanently set up at a workstation', True),
            ('A gamer who needs extra audio ports for a headset', False),
        ]
    },
    {
        'text': 'What should you try if a USB device works when connected directly to the laptop but not through the docking station or port replicator?',
        'domain': 'Laptops',
        'choices': [
            ('Replace the USB device as it is incompatible with docking stations', False),
            ('Update the laptop BIOS immediately', False),
            ('Verify that the docking station or port replicator is providing adequate power to the USB device', True),
            ('Disable the built-in USB ports on the laptop', False),
        ]
    },
    {
        'text': 'Which of the following best describes when a port replicator would be the better choice over a docking station?',
        'domain': 'Laptops',
        'choices': [
            ('When the user needs maximum power delivery for multiple external hard drives', False),
            ('When the user needs to run three or more external monitors simultaneously', False),
            ('When the user needs a portable, affordable solution for extra ports and basic connectivity while traveling', True),
            ('When the user needs a proprietary high-speed connection for professional video editing', False),
        ]
    },
    {
        'text': 'What happens to all the peripherals connected to a docking station when the user undocks their laptop to travel?',
        'domain': 'Laptops',
        'choices': [
            ('They all disconnect and must be manually reconnected on return', False),
            ('They power down and lose their configuration settings', False),
            ('They all stay connected to the docking station and remain set up, ready for when the laptop is docked again', True),
            ('They switch to wireless mode automatically until the laptop returns', False),
        ]
    },
    # ── Hardware Cleaning ─────────────────────────────────────────────────────
    {
        'text': 'What is the primary reason for regularly cleaning computer hardware components?',
        'domain': 'Maintenance',
        'choices': [
            ('To improve the aesthetic appearance of the system', False),
            ('To allow for easier component upgrades in the future', False),
            ('To prevent overheating by improving airflow and reducing dust buildup which also reduces the risk of component failure', True),
            ('To maintain the warranty on computer components', False),
        ]
    },
    {
        'text': 'What concentration of isopropyl alcohol is recommended for cleaning computer components and why?',
        'domain': 'Maintenance',
        'choices': [
            ('50% because it is gentle enough not to damage components', False),
            ('70% because it is the most commonly available concentration', False),
            ('90% or higher because it evaporates very quickly and does not leave moisture on components', True),
            ('100% because it provides the strongest cleaning power', False),
        ]
    },
    {
        'text': 'What is the purpose of using an anti-static brush when cleaning components?',
        'domain': 'Maintenance',
        'choices': [
            ('It removes thermal paste more effectively than a cloth', False),
            ('It generates a small static charge that attracts dust particles', False),
            ('It allows you to brush components without generating static electricity that could damage them', True),
            ('It is softer than a microfiber cloth and less likely to scratch components', False),
        ]
    },
    {
        'text': 'What is the advantage of a microfiber cloth over a regular cloth for cleaning?',
        'domain': 'Maintenance',
        'choices': [
            ('Microfiber cloths are pre-treated with isopropyl alcohol', False),
            ('Microfiber cloths are anti-static and can be used inside the case', False),
            ('Microfiber cloths do not leave dust or lint behind after cleaning', True),
            ('Microfiber cloths are safe to use on internal components with the power on', False),
        ]
    },
    {
        'text': 'What is the best practice when using compressed air to blow dust out of internal components?',
        'domain': 'Maintenance',
        'choices': [
            ('Use compressed air alone and let the dust settle naturally', False),
            ('Always use compressed air from at least 3 feet away to prevent damage', False),
            ('Have a vacuum cleaner nearby to capture the dust as it is removed rather than blowing it into the room', True),
            ('Only use compressed air on external components — never use it internally', False),
        ]
    },
    {
        'text': 'What tool should you use to clean RAM modules and their slots?',
        'domain': 'Maintenance',
        'choices': [
            ('Compressed air at high pressure to dislodge dust', False),
            ('Isopropyl alcohol applied directly with a cotton swab', False),
            ('An anti-static brush to gently clear any dust without generating static', True),
            ('A microfiber cloth dampened with distilled water', False),
        ]
    },
    {
        'text': 'Why must you be extremely careful when cleaning inside a power supply unit?',
        'domain': 'Maintenance',
        'choices': [
            ('The internal fans can spin up suddenly and cause injury', False),
            ('The power supply contains liquid cooling components that can spill', False),
            ('Internal copper coils can store a significant electrical charge even when the unit is unplugged and must not be touched with anything conductive', True),
            ('The power supply casing is made of a material that generates static when touched', False),
        ]
    },
    {
        'text': 'What type of nozzle or attachment should be used when applying compressed air or a vacuum near power supply coils?',
        'domain': 'Maintenance',
        'choices': [
            ('A metal nozzle for maximum precision', False),
            ('A rubber nozzle to create a tight seal', False),
            ('A plastic nozzle or attachment to avoid conducting any stored electrical charge', True),
            ('No nozzle — direct airflow is safest near coils', False),
        ]
    },
    {
        'text': 'What is the correct process for replacing thermal paste on a CPU?',
        'domain': 'Maintenance',
        'choices': [
            ('Apply new thermal paste directly on top of the old paste without removing it', False),
            ('Use a dry cloth to wipe off the old paste then apply new paste immediately', False),
            ('Remove old thermal paste with isopropyl alcohol and a lint-free cloth, apply a pea-sized amount of new paste, then secure the cooler evenly to spread it', True),
            ('Apply a thick layer of thermal paste to ensure maximum coverage between the CPU and cooler', False),
        ]
    },
    {
        'text': 'How much thermal paste should be applied to the CPU?',
        'domain': 'Maintenance',
        'choices': [
            ('A thin layer covering the entire CPU surface', False),
            ('A large amount to ensure full coverage', False),
            ('A pea-sized amount placed onto the CPU', True),
            ('Two small dots on opposite corners of the CPU', False),
        ]
    },
    {
        'text': 'After applying new thermal paste and reattaching the cooler, how can you verify the paste was applied correctly?',
        'domain': 'Maintenance',
        'choices': [
            ('Visually inspect the paste spreading out from under the cooler edges', False),
            ('Run a gaming benchmark for 30 minutes and check for crashes', False),
            ('Monitor the CPU temperatures in the BIOS or UEFI utilities to ensure they are within normal range', True),
            ('Check the system event log for any thermal warning messages', False),
        ]
    },
    {
        'text': 'How should you clean the exterior of a computer case and its vents?',
        'domain': 'Maintenance',
        'choices': [
            ('Use a damp cloth with warm water and mild soap', False),
            ('Use isopropyl alcohol applied directly to the case surface', False),
            ('Use a vacuum cleaner to remove dust from vents and a microfiber cloth for the exterior surfaces', True),
            ('Use compressed air only from outside the case to push dust inward', False),
        ]
    },
    {
        'text': 'What is the recommended method for cleaning laser and inkjet printers?',
        'domain': 'Maintenance',
        'choices': [
            ('Disassemble the printer completely and clean each part with isopropyl alcohol', False),
            ('Use compressed air exclusively on all internal printer components', False),
            ("Use the printer's own built-in cleaning processes for internal components like print heads, and use compressed air or isopropyl alcohol for physical parts like paper trays and feed rollers", True),
            ('Clean printers only when print quality visibly degrades', False),
        ]
    },
    {
        'text': 'How often should external computer components generally be cleaned?',
        'domain': 'Maintenance',
        'choices': [
            ('Monthly', False),
            ('Every 3 to 6 months', True),
            ('Weekly', False),
            ('Annually', False),
        ]
    },
    {
        'text': 'How often should internal dust removal be performed on desktop systems?',
        'domain': 'Maintenance',
        'choices': [
            ('Weekly to prevent any dust accumulation', False),
            ('Annually as part of a scheduled maintenance plan', False),
            ('Every 3 to 6 months, or more frequently depending on the environment', True),
            ('Only when the system shows signs of overheating', False),
        ]
    },
    {
        'text': 'How often should thermal paste be replaced?',
        'domain': 'Maintenance',
        'choices': [
            ('Every 6 months', False),
            ('Every 5 years', False),
            ('Every 1 to 2 years', True),
            ('Only when the CPU is replaced', False),
        ]
    },
    {
        'text': 'How often should printers be checked and cleaned?',
        'domain': 'Maintenance',
        'choices': [
            ('Weekly', False),
            ('Every 3 to 6 months', True),
            ('Monthly', False),
            ('Only when print quality issues are noticed', False),
        ]
    },
    {
        'text': 'Why might a home computer with pets need to be cleaned more frequently than the standard recommendation?',
        'domain': 'Maintenance',
        'choices': [
            ('Pet owners tend to use their computers more intensively', False),
            ('Pets generate more static electricity in the home environment', False),
            ('Pet hair accumulates inside the case more quickly than regular dust, requiring more frequent cleaning', True),
            ('Pets can damage dust filters making them less effective', False),
        ]
    },
    {
        'text': 'What is the purpose of using dust filters on PC cases?',
        'domain': 'Maintenance',
        'choices': [
            ('To improve the airflow by directing it over specific components', False),
            ('To reduce the noise generated by case fans', False),
            ('To minimize the amount of dust that enters the case in the first place', True),
            ('To prevent static electricity from building up inside the case', False),
        ]
    },
    {
        'text': 'What environmental conditions should be maintained when performing cleaning and maintenance on computer systems?',
        'domain': 'Maintenance',
        'choices': [
            ('Warm and humid to prevent static buildup during cleaning', False),
            ('Bright and warm to allow better visibility of components', False),
            ('Cool and dry to prevent overheating during work and to avoid condensation on components', True),
            ('Any conditions are acceptable as long as the system is unplugged', False),
        ]
    },
    # ── Laptop Form Factors & Displays ────────────────────────────────────────
    {
        'text': 'What is the standard laptop form factor where the screen simply opens and closes on a hinge?',
        'domain': 'Laptops',
        'choices': [
            ('2-in-1 Convertible', False),
            ('Detachable Tablet', False),
            ('Clamshell laptop', True),
            ('Fold-back tablet', False),
        ]
    },
    {
        'text': 'What makes a 2-in-1 convertible laptop different from a standard clamshell laptop?',
        'domain': 'Laptops',
        'choices': [
            ('It has two separate screens', False),
            ('It uses a detachable keyboard only', False),
            ('The screen can fold all the way back so the device can be used as a tablet', True),
            ('It runs two operating systems simultaneously', False),
        ]
    },
    {
        'text': 'What is the key difference between a 2-in-1 convertible and a detachable tablet laptop?',
        'domain': 'Laptops',
        'choices': [
            ('A detachable tablet has a higher resolution screen', False),
            ('A 2-in-1 convertible always has a touchscreen, a detachable does not', False),
            ('A detachable tablet has a screen that fully separates from the primary unit, while a 2-in-1 folds back but stays attached', True),
            ('A detachable tablet cannot be used with a keyboard', False),
        ]
    },
    {
        'text': 'What display panel technology is described as using liquid crystals that twist to block the backlight when no power is applied?',
        'domain': 'Laptops',
        'choices': [
            ('IPS (In-Plane Switching)', False),
            ('OLED (Organic Light-Emitting Diode)', False),
            ('TN (Twisted Nematic)', True),
            ('QLED (Quantum Light-Emitting Diode)', False),
        ]
    },
    {
        'text': 'What are the main advantages of IPS displays over TN displays?',
        'domain': 'Laptops',
        'choices': [
            ('IPS is cheaper and has faster response times', False),
            ('IPS offers better contrast and truer blacks', False),
            ('IPS offers better color reproduction and wider viewing angles', True),
            ('IPS is more energy efficient and thinner', False),
        ]
    },
    {
        'text': 'What are the main advantages of OLED displays?',
        'domain': 'Laptops',
        'choices': [
            ('OLED is the cheapest display technology available', False),
            ('OLED has the fastest response time but poorest color accuracy', False),
            ('OLED offers the best contrast, truest blacks, and is more energy efficient', True),
            ('OLED has the widest viewing angles but lower color accuracy than IPS', False),
        ]
    },
    {
        'text': 'What is the resolution of a 720P display?',
        'domain': 'Laptops',
        'choices': [
            ('1920 x 1080 pixels', False),
            ('3840 x 2160 pixels', False),
            ('1280 x 720 pixels', True),
            ('2560 x 1440 pixels', False),
        ]
    },
    {
        'text': 'What is 1080P also commonly referred to as?',
        'domain': 'Laptops',
        'choices': [
            ('Ultra High Definition', False),
            ('Standard Definition', False),
            ('Full HD', True),
            ('Quad HD', False),
        ]
    },
    {
        'text': 'What is the resolution of a 4K display?',
        'domain': 'Laptops',
        'choices': [
            ('1920 x 1080 pixels', False),
            ('2560 x 1440 pixels', False),
            ('3840 x 2160 pixels', True),
            ('7680 x 4320 pixels', False),
        ]
    },
    {
        'text': 'How many times more pixels does a 4K display have compared to a 1080P Full HD display?',
        'domain': 'Laptops',
        'choices': [
            ('Twice as many pixels', False),
            ('Three times as many pixels', False),
            ('Four times as many pixels', True),
            ('Eight times as many pixels', False),
        ]
    },
    {
        'text': 'What is the standard refresh rate found on most general use laptops?',
        'domain': 'Laptops',
        'choices': [
            ('30Hz', False),
            ('120Hz', False),
            ('60Hz', True),
            ('144Hz', False),
        ]
    },
    {
        'text': 'Which refresh rates are better suited for gaming and motion-heavy applications?',
        'domain': 'Laptops',
        'choices': [
            ('30Hz and 60Hz', False),
            ('60Hz and 75Hz', False),
            ('120Hz and 144Hz', True),
            ('240Hz only', False),
        ]
    },
    {
        'text': 'What type of touchscreen technology is found in most modern laptops and supports multi-touch gestures like tapping and swiping?',
        'domain': 'Laptops',
        'choices': [
            ('Resistive touchscreen', False),
            ('Active digitizer panel', False),
            ('Capacitive touchscreen', True),
            ('Infrared touchscreen', False),
        ]
    },
    {
        'text': 'What type of touchscreen requires physical pressure to register input and is typically used in industrial devices?',
        'domain': 'Laptops',
        'choices': [
            ('Capacitive touchscreen', False),
            ('Active digitizer panel', False),
            ('Resistive touchscreen', True),
            ('OLED touchscreen', False),
        ]
    },
    {
        'text': 'What type of touchscreen panel is found in professional tablets and supports precision styluses for drawing and animation?',
        'domain': 'Laptops',
        'choices': [
            ('Capacitive touchscreen', False),
            ('Resistive touchscreen', False),
            ('Active digitizer panel', True),
            ('TN touch panel', False),
        ]
    },
    {
        'text': 'What is OLED screen burn-in and what causes it?',
        'domain': 'Laptops',
        'choices': [
            ('Physical cracks caused by dropping the device', False),
            ('Dead pixels caused by excessive pressure on the screen', False),
            ('Images that permanently remain on the screen caused by running high brightness for extended periods without a screensaver or sleep mode', True),
            ('Color distortion caused by a faulty display cable connection', False),
        ]
    },
    {
        'text': 'What is the recommended way to prevent OLED burn-in?',
        'domain': 'Laptops',
        'choices': [
            ('Always run the display at maximum brightness for best clarity', False),
            ('Disable the touchscreen feature when not in use', False),
            ('Adjust brightness settings and use a screensaver or sleep mode to prevent static images from burning into the screen', True),
            ('Clean the screen daily with an alcohol-based cleaner', False),
        ]
    },
    {
        'text': 'What does the P stand for in display resolutions like 720P and 1080P?',
        'domain': 'Laptops',
        'choices': [
            ('Pixels', False),
            ('Power', False),
            ('Progressive, referring to the method of drawing the screen from top to bottom', True),
            ('Performance', False),
        ]
    },
    {
        'text': 'What is the minimum resolution required to meet High Definition standards?',
        'domain': 'Laptops',
        'choices': [
            ('640 x 480 (480P)', False),
            ('1920 x 1080 (1080P)', False),
            ('1280 x 720 (720P)', True),
            ('3840 x 2160 (4K)', False),
        ]
    },
    {
        'text': 'What is the best practice for protecting a laptop display when traveling?',
        'domain': 'Laptops',
        'choices': [
            ('Remove the battery before traveling to reduce weight on the screen', False),
            ('Keep the brightness at maximum so the screen is visible if the bag is opened', False),
            ('Store the laptop in a protective case to prevent impact damage and avoid placing heavy items on top of it', True),
            ('Fold the screen back into tablet mode to reduce hinge stress during travel', False),
        ]
    },
    # ── SSD Upgrade & Management ──────────────────────────────────────────────
    {
        'text': 'When upgrading from an HDD to an SSD, what is the most important compatibility factor to check?',
        'domain': 'Storage',
        'choices': [
            ('The brand of the drive', False),
            ('The storage capacity of the new drive', False),
            ('The interface type must match between the old and new drive', True),
            ('The color and size of the drive casing', False),
        ]
    },
    {
        'text': 'Can a SATA SSD and an NVMe SSD be swapped directly for each other?',
        'domain': 'Storage',
        'choices': [
            ('Yes, they use the same physical connector', False),
            ('Yes, as long as the capacity is the same', False),
            ('No, they use different interfaces and are not directly interchangeable', True),
            ('Yes, but only in desktop systems', False),
        ]
    },
    {
        'text': 'If you need more storage capacity on a desktop system, what option do you have besides replacing the existing drive?',
        'domain': 'Storage',
        'choices': [
            ('Partition the existing drive into smaller sections', False),
            ('Upgrade the RAM to compensate for storage', False),
            ('Add an additional drive, as most desktop systems have room for multiple drives', True),
            ('Use cloud storage exclusively instead', False),
        ]
    },
    {
        'text': 'Why is adding an internal second drive unlikely on a laptop?',
        'domain': 'Storage',
        'choices': [
            ('Laptops use a different file system that prevents multiple drives', False),
            ('Laptop drives are soldered and cannot be removed', False),
            ('Laptops have very limited internal space and typically only one storage bay', True),
            ('Laptop motherboards only support one drive interface', False),
        ]
    },
    {
        'text': 'What is the recommended way to add more storage to a laptop when the internal bay is full?',
        'domain': 'Storage',
        'choices': [
            ('Replace the RAM with a hybrid RAM/storage chip', False),
            ('Upgrade to a larger NVMe drive only', False),
            ('Connect an external drive via a USB-C port', True),
            ('Install a PCIe expansion card', False),
        ]
    },
    {
        'text': 'What should you always do BEFORE physically replacing a storage drive?',
        'domain': 'Storage',
        'choices': [
            ('Update the BIOS firmware', False),
            ('Disable the TRIM command', False),
            ('Back up all existing data on the drive', True),
            ('Format the new drive before installing it', False),
        ]
    },
    {
        'text': 'What tools are typically needed to replace a drive in a desktop system?',
        'domain': 'Storage',
        'choices': [
            ('Torx screwdriver and soldering iron', False),
            ('Flathead screwdriver and thermal paste', False),
            ('Phillips screwdriver and an anti-static wrist strap', True),
            ("Jeweler's screwdrivers and a heat gun", False),
        ]
    },
    {
        'text': 'What tools are typically needed to replace a drive in a laptop?',
        'domain': 'Storage',
        'choices': [
            ('Phillips screwdriver and anti-static wrist strap', False),
            ('Power drill and flathead screwdriver', False),
            ("Jeweler's screwdrivers, which are smaller and available at hardware stores", True),
            ('Torx screwdriver and soldering iron', False),
        ]
    },
    {
        'text': 'What is the correct first step when physically replacing a storage drive?',
        'domain': 'Storage',
        'choices': [
            ('Open the case and disconnect the data cable', False),
            ('Enter the BIOS and disable the drive', False),
            ('Power down the system and unplug it entirely from the wall', True),
            ('Format the new drive before installation', False),
        ]
    },
    {
        'text': 'When installing an NVMe SSD, how does it connect to the motherboard?',
        'domain': 'Storage',
        'choices': [
            ('Via a SATA data cable and a separate power cable', False),
            ('Via a USB-C cable', False),
            ('Directly into a port on the motherboard with no cables required', True),
            ('Via a PCIe riser cable', False),
        ]
    },
    {
        'text': 'What does BIOS stand for?',
        'domain': 'Hardware',
        'choices': [
            ('Basic Integrated Operating System', False),
            ('Binary Input Output Software', False),
            ('Basic Input/Output System', True),
            ('Board Integrated OS Settings', False),
        ]
    },
    {
        'text': 'What does UEFI stand for?',
        'domain': 'Hardware',
        'choices': [
            ('Universal Extended Firmware Intelligence', False),
            ('Unified External Firmware Interface', False),
            ('Unified Extensible Firmware Interface', True),
            ('Universal Extensible File Interface', False),
        ]
    },
    {
        'text': 'What is the purpose of partitioning a new drive?',
        'domain': 'Storage',
        'choices': [
            ('It speeds up the drive by removing unused sectors', False),
            ('It applies the file system so the drive can perform read/write operations', False),
            ('It divides the drive into multiple logical sections, such as separate C, D, or E drives', True),
            ('It checks the drive for hardware errors before use', False),
        ]
    },
    {
        'text': 'What is the purpose of formatting a drive?',
        'domain': 'Storage',
        'choices': [
            ('It divides the drive into logical sections', False),
            ('It erases the drive firmware', False),
            ('It applies the file system so the drive can perform read and write operations', True),
            ('It enables the TRIM command on the drive', False),
        ]
    },
    {
        'text': 'A newly installed drive is not being detected by the system. What are possible causes?',
        'domain': 'Storage',
        'choices': [
            ('The drive capacity is too large for the system', False),
            ('The drive brand is not supported', False),
            ('A loose or missing cable connection, an incompatible drive type, or a BIOS/UEFI configuration error', True),
            ('The operating system needs to be reinstalled first', False),
        ]
    },
    {
        'text': 'What is the boot sequence and why does it matter when replacing a drive?',
        'domain': 'Storage',
        'choices': [
            ('It is the order in which the CPU processes instructions', False),
            ('It determines how fast the drive reads data on startup', False),
            ('It is the order in which the system looks for an operating system — if set incorrectly, the system may try to boot from the wrong device', True),
            ('It is the startup checklist the BIOS performs to check hardware health', False),
        ]
    },
    {
        'text': 'What is the TRIM command and what does it do?',
        'domain': 'Storage',
        'choices': [
            ('It defragments the SSD to improve read speeds', False),
            ('It monitors drive temperature and adjusts performance', False),
            ('It tells the SSD which blocks of data are no longer in use so they can be erased internally, improving performance', True),
            ('It partitions unused space on the drive automatically', False),
        ]
    },
    {
        'text': 'How do you check if TRIM is enabled on a Windows system?',
        'domain': 'Storage',
        'choices': [
            ('Open Device Manager and check drive properties', False),
            ('Run the command chkdsk /f in Command Prompt', False),
            ('Run the command fsutil behavior query DisableDeleteNotify in Command Prompt', True),
            ('Open Disk Management and check the drive status', False),
        ]
    },
    {
        'text': 'Why should defragmentation be disabled for SSDs?',
        'domain': 'Storage',
        'choices': [
            ('SSDs cannot read fragmented files at all', False),
            ('Defragmentation causes SSDs to overheat', False),
            ('SSDs do not suffer from fragmentation like HDDs do, and running defragmentation causes unnecessary reads and writes that can harm performance', True),
            ('Defragmentation will erase the partition table on an SSD', False),
        ]
    },
    {
        'text': 'What is the recommended minimum amount of free space to keep on an SSD for best performance?',
        'domain': 'Storage',
        'choices': [
            ('5%', False),
            ('50%', False),
            ('10 to 20%', True),
            ('30%', False),
        ]
    },
    # ── Integrated Peripherals ────────────────────────────────────────────────
    {
        'text': 'Which of the following are common integrated peripherals found in most modern laptops?',
        'domain': 'Laptops',
        'choices': [
            ('DVD drives, card readers, and fingerprint scanners', False),
            ('Dedicated GPU, sound card, and network card', False),
            ('Webcams, microphones, speakers, and Wi-Fi and Bluetooth modules', True),
            ('External hard drives, USB hubs, and cooling pads', False),
        ]
    },
    {
        'text': 'What is the standard frame rate for a laptop webcam?',
        'domain': 'Laptops',
        'choices': [
            ('15 frames per second', False),
            ('24 frames per second', False),
            ('30 frames per second', True),
            ('60 frames per second', False),
        ]
    },
    {
        'text': 'What is the purpose of a physical privacy shutter on a webcam?',
        'domain': 'Laptops',
        'choices': [
            ('To improve the image quality in low light conditions', False),
            ('To reduce the webcam power consumption', False),
            ('To physically cover the camera and prevent malware from using it to spy on the user', True),
            ('To protect the lens from dust when not in use', False),
        ]
    },
    {
        'text': 'What is the difference between an omnidirectional and a unidirectional microphone?',
        'domain': 'Laptops',
        'choices': [
            ('Omnidirectional microphones only work outdoors, unidirectional works indoors', False),
            ('Unidirectional microphones pick up sound from all directions, omnidirectional from one', False),
            ('Unidirectional focuses on sound from a single source for better quality, while omnidirectional picks up sound from all directions making it better for group settings', True),
            ('Omnidirectional microphones require external power, unidirectional does not', False),
        ]
    },
    {
        'text': 'What is beamforming in relation to microphones?',
        'domain': 'Laptops',
        'choices': [
            ('A noise canceling feature that removes all background sound', False),
            ('A technology that increases microphone volume automatically', False),
            ('A feature that uses multiple microphones to determine which is getting the best signal and focuses on that source', True),
            ('A feature that converts analog sound to digital format more efficiently', False),
        ]
    },
    {
        'text': 'Why do integrated laptop speakers have limited bass output?',
        'domain': 'Laptops',
        'choices': [
            ('Laptop speakers use low-quality drivers to save on cost', False),
            ('Bass frequencies require more power than laptops can supply', False),
            ('The speakers are very small and compact due to the need for lightweight portability', True),
            ('Laptop operating systems limit bass output to protect the speakers', False),
        ]
    },
    {
        'text': 'What are Dolby Atmos and DTS?',
        'domain': 'Laptops',
        'choices': [
            ('Types of microphone noise cancellation technology', False),
            ('Wi-Fi audio streaming protocols', False),
            ('Spatial audio enhancements for immersive sound, best experienced through headphones or external speakers rather than integrated laptop speakers', True),
            ('Display technologies that synchronize audio with screen refresh rates', False),
        ]
    },
    {
        'text': 'What was the purpose of a screen inverter in older laptop displays?',
        'domain': 'Laptops',
        'choices': [
            ('It converted AC power to DC for the LED backlight', False),
            ('It regulated the refresh rate of the LCD panel', False),
            ('It converted DC power to AC to power the cold cathode fluorescent lamp backlight in older LCD displays', True),
            ('It controlled the color accuracy of the TN display panel', False),
        ]
    },
    {
        'text': 'Why do modern LED-backlit displays no longer require an inverter?',
        'domain': 'Laptops',
        'choices': [
            ('LED displays do not have a backlight', False),
            ('LED displays use AC power directly from the wall', False),
            ('LED displays use direct DC power and therefore do not need the DC to AC conversion that inverters provided', True),
            ('LED displays have the inverter built directly into the display panel', False),
        ]
    },
    {
        'text': 'What is one benefit of upgrading from an older LCD display with an inverter to a modern LED display?',
        'domain': 'Laptops',
        'choices': [
            ('LED displays support higher resolutions automatically', False),
            ('LED displays are always touchscreen compatible', False),
            ('Improved power efficiency and reduced flickering issues', True),
            ('LED displays have built-in privacy shutters', False),
        ]
    },
    {
        'text': 'Which wireless antenna types are typically built into a modern laptop?',
        'domain': 'Laptops',
        'choices': [
            ('Only Wi-Fi antenna', False),
            ('Wi-Fi, Bluetooth, and always cellular/LTE', False),
            ('Wi-Fi and Bluetooth antennas, with cellular/LTE and 5G typically found in tablets or available as an add-on', True),
            ('Bluetooth and cellular antennas only', False),
        ]
    },
    {
        'text': 'What frequency band does a standard microwave oven operate on that can interfere with Wi-Fi?',
        'domain': 'Laptops',
        'choices': [
            ('5 GHz', False),
            ('900 MHz', False),
            ('2.4 GHz', True),
            ('60 GHz', False),
        ]
    },
    {
        'text': 'Why is the 5 GHz Wi-Fi band less susceptible to interference than the 2.4 GHz band?',
        'domain': 'Laptops',
        'choices': [
            ('5 GHz has a longer range so it avoids obstacles better', False),
            ('5 GHz is a newer standard that all modern devices support', False),
            ('Fewer devices operate on the 5 GHz band so there are less sources of interference', True),
            ('5 GHz signals are stronger and can overpower interference', False),
        ]
    },
    {
        'text': 'What should you check first if the laptop webcam is not being detected by the system?',
        'domain': 'Laptops',
        'choices': [
            ('Replace the webcam immediately as it has likely failed', False),
            ('Check if the privacy shutter is closed', False),
            ('Check the drivers and enable or reconfigure the camera settings', True),
            ('Perform a full factory reset of the operating system', False),
        ]
    },
    {
        'text': 'What should you check if the built-in microphone does not appear to be working?',
        'domain': 'Laptops',
        'choices': [
            ('Replace the microphone module immediately', False),
            ('Check if beamforming is disabled in the settings', False),
            ('Adjust the input levels or reinstall the drivers, and check if there is a volume adjustment on the device that may have been accidentally set too low', True),
            ('Check if the webcam privacy shutter is interfering with the microphone', False),
        ]
    },
    {
        'text': 'What is the most common reason for a weak Wi-Fi signal on a laptop?',
        'domain': 'Laptops',
        'choices': [
            ('The Wi-Fi antenna drivers are outdated', False),
            ('The 5 GHz band is overloaded with devices', False),
            ('The laptop is too far from the Wi-Fi router', True),
            ('The Bluetooth antenna is causing interference with the Wi-Fi antenna', False),
        ]
    },
    {
        'text': 'What is the best practice regarding application permissions for integrated peripherals like cameras and microphones?',
        'domain': 'Laptops',
        'choices': [
            ('Grant all applications access to all peripherals for maximum compatibility', False),
            ('Disable camera and microphone access for all applications permanently', False),
            ('Control access on a per application basis, allowing only applications that genuinely need access such as video conferencing apps, and denying access to apps that do not need it', True),
            ('Only allow access when the physical privacy shutter is open', False),
        ]
    },
    {
        'text': 'What is AI noise suppression in relation to laptop audio?',
        'domain': 'Laptops',
        'choices': [
            ('A hardware component that physically blocks background sound', False),
            ('A feature that increases microphone sensitivity in noisy environments', False),
            ('A software feature that filters out unwanted background noise from audio input', True),
            ('A Bluetooth protocol that reduces audio lag during wireless transmission', False),
        ]
    },
    {
        'text': 'What can you use if your laptop is too far from the Wi-Fi router to get a strong signal?',
        'domain': 'Laptops',
        'choices': [
            ('Switch to Bluetooth internet instead', False),
            ('Use a USB to Ethernet adapter', False),
            ('Attach an external antenna to the system to improve signal reception', True),
            ('Upgrade the laptop RAM to improve wireless processing', False),
        ]
    },
    {
        'text': 'What is a best practice for maintaining webcam performance over time?',
        'domain': 'Laptops',
        'choices': [
            ('Update the webcam firmware every month', False),
            ('Keep the privacy shutter closed at all times when not in use', False),
            ('Regularly clean the webcam lens and keep device drivers updated', True),
            ('Disable the webcam in device manager when not in video calls', False),
        ]
    },
    # ── Battery Health ────────────────────────────────────────────────────────
    {
        'text': 'Why do rechargeable laptop batteries eventually need to be replaced?',
        'domain': 'Laptops',
        'choices': [
            ('They overheat and melt the internal components', False),
            ('They lose their chemical composition after one year', False),
            ('Charge cycles degrade capacity over time until the battery can no longer hold a charge', True),
            ('They expand and take up too much space inside the laptop', False),
        ]
    },
    {
        'text': 'What is the main practical difference between Lithium-ion and Lithium polymer batteries?',
        'domain': 'Laptops',
        'choices': [
            ('Lithium polymer lasts significantly longer per charge', False),
            ('Lithium-ion is more flexible in shape and size', False),
            ('Lithium-ion uses a liquid electrolyte in a cylindrical container, while Lithium polymer uses a gel-like electrolyte allowing more flexible shapes', True),
            ('Lithium polymer batteries cannot be recharged as many times as Lithium-ion', False),
        ]
    },
    {
        'text': 'Which of the following is a sign of battery degradation?',
        'domain': 'Laptops',
        'choices': [
            ('The laptop runs faster than usual', False),
            ('The battery charges faster than when new', False),
            ('Reduced battery life per charge, overheating, swelling, or sudden shutdowns', True),
            ('The screen brightness automatically increases', False),
        ]
    },
    {
        'text': 'What Windows command is used to generate a battery health report?',
        'domain': 'Laptops',
        'choices': [
            ('powercfg /batterycheck', False),
            ('fsutil behavior query battery', False),
            ('powercfg /batteryreport', True),
            ('chkdsk /batteryreport', False),
        ]
    },
    {
        'text': 'Where is the battery report file saved after running the powercfg /batteryreport command?',
        'domain': 'Laptops',
        'choices': [
            ('It displays directly in the Command Prompt window', False),
            ('It is saved to the C:\\Windows\\System32 folder', False),
            ('It is saved as an HTML file in the home directory and opens in a browser', True),
            ('It is emailed to the system administrator', False),
        ]
    },
    {
        'text': 'How do you check battery health on a Mac?',
        'domain': 'Laptops',
        'choices': [
            ('Run the terminal command batteryreport /mac', False),
            ('Open Finder, then go to Applications, then Battery Health', False),
            ('Go to About This Mac, then System Report, then the Power section', True),
            ('Open System Preferences and click on Battery Diagnostics', False),
        ]
    },
    {
        'text': 'Which third-party tools can be used to check battery health?',
        'domain': 'Laptops',
        'choices': [
            ('CPU-Z for Windows and iStat for Mac', False),
            ('HWMonitor for Windows and CleanMyMac for Mac', False),
            ('BatteryInfoView for Windows and coconutBattery for Mac', True),
            ('Speccy for Windows and Disk Utility for Mac', False),
        ]
    },
    {
        'text': 'What charge level range is recommended to keep your battery between to maximize its lifespan?',
        'domain': 'Laptops',
        'choices': [
            ('0% to 100%', False),
            ('10% to 90%', False),
            ('20% to 80%', True),
            ('50% to 100%', False),
        ]
    },
    {
        'text': 'Which of the following factors can accelerate battery wear?',
        'domain': 'Laptops',
        'choices': [
            ('Keeping the laptop plugged in occasionally', False),
            ('Using the laptop in a well-ventilated area', False),
            ('Frequent full charges and discharges, exposure to heat, and high brightness levels', True),
            ('Regularly updating the operating system', False),
        ]
    },
    {
        'text': 'At what battery health level is it recommended to replace a laptop battery?',
        'domain': 'Laptops',
        'choices': [
            ('When it reaches 90% of original capacity', False),
            ('When it reaches 75% of original capacity', False),
            ('When it falls below 50% of its original capacity', True),
            ('When it reaches 25% of original capacity', False),
        ]
    },
    {
        'text': 'What does the manufacturer\'s recommended cycle count refer to?',
        'domain': 'Laptops',
        'choices': [
            ('The number of times the battery can be fully discharged before swelling', False),
            ('The number of hours the battery can last on a single charge', False),
            ('How many times the battery can be recharged before it degrades significantly', True),
            ('The number of times the laptop can be restarted on battery power', False),
        ]
    },
    {
        'text': 'What is the correct first step before physically replacing a laptop battery?',
        'domain': 'Laptops',
        'choices': [
            ('Run the powercfg /batteryreport command one final time', False),
            ('Charge the battery to 100% before removal', False),
            ('Unplug the device entirely and make sure it is powered off', True),
            ('Enter the BIOS and disable the battery controller', False),
        ]
    },
    {
        'text': 'On some laptops the battery is directly accessible from the outside. How is it typically removed?',
        'domain': 'Laptops',
        'choices': [
            ('By unscrewing four Phillips screws on the bottom panel', False),
            ('By inserting a tool into a pinhole reset button', False),
            ('By flipping the unit over and using a slide-release lock on the underside', True),
            ('By removing the keyboard to access the battery underneath', False),
        ]
    },
    {
        'text': 'What should you do if the battery is located inside the laptop and not directly accessible?',
        'domain': 'Laptops',
        'choices': [
            ('Take it to a manufacturer service center only — it cannot be done at home', False),
            ('Use a heat gun to loosen the adhesive holding the back panel', False),
            ('Verify how to open the unit, remove the access panel, then access the battery', True),
            ('Replace the entire laptop as internal batteries cannot be swapped', False),
        ]
    },
    {
        'text': 'What is battery calibration and when is it recommended?',
        'domain': 'Laptops',
        'choices': [
            ('A weekly process of charging to 80% and discharging to 20%', False),
            ('A BIOS setting that adjusts power delivery to the battery', False),
            ('A one-time process after replacement where you charge fully to 100%, discharge to around 5-10%, then recharge — helping the system accurately track battery status', True),
            ('A manufacturer reset that clears all battery charge history', False),
        ]
    },
    {
        'text': 'After replacing a laptop battery, what power settings should you configure on Windows?',
        'domain': 'Laptops',
        'choices': [
            ('Set the power plan to High Performance for best results', False),
            ('Disable all background processes permanently', False),
            ('Enable battery-saver mode in Windows power settings', True),
            ('Set the screen brightness to maximum to test the new battery', False),
        ]
    },
    {
        'text': 'Why should you avoid exposing a laptop battery to heat?',
        'domain': 'Laptops',
        'choices': [
            ('Heat causes the battery to charge faster which reduces accuracy', False),
            ('Heat permanently increases the charge cycle count', False),
            ('Exposure to heat reduces battery longevity and can cause degradation', True),
            ('Heat causes the lithium electrolyte to solidify and stop working', False),
        ]
    },
    {
        'text': 'Which of the following best describes how to maintain good battery health long term?',
        'domain': 'Laptops',
        'choices': [
            ('Always fully charge to 100% and drain to 0% for accurate readings', False),
            ('Keep the laptop plugged in at all times to avoid using the battery', False),
            ('Keep charge between 20-80%, store in a cool dry place, minimize background processes, and regularly monitor battery health', True),
            ('Replace the battery every 6 months regardless of health status', False),
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