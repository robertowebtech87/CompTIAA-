import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app import app, db
from models import Question, Choice

questions_data = [

    # ── NETWORKING ────────────────────────────────────────────────────────────

    {
        'text': 'What does IP stand for in networking?',
        'domain': 'Networking',
        'choices': [
            ('Internet Protocol', True),
            ('Internal Process', False),
            ('Integrated Port', False),
            ('Interface Protocol', False),
        ]
    },
    {
        'text': 'Which IP address class is used for most home and small office networks?',
        'domain': 'Networking',
        'choices': [
            ('Class A', False),
            ('Class B', False),
            ('Class C', True),
            ('Class D', False),
        ]
    },
    {
        'text': 'What is the purpose of a subnet mask?',
        'domain': 'Networking',
        'choices': [
            ('To encrypt data traveling across the network', False),
            ('To divide an IP address into network and host portions', True),
            ('To assign IP addresses automatically to devices', False),
            ('To block unauthorized access to the network', False),
        ]
    },
    {
        'text': 'What does DHCP stand for and what does it do?',
        'domain': 'Networking',
        'choices': [
            ('Dynamic Host Configuration Protocol — it automatically assigns IP addresses to devices on a network', True),
            ('Direct Host Communication Protocol — it enables peer-to-peer connections', False),
            ('Dynamic Hardware Control Protocol — it manages network hardware', False),
            ('Distributed Host Connection Protocol — it distributes bandwidth', False),
        ]
    },
    {
        'text': 'What does DNS stand for and what is its primary function?',
        'domain': 'Networking',
        'choices': [
            ('Data Network System — it routes data packets', False),
            ('Dynamic Name Server — it assigns IP addresses', False),
            ('Domain Name System — it translates domain names into IP addresses', True),
            ('Direct Network Service — it provides internet access', False),
        ]
    },
    {
        'text': 'What is the default subnet mask for a Class C network?',
        'domain': 'Networking',
        'choices': [
            ('255.0.0.0', False),
            ('255.255.0.0', False),
            ('255.255.255.0', True),
            ('255.255.255.255', False),
        ]
    },
    {
        'text': 'Which of the following is a valid private IP address range?',
        'domain': 'Networking',
        'choices': [
            ('8.8.8.0/24', False),
            ('192.168.0.0/16', True),
            ('172.217.0.0/16', False),
            ('204.79.197.0/24', False),
        ]
    },
    {
        'text': 'What port does HTTP use by default?',
        'domain': 'Networking',
        'choices': [
            ('21', False),
            ('25', False),
            ('80', True),
            ('443', False),
        ]
    },
    {
        'text': 'What port does HTTPS use by default?',
        'domain': 'Networking',
        'choices': [
            ('80', False),
            ('443', True),
            ('8080', False),
            ('8443', False),
        ]
    },
    {
        'text': 'What port does FTP use for control connections?',
        'domain': 'Networking',
        'choices': [
            ('20', False),
            ('21', True),
            ('22', False),
            ('23', False),
        ]
    },
    {
        'text': 'What port does SSH use by default?',
        'domain': 'Networking',
        'choices': [
            ('21', False),
            ('22', True),
            ('23', False),
            ('25', False),
        ]
    },
    {
        'text': 'What port does SMTP use for sending email?',
        'domain': 'Networking',
        'choices': [
            ('25', True),
            ('110', False),
            ('143', False),
            ('465', False),
        ]
    },
    {
        'text': 'What port does RDP (Remote Desktop Protocol) use?',
        'domain': 'Networking',
        'choices': [
            ('22', False),
            ('80', False),
            ('3389', True),
            ('5900', False),
        ]
    },
    {
        'text': 'What is the loopback address in IPv4?',
        'domain': 'Networking',
        'choices': [
            ('0.0.0.0', False),
            ('127.0.0.1', True),
            ('192.168.1.1', False),
            ('255.255.255.255', False),
        ]
    },
    {
        'text': 'What type of device operates at Layer 3 of the OSI model and routes traffic between networks?',
        'domain': 'Networking',
        'choices': [
            ('Switch', False),
            ('Hub', False),
            ('Router', True),
            ('Access point', False),
        ]
    },
    {
        'text': 'What is the main difference between a hub and a switch?',
        'domain': 'Networking',
        'choices': [
            ('A hub is faster than a switch', False),
            ('A switch broadcasts data to all ports while a hub sends data only to the destination port', False),
            ('A hub sends data to all ports while a switch sends data only to the destination port', True),
            ('A hub operates at Layer 3 while a switch operates at Layer 2', False),
        ]
    },
    {
        'text': 'What does MAC address stand for?',
        'domain': 'Networking',
        'choices': [
            ('Machine Access Code', False),
            ('Media Access Control', True),
            ('Multiple Address Channel', False),
            ('Master Address Configuration', False),
        ]
    },
    {
        'text': 'What is the purpose of ARP (Address Resolution Protocol)?',
        'domain': 'Networking',
        'choices': [
            ('To assign IP addresses dynamically', False),
            ('To translate domain names to IP addresses', False),
            ('To map IP addresses to MAC addresses on a local network', True),
            ('To encrypt network traffic between two hosts', False),
        ]
    },
    {
        'text': 'What does NAT stand for and what is its purpose?',
        'domain': 'Networking',
        'choices': [
            ('Network Address Translation — it allows multiple devices to share a single public IP address', True),
            ('Network Access Technology — it controls who can access the network', False),
            ('Node Assignment Table — it tracks which devices are on the network', False),
            ('Network Authentication Token — it verifies user identity', False),
        ]
    },
    {
        'text': 'What is the difference between TCP and UDP?',
        'domain': 'Networking',
        'choices': [
            ('TCP is faster but unreliable, UDP is slower but reliable', False),
            ('TCP provides reliable, ordered delivery with error checking while UDP is faster but does not guarantee delivery', True),
            ('TCP is used for wireless connections and UDP for wired connections', False),
            ('TCP and UDP are identical protocols used for different port ranges', False),
        ]
    },
    {
        'text': 'What is a VLAN?',
        'domain': 'Networking',
        'choices': [
            ('A physical network segment separated by a router', False),
            ('A virtual private network that encrypts internet traffic', False),
            ('A logical grouping of network devices regardless of physical location that segments a network for security and performance', True),
            ('A wireless network standard that operates at 5 GHz', False),
        ]
    },
    {
        'text': 'What does PoE stand for and what is its benefit?',
        'domain': 'Networking',
        'choices': [
            ('Power over Ethernet — it allows network cables to carry electrical power to devices like IP cameras and access points', True),
            ('Port over Ethernet — it allows multiple ports to share one cable', False),
            ('Protocol over Ethernet — it encapsulates multiple protocols in one connection', False),
            ('Packet over Ethernet — it improves packet delivery speed', False),
        ]
    },
    {
        'text': 'What is the maximum cable length for a standard Cat5e or Cat6 Ethernet cable run?',
        'domain': 'Networking',
        'choices': [
            ('50 meters', False),
            ('100 meters', True),
            ('150 meters', False),
            ('200 meters', False),
        ]
    },
    {
        'text': 'Which wireless standard offers the fastest theoretical maximum speed?',
        'domain': 'Networking',
        'choices': [
            ('802.11g', False),
            ('802.11n', False),
            ('802.11ac (Wi-Fi 5)', False),
            ('802.11ax (Wi-Fi 6)', True),
        ]
    },
    {
        'text': 'What is the purpose of a default gateway?',
        'domain': 'Networking',
        'choices': [
            ('To provide wireless access to the network', False),
            ('To assign IP addresses to devices on the network', False),
            ('To forward traffic from a local network to other networks such as the internet', True),
            ('To block malicious traffic from entering the network', False),
        ]
    },
    {
        'text': 'What command is used to test basic network connectivity to another host?',
        'domain': 'Networking',
        'choices': [
            ('ipconfig', False),
            ('tracert', False),
            ('ping', True),
            ('netstat', False),
        ]
    },
    {
        'text': 'What does the ipconfig command display on a Windows system?',
        'domain': 'Networking',
        'choices': [
            ('A list of all active network connections and their ports', False),
            ('The current IP address, subnet mask, and default gateway of network adapters', True),
            ('The route packets take to reach a destination', False),
            ('The MAC addresses of all devices on the local network', False),
        ]
    },
    {
        'text': 'What does the tracert command do?',
        'domain': 'Networking',
        'choices': [
            ('Tests if a remote host is reachable', False),
            ('Displays current network adapter configuration', False),
            ('Shows the route packets take to reach a destination, including each hop', True),
            ('Lists all open network ports on the local machine', False),
        ]
    },
    {
        'text': 'What is an APIPA address and when does a device use one?',
        'domain': 'Networking',
        'choices': [
            ('A static IP address manually assigned by an administrator', False),
            ('A public IP address assigned by the ISP', False),
            ('An Automatic Private IP Address in the 169.254.x.x range that a device assigns itself when it cannot reach a DHCP server', True),
            ('An IPv6 address used when IPv4 is unavailable', False),
        ]
    },
    {
        'text': 'What type of cable is used to directly connect two computers without a switch?',
        'domain': 'Networking',
        'choices': [
            ('Straight-through cable', False),
            ('Crossover cable', True),
            ('Rollover cable', False),
            ('Coaxial cable', False),
        ]
    },
    {
        'text': 'What is the purpose of a firewall in a network?',
        'domain': 'Networking',
        'choices': [
            ('To increase network speed by caching frequently accessed data', False),
            ('To assign IP addresses to devices on the network', False),
            ('To monitor and control incoming and outgoing network traffic based on security rules', True),
            ('To convert between wired and wireless network connections', False),
        ]
    },
    {
        'text': 'What does VPN stand for and what does it do?',
        'domain': 'Networking',
        'choices': [
            ('Virtual Private Network — it creates an encrypted tunnel over a public network to securely connect remote users or sites', True),
            ('Virtual Port Number — it assigns virtual port addresses to applications', False),
            ('Verified Protocol Node — it authenticates network nodes', False),
            ('Variable Packet Network — it optimizes packet sizes for better performance', False),
        ]
    },
    {
        'text': 'What is a network topology?',
        'domain': 'Networking',
        'choices': [
            ('The physical location of network servers', False),
            ('The arrangement or layout of how devices are connected in a network', True),
            ('The speed and bandwidth of a network connection', False),
            ('The security protocols used on a network', False),
        ]
    },
    {
        'text': 'In a star topology, what happens if the central switch fails?',
        'domain': 'Networking',
        'choices': [
            ('Only the devices closest to the switch lose connectivity', False),
            ('The network continues to function through alternative paths', False),
            ('All devices on the network lose connectivity', True),
            ('The network automatically switches to a ring topology', False),
        ]
    },
    {
        'text': 'What does the netstat command show?',
        'domain': 'Networking',
        'choices': [
            ('The IP configuration of all network adapters', False),
            ('Active network connections, listening ports, and network statistics', True),
            ('The route taken by packets to a destination', False),
            ('The MAC address table of a switch', False),
        ]
    },
    {
        'text': 'What is the difference between Cat5e and Cat6 Ethernet cables?',
        'domain': 'Networking',
        'choices': [
            ('Cat5e supports 10 Gbps while Cat6 only supports 1 Gbps', False),
            ('Cat6 supports higher frequencies and reduced crosstalk compared to Cat5e, making it better for 10 Gbps over short distances', True),
            ('Cat5e uses fiber optic technology while Cat6 uses copper', False),
            ('There is no practical difference between Cat5e and Cat6', False),
        ]
    },
    {
        'text': 'What is the purpose of QoS (Quality of Service) in networking?',
        'domain': 'Networking',
        'choices': [
            ('To encrypt data transmitted over the network', False),
            ('To prioritize certain types of network traffic to ensure performance for critical applications like VoIP and video', True),
            ('To automatically assign IP addresses to new devices', False),
            ('To monitor network performance and alert administrators to issues', False),
        ]
    },
    {
        'text': 'What does SSID stand for in wireless networking?',
        'domain': 'Networking',
        'choices': [
            ('Secure System ID', False),
            ('Service Set Identifier — the name of a wireless network', True),
            ('Static Station Internet Device', False),
            ('Subnet Segment ID', False),
        ]
    },
    {
        'text': 'What is the purpose of WPA3 in wireless networking?',
        'domain': 'Networking',
        'choices': [
            ('It is a cable standard for high-speed wired connections', False),
            ('It is the latest wireless security protocol that provides stronger encryption than WPA2', True),
            ('It is a wireless frequency band above 5 GHz', False),
            ('It is a protocol that extends Wi-Fi range using mesh networking', False),
        ]
    },
    {
        'text': 'What is a proxy server?',
        'domain': 'Networking',
        'choices': [
            ('A server that assigns IP addresses to network clients', False),
            ('A server that acts as an intermediary between clients and the internet, providing caching, filtering, and security', True),
            ('A server that stores backup copies of network data', False),
            ('A server that manages wireless access points on the network', False),
        ]
    },
    {
        'text': 'What happens when you type ipconfig /release and then ipconfig /renew on Windows?',
        'domain': 'Networking',
        'choices': [
            ('It resets the network adapter driver', False),
            ('It releases the current DHCP-assigned IP address and requests a new one from the DHCP server', True),
            ('It clears the DNS cache and refreshes DNS settings', False),
            ('It restarts all network services on the machine', False),
        ]
    },
    {
        'text': 'What is a DMZ in network security?',
        'domain': 'Networking',
        'choices': [
            ('A type of VPN connection used for remote access', False),
            ('A network segment that sits between a trusted internal network and an untrusted external network, hosting publicly accessible services', True),
            ('A zone on a switch where all traffic is blocked', False),
            ('A wireless security protocol stronger than WPA2', False),
        ]
    },
    {
        'text': 'What is the IPv6 loopback address?',
        'domain': 'Networking',
        'choices': [
            ('::0', False),
            ('::1', True),
            ('fe80::1', False),
            ('ff02::1', False),
        ]
    },
    {
        'text': 'What does the nslookup command do?',
        'domain': 'Networking',
        'choices': [
            ('It displays the current network speed and bandwidth', False),
            ('It queries DNS servers to look up domain name to IP address mappings', True),
            ('It lists all connected devices on the local network', False),
            ('It tests connectivity to a remote host using ICMP', False),
        ]
    },
    {
        'text': 'What type of connector is used on standard Ethernet cables?',
        'domain': 'Networking',
        'choices': [
            ('RJ11', False),
            ('RJ45', True),
            ('BNC', False),
            ('LC', False),
        ]
    },
    {
        'text': 'What is the purpose of a network switch?',
        'domain': 'Networking',
        'choices': [
            ('To connect different networks together and route traffic between them', False),
            ('To connect multiple devices within the same network and forward frames based on MAC addresses', True),
            ('To provide wireless connectivity to mobile devices', False),
            ('To assign IP addresses to devices on the network', False),
        ]
    },
    {
        'text': 'What does the acronym OSI stand for in the OSI model?',
        'domain': 'Networking',
        'choices': [
            ('Open System Interconnection', True),
            ('Organized System Interface', False),
            ('Open Standard Internet', False),
            ('Operational System Integration', False),
        ]
    },
    {
        'text': 'How many layers does the OSI model have?',
        'domain': 'Networking',
        'choices': [
            ('4', False),
            ('5', False),
            ('7', True),
            ('9', False),
        ]
    },
    {
        'text': 'At which OSI layer do routers operate?',
        'domain': 'Networking',
        'choices': [
            ('Layer 1 — Physical', False),
            ('Layer 2 — Data Link', False),
            ('Layer 3 — Network', True),
            ('Layer 4 — Transport', False),
        ]
    },
    {
        'text': 'What is the purpose of ICMP in networking?',
        'domain': 'Networking',
        'choices': [
            ('To encrypt data between two network hosts', False),
            ('To assign IP addresses automatically', False),
            ('To send error messages and operational information about network conditions — used by tools like ping and tracert', True),
            ('To establish reliable connections between applications', False),
        ]
    },

    # ── OPERATING SYSTEMS ─────────────────────────────────────────────────────

    {
        'text': 'What is the primary function of an operating system?',
        'domain': 'Operating Systems',
        'choices': [
            ('To provide internet connectivity to the computer', False),
            ('To manage hardware resources and provide services to application software', True),
            ('To protect the computer from viruses and malware', False),
            ('To store and retrieve files from the hard drive', False),
        ]
    },
    {
        'text': 'What is the Windows Registry?',
        'domain': 'Operating Systems',
        'choices': [
            ('A list of all installed software and their version numbers', False),
            ('A hierarchical database that stores low-level settings for Windows and installed applications', True),
            ('A log file that records all system errors and events', False),
            ('A folder containing all Windows system files and drivers', False),
        ]
    },
    {
        'text': 'What command opens the Windows Registry Editor?',
        'domain': 'Operating Systems',
        'choices': [
            ('regedit', True),
            ('msconfig', False),
            ('devmgmt.msc', False),
            ('services.msc', False),
        ]
    },
    {
        'text': 'What does msconfig do in Windows?',
        'domain': 'Operating Systems',
        'choices': [
            ('It opens the Windows Security Center', False),
            ('It opens System Configuration to manage startup programs, boot options, and services', True),
            ('It displays all installed hardware and drivers', False),
            ('It opens the Windows Update settings', False),
        ]
    },
    {
        'text': 'What is the Windows file system used on most modern Windows installations?',
        'domain': 'Operating Systems',
        'choices': [
            ('FAT32', False),
            ('exFAT', False),
            ('NTFS', True),
            ('ext4', False),
        ]
    },
    {
        'text': 'What is the difference between FAT32 and NTFS?',
        'domain': 'Operating Systems',
        'choices': [
            ('FAT32 supports larger file sizes than NTFS', False),
            ('NTFS supports larger files, file permissions, encryption, and journaling while FAT32 has a 4GB maximum file size limit', True),
            ('FAT32 is faster than NTFS for all operations', False),
            ('NTFS is only used on external drives while FAT32 is used for internal drives', False),
        ]
    },
    {
        'text': 'What is the purpose of the Windows Task Manager?',
        'domain': 'Operating Systems',
        'choices': [
            ('To schedule automated tasks and backups', False),
            ('To monitor running processes, CPU and memory usage, and manage startup applications', True),
            ('To manage user accounts and permissions', False),
            ('To configure network settings and connections', False),
        ]
    },
    {
        'text': 'How do you open Task Manager quickly in Windows?',
        'domain': 'Operating Systems',
        'choices': [
            ('Ctrl + Alt + Delete, then select Task Manager', False),
            ('Ctrl + Shift + Esc', False),
            ('Both Ctrl+Alt+Delete and Ctrl+Shift+Esc can open Task Manager', True),
            ('Right-clicking the desktop and selecting Task Manager', False),
        ]
    },
    {
        'text': 'What is the purpose of the Windows Device Manager?',
        'domain': 'Operating Systems',
        'choices': [
            ('To manage user accounts on the system', False),
            ('To view, update, and troubleshoot hardware device drivers', True),
            ('To configure network sharing settings', False),
            ('To manage installed applications and programs', False),
        ]
    },
    {
        'text': 'What does a yellow exclamation mark next to a device in Device Manager indicate?',
        'domain': 'Operating Systems',
        'choices': [
            ('The device is working correctly but needs an update', False),
            ('The device has a driver problem or is not functioning correctly', True),
            ('The device is disabled but available', False),
            ('The device requires a restart to complete installation', False),
        ]
    },
    {
        'text': 'What is the Windows command to check and repair file system errors?',
        'domain': 'Operating Systems',
        'choices': [
            ('sfc /scannow', False),
            ('chkdsk /f', True),
            ('diskpart', False),
            ('format /q', False),
        ]
    },
    {
        'text': 'What does the sfc /scannow command do?',
        'domain': 'Operating Systems',
        'choices': [
            ('It scans the hard drive for bad sectors and repairs them', False),
            ('It scans and repairs corrupted or missing Windows system files', True),
            ('It scans installed programs for outdated versions', False),
            ('It scans the network for security vulnerabilities', False),
        ]
    },
    {
        'text': 'What is the purpose of the Windows Event Viewer?',
        'domain': 'Operating Systems',
        'choices': [
            ('To view and stream media files on the computer', False),
            ('To view logs of system events, errors, warnings, and application activity', True),
            ('To monitor live network traffic on the system', False),
            ('To view the history of Windows Update installations', False),
        ]
    },
    {
        'text': 'What is the default location of Windows system files?',
        'domain': 'Operating Systems',
        'choices': [
            ('C:\\Program Files', False),
            ('C:\\Users', False),
            ('C:\\Windows\\System32', True),
            ('C:\\ProgramData', False),
        ]
    },
    {
        'text': 'What is the purpose of Windows Update?',
        'domain': 'Operating Systems',
        'choices': [
            ('To upgrade the Windows version to the latest release only', False),
            ('To deliver security patches, bug fixes, and feature updates to keep the OS secure and stable', True),
            ('To update all installed third-party applications', False),
            ('To synchronize files with OneDrive cloud storage', False),
        ]
    },
    {
        'text': 'What is Safe Mode in Windows?',
        'domain': 'Operating Systems',
        'choices': [
            ('A mode that prevents any changes from being saved to the system', False),
            ('A diagnostic startup mode that loads only essential drivers and services, used for troubleshooting', True),
            ('A mode that encrypts all data on the drive for security', False),
            ('A parental control mode that restricts access to certain applications', False),
        ]
    },
    {
        'text': 'How do you access the Windows boot options to enter Safe Mode on a modern Windows 10/11 system?',
        'domain': 'Operating Systems',
        'choices': [
            ('Press F8 repeatedly during boot', False),
            ('Hold Shift while clicking Restart, then navigate to Troubleshoot > Advanced Options > Startup Settings', True),
            ('Press Ctrl+Alt+Delete during the boot screen', False),
            ('Type safemode in the Run dialog', False),
        ]
    },
    {
        'text': 'What is the purpose of the Windows Recycle Bin?',
        'domain': 'Operating Systems',
        'choices': [
            ('To permanently delete files immediately to free up space', False),
            ('To temporarily store deleted files so they can be recovered before permanent deletion', True),
            ('To store system temporary files that can be safely removed', False),
            ('To archive old files that have not been accessed recently', False),
        ]
    },
    {
        'text': 'What is the difference between 32-bit and 64-bit operating systems?',
        'domain': 'Operating Systems',
        'choices': [
            ('32-bit systems are faster for gaming and multimedia tasks', False),
            ('64-bit systems can address more RAM and process more data per clock cycle than 32-bit systems', True),
            ('32-bit and 64-bit refer to the screen resolution the OS supports', False),
            ('64-bit systems can only run on Intel processors', False),
        ]
    },
    {
        'text': 'What is the maximum RAM that a 32-bit operating system can address?',
        'domain': 'Operating Systems',
        'choices': [
            ('2 GB', False),
            ('4 GB', True),
            ('8 GB', False),
            ('16 GB', False),
        ]
    },
    {
        'text': 'What does UAC stand for in Windows and what is its purpose?',
        'domain': 'Operating Systems',
        'choices': [
            ('User Account Control — it prompts for confirmation or credentials before allowing changes that require administrator privileges', True),
            ('Unified Access Configuration — it manages network access settings', False),
            ('User Authentication Certificate — it verifies user identity on the network', False),
            ('Universal App Controller — it manages Windows Store applications', False),
        ]
    },
    {
        'text': 'What is the Windows command prompt command to display all running processes?',
        'domain': 'Operating Systems',
        'choices': [
            ('tasklist', True),
            ('proclist', False),
            ('showproc', False),
            ('pslist', False),
        ]
    },
    {
        'text': 'What is the purpose of virtual memory in an operating system?',
        'domain': 'Operating Systems',
        'choices': [
            ('To create virtual machines on the system', False),
            ('To extend available RAM by using a portion of the hard drive as additional memory when physical RAM is full', True),
            ('To allocate memory between multiple users on the same system', False),
            ('To encrypt memory contents to prevent data theft', False),
        ]
    },
    {
        'text': 'What is the Windows pagefile and what is its function?',
        'domain': 'Operating Systems',
        'choices': [
            ('A file that stores web page cache for faster browsing', False),
            ('A hidden system file on the hard drive that Windows uses as virtual memory when RAM is insufficient', True),
            ('A file that logs all page faults and memory errors', False),
            ('A configuration file for the Windows boot loader', False),
        ]
    },
    {
        'text': 'What command is used in Windows to see the IP configuration of network adapters?',
        'domain': 'Operating Systems',
        'choices': [
            ('netstat', False),
            ('ipconfig', True),
            ('ifconfig', False),
            ('netconfig', False),
        ]
    },
    {
        'text': 'What is the purpose of the Windows command gpupdate /force?',
        'domain': 'Operating Systems',
        'choices': [
            ('It forces a Windows Update check and installation', False),
            ('It immediately applies all Group Policy settings without waiting for the next automatic refresh', True),
            ('It updates all installed GPU drivers on the system', False),
            ('It resets all Group Policy settings to their defaults', False),
        ]
    },
    {
        'text': 'What file extension do Windows executable program files typically use?',
        'domain': 'Operating Systems',
        'choices': [
            ('.bat', False),
            ('.sys', False),
            ('.exe', True),
            ('.dll', False),
        ]
    },
    {
        'text': 'What is a DLL file in Windows?',
        'domain': 'Operating Systems',
        'choices': [
            ('A log file that records disk errors', False),
            ('A Dynamic Link Library — a file containing code and data that multiple programs can use simultaneously', True),
            ('A driver file for hardware devices', False),
            ('A Windows system backup file', False),
        ]
    },
    {
        'text': 'What does the Windows command diskpart do?',
        'domain': 'Operating Systems',
        'choices': [
            ('It defragments the hard drive to improve performance', False),
            ('It checks the disk for errors and bad sectors', False),
            ('It is a command-line tool for managing disk partitions, volumes, and virtual hard disks', True),
            ('It displays disk usage statistics for all drives', False),
        ]
    },
    {
        'text': 'What is the purpose of System Restore in Windows?',
        'domain': 'Operating Systems',
        'choices': [
            ('To restore deleted files from the Recycle Bin', False),
            ('To return Windows system files and settings to a previous point in time without affecting personal files', True),
            ('To reinstall Windows from scratch to fix serious issues', False),
            ('To restore the computer to factory settings', False),
        ]
    },
    {
        'text': 'What is the difference between a local user account and a Microsoft account in Windows?',
        'domain': 'Operating Systems',
        'choices': [
            ('Local accounts have more privileges than Microsoft accounts', False),
            ('A local account exists only on the device while a Microsoft account syncs settings and data across devices via the cloud', True),
            ('Microsoft accounts can only be used on Windows 11 and newer', False),
            ('Local accounts require internet access to log in', False),
        ]
    },
    {
        'text': 'What is the Windows command to flush the DNS resolver cache?',
        'domain': 'Operating Systems',
        'choices': [
            ('ipconfig /release', False),
            ('netsh reset', False),
            ('ipconfig /flushdns', True),
            ('dns /clear', False),
        ]
    },
    {
        'text': 'What does the acronym GUI stand for?',
        'domain': 'Operating Systems',
        'choices': [
            ('General User Interface', False),
            ('Graphical User Interface', True),
            ('Generic Unified Interface', False),
            ('Global User Input', False),
        ]
    },
    {
        'text': 'What is the macOS equivalent of Windows Task Manager?',
        'domain': 'Operating Systems',
        'choices': [
            ('System Preferences', False),
            ('Console', False),
            ('Activity Monitor', True),
            ('Terminal', False),
        ]
    },
    {
        'text': 'What type of file system does macOS use on modern Macs?',
        'domain': 'Operating Systems',
        'choices': [
            ('HFS+', False),
            ('NTFS', False),
            ('APFS (Apple File System)', True),
            ('ext4', False),
        ]
    },
    {
        'text': 'What is the Linux command to list files and directories?',
        'domain': 'Operating Systems',
        'choices': [
            ('dir', False),
            ('list', False),
            ('ls', True),
            ('show', False),
        ]
    },
    {
        'text': 'What does the command cd mean in both Windows and Linux?',
        'domain': 'Operating Systems',
        'choices': [
            ('Copy Directory', False),
            ('Change Drive', False),
            ('Change Directory — it navigates to a different folder', True),
            ('Clear Display', False),
        ]
    },
    {
        'text': 'What is the purpose of the Windows hosts file?',
        'domain': 'Operating Systems',
        'choices': [
            ('It stores the login credentials for network hosts', False),
            ('It maps hostnames to IP addresses and is checked before DNS queries', True),
            ('It contains a list of trusted websites for the browser', False),
            ('It stores network adapter configuration settings', False),
        ]
    },
    {
        'text': 'What is the Windows command to repair the Master Boot Record?',
        'domain': 'Operating Systems',
        'choices': [
            ('chkdsk /mbr', False),
            ('fixmbr', False),
            ('bootrec /fixmbr', True),
            ('repair-bcd', False),
        ]
    },
    {
        'text': 'What does OS stand for?',
        'domain': 'Operating Systems',
        'choices': [
            ('Output System', False),
            ('Operating System', True),
            ('Online Service', False),
            ('Optical Storage', False),
        ]
    },

    # ── SECURITY ──────────────────────────────────────────────────────────────

    {
        'text': 'What is malware?',
        'domain': 'Security',
        'choices': [
            ('Hardware that is damaged or malfunctioning', False),
            ('Any software intentionally designed to cause damage, disruption, or unauthorized access to a computer system', True),
            ('Software that runs in the background consuming system resources', False),
            ('A type of network attack that floods a server with requests', False),
        ]
    },
    {
        'text': 'What is a computer virus?',
        'domain': 'Security',
        'choices': [
            ('Any type of malicious software that damages a computer', False),
            ('A type of malware that attaches itself to a legitimate program and spreads when the infected program is run', True),
            ('A program that displays unwanted advertisements', False),
            ('A program that encrypts files and demands a ransom', False),
        ]
    },
    {
        'text': 'What is ransomware?',
        'domain': 'Security',
        'choices': [
            ('Malware that records keystrokes to steal passwords', False),
            ('Software that displays pop-up advertisements', False),
            ('A type of malware that encrypts the victim\'s files and demands payment for the decryption key', True),
            ('A program that secretly sends user data to a third party', False),
        ]
    },
    {
        'text': 'What is a Trojan horse in cybersecurity?',
        'domain': 'Security',
        'choices': [
            ('A firewall that blocks unauthorized access', False),
            ('Malware disguised as legitimate software that performs malicious actions once installed', True),
            ('A virus that replicates itself across a network without user interaction', False),
            ('A type of attack that overwhelms a server with traffic', False),
        ]
    },
    {
        'text': 'What is a worm in cybersecurity?',
        'domain': 'Security',
        'choices': [
            ('Malware that requires user interaction to spread', False),
            ('A type of spyware that records keystrokes', False),
            ('Self-replicating malware that spreads across networks without needing to attach to a host file or user interaction', True),
            ('A program that displays unwanted advertisements', False),
        ]
    },
    {
        'text': 'What is spyware?',
        'domain': 'Security',
        'choices': [
            ('Software used by IT administrators to monitor network performance', False),
            ('Malware that secretly monitors and collects user activity, often sending it to a third party without consent', True),
            ('A type of firewall that inspects encrypted traffic', False),
            ('Software that blocks access to certain websites', False),
        ]
    },
    {
        'text': 'What is a phishing attack?',
        'domain': 'Security',
        'choices': [
            ('A brute force attack that tries every possible password combination', False),
            ('A social engineering attack that tricks users into revealing sensitive information through fake emails or websites that appear legitimate', True),
            ('An attack that intercepts network traffic between two parties', False),
            ('An attack that exploits vulnerabilities in unpatched software', False),
        ]
    },
    {
        'text': 'What is a DDoS attack?',
        'domain': 'Security',
        'choices': [
            ('An attack that encrypts all data on a target system', False),
            ('An attack that steals login credentials using fake login pages', False),
            ('A Distributed Denial of Service attack that overwhelms a target with traffic from multiple sources to make it unavailable', True),
            ('An attack that intercepts and reads encrypted communications', False),
        ]
    },
    {
        'text': 'What is multi-factor authentication (MFA)?',
        'domain': 'Security',
        'choices': [
            ('Using multiple passwords for different accounts', False),
            ('A security method requiring users to verify identity using two or more different types of credentials', True),
            ('A system that manages passwords for multiple accounts', False),
            ('Authentication that works across multiple devices simultaneously', False),
        ]
    },
    {
        'text': 'What are the three factors used in multi-factor authentication?',
        'domain': 'Security',
        'choices': [
            ('Username, password, and email', False),
            ('Something you know, something you have, and something you are', True),
            ('PIN, password, and security question', False),
            ('Email, phone number, and physical address', False),
        ]
    },
    {
        'text': 'What is the purpose of encryption?',
        'domain': 'Security',
        'choices': [
            ('To compress data for faster transmission', False),
            ('To convert data into an unreadable format that can only be decoded with the correct key', True),
            ('To back up data to a secure location', False),
            ('To scan data for viruses before transmission', False),
        ]
    },
    {
        'text': 'What is BitLocker?',
        'domain': 'Security',
        'choices': [
            ('A Windows antivirus program', False),
            ('A password manager built into Windows', False),
            ('A Windows full-disk encryption feature that protects data if the drive is stolen or removed', True),
            ('A Windows firewall configuration tool', False),
        ]
    },
    {
        'text': 'What is the principle of least privilege?',
        'domain': 'Security',
        'choices': [
            ('Giving all users administrator access for maximum productivity', False),
            ('Restricting user access rights to only what is necessary to perform their job function', True),
            ('Limiting internet access to only approved websites', False),
            ('Requiring users to change passwords every 30 days', False),
        ]
    },
    {
        'text': 'What is a strong password policy?',
        'domain': 'Security',
        'choices': [
            ('Requiring passwords to be at least 4 characters and changed yearly', False),
            ('Using the same password across all systems for consistency', False),
            ('Requiring passwords to be long, complex, unique, and changed regularly', True),
            ('Using only numbers in passwords for simplicity', False),
        ]
    },
    {
        'text': 'What is social engineering in cybersecurity?',
        'domain': 'Security',
        'choices': [
            ('Using automation tools to manage social media accounts', False),
            ('Manipulating people into revealing confidential information or performing actions that compromise security', True),
            ('Building social networks within a corporate environment', False),
            ('Using machine learning to detect security threats', False),
        ]
    },
    {
        'text': 'What is a zero-day vulnerability?',
        'domain': 'Security',
        'choices': [
            ('A vulnerability that has been patched for zero days', False),
            ('A security flaw that is unknown to the software vendor and has no available patch', True),
            ('A vulnerability in new software released on its launch day', False),
            ('A vulnerability that only affects systems that have never been updated', False),
        ]
    },
    {
        'text': 'What does antivirus software do?',
        'domain': 'Security',
        'choices': [
            ('It monitors network traffic and blocks unauthorized connections', False),
            ('It detects, prevents, and removes malicious software from a computer', True),
            ('It encrypts files to prevent unauthorized access', False),
            ('It creates backups of important system files', False),
        ]
    },
    {
        'text': 'What is the purpose of a DMZ in network security?',
        'domain': 'Security',
        'choices': [
            ('To provide a fully trusted internal network segment', False),
            ('To create an isolated network zone for publicly accessible servers that separates them from the internal network', True),
            ('To encrypt all traffic leaving the corporate network', False),
            ('To store backup data in a secure offsite location', False),
        ]
    },
    {
        'text': 'What is tailgating in physical security?',
        'domain': 'Security',
        'choices': [
            ('Following someone too closely while driving to their workplace', False),
            ('Unauthorized entry into a secured area by following an authorized person through a secure door', True),
            ('Installing tracking software on someone\'s device without permission', False),
            ('An attack that intercepts wireless communications', False),
        ]
    },
    {
        'text': 'What is the purpose of a VPN from a security perspective?',
        'domain': 'Security',
        'choices': [
            ('To increase internet speed by routing through faster servers', False),
            ('To encrypt internet traffic and hide the user\'s IP address, protecting data on untrusted networks', True),
            ('To block malicious websites and advertisements', False),
            ('To back up data securely to the cloud', False),
        ]
    },
    {
        'text': 'What is a brute force attack?',
        'domain': 'Security',
        'choices': [
            ('A physical attack that damages computer hardware', False),
            ('An attack that tricks users into clicking malicious links', False),
            ('An attack that systematically tries every possible combination of characters to guess a password', True),
            ('An attack that floods a network with excessive traffic', False),
        ]
    },
    {
        'text': 'What is the purpose of Windows Defender?',
        'domain': 'Security',
        'choices': [
            ('To manage user accounts and permissions in Windows', False),
            ('A built-in Windows security tool that provides real-time protection against malware, viruses, and other threats', True),
            ('To configure Windows Firewall rules', False),
            ('To encrypt files and folders in Windows', False),
        ]
    },
    {
        'text': 'What is a Man-in-the-Middle (MitM) attack?',
        'domain': 'Security',
        'choices': [
            ('An attack where the attacker sits between two communicating parties, intercepting and potentially altering their communications', True),
            ('An attack that uses multiple systems to overwhelm a target', False),
            ('An attack that installs malware by disguising it as legitimate software', False),
            ('An attack that guesses passwords by trying all combinations', False),
        ]
    },
    {
        'text': 'What should you do if you receive a suspicious email asking for your login credentials?',
        'domain': 'Security',
        'choices': [
            ('Reply to verify if the email is legitimate', False),
            ('Click the link to check if it leads to a real website', False),
            ('Do not click any links or provide any information — report the email as phishing and delete it', True),
            ('Forward the email to your contacts to warn them', False),
        ]
    },
    {
        'text': 'What is the purpose of a password manager?',
        'domain': 'Security',
        'choices': [
            ('To enforce password policies across a corporate network', False),
            ('To securely store and manage multiple complex passwords so users only need to remember one master password', True),
            ('To automatically change passwords on a schedule', False),
            ('To recover forgotten passwords from encrypted drives', False),
        ]
    },
    {
        'text': 'What does HTTPS indicate about a website?',
        'domain': 'Security',
        'choices': [
            ('The website is free of malware and safe to use', False),
            ('The website is owned by a verified company', False),
            ('The connection between your browser and the website is encrypted using SSL/TLS', True),
            ('The website has been approved by a government authority', False),
        ]
    },
    {
        'text': 'What is adware?',
        'domain': 'Security',
        'choices': [
            ('Software used to block advertisements on websites', False),
            ('Malware that displays unwanted advertisements, often bundled with free software', True),
            ('A type of ransomware that locks advertising accounts', False),
            ('Software that analyzes advertising data for marketing purposes', False),
        ]
    },
    {
        'text': 'What is the best defense against ransomware?',
        'domain': 'Security',
        'choices': [
            ('Paying the ransom immediately to recover files quickly', False),
            ('Disabling all internet access on the affected machine', False),
            ('Maintaining regular offline backups of critical data so files can be restored without paying a ransom', True),
            ('Installing multiple antivirus programs simultaneously', False),
        ]
    },
    {
        'text': 'What is physical security in the context of IT?',
        'domain': 'Security',
        'choices': [
            ('The practice of installing physical firewalls in server rooms', False),
            ('Measures that protect hardware, software, and data from physical actions and events', True),
            ('The process of physically destroying old hard drives', False),
            ('Security software that monitors physical keyboard input', False),
        ]
    },
    {
        'text': 'What is the purpose of a TPM chip?',
        'domain': 'Security',
        'choices': [
            ('To improve CPU thermal management', False),
            ('To provide hardware-based security functions including encryption key storage and platform integrity verification', True),
            ('To manage power supply to system components', False),
            ('To accelerate GPU rendering performance', False),
        ]
    },
    {
        'text': 'What does SSL/TLS stand for and what is its purpose?',
        'domain': 'Security',
        'choices': [
            ('Secure Socket Layer / Transport Layer Security — protocols that encrypt data transmitted between a client and server', True),
            ('System Security Lock / Transfer Level Shield — protocols that lock down system access', False),
            ('Secure Server Link / Trusted Link Standard — standards for server authentication', False),
            ('Simple Security Layer / Terminal Lock System — tools for terminal security', False),
        ]
    },
    {
        'text': 'What is the purpose of an Intrusion Detection System (IDS)?',
        'domain': 'Security',
        'choices': [
            ('To automatically block unauthorized network access', False),
            ('To monitor network or system activity and alert administrators to potential security policy violations or attacks', True),
            ('To manage user authentication and authorization', False),
            ('To encrypt all inbound and outbound network traffic', False),
        ]
    },
    {
        'text': 'What is the difference between an IDS and an IPS?',
        'domain': 'Security',
        'choices': [
            ('IDS is hardware-based while IPS is software-based', False),
            ('An IDS detects and alerts on threats while an IPS actively blocks them', True),
            ('IDS works on wireless networks while IPS works on wired networks', False),
            ('There is no difference — IDS and IPS are the same thing', False),
        ]
    },

    # ── TROUBLESHOOTING ───────────────────────────────────────────────────────

    {
        'text': 'What is the first step in the CompTIA troubleshooting methodology?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Establish a theory of probable cause', False),
            ('Identify the problem', True),
            ('Test the theory to determine cause', False),
            ('Document findings and outcomes', False),
        ]
    },
    {
        'text': 'What are the six steps of the CompTIA troubleshooting methodology in order?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Fix, Test, Document, Identify, Theory, Plan', False),
            ('Identify the problem, Establish a theory, Test the theory, Establish a plan of action, Implement the solution, Document findings', True),
            ('Document, Identify, Test, Fix, Verify, Close', False),
            ('Theory, Identify, Plan, Test, Fix, Document', False),
        ]
    },
    {
        'text': 'When troubleshooting, why is it important to question the user about recent changes?',
        'domain': 'Troubleshooting',
        'choices': [
            ('To assign blame for the problem', False),
            ('Recent changes are often the cause of new problems and can quickly narrow down the source of the issue', True),
            ('To document the user\'s work habits for future reference', False),
            ('To determine if the user is qualified to use the equipment', False),
        ]
    },
    {
        'text': 'A computer powers on but there is no display output. What should you check first?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Reinstall the operating system', False),
            ('Replace the CPU immediately', False),
            ('Check the monitor connection, power, and ensure the correct input source is selected', True),
            ('Replace the RAM modules', False),
        ]
    },
    {
        'text': 'A computer is running very slowly. What are the most likely causes?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The keyboard and mouse are malfunctioning', False),
            ('Insufficient RAM, too many startup programs, malware infection, or a failing hard drive', True),
            ('The monitor resolution is set too high', False),
            ('The network cable is damaged', False),
        ]
    },
    {
        'text': 'A user reports their computer randomly restarts. What is the most likely cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The screen saver is misconfigured', False),
            ('Overheating, failing RAM, a bad power supply, or a corrupted operating system', True),
            ('Too many browser tabs are open', False),
            ('The keyboard driver needs updating', False),
        ]
    },
    {
        'text': 'What does POST stand for in the context of computer troubleshooting?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Power On Self Test — a diagnostic test run by the BIOS when the computer starts', True),
            ('Program Output Status Test — a test that checks software integrity', False),
            ('Peripheral Output Signal Test — a test for connected devices', False),
            ('Power Output Stability Test — a test for the PSU', False),
        ]
    },
    {
        'text': 'What do POST beep codes indicate?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The computer is starting up normally', False),
            ('A hardware problem detected during the Power On Self Test before video is initialized', True),
            ('The computer is running a scheduled maintenance task', False),
            ('The system needs a BIOS update', False),
        ]
    },
    {
        'text': 'A printer is not printing. What should you check first?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Replace the printer cartridges immediately', False),
            ('Reinstall the printer drivers', False),
            ('Check that the printer is powered on, connected, set as the default printer, and has no pending jobs in the queue', True),
            ('Restart the computer and try again', False),
        ]
    },
    {
        'text': 'What is the purpose of checking the Event Viewer when troubleshooting a Windows problem?',
        'domain': 'Troubleshooting',
        'choices': [
            ('To view a list of recently installed programs', False),
            ('To find error messages and warnings that can help identify the cause of a problem', True),
            ('To check which users have been logged into the system', False),
            ('To view current CPU and memory usage', False),
        ]
    },
    {
        'text': 'A user cannot connect to a website but can ping its IP address. What is the most likely cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The network cable is faulty', False),
            ('The website is down permanently', False),
            ('A DNS resolution problem — the domain name is not being translated to an IP address correctly', True),
            ('The user\'s firewall is blocking all internet traffic', False),
        ]
    },
    {
        'text': 'What does a spinning beach ball or loading cursor typically indicate on a computer?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The display driver needs updating', False),
            ('The system is waiting for a process to complete — often caused by high CPU or memory usage, or a hanging application', True),
            ('The mouse driver has failed', False),
            ('The hard drive is full', False),
        ]
    },
    {
        'text': 'What is the first thing you should do before working on a computer that has been brought in for repair?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Open the case and inspect the components', False),
            ('Run a full virus scan', False),
            ('Back up the user\'s data in case something goes wrong during the repair process', True),
            ('Update all drivers to the latest version', False),
        ]
    },
    {
        'text': 'A user reports getting a BSOD (Blue Screen of Death). What information should you collect?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The username and password for the account', False),
            ('The stop code or error message displayed on the BSOD, and what the user was doing when it occurred', True),
            ('The serial number of the monitor', False),
            ('The version of the browser being used', False),
        ]
    },
    {
        'text': 'What does BSOD stand for?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Basic System Output Display', False),
            ('Blue Screen of Death — a Windows stop error that indicates a critical system failure', True),
            ('Boot Sequence Operational Diagnostic', False),
            ('Background System Operations Daemon', False),
        ]
    },
    {
        'text': 'A computer turns on but does not boot into the operating system. What could be the cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The monitor is broken', False),
            ('A corrupted boot sector, incorrect boot order in BIOS, or a failed storage drive', True),
            ('The USB keyboard is disconnected', False),
            ('The GPU needs to be reseated', False),
        ]
    },
    {
        'text': 'What is the best approach when a problem cannot be reproduced?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Close the support ticket immediately since there is no issue', False),
            ('Replace all hardware components as a precaution', False),
            ('Document the symptoms reported, monitor the system, and ask the user to report when it happens again', True),
            ('Reinstall the operating system to prevent future issues', False),
        ]
    },
    {
        'text': 'What does it mean to "isolate the problem" during troubleshooting?',
        'domain': 'Troubleshooting',
        'choices': [
            ('To physically separate the faulty component from the rest of the system', False),
            ('To narrow down the cause by eliminating variables one at a time until the source is identified', True),
            ('To keep the problem confidential from other users', False),
            ('To prevent the problem from spreading to other computers on the network', False),
        ]
    },
    {
        'text': 'A user reports that their USB device is not recognized. What should you check?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Replace the USB device immediately', False),
            ('Try a different USB port, check Device Manager for driver issues, and test the device on another computer to determine if the device or port is at fault', True),
            ('Reinstall Windows to fix the USB subsystem', False),
            ('Update the BIOS firmware', False),
        ]
    },
    {
        'text': 'What is the importance of documenting the troubleshooting process?',
        'domain': 'Troubleshooting',
        'choices': [
            ('It is required by law for all IT technicians', False),
            ('Documentation helps with future similar problems, provides a record for billing, and enables other technicians to understand what was done', True),
            ('It helps the user understand technical processes', False),
            ('It is only required for warranty repairs', False),
        ]
    },
    {
        'text': 'What is a common cause of a computer not recognizing newly installed RAM?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The RAM is from a different manufacturer than the existing modules', False),
            ('The RAM module is not fully seated in the slot or is installed in the wrong slot', True),
            ('The operating system needs to be reinstalled to recognize new RAM', False),
            ('The BIOS needs to be flashed before any RAM upgrade', False),
        ]
    },
    {
        'text': 'A technician suspects a PSU is failing. What symptoms might indicate this?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The monitor flickers and the keyboard stops working', False),
            ('Random shutdowns, failure to boot, system instability under load, or burning smell', True),
            ('The computer runs slowly and applications crash', False),
            ('The network connection drops frequently', False),
        ]
    },
    {
        'text': 'What is the purpose of reseating components when troubleshooting?',
        'domain': 'Troubleshooting',
        'choices': [
            ('To clean the contacts of the component', False),
            ('To remove and reinsert a component to ensure it is making proper electrical contact in its slot', True),
            ('To replace a faulty component with a spare', False),
            ('To test the component in a different system', False),
        ]
    },
    {
        'text': 'When should you escalate a problem to a higher level of support?',
        'domain': 'Troubleshooting',
        'choices': [
            ('As soon as the user reports the problem', False),
            ('When the problem is beyond your expertise, requires special access, or has exceeded a reasonable troubleshooting time', True),
            ('Only when the user specifically requests it', False),
            ('After exactly one hour of troubleshooting regardless of progress', False),
        ]
    },

    # ── VIRTUALIZATION & CLOUD ────────────────────────────────────────────────

    {
        'text': 'What is virtualization in computing?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('Creating a visual representation of network topology', False),
            ('The process of creating a virtual version of a resource such as a server, storage device, or operating system on a single physical machine', True),
            ('Connecting multiple computers together to act as one', False),
            ('Encrypting data to create a virtual secure environment', False),
        ]
    },
    {
        'text': 'What is a hypervisor?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('A high-performance processor designed for server workloads', False),
            ('Software that creates and manages virtual machines on physical hardware', True),
            ('A network device that manages virtual LANs', False),
            ('A high-speed storage controller for virtualized environments', False),
        ]
    },
    {
        'text': 'What is the difference between a Type 1 and Type 2 hypervisor?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('Type 1 runs on Windows while Type 2 runs on Linux', False),
            ('Type 1 (bare-metal) runs directly on hardware while Type 2 runs on top of an existing operating system', True),
            ('Type 1 supports more virtual machines than Type 2', False),
            ('Type 1 is software-based while Type 2 is hardware-based', False),
        ]
    },
    {
        'text': 'What is a Virtual Machine (VM)?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('A physical server dedicated to one specific task', False),
            ('An emulation of a computer system that runs on physical hardware and behaves like a separate computer', True),
            ('A remote computer accessed over the internet', False),
            ('A computer that operates without an operating system', False),
        ]
    },
    {
        'text': 'What is the main benefit of server virtualization?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('It eliminates the need for network security', False),
            ('It allows multiple virtual servers to run on one physical server, reducing hardware costs and improving resource utilization', True),
            ('It makes servers immune to hardware failures', False),
            ('It automatically backs up all data on the server', False),
        ]
    },
    {
        'text': 'What is cloud computing?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('Computing that uses weather data to optimize performance', False),
            ('Delivering computing services such as servers, storage, databases, and software over the internet on a pay-as-you-go basis', True),
            ('A type of wireless networking that operates above standard Wi-Fi frequencies', False),
            ('A distributed computing system where all processing is done locally', False),
        ]
    },
    {
        'text': 'What does IaaS stand for in cloud computing?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('Internet as a Service', False),
            ('Infrastructure as a Service — provides virtualized computing resources like servers and storage over the internet', True),
            ('Integration as a Service', False),
            ('Interface as a Service', False),
        ]
    },
    {
        'text': 'What does SaaS stand for in cloud computing?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('Storage as a Service', False),
            ('Security as a Service', False),
            ('Software as a Service — delivers software applications over the internet on a subscription basis', True),
            ('Server as a Service', False),
        ]
    },
    {
        'text': 'What does PaaS stand for in cloud computing?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('Platform as a Service — provides a platform for developers to build and deploy applications without managing infrastructure', True),
            ('Protection as a Service', False),
            ('Performance as a Service', False),
            ('Provisioning as a Service', False),
        ]
    },
    {
        'text': 'What is a snapshot in virtualization?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('A screenshot of the virtual machine\'s current display', False),
            ('A point-in-time copy of a virtual machine\'s state that can be used to restore the VM to that state', True),
            ('A backup of the physical server\'s configuration', False),
            ('A performance benchmark of a virtual machine', False),
        ]
    },
    {
        'text': 'What is the purpose of VM migration (live migration)?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('To permanently delete a virtual machine from the system', False),
            ('To move a running virtual machine from one physical host to another with minimal or no downtime', True),
            ('To upgrade a virtual machine to a newer version', False),
            ('To clone a virtual machine for testing purposes', False),
        ]
    },
    {
        'text': 'What is a private cloud?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('A cloud service used by only one person', False),
            ('Cloud infrastructure dedicated to and operated for a single organization, providing more control and security', True),
            ('A cloud service that is not connected to the internet', False),
            ('A free cloud service with limited storage', False),
        ]
    },
    {
        'text': 'What is a public cloud?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('A cloud owned and managed by a government agency', False),
            ('Cloud services offered over the public internet and available to anyone who wants to use or purchase them', True),
            ('A cloud that is accessible to the public but owned by a private company', False),
            ('A cloud service with no security restrictions', False),
        ]
    },
    {
        'text': 'What is a hybrid cloud?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('A cloud that uses both Windows and Linux servers', False),
            ('A cloud environment that combines private and public cloud services allowing data and applications to be shared between them', True),
            ('A cloud that provides both storage and computing services', False),
            ('A cloud service that works on both mobile and desktop devices', False),
        ]
    },
    {
        'text': 'What is the purpose of containers in computing?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('Physical boxes used to ship server hardware', False),
            ('Lightweight, portable units that package an application with all its dependencies so it runs consistently across different environments', True),
            ('Network segments that isolate different types of traffic', False),
            ('Security zones that contain malware and prevent it from spreading', False),
        ]
    },
    {
        'text': 'How do containers differ from virtual machines?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('Containers are slower but more secure than virtual machines', False),
            ('Containers share the host OS kernel and are more lightweight while VMs include a full OS and are more isolated', True),
            ('Virtual machines are newer technology than containers', False),
            ('Containers can only run on Linux while VMs work on any OS', False),
        ]
    },
    {
        'text': 'What is resource pooling in cloud computing?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('Combining multiple internet connections for faster speeds', False),
            ('The provider\'s computing resources serving multiple consumers using a multi-tenant model, dynamically assigned based on demand', True),
            ('A backup method that copies data to multiple locations', False),
            ('Grouping servers by geographic location for faster access', False),
        ]
    },
    {
        'text': 'What does VDI stand for in virtualization?',
        'domain': 'Virtualization & Cloud',
        'choices': [
            ('Virtual Data Integration', False),
            ('Virtual Desktop Infrastructure — a technology that hosts desktop environments on centralized servers accessed remotely', True),
            ('Virtualized Drive Interface', False),
            ('Variable Display Input', False),
        ]
    },

    # ── PRINTERS ──────────────────────────────────────────────────────────────

    {
        'text': 'What are the two main types of printers commonly found in offices?',
        'domain': 'Printers',
        'choices': [
            ('Dot matrix and inkjet printers', False),
            ('Laser and inkjet printers', True),
            ('Thermal and impact printers', False),
            ('3D and laser printers', False),
        ]
    },
    {
        'text': 'How does a laser printer create an image on paper?',
        'domain': 'Printers',
        'choices': [
            ('By spraying ink droplets onto the paper through tiny nozzles', False),
            ('By pressing an inked ribbon against the paper', False),
            ('By using a laser to create a static charge on a drum that attracts toner, which is then fused to the paper with heat', True),
            ('By burning the image directly onto specially coated paper', False),
        ]
    },
    {
        'text': 'What is toner?',
        'domain': 'Printers',
        'choices': [
            ('A liquid ink used in inkjet printers', False),
            ('A fine powder used in laser printers that is fused to paper using heat', True),
            ('A cleaning solution used to maintain print heads', False),
            ('A chemical used to coat paper for thermal printing', False),
        ]
    },
    {
        'text': 'What component in a laser printer fuses the toner permanently to the paper?',
        'domain': 'Printers',
        'choices': [
            ('The drum unit', False),
            ('The transfer roller', False),
            ('The fuser assembly', True),
            ('The corona wire', False),
        ]
    },
    {
        'text': 'What is the correct order of the laser printing process?',
        'domain': 'Printers',
        'choices': [
            ('Charging, Exposing, Developing, Transferring, Fusing, Cleaning', True),
            ('Cleaning, Charging, Exposing, Developing, Transferring, Fusing', False),
            ('Exposing, Charging, Transferring, Developing, Fusing, Cleaning', False),
            ('Developing, Charging, Exposing, Transferring, Cleaning, Fusing', False),
        ]
    },
    {
        'text': 'What is a common cause of vertical lines appearing on laser printer output?',
        'domain': 'Printers',
        'choices': [
            ('Low ink levels in the cartridge', False),
            ('A scratch or damage on the drum unit or a dirty fuser', True),
            ('The paper is damp or of poor quality', False),
            ('The printer driver is outdated', False),
        ]
    },
    {
        'text': 'What does a thermal printer use to create images?',
        'domain': 'Printers',
        'choices': [
            ('Ink cartridges filled with liquid dye', False),
            ('Heat applied to specially coated thermal paper to create marks', True),
            ('A laser beam to charge a photosensitive drum', False),
            ('A ribbon coated with ink pressed against regular paper', False),
        ]
    },
    {
        'text': 'What are thermal printers commonly used for?',
        'domain': 'Printers',
        'choices': [
            ('High-quality photo printing', False),
            ('Printing receipts, shipping labels, and barcode labels', True),
            ('Office document printing', False),
            ('Large format printing like posters and banners', False),
        ]
    },
    {
        'text': 'What is the most common cause of paper jams in a printer?',
        'domain': 'Printers',
        'choices': [
            ('Using the wrong type of toner cartridge', False),
            ('Incorrect paper size selected in the driver', False),
            ('Damp or curled paper, overfilled paper tray, worn pick rollers, or foreign objects in the paper path', True),
            ('The printer being in an area with too much light', False),
        ]
    },
    {
        'text': 'What should you do immediately after removing a paper jam from a printer?',
        'domain': 'Printers',
        'choices': [
            ('Replace the toner cartridge', False),
            ('Run the printer\'s cleaning cycle', False),
            ('Check that all paper fragments have been removed before resuming printing to avoid further jams', True),
            ('Restart the printer and computer', False),
        ]
    },
    {
        'text': 'What does duplexing mean in printing?',
        'domain': 'Printers',
        'choices': [
            ('Printing in two colors simultaneously', False),
            ('Printing on both sides of the paper automatically', True),
            ('Printing two copies of each document simultaneously', False),
            ('Connecting two printers to one computer', False),
        ]
    },
    {
        'text': 'What is a print spooler?',
        'domain': 'Printers',
        'choices': [
            ('A physical component that feeds paper into the printer', False),
            ('A Windows service that manages print jobs, storing them in a queue until the printer is ready', True),
            ('A type of printer cable used for high-speed data transfer', False),
            ('Software that converts documents into printer-readable format', False),
        ]
    },
    {
        'text': 'How do you clear a stuck print queue in Windows?',
        'domain': 'Printers',
        'choices': [
            ('Restart the printer only', False),
            ('Reinstall the printer drivers', False),
            ('Stop the Print Spooler service, delete the files in the spool folder, then restart the service', True),
            ('Uninstall and reinstall Windows', False),
        ]
    },
    {
        'text': 'What is a printer driver?',
        'domain': 'Printers',
        'choices': [
            ('The physical mechanism that moves the print head across the paper', False),
            ('Software that allows the operating system to communicate with and control a specific printer model', True),
            ('The USB cable that connects the printer to the computer', False),
            ('The firmware installed on the printer\'s internal memory', False),
        ]
    },
    {
        'text': 'What is the purpose of a printer\'s built-in self-test page?',
        'domain': 'Printers',
        'choices': [
            ('To calibrate the ink cartridges', False),
            ('To verify that the printer hardware is functioning correctly independently of the computer and driver', True),
            ('To update the printer firmware', False),
            ('To clear the print queue of pending jobs', False),
        ]
    },
    {
        'text': 'What causes ghosting on laser printer output?',
        'domain': 'Printers',
        'choices': [
            ('Low toner levels in the cartridge', False),
            ('A failing fuser assembly that does not fully fuse toner, or a drum that is not fully cleaned between passes', True),
            ('Using the wrong paper type', False),
            ('The printer resolution being set too low', False),
        ]
    },
    {
        'text': 'How does an inkjet printer work?',
        'domain': 'Printers',
        'choices': [
            ('It uses heat to burn images onto specially coated paper', False),
            ('It uses a laser to charge a drum that picks up toner and transfers it to paper', False),
            ('It sprays tiny droplets of liquid ink onto paper through microscopic nozzles in the print head', True),
            ('It presses an inked ribbon against paper to form characters', False),
        ]
    },
    {
        'text': 'What is a common maintenance task for inkjet printers?',
        'domain': 'Printers',
        'choices': [
            ('Replacing the fuser assembly regularly', False),
            ('Cleaning or aligning the print heads to prevent clogged nozzles and ensure print quality', True),
            ('Replacing the drum unit every 10,000 pages', False),
            ('Cleaning the corona wire monthly', False),
        ]
    },
    {
        'text': 'What does PCL stand for in printing?',
        'domain': 'Printers',
        'choices': [
            ('Printer Control Language — a page description language developed by HP for communicating with printers', True),
            ('Print Circuit Layout', False),
            ('Peripheral Connection Link', False),
            ('Paper Calibration Level', False),
        ]
    },
    {
        'text': 'What is the difference between a local printer and a network printer?',
        'domain': 'Printers',
        'choices': [
            ('A local printer is faster than a network printer', False),
            ('A local printer is connected directly to one computer while a network printer is connected to the network and accessible by multiple users', True),
            ('Local printers use USB while network printers use Bluetooth', False),
            ('Network printers require a separate computer to function', False),
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