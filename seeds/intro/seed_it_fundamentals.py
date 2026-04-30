import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app import app, db
from models import Question, Choice

questions_data = [

    # ── WHAT IS A COMPUTER / IPOS MODEL ───────────────────────────────────────

    {
        'text': 'What does IPOS stand for in the context of computers?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'IPOS stands for Input Processing Output Storage — the four fundamental functions of any computer system.',
        'choices': [
            ('Internet Protocol Operating System', False),
            ('Input Processing Output Storage', True),
            ('Integrated Program Operating Sequence', False),
            ('Internal Processing Output Signal', False),
        ]
    },
    {
        'text': 'Which of the following is an example of an INPUT device?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'A keyboard is an input device because it sends data into the computer. Monitors and speakers are output devices. An SSD is a storage device.',
        'choices': [
            ('Monitor', False),
            ('Keyboard', True),
            ('Speaker', False),
            ('SSD', False),
        ]
    },
    {
        'text': 'Which components handle the PROCESSING stage of the IPOS model?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'The CPU (Central Processing Unit) and RAM (memory) handle processing. The CPU executes instructions while RAM holds the data currently being worked on.',
        'choices': [
            ('Monitor and speakers', False),
            ('CPU and memory (RAM)', True),
            ('Hard drive and SSD', False),
            ('Keyboard and mouse', False),
        ]
    },
    {
        'text': 'Which of the following is an example of an OUTPUT device?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'A monitor displays results from the computer making it an output device. Keyboards and mice are input devices. Hard drives are storage devices.',
        'choices': [
            ('Keyboard', False),
            ('Hard drive', False),
            ('Monitor', True),
            ('Touchscreen (input mode)', False),
        ]
    },
    {
        'text': 'Which of the following is an example of STORAGE in the IPOS model?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Cloud storage hard drives and SSDs are all storage examples. They hold data long-term unlike RAM which is temporary processing memory.',
        'choices': [
            ('CPU', False),
            ('Monitor', False),
            ('Cloud storage', True),
            ('Mouse', False),
        ]
    },
    {
        'text': 'What is the main difference between a workstation and a regular desktop PC?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Workstations are high-performance computers designed for demanding professional tasks like 3D rendering video editing and engineering. They have more powerful components than standard desktop PCs.',
        'choices': [
            ('Workstations are smaller and more portable than desktop PCs', False),
            ('Workstations are high-performance computers designed for demanding professional tasks', True),
            ('Workstations only run Linux while desktops run Windows', False),
            ('Workstations have no monitors while desktops do', False),
        ]
    },
    {
        'text': 'What is the primary purpose of a server computer?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Servers provide services and resources to other computers (clients) on a network. They host websites store files run databases and manage network resources.',
        'choices': [
            ('Personal computing for one user', False),
            ('Providing services and resources to other computers on a network', True),
            ('Gaming and multimedia entertainment', False),
            ('Portable computing while travelling', False),
        ]
    },

    # ── STATIC ELECTRICITY / ESD ──────────────────────────────────────────────

    {
        'text': 'What does ESD stand for?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'ESD stands for Electrostatic Discharge — the sudden release of static electricity that can damage or destroy sensitive computer components.',
        'choices': [
            ('Electrical System Damage', False),
            ('Electrostatic Discharge', True),
            ('Electronic Static Disruption', False),
            ('Electrical Surge Damage', False),
        ]
    },
    {
        'text': 'How does static electricity build up on a person?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Static electricity builds up when two materials rub together such as walking on carpet wearing synthetic clothing or handling plastic packaging. This causes electrons to transfer between materials.',
        'choices': [
            ('By using electronic devices for extended periods', False),
            ('When two materials rub together transferring electrons', True),
            ('By being near high-voltage power lines', False),
            ('By touching metal surfaces frequently', False),
        ]
    },
    {
        'text': 'What is "latent" ESD damage?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Latent ESD damage occurs when a component is partially damaged by static discharge. The device continues to work for a period of time but fails prematurely later. This is more dangerous than catastrophic damage because it is not immediately obvious.',
        'choices': [
            ('Damage that causes immediate and complete component failure', False),
            ('Damage where the device works for a while then fails prematurely later', True),
            ('Damage visible to the naked eye on the circuit board', False),
            ('Damage caused by high-voltage power surges only', False),
        ]
    },
    {
        'text': 'What is the recommended humidity level to reduce ESD risk when working on computers?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Keeping humidity between 40-60% helps reduce static buildup. Dry air below 40% allows static to build up much more easily which increases ESD risk.',
        'choices': [
            ('Below 20%', False),
            ('Between 40-60%', True),
            ('Above 80%', False),
            ('Exactly 100%', False),
        ]
    },
    {
        'text': 'Which of the following is a common cause of static electricity buildup?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Walking on carpet is one of the most common causes of static buildup as friction between shoe soles and carpet fibers transfers electrons.',
        'choices': [
            ('Working near a window', False),
            ('Walking on carpet', True),
            ('Using a metal screwdriver', False),
            ('Working under bright lights', False),
        ]
    },
    {
        'text': 'Why is the ESD myth "I didn\'t feel a shock so it\'s fine" dangerous?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Humans cannot feel static discharges below about 3,000 volts. However computer components can be damaged by discharges as low as 100 volts — well below human detection threshold.',
        'choices': [
            ('Because modern components are completely immune to ESD', False),
            ('Because components can be damaged by discharges too small for humans to feel', True),
            ('Because the shock feeling is delayed and comes later', False),
            ('Because ESD only damages mechanical components not electronic ones', False),
        ]
    },
    {
        'text': 'What is the purpose of an anti-static wrist strap?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'An anti-static wrist strap keeps you continuously grounded by safely discharging any static buildup through a resistor to ground preventing it from discharging through sensitive components.',
        'choices': [
            ('To protect your wrist from sharp edges inside the computer case', False),
            ('To keep you continuously grounded so static safely discharges to ground instead of into components', True),
            ('To measure the static electricity level in the room', False),
            ('To prevent electrical current from the power supply reaching your hands', False),
        ]
    },
    {
        'text': 'Why should you avoid working on computers in carpeted rooms?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Carpet generates static electricity easily when walked on. This dramatically increases the risk of ESD damage to sensitive components. Hard floor surfaces are much safer.',
        'choices': [
            ('Because carpet fibres can get inside the computer', False),
            ('Because carpet generates static electricity making ESD damage much more likely', True),
            ('Because carpet makes it harder to see dropped screws', False),
            ('Because carpets absorb heat from components', False),
        ]
    },
    {
        'text': 'How should you correctly handle a motherboard or expansion card?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Components should always be held by their edges avoiding contact with circuits connectors and chips. This prevents both ESD damage from skin contact and physical damage to the circuitry.',
        'choices': [
            ('Hold it firmly in the centre for maximum control', False),
            ('Hold it by the edges avoiding contact with circuits and connectors', True),
            ('Hold it by the CPU socket for the most stable grip', False),
            ('Grab it wherever is most comfortable — edges are not important', False),
        ]
    },

    # ── HOW DATA IS MEASURED ──────────────────────────────────────────────────

    {
        'text': 'What is a bit and what are its possible values?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'A bit is the smallest unit of data in computing. It can only have one of two values: 0 or 1. The word "bit" comes from "binary digit".',
        'choices': [
            ('A bit is 8 bytes and can hold values 0-255', False),
            ('A bit is the smallest unit of data with only two possible values: 0 or 1', True),
            ('A bit is equivalent to one character of text', False),
            ('A bit holds one letter number or symbol', False),
        ]
    },
    {
        'text': 'How many bits make up one byte?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': '8 bits make up 1 byte. This is a fundamental relationship in computing — the byte is the standard unit for measuring file sizes and storage capacity.',
        'choices': [
            ('4 bits', False),
            ('16 bits', False),
            ('8 bits', True),
            ('1024 bits', False),
        ]
    },
    {
        'text': 'What is the correct order of data storage units from smallest to largest?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'The correct order is Bit → Byte → Kilobyte → Megabyte → Gigabyte → Terabyte. Each unit is approximately 1000 times larger than the previous one.',
        'choices': [
            ('Byte → Bit → Kilobyte → Gigabyte → Megabyte → Terabyte', False),
            ('Bit → Byte → Kilobyte → Megabyte → Gigabyte → Terabyte', True),
            ('Kilobyte → Megabyte → Byte → Bit → Gigabyte → Terabyte', False),
            ('Bit → Byte → Megabyte → Kilobyte → Terabyte → Gigabyte', False),
        ]
    },
    {
        'text': 'Approximately how large is a typical digital photo file?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'A typical digital photo is between 1 and 5 MB (Megabytes). Text documents are much smaller (10-100 KB) while movies are much larger (1-5 GB).',
        'choices': [
            ('10-100 KB', False),
            ('1-5 MB', True),
            ('1-5 GB', False),
            ('15-30 GB', False),
        ]
    },
    {
        'text': 'How many gigabytes are in one terabyte?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': '1 terabyte (TB) equals 1,000 gigabytes (GB). Modern hard drives and SSDs are often sold in terabyte capacities.',
        'choices': [
            ('100 GB', False),
            ('500 GB', False),
            ('1,000 GB', True),
            ('1,024 GB', False),
        ]
    },

    # ── DATA SPEED MEASUREMENTS ───────────────────────────────────────────────

    {
        'text': 'What is the key difference between bits (b) and bytes (B) in computing?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Bits (lowercase b) are used to measure data transfer speed (Mbps Gbps). Bytes (uppercase B) are used to measure file size and storage capacity (MB GB). 8 bits = 1 byte.',
        'choices': [
            ('They are the same — just different names for the same unit', False),
            ('Bits measure data transfer speed while bytes measure file size and storage', True),
            ('Bytes measure speed while bits measure file size', False),
            ('Bits are used for storage while bytes are for RAM only', False),
        ]
    },
    {
        'text': 'An internet provider advertises 300 Mbps. What is the actual download speed in MB/s?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'To convert Mbps to MB/s divide by 8 (since 8 bits = 1 byte). 300 Mbps ÷ 8 = 37.5 MB/s. ISPs advertise in megabits while download managers show megabytes.',
        'choices': [
            ('300 MB/s', False),
            ('150 MB/s', False),
            ('37.5 MB/s', True),
            ('2400 MB/s', False),
        ]
    },
    {
        'text': 'What unit is used to measure CPU processing speed?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'CPU speed is measured in GHz (gigahertz) — billions of cycles per second. A higher GHz generally means faster processing.',
        'choices': [
            ('MB/s (megabytes per second)', False),
            ('GHz (gigahertz)', True),
            ('Mbps (megabits per second)', False),
            ('GB (gigabytes)', False),
        ]
    },
    {
        'text': 'What does "Mbps" stand for and what does it measure?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Mbps stands for Megabits per second. It is used to measure data transfer speed such as internet connection speed or network speed.',
        'choices': [
            ('Megabytes per second — measures file storage', False),
            ('Megabits per second — measures data transfer speed', True),
            ('Memory bits per second — measures RAM speed', False),
            ('Megabaud per second — measures modem speed only', False),
        ]
    },
    {
        'text': 'What is the approximate read/write speed of a modern NVMe SSD compared to a traditional HDD?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'NVMe SSDs achieve 1,500-7,000+ MB/s while traditional HDDs only reach 80-160 MB/s. This makes NVMe SSDs up to 50x faster than HDDs for storage access.',
        'choices': [
            ('NVMe SSD is about twice as fast as an HDD', False),
            ('NVMe SSD (1,500-7,000+ MB/s) vs HDD (80-160 MB/s) — NVMe can be up to 50x faster', True),
            ('NVMe SSD and HDD have similar speeds — the difference is in reliability', False),
            ('HDD is faster for large files while NVMe is faster for small files only', False),
        ]
    },

    # ── CORE HARDWARE COMPONENTS ──────────────────────────────────────────────

    {
        'text': 'What is the role of the CPU in a computer?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'The CPU (Central Processing Unit) is the brain of the computer. It executes instructions and performs calculations for all programs running on the system.',
        'choices': [
            ('Stores data permanently even when powered off', False),
            ('Executes instructions and performs calculations — the brain of the computer', True),
            ('Converts AC power to DC power for components', False),
            ('Displays graphics and video output', False),
        ]
    },
    {
        'text': 'Why do CPUs require cooling systems?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'CPUs generate significant heat when executing billions of calculations per second. Without cooling they would overheat causing throttling damage or complete failure.',
        'choices': [
            ('To keep the CPU moist and prevent corrosion', False),
            ('Because CPUs generate significant heat and will overheat and fail without cooling', True),
            ('To prevent static electricity buildup on the CPU die', False),
            ('To slow the CPU down to safe operating speeds', False),
        ]
    },
    {
        'text': 'What does it mean that RAM is "volatile"?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Volatile means RAM loses all its data when power is removed. This is why unsaved work disappears if the computer crashes or loses power — it was only in RAM not saved to storage.',
        'choices': [
            ('RAM is dangerous and can explode if overloaded', False),
            ('RAM loses all data when power is removed — it cannot hold data without power', True),
            ('RAM data can become corrupted over time spontaneously', False),
            ('RAM is unstable and frequently causes system crashes', False),
        ]
    },
    {
        'text': 'What is the minimum recommended amount of RAM for a modern computer?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'While 4GB is very basic the minimum for modern computing is considered 8GB. 16GB or more is recommended for comfortable multitasking and running modern applications.',
        'choices': [
            ('2 GB', False),
            ('4 GB', False),
            ('8 GB', True),
            ('32 GB', False),
        ]
    },
    {
        'text': 'What are the main disadvantages of a traditional HDD compared to an SSD?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'HDDs are slower use mechanical spinning platters are susceptible to physical damage from drops and impacts and make audible spinning and clicking sounds during operation.',
        'choices': [
            ('HDDs are more expensive and less reliable than SSDs', False),
            ('HDDs are slower use mechanical parts susceptible to physical damage and make noise', True),
            ('HDDs cannot store as much data as SSDs', False),
            ('HDDs require more power and only work in desktop computers', False),
        ]
    },
    {
        'text': 'What is the motherboard\'s role in a computer system?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'The motherboard is the central circuit board that connects all components together. Everything — CPU RAM storage GPU expansion cards and ports — connects to or through the motherboard.',
        'choices': [
            ('It powers all components by converting AC to DC', False),
            ('It is the central circuit board that connects all components allowing them to communicate', True),
            ('It stores the operating system permanently', False),
            ('It controls the display output only', False),
        ]
    },
    {
        'text': 'What does the power supply unit (PSU) do?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'The PSU converts AC (alternating current) from the wall outlet to DC (direct current) at the voltages needed by computer components. Different components require different DC voltages.',
        'choices': [
            ('Stores electrical charge as a backup power source', False),
            ('Converts AC power from the wall outlet to the DC voltages needed by computer components', True),
            ('Regulates how much power the CPU uses during processing', False),
            ('Generates its own power using a small internal generator', False),
        ]
    },
    {
        'text': 'Which symptoms suggest a failing power supply unit?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Common PSU failure symptoms include random shutdowns the computer not booting at all and a burning smell. These occur because the PSU cannot deliver stable power to components.',
        'choices': [
            ('Slow internet connection and display flickering only', False),
            ('Random shutdowns failure to boot and burning smell', True),
            ('Blue screen errors and corrupted files only', False),
            ('Overheating CPU and loud fan noise only', False),
        ]
    },
    {
        'text': 'What is thermal paste and why is it used?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Thermal paste is applied between a CPU and its heatsink to fill microscopic air gaps in the metal surfaces. Air is a poor heat conductor so thermal paste improves heat transfer from the CPU to the heatsink.',
        'choices': [
            ('A glue used to permanently attach heatsinks to CPUs', False),
            ('A compound applied between CPU and heatsink to improve heat transfer by filling microscopic air gaps', True),
            ('A lubricant for cooling fans to reduce noise', False),
            ('An electrical conductor applied to CPU pins for better contact', False),
        ]
    },
    {
        'text': 'What RAM speed specification would you see on a DDR5 memory module?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'DDR5 RAM typically operates at speeds like 5200 MHz and above. DDR4 typically runs at speeds like 2400 MHz or 3200 MHz. Higher MHz means faster data transfer.',
        'choices': [
            ('800 MHz — DDR5 runs slower for reliability', False),
            ('5200 MHz or higher — DDR5 is significantly faster than DDR4', True),
            ('2400 MHz — same as DDR4', False),
            ('100 MHz — DDR5 uses a different measurement system', False),
        ]
    },

    # ── SOFTWARE TYPES ────────────────────────────────────────────────────────

    {
        'text': 'What is the difference between system software and application software?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'System software (OS drivers utilities) manages hardware and provides the platform for other software. Application software (Word Excel browsers) performs specific tasks for users.',
        'choices': [
            ('System software is free while application software must be purchased', False),
            ('System software manages hardware and provides the platform while application software performs specific user tasks', True),
            ('System software runs in the background while application software only runs when clicked', False),
            ('There is no practical difference — they are the same category', False),
        ]
    },
    {
        'text': 'Which of the following is an example of system software?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'A device driver is system software — it allows the operating system to communicate with hardware devices. Word Excel and VLC are application software.',
        'choices': [
            ('Microsoft Word', False),
            ('VLC Media Player', False),
            ('A device driver', True),
            ('Google Chrome', False),
        ]
    },
    {
        'text': 'What file format is typically used to install software on Windows?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': '.exe (executable) and .msi (Microsoft Installer) are the standard formats for installing software on Windows. Linux uses package managers while mobile devices use app stores.',
        'choices': [
            ('.dmg and .pkg files', False),
            ('.exe and .msi files', True),
            ('.apk and .ipa files', False),
            ('.deb and .rpm files', False),
        ]
    },

    # ── WORKING SAFELY ────────────────────────────────────────────────────────

    {
        'text': 'What should you always do before opening a desktop computer case to work inside?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Always disconnect (unplug) the power before working inside a desktop. For laptops also remove the battery. Working on powered components risks electric shock and component damage.',
        'choices': [
            ('Turn off the monitor only', False),
            ('Disconnect the power by unplugging the computer', True),
            ('Switch to power saving mode', False),
            ('Enable safe mode in Windows first', False),
        ]
    },
    {
        'text': 'Why are magnetic screwdrivers recommended for computer work?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Magnetic screwdrivers hold screws so they don\'t fall onto the motherboard or other components where they could cause short circuits. They also help retrieve dropped screws from tight spaces.',
        'choices': [
            ('They create an anti-static field that protects components', False),
            ('They hold screws preventing them from falling onto components and causing short circuits', True),
            ('They are required by law for working on computers', False),
            ('They are stronger than regular screwdrivers for tight screws only', False),
        ]
    },
    {
        'text': 'Why should you never have liquids near a computer while working on it?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Liquid spills on electronic components cause short circuits corrosion and permanent damage. Even a small amount of water can destroy a motherboard CPU or other expensive components.',
        'choices': [
            ('Liquids create static electricity that damages components', False),
            ('Liquid spills cause short circuits corrosion and permanent damage to electronic components', True),
            ('Liquids are only dangerous if they freeze inside the computer', False),
            ('Only certain liquids are dangerous — water is safe near computers', False),
        ]
    },
    {
        'text': 'Why should you let a computer system cool down before touching internal components?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Components like CPUs heatsinks and GPUs can be extremely hot after operation. Touching them immediately can cause burns. Allow the system to cool for several minutes before reaching inside.',
        'choices': [
            ('Hot components generate static electricity that could damage other parts', False),
            ('Components like CPUs and heatsinks can be extremely hot and cause burns', True),
            ('The cooling fans create a vacuum that makes it difficult to work inside a hot system', False),
            ('Hot components expand and become harder to remove', False),
        ]
    },
    {
        'text': 'Why is documentation important before disassembling a computer?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Taking photos and labelling cables before disassembly ensures correct reassembly. Complex cable routing can be difficult to remember and incorrect connections can damage components.',
        'choices': [
            ('Documentation is required by law for warranty purposes', False),
            ('Photos and labels ensure correct reassembly as cable routing can be complex and hard to remember', True),
            ('Documentation is only needed for professional repairs not home work', False),
            ('It helps the customer understand what was done wrong', False),
        ]
    },
    {
        'text': 'How should you handle sharp metal edges inside a computer case?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Computer cases and metal brackets often have sharp edges that can cut skin. Using slow controlled movements and being aware of edges reduces the risk of cuts during assembly and repair.',
        'choices': [
            ('Always wear full gloves to eliminate all risk of cuts', False),
            ('Use slow controlled movements and be aware of sharp edges to avoid cuts', True),
            ('Sharp edges only exist in older cases — modern cases have no sharp parts', False),
            ('File down all sharp edges before beginning any work', False),
        ]
    },
    {
        'text': 'What is the correct way to remove dust from a computer during maintenance?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Compressed air or an electronics vacuum should be used to remove dust. The direction should be front to inside to back to push dust out. A regular vacuum creates too much static and suction.',
        'choices': [
            ('Use a household vacuum cleaner for thorough dust removal', False),
            ('Use compressed air or an electronics vacuum working from front to inside to back', True),
            ('Use a damp cloth to wipe dust from all components', False),
            ('Blow with your mouth to remove dust without any tools', False),
        ]
    },
    {
        'text': 'Why is cable management important inside a computer?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Good cable management improves airflow preventing overheating makes future repairs easier and reduces the risk of cables interfering with fans or becoming accidentally disconnected.',
        'choices': [
            ('Neatly arranged cables make the computer look better for photos only', False),
            ('Cable management improves airflow prevents overheating and makes future repairs easier', True),
            ('Cables must be tied together tightly to prevent electrical interference', False),
            ('Cable management is only important for servers not desktop computers', False),
        ]
    },

    # ── TECHNICIAN TOOLKIT ────────────────────────────────────────────────────

    {
        'text': 'What type of screwdriver is most commonly needed when working inside computers?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Phillips head screwdrivers are the most commonly used for computer work as most case screws and component mounting screws use Phillips heads. Flat-head screwdrivers are also useful for prying and some screws.',
        'choices': [
            ('Torx drivers only', False),
            ('Phillips head screwdrivers — most computer screws use Phillips heads', True),
            ('Allen/hex keys for all computer components', False),
            ('Flat-head only as Phillips can strip screws easily', False),
        ]
    },
    {
        'text': 'What are Torx screwdrivers used for in computer work?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Torx screwdrivers have a star-shaped tip and are commonly used in laptops Apple devices and some desktop components. The T4 through T10 sizes cover most computer Torx screws.',
        'choices': [
            ('Only for Apple MacBook computers exclusively', False),
            ('For star-shaped Torx screws commonly found in laptops Apple devices and some desktop components', True),
            ('For loosening stripped Phillips screws', False),
            ('For very tiny screws on circuit boards only', False),
        ]
    },
    {
        'text': 'What is the purpose of anti-static tweezers in a technician\'s toolkit?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Anti-static tweezers allow technicians to pick up and place small components like jumpers SMD components and screws without risk of ESD damage or dropping them in hard-to-reach places.',
        'choices': [
            ('To remove thermal paste from CPU surfaces only', False),
            ('To pick up and place small components safely without risk of ESD or dropping them', True),
            ('To test whether components are properly grounded', False),
            ('Only for extracting broken screws from motherboards', False),
        ]
    },
    {
        'text': 'Why would a technician use a precision screwdriver kit rather than standard screwdrivers?',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': False,
        'explanation': 'Precision screwdriver kits contain very small screwdrivers needed for laptops tablets smartphones and other compact devices where standard-size screwdrivers are too large.',
        'choices': [
            ('Precision screwdrivers are magnetic while standard ones are not', False),
            ('For working on laptops tablets and phones where standard screwdrivers are too large', True),
            ('Precision screwdrivers provide more torque for tight screws', False),
            ('Only for working on hard drives and SSDs specifically', False),
        ]
    },

    # ── MULTI SELECT QUESTIONS ─────────────────────────────────────────────────

    {
        'text': 'Which TWO of the following are examples of OUTPUT devices? (Select TWO)',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': True,
        'explanation': 'Monitors display results and speakers produce audio — both are output devices. Keyboards and mice are input devices.',
        'choices': [
            ('Monitor', True),
            ('Keyboard', False),
            ('Speakers', True),
            ('Mouse', False),
        ]
    },
    {
        'text': 'Which TWO of the following are correct methods to prevent ESD damage? (Select TWO)',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': True,
        'explanation': 'Using an anti-static wrist strap keeps you grounded. Handling components by their edges avoids skin contact with circuits. Both are essential ESD prevention practices.',
        'choices': [
            ('Wear an anti-static wrist strap while working', True),
            ('Work on a carpeted surface for stability', False),
            ('Handle components only by their edges', True),
            ('Blow on components before installing them', False),
        ]
    },
    {
        'text': 'Which TWO of the following correctly describe SSD advantages over HDD? (Select TWO)',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': True,
        'explanation': 'SSDs have no moving parts making them faster and more resistant to physical shock damage compared to mechanical HDDs.',
        'choices': [
            ('SSDs are significantly faster than HDDs', True),
            ('SSDs are always cheaper than equivalent HDD storage', False),
            ('SSDs have no moving parts making them more resistant to physical damage', True),
            ('SSDs have unlimited read/write cycles', False),
        ]
    },
    {
        'text': 'Which TWO of the following are included in the STORAGE category of the IPOS model? (Select TWO)',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': True,
        'explanation': 'Hard drives and SSDs are storage devices that hold data long-term. The CPU handles processing and the monitor is output.',
        'choices': [
            ('Hard drive', True),
            ('CPU', False),
            ('SSD', True),
            ('Monitor', False),
        ]
    },
    {
        'text': 'Which TWO safety precautions should always be followed before working inside a computer? (Select TWO)',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': True,
        'explanation': 'Disconnecting power prevents electric shock. Using an anti-static wrist strap prevents ESD damage. Both are essential safety steps before opening a computer.',
        'choices': [
            ('Disconnect the power supply before opening the case', True),
            ('Keep a glass of water nearby to stay hydrated', False),
            ('Use an anti-static wrist strap to prevent ESD', True),
            ('Always work on a carpeted floor', False),
        ]
    },
    {
        'text': 'Which TWO of the following are symptoms of a failing power supply? (Select TWO)',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': True,
        'explanation': 'Random shutdowns and burning smell are classic PSU failure symptoms. The PSU cannot maintain stable power causing random crashes and may emit a burning smell from failing components.',
        'choices': [
            ('Random unexplained shutdowns', True),
            ('Slow internet connection', False),
            ('Burning smell from the computer', True),
            ('Display showing wrong colours', False),
        ]
    },
    {
        'text': 'Which TWO tools from a technician\'s toolkit help prevent ESD damage? (Select TWO)',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': True,
        'explanation': 'Anti-static wrist straps keep the technician grounded. Anti-static tweezers allow safe handling of small components without ESD risk from fingers.',
        'choices': [
            ('Anti-static wrist strap', True),
            ('Phillips screwdriver', False),
            ('Anti-static tweezers', True),
            ('Torx driver', False),
        ]
    },
    {
        'text': 'Which TWO of the following are true about RAM? (Select TWO)',
        'domain': 'IT Fundamentals',
        'exam': 'intro',
        'multi_select': True,
        'explanation': 'RAM is volatile meaning it loses data when power is removed. More RAM allows smoother multitasking by giving the CPU more workspace for active processes.',
        'choices': [
            ('RAM loses all its data when the computer is powered off', True),
            ('RAM stores data permanently like a hard drive', False),
            ('More RAM allows smoother multitasking', True),
            ('RAM speed is measured in MB/s like storage drives', False),
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
            exam=qd.get('exam', 'intro'),
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
    intro = Question.query.filter_by(exam='intro').count()
    print(f'Added {added} questions. Skipped {skipped} duplicates.')
    print(f'IT Fundamentals total: {intro} | Overall: {total}')