import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app import app, db
from models import Question, Choice

questions_data = [

    # ── 3 SCENARIO QUESTIONS ──────────────────────────────────────────────────

    {
        'text': 'A user reports that after their phone fell they are not able to use the screen to select any of the icons. Which of the following is MOST likely the cause?',
        'domain': 'Troubleshooting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'The digitizer is what allows the touchscreen to detect touch input. If the phone was dropped and the digitizer was damaged the touch feature will not work even though the display may still show images.',
        'choices': [
            ('Digitizer', True),
            ('Overheating', False),
            ('Malware', False),
            ('Stylus', False),
        ]
    },
    {
        'text': 'An organization has implemented a short-range wireless method to authenticate to the front door of their office building. Which of the following must be enabled on the mobile device to authenticate?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'NFC (Near Field Communication) is used for short-range authentication of about 4cm. It is commonly used for building access control payments and device pairing. Bluetooth operates at longer distances generally up to 30 feet.',
        'choices': [
            ('Biometrics', False),
            ('NFC', True),
            ('Bluetooth', False),
            ('Hotspot', False),
        ]
    },
    {
        'text': 'A user\'s laptop is having screen issues. The screen is able to display images but only when a light shines on it — the display appears very dark. What should the technician do first?',
        'domain': 'Troubleshooting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'When a screen displays images but appears very dark it is a classic symptom of a failing backlight. The technician should first verify the backlight is functioning before replacing the screen or graphics card.',
        'choices': [
            ('Replace the graphics card', False),
            ('Replace the screen', False),
            ('Have the user use an external display only', False),
            ('Ensure the backlight is functioning as expected', True),
        ]
    },

    # ── NETWORKING QUESTIONS ──────────────────────────────────────────────────

    {
        'text': 'Which port is used by SSH for encrypted remote access?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'SSH (Secure Shell) uses port 22 for encrypted remote access. It replaced Telnet which used port 23 and transmitted data in plain text.',
        'choices': [
            ('Port 21', False),
            ('Port 22', True),
            ('Port 23', False),
            ('Port 25', False),
        ]
    },
    {
        'text': 'What port does DNS use to resolve domain names to IP addresses?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'DNS uses port 53 for name resolution. It typically uses UDP for standard queries but can use TCP for larger responses like zone transfers.',
        'choices': [
            ('Port 25', False),
            ('Port 80', False),
            ('Port 53', True),
            ('Port 443', False),
        ]
    },
    {
        'text': 'Which port does HTTPS use for secure web browsing?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'HTTPS uses port 443. It is HTTP encrypted with TLS/SSL. Regular HTTP uses port 80.',
        'choices': [
            ('Port 80', False),
            ('Port 443', True),
            ('Port 8080', False),
            ('Port 3389', False),
        ]
    },
    {
        'text': 'FTP uses which two port numbers?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'FTP uses port 21 for control (commands) and port 20 for data transfer. Both ports are needed for a complete FTP connection.',
        'choices': [
            ('20 and 21', True),
            ('22 and 23', False),
            ('25 and 26', False),
            ('80 and 81', False),
        ]
    },
    {
        'text': 'Which port is used by the Remote Desktop Protocol (RDP)?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'RDP uses port 3389. It allows users to remotely access and control a Windows computer over a network connection.',
        'choices': [
            ('1433', False),
            ('3306', False),
            ('3389', True),
            ('5900', False),
        ]
    },
    {
        'text': 'Port 25 is associated with which protocol?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Port 25 is used by SMTP (Simple Mail Transfer Protocol) for sending email between mail servers.',
        'choices': [
            ('HTTP', False),
            ('FTP', False),
            ('SMTP', True),
            ('DNS', False),
        ]
    },
    {
        'text': 'What does the TCP/IP model govern?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'The TCP/IP model governs most internet and network communications. It is the foundational protocol suite that defines how data is transmitted across networks.',
        'choices': [
            ('Only local area network traffic', False),
            ('Most internet and network communications', True),
            ('Only wireless communications', False),
            ('Only file transfer protocols', False),
        ]
    },
    {
        'text': 'In a network address what does the colon after the IP address indicate?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'In a network address the colon separates the IP address from the port number. For example 192.168.1.10:80 means IP 192.168.1.10 on port 80.',
        'choices': [
            ('Subnet mask separator', False),
            ('Port number separator', True),
            ('VLAN identifier', False),
            ('Protocol version', False),
        ]
    },
    {
        'text': 'Which protocol uses a three-way handshake before data transmission?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'TCP uses a three-way handshake (SYN SYN-ACK ACK) to establish a connection before data is sent. This ensures both parties are ready and the connection is reliable.',
        'choices': [
            ('UDP', False),
            ('ICMP', False),
            ('TCP', True),
            ('FTP', False),
        ]
    },
    {
        'text': 'Which transport protocol is preferred for video streaming and online gaming?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'UDP is preferred for video streaming and gaming because its lower overhead provides faster transmission. Small packet losses are acceptable whereas the delay from TCP retransmissions would be worse.',
        'choices': [
            ('TCP', False),
            ('UDP', True),
            ('FTP', False),
            ('SMTP', False),
        ]
    },
    {
        'text': 'What does UDP sacrifice in exchange for speed?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'UDP sacrifices reliable packet delivery for speed. It does not confirm that packets were received does not retransmit lost packets and has no handshake.',
        'choices': [
            ('Encryption', False),
            ('Reliable packet delivery', True),
            ('Port numbers', False),
            ('IP addressing', False),
        ]
    },
    {
        'text': 'Which statement about TCP is correct?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'TCP uses checksums and acknowledgments for error detection and reliable delivery. It is connection-oriented and verifies packet receipt making it slower but reliable.',
        'choices': [
            ('It is connectionless', False),
            ('It does not verify packet delivery', False),
            ('It uses checksums and acknowledgments for error detection', True),
            ('It is faster than UDP', False),
        ]
    },
    {
        'text': 'DNS lookups primarily use which transport protocol?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'DNS primarily uses UDP because queries are small and fast responses are more important than guaranteed delivery. TCP is used for larger operations like zone transfers.',
        'choices': [
            ('TCP', False),
            ('UDP', True),
            ('ICMP', False),
            ('SMTP', False),
        ]
    },
    {
        'text': 'Which of the following is a TCP use case?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Email (SMTP) uses TCP because reliable delivery is critical — you cannot afford to lose parts of an email. VoIP DNS lookups and IoT sensors typically use UDP.',
        'choices': [
            ('Voice over IP calls', False),
            ('DNS lookups', False),
            ('Email via SMTP', True),
            ('IoT sensor data', False),
        ]
    },
    {
        'text': 'What is the purpose of a checksum in TCP?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A checksum in TCP is used to detect transmission errors. The sender calculates a checksum value and the receiver recalculates it — if they do not match the packet was corrupted.',
        'choices': [
            ('To encrypt the packet', False),
            ('To detect transmission errors', True),
            ('To identify the destination port', False),
            ('To compress data', False),
        ]
    },
    {
        'text': 'At which OSI layer do standard switches operate?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Standard switches operate at Layer 2 (Data Link) and use MAC addresses to forward frames between devices on the same network.',
        'choices': [
            ('Layer 1 (Physical)', False),
            ('Layer 2 (Data Link)', True),
            ('Layer 3 (Network)', False),
            ('Layer 4 (Transport)', False),
        ]
    },
    {
        'text': 'What addressing does a router use to forward packets?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Routers use IP addresses (Layer 3) to forward packets between different networks. Switches use MAC addresses for forwarding within the same network.',
        'choices': [
            ('MAC addresses', False),
            ('Port numbers', False),
            ('IP addresses', True),
            ('Serial numbers', False),
        ]
    },
    {
        'text': 'What is the main difference between a managed and unmanaged switch?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Managed switches support VLANs advanced security settings quality of service and remote management. Unmanaged switches are plug-and-play with no configuration options.',
        'choices': [
            ('Managed switches are always faster', False),
            ('Managed switches support VLANs and advanced security settings', True),
            ('Unmanaged switches cost more', False),
            ('Unmanaged switches require more configuration', False),
        ]
    },
    {
        'text': 'A layer 3 switch can perform which additional function compared to a layer 2 switch?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A Layer 3 switch can route between different networks (VLANs or subnets) in addition to switching. A Layer 2 switch can only forward frames within the same network.',
        'choices': [
            ('Wi-Fi transmission', False),
            ('Routing between networks', True),
            ('Firewall filtering', False),
            ('PoE power delivery', False),
        ]
    },
    {
        'text': 'What does a VLAN allow you to do?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'VLANs (Virtual Local Area Networks) logically isolate groups of devices on the same physical switches. This improves security and reduces broadcast traffic without requiring separate physical hardware.',
        'choices': [
            ('Extend Wi-Fi coverage', False),
            ('Logically isolate groups of devices on the same physical switches', True),
            ('Increase internet speed', False),
            ('Replace the need for a router', False),
        ]
    },
    {
        'text': 'Which routing type uses protocols like OSPF and BGP for automated path selection?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Dynamic routing uses protocols like OSPF (Open Shortest Path First) and BGP (Border Gateway Protocol) to automatically discover and select the best paths between networks.',
        'choices': [
            ('Static routing', False),
            ('Manual routing', False),
            ('Dynamic routing', True),
            ('Default routing', False),
        ]
    },
    {
        'text': 'What is the primary function of a wireless access point?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A wireless access point (WAP) converts a wired network to include wireless connectivity allowing Wi-Fi devices to connect to the existing wired infrastructure.',
        'choices': [
            ('Replace a router', False),
            ('Convert a wired network to include wireless connectivity', True),
            ('Boost an existing Wi-Fi signal only', False),
            ('Connect two routers together', False),
        ]
    },
    {
        'text': 'What is the key technical difference between a wireless repeater and a Wi-Fi extender?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Extenders can use a wired (Ethernet) backhaul connection to the router which is more efficient. Repeaters must receive and retransmit wirelessly consuming bandwidth twice.',
        'choices': [
            ('Extenders are cheaper', False),
            ('Repeaters support wired backhaul while extenders do not', False),
            ('Extenders can use a wired backhaul connection while repeaters cannot', True),
            ('Repeaters work on 5GHz only', False),
        ]
    },
    {
        'text': 'What is a "backhaul" in the context of Wi-Fi extenders?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'The backhaul is the connection from the extender back to the original router. A wired backhaul (Ethernet cable) is more efficient than a wireless backhaul.',
        'choices': [
            ('The antenna pointing backward', False),
            ('The connection from the extender back to the original router', True),
            ('The signal sent to mobile devices', False),
            ('The security encryption layer', False),
        ]
    },
    {
        'text': 'Why does a wireless repeater reduce available bandwidth for clients?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A wireless repeater must receive the signal then retransmit it wirelessly consuming the wireless bandwidth twice — once for receiving and once for retransmitting.',
        'choices': [
            ('It uses older Wi-Fi standards', False),
            ('It must receive then retransmit the signal wirelessly consuming bandwidth twice', True),
            ('It only supports 2.4 GHz', False),
            ('It does not have an Ethernet port', False),
        ]
    },
    {
        'text': 'What is the primary purpose of a patch panel?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A patch panel acts as a centralized termination point for network cables. All cable runs from throughout a building terminate at the patch panel making organization and troubleshooting much easier.',
        'choices': [
            ('Provide wireless coverage', False),
            ('Act as a centralized termination point for network cables', True),
            ('Replace a switch', False),
            ('Boost network signals', False),
        ]
    },
    {
        'text': 'What type of connector is typically used on the front of a copper patch panel?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Copper patch panels use RJ45 connectors on the front for patch cables connecting to the switch. The rear uses punch-down connections for the permanent cable runs.',
        'choices': [
            ('RJ11', False),
            ('BNC', False),
            ('RJ45', True),
            ('SC fiber', False),
        ]
    },
    {
        'text': 'Why is labeling important on a patch panel?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Labels help identify which port connects to which physical location. This is essential for troubleshooting and moves adds and changes without tracing cables manually.',
        'choices': [
            ('It is required by law', False),
            ('It helps identify which port connects to which physical location for troubleshooting', True),
            ('It speeds up data transmission', False),
            ('It enables VLAN configuration', False),
        ]
    },
    {
        'text': 'Which type of firewall inspects the actual contents of packets not just headers?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A Next-Generation Firewall (NGFW) performs deep packet inspection examining actual packet contents. Basic packet filtering only checks headers and stateful inspection tracks connection state.',
        'choices': [
            ('Packet filtering firewall', False),
            ('Stateful inspection firewall', False),
            ('Next-generation firewall (NGFW)', True),
            ('Host-based firewall', False),
        ]
    },
    {
        'text': 'What is a host-based firewall?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A host-based firewall is software installed on a specific computer to protect that individual system. Windows Defender Firewall is a common example. It differs from network firewalls that protect the entire network.',
        'choices': [
            ('A firewall that protects the entire network', False),
            ('A physical rack-mounted device', False),
            ('Software installed on a specific computer to protect that system', True),
            ('A cloud service', False),
        ]
    },
    {
        'text': 'What does "stateful inspection" mean in firewall terms?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Stateful inspection tracks the state of active connections and only allows traffic that belongs to an already established session. This is more secure than simple packet filtering.',
        'choices': [
            ('It checks packet size', False),
            ('It only allows traffic from already established sessions', True),
            ('It logs all traffic', False),
            ('It scans for viruses', False),
        ]
    },
    {
        'text': 'What is FWaaS?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'FWaaS stands for Firewall as a Service — a cloud-based firewall solution. Instead of deploying physical firewall hardware the firewall runs in the cloud protecting users regardless of location.',
        'choices': [
            ('Firewall with Advanced Security Standards', False),
            ('Firmware as a Standard', False),
            ('Firewall as a Service — a cloud-based firewall solution', True),
            ('Fast Wireless Access Security', False),
        ]
    },
    {
        'text': 'What does PoE stand for and what does it do?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'PoE stands for Power over Ethernet. It delivers both data and electrical power through a single network cable eliminating the need for a separate power adapter for devices like IP cameras and VoIP phones.',
        'choices': [
            ('Protocol over Ethernet — defines communication rules', False),
            ('Power over Ethernet — delivers data and electrical power through a network cable', True),
            ('Port over Ethernet — manages port numbering', False),
            ('Packet over Ethernet — transfers data packets', False),
        ]
    },
    {
        'text': 'What is the maximum power output of the PoE++ standard (802.3bt)?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'PoE++ (802.3bt) supports 60-100 watts. The original PoE (802.3af) supports 15.4W and PoE+ (802.3at) supports 30W. PoE++ enables powering larger devices like laptops and video conferencing systems.',
        'choices': [
            ('15.4 watts', False),
            ('30 watts', False),
            ('60 to 100 watts', True),
            ('200 watts', False),
        ]
    },
    {
        'text': 'Which IEEE standard defines the original PoE specification?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '802.3af defines the original PoE standard at 15.4W. 802.3at is PoE+ at 30W and 802.3bt is PoE++ at 60-100W. 802.11 is the Wi-Fi standard.',
        'choices': [
            ('802.11', False),
            ('802.3af', True),
            ('802.3at', False),
            ('802.3bt', False),
        ]
    },
    {
        'text': 'What device would you use to add PoE capability to an existing non-PoE switch?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A PoE injector adds power to a network cable between a non-PoE switch and a PoE device. This allows PoE devices to be powered without replacing the entire switch.',
        'choices': [
            ('PoE extender', False),
            ('PoE injector', True),
            ('PoE repeater', False),
            ('PoE bridge', False),
        ]
    },
    {
        'text': 'What is the maximum Ethernet cable run distance for PoE?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'The maximum Ethernet cable run is 100 metres (328 feet) for both standard Ethernet and PoE. Beyond this distance signal quality degrades requiring a switch or repeater.',
        'choices': [
            ('50 meters', False),
            ('100 meters', True),
            ('200 meters', False),
            ('Unlimited', False),
        ]
    },
    {
        'text': 'What does the term "modem" stand for?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Modem is short for modulate and demodulate. It converts digital signals from a computer into analog signals for transmission and converts incoming analog signals back to digital.',
        'choices': [
            ('Mobile device network', False),
            ('Modulate and demodulate', True),
            ('Modern networking device', False),
            ('Multi-output device', False),
        ]
    },
    {
        'text': 'What type of cable does a cable modem use?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Cable modems connect via coaxial cable — the same type used for cable TV. This is different from DSL modems which use telephone twisted-pair wiring.',
        'choices': [
            ('Twisted pair (Cat5/6)', False),
            ('Fiber optic', False),
            ('Coaxial cable', True),
            ('Serial cable', False),
        ]
    },
    {
        'text': 'What does ADSL stand for and what does "asymmetric" refer to?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'ADSL stands for Asymmetric Digital Subscriber Line. Asymmetric means download speeds are much higher than upload speeds which suits most home users who download more than they upload.',
        'choices': [
            ('Advanced DSL — supports more devices', False),
            ('Asymmetric DSL — more bandwidth for downloads than uploads', True),
            ('Automated DSL — self-configuring', False),
            ('Analog DSL — uses analog signals only', False),
        ]
    },
    {
        'text': 'What is the latest DOCSIS standard\'s maximum speed?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'DOCSIS 3.1 (the latest widely deployed standard) supports up to 10 Gbps download. DOCSIS 4.0 is emerging and promises even higher speeds.',
        'choices': [
            ('100 Mbps', False),
            ('1 Gbps', False),
            ('10 Gbps', True),
            ('100 Gbps', False),
        ]
    },
    {
        'text': 'Why might cable internet users experience network congestion?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Cable internet shares bandwidth among multiple users in the same neighbourhood. During peak hours when many users are online simultaneously speeds can drop significantly.',
        'choices': [
            ('They use older copper wiring', False),
            ('They share bandwidth among multiple users in the same area', True),
            ('They cannot handle HD video', False),
            ('Their firewall slows traffic', False),
        ]
    },
    {
        'text': 'What does ONT stand for and what is its main function?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'ONT stands for Optical Network Terminal. It converts fiber optic signals (light) to Ethernet signals that home devices can use. It is typically installed where the fiber cable enters the building.',
        'choices': [
            ('Optical Network Terminal — converts fiber optic signals to Ethernet', True),
            ('Open Network Transfer — routes internet traffic', False),
            ('Optical Node Transmitter — broadcasts Wi-Fi', False),
            ('Output Network Terminal — connects a modem to a router', False),
        ]
    },
    {
        'text': 'Why is fiber optic less susceptible to electromagnetic interference than cable or DSL?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Fiber optic uses light for data transmission rather than electrical signals. Light is immune to electromagnetic interference (EMI) making fiber more reliable in environments with electrical equipment.',
        'choices': [
            ('It uses thicker copper wire', False),
            ('It uses light for transmission which is immune to electromagnetic interference', True),
            ('It operates at higher frequencies', False),
            ('It uses digital encoding only', False),
        ]
    },
    {
        'text': 'What does NIC stand for and what is its function?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'NIC stands for Network Interface Card. It enables a device to connect to a network by providing the physical and logical interface between the device and the network medium.',
        'choices': [
            ('Network Intrusion Controller — detects attacks', False),
            ('Network Interface Card — enables a device to connect to a network', True),
            ('Network Identification Code — assigns IP addresses', False),
            ('Node Interconnect Cable — physical network cable', False),
        ]
    },
    {
        'text': 'What is NIC teaming?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'NIC teaming combines multiple NICs into a single logical interface to increase bandwidth and provide redundancy. If one NIC fails the others continue to function.',
        'choices': [
            ('Assigning multiple IP addresses to one NIC', False),
            ('Combining multiple NICs to increase bandwidth and provide redundancy', True),
            ('Connecting NICs from different computers', False),
            ('Using a NIC for both wired and wireless connections simultaneously', False),
        ]
    },
    {
        'text': 'Which network topology is most commonly found in office and home environments?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Star topology is the most common in offices and homes. All devices connect to a central switch or router. It is easy to manage and a single device failure does not affect others.',
        'choices': [
            ('Bus topology', False),
            ('Ring topology', False),
            ('Star topology', True),
            ('Mesh topology', False),
        ]
    },
    {
        'text': 'What is the key characteristic of a mesh topology?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'In a full mesh topology each device connects to every other device providing maximum redundancy. If any link fails traffic can be rerouted through another path.',
        'choices': [
            ('All devices connect to one central hub', False),
            ('Each device connects to every other device', True),
            ('Devices are arranged in a circle', False),
            ('Devices connect in a single line', False),
        ]
    },
    {
        'text': 'What is the main purpose of subnetting?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Subnetting divides a large network into smaller more manageable sub-networks. This improves performance reduces broadcast traffic and enhances security by isolating network segments.',
        'choices': [
            ('To increase internet speed', False),
            ('To divide a large network into smaller more manageable sub-networks', True),
            ('To replace the need for a router', False),
            ('To assign MAC addresses automatically', False),
        ]
    },
    {
        'text': 'In IPv4 how many bits make up an IP address?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'IPv4 addresses are 32 bits long written as four octets (groups of 8 bits) separated by dots. For example 192.168.1.10 — each number represents 8 bits.',
        'choices': [
            ('16 bits', False),
            ('24 bits', False),
            ('32 bits', True),
            ('64 bits', False),
        ]
    },
    {
        'text': 'In the address 192.168.1.10/24 what does the "/24" indicate?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'The /24 (CIDR notation) indicates that 24 bits are allocated to the network portion of the address. This corresponds to a subnet mask of 255.255.255.0 leaving 8 bits for host addresses.',
        'choices': [
            ('There are 24 devices on the network', False),
            ('24 bits are allocated to the network portion (subnet mask)', True),
            ('The network supports 24 subnets', False),
            ('The VLAN ID is 24', False),
        ]
    },
    {
        'text': 'Why are private IP address ranges used in networks?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Private IP addresses do not route over the public internet allowing the same address ranges to be reused across many different private networks. NAT translates them to public IPs for internet access.',
        'choices': [
            ('They are faster than public addresses', False),
            ('They do not route over the public internet allowing reuse across many private networks', True),
            ('They are required by law for home networks', False),
            ('They support IPv6 only', False),
        ]
    },
    {
        'text': 'How many usable host addresses does a /30 subnet provide?',
        'domain': 'Networking',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A /30 subnet has 4 total addresses (2 host bits = 2² = 4). Subtract 1 for the network address and 1 for the broadcast address leaving 2 usable host addresses. /30 is commonly used for point-to-point links.',
        'choices': [
            ('4', False),
            ('2', True),
            ('8', False),
            ('6', False),
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
            db.session.add(Choice(question_id=q.id, text=choice_text, is_correct=is_correct))
        added += 1
    db.session.commit()
    total = Question.query.count()
    core1 = Question.query.filter_by(exam='core1').count()
    print(f'Added {added} questions. Skipped {skipped} duplicates.')
    print(f'Core 1 total: {core1} | Overall: {total}')