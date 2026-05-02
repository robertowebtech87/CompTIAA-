import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from app import app, db
from models import Question, Choice

questions_data = [

    # ── WHAT IS SUBNETTING ────────────────────────────────────────────────────

    {
        'text': 'What is the purpose of subnetting a network?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Subnetting divides a large network into smaller sub-networks. This improves performance by reducing broadcast traffic, improves security by isolating segments, and makes IP address management more efficient.',
        'choices': [
            ('To increase the speed of internet connections', False),
            ('To divide a large network into smaller segments improving performance security and address management', True),
            ('To connect two different types of networks together', False),
            ('To assign public IP addresses to private devices', False),
        ]
    },

    # ── SUBNET MASK BASICS ────────────────────────────────────────────────────

    {
        'text': 'What is a subnet mask used for?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A subnet mask tells a device which part of an IP address is the network portion and which part is the host portion. It determines whether a destination is on the local network or needs to be sent to the default gateway.',
        'choices': [
            ('To encrypt traffic between two devices', False),
            ('To identify which part of an IP address is the network and which part is the host', True),
            ('To assign IP addresses automatically to devices', False),
            ('To translate private IP addresses to public ones', False),
        ]
    },
    {
        'text': 'What subnet mask is associated with a /24 prefix length?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '/24 means 24 bits are used for the network portion. Written in decimal this is 255.255.255.0 — three octets of 255 (all 1s) and one octet of 0 (all 0s for hosts).',
        'choices': [
            ('255.255.0.0', False),
            ('255.255.255.0', True),
            ('255.255.255.128', False),
            ('255.0.0.0', False),
        ]
    },
    {
        'text': 'What subnet mask corresponds to /16?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '/16 means 16 bits are network bits. In decimal this is 255.255.0.0 — two octets of 255 and two octets of 0 available for hosts. This allows 65,534 usable host addresses.',
        'choices': [
            ('255.255.255.0', False),
            ('255.255.0.0', True),
            ('255.0.0.0', False),
            ('255.255.255.128', False),
        ]
    },
    {
        'text': 'What subnet mask corresponds to /8?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '/8 means only 8 bits are network bits. In decimal this is 255.0.0.0 — only the first octet identifies the network leaving three octets for hosts. This allows over 16 million host addresses.',
        'choices': [
            ('255.255.0.0', False),
            ('255.0.0.0', True),
            ('255.255.255.0', False),
            ('128.0.0.0', False),
        ]
    },

    # ── CIDR NOTATION ────────────────────────────────────────────────────────

    {
        'text': 'What does the "/24" mean in the IP address 192.168.1.0/24?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'The /24 is CIDR (Classless Inter-Domain Routing) notation. It means 24 bits are used for the network portion of the address. The remaining 8 bits (32-24=8) are used for host addresses giving 256 total addresses and 254 usable hosts.',
        'choices': [
            ('There are 24 devices on this network', False),
            ('24 bits are allocated to the network portion leaving 8 bits for hosts', True),
            ('The network supports 24 subnets', False),
            ('The VLAN ID for this network is 24', False),
        ]
    },
    {
        'text': 'How many bits are in a complete IPv4 address?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'An IPv4 address is 32 bits long written as four octets of 8 bits each separated by dots. For example 192.168.1.1 = 11000000.10101000.00000001.00000001.',
        'choices': [
            ('16 bits', False),
            ('32 bits', True),
            ('48 bits', False),
            ('64 bits', False),
        ]
    },

    # ── HOST CALCULATIONS ─────────────────────────────────────────────────────

    {
        'text': 'How many usable host addresses does a /24 subnet provide?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A /24 has 8 host bits giving 2^8 = 256 total addresses. Subtract 1 for the network address and 1 for the broadcast address leaving 254 usable host addresses.',
        'choices': [
            ('256', False),
            ('254', True),
            ('255', False),
            ('128', False),
        ]
    },
    {
        'text': 'How many usable host addresses does a /25 subnet provide?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A /25 has 7 host bits giving 2^7 = 128 total addresses. Subtract 2 (network + broadcast) leaving 126 usable hosts. A /25 splits a /24 into two equal halves.',
        'choices': [
            ('128', False),
            ('126', True),
            ('64', False),
            ('254', False),
        ]
    },
    {
        'text': 'How many usable host addresses does a /30 subnet provide?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A /30 has 2 host bits giving 2^2 = 4 total addresses. Subtract 2 (network + broadcast) leaving only 2 usable hosts. /30 subnets are commonly used for point-to-point links between routers.',
        'choices': [
            ('4', False),
            ('2', True),
            ('6', False),
            ('8', False),
        ]
    },
    {
        'text': 'A technician needs a subnet that supports exactly 30 hosts. Which is the smallest subnet that works?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A /27 has 5 host bits giving 2^5 = 32 total addresses minus 2 = 30 usable hosts. This is the smallest subnet that fits exactly 30 hosts. A /28 only gives 14 usable hosts which is not enough.',
        'choices': [
            ('/28 — 14 usable hosts', False),
            ('/27 — 30 usable hosts', True),
            ('/26 — 62 usable hosts', False),
            ('/29 — 6 usable hosts', False),
        ]
    },

    # ── NETWORK AND BROADCAST ─────────────────────────────────────────────────

    {
        'text': 'In the subnet 192.168.1.0/24 what is the network address?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'The network address is the first address in the subnet where all host bits are set to 0. For 192.168.1.0/24 the network address is 192.168.1.0. This address cannot be assigned to any host.',
        'choices': [
            ('192.168.1.1', False),
            ('192.168.1.0', True),
            ('192.168.1.255', False),
            ('192.168.0.0', False),
        ]
    },
    {
        'text': 'In the subnet 192.168.1.0/24 what is the broadcast address?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'The broadcast address is the last address in the subnet where all host bits are set to 1. For 192.168.1.0/24 the broadcast address is 192.168.1.255. Frames sent to this address are received by all hosts on the subnet.',
        'choices': [
            ('192.168.1.0', False),
            ('192.168.1.254', False),
            ('192.168.1.255', True),
            ('192.168.255.255', False),
        ]
    },
    {
        'text': 'What is the valid host range for the subnet 192.168.1.0/24?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'The valid host range excludes the network address (.0) and broadcast address (.255). So usable hosts are 192.168.1.1 through 192.168.1.254 giving 254 valid host addresses.',
        'choices': [
            ('192.168.1.0 to 192.168.1.255', False),
            ('192.168.1.1 to 192.168.1.254', True),
            ('192.168.1.1 to 192.168.1.255', False),
            ('192.168.1.0 to 192.168.1.254', False),
        ]
    },

    # ── PRIVATE vs PUBLIC ─────────────────────────────────────────────────────

    {
        'text': 'Which of the following is a private IP address?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '192.168.10.5 is a private IP address in the 192.168.0.0/16 range defined by RFC 1918. Private IPs cannot route on the public internet. The others are public addresses.',
        'choices': [
            ('8.8.8.8', False),
            ('172.32.0.1', False),
            ('192.168.10.5', True),
            ('203.0.113.1', False),
        ]
    },
    {
        'text': 'Which THREE address ranges are defined as private by RFC 1918? (Select THREE)',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'RFC 1918 defines three private ranges: 10.0.0.0/8, 172.16.0.0/12 (172.16-31.x.x), and 192.168.0.0/16. These do not route on the public internet and require NAT to access the internet.',
        'choices': [
            ('10.0.0.0/8 (10.x.x.x)', True),
            ('172.16.0.0/12 (172.16-31.x.x)', True),
            ('192.168.0.0/16 (192.168.x.x)', True),
            ('169.254.0.0/16 (APIPA range)', False),
        ]
    },
    {
        'text': 'Is the IP address 172.20.5.10 a private address?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Yes — 172.20.5.10 falls within the private range 172.16.0.0 to 172.31.255.255 (172.16.0.0/12 per RFC 1918). The private 172.x range covers 172.16 through 172.31 — a common exam trick since many people only remember 172.16.',
        'choices': [
            ('No — only 172.16.x.x addresses are private', False),
            ('Yes — 172.20.x.x falls within the private 172.16.0.0/12 range (172.16-31.x.x)', True),
            ('No — 172.20.x.x is a public address', False),
            ('Yes — but only if the subnet mask is /24', False),
        ]
    },

    # ── DEFAULT GATEWAY ──────────────────────────────────────────────────────

    {
        'text': 'What is the default gateway and when does a device use it?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'The default gateway is the IP address of the local router. A device uses it whenever the destination IP address is outside the local subnet. The device sends the packet to the gateway which then routes it toward the destination.',
        'choices': [
            ('The first IP address in the subnet used for network identification', False),
            ('The router IP address used when the destination is outside the local subnet', True),
            ('The DNS server address used to resolve domain names', False),
            ('The broadcast address at the end of every subnet', False),
        ]
    },
    {
        'text': 'A computer has IP 192.168.1.50/24 and default gateway 192.168.1.1. It tries to reach 10.0.0.1. What happens?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '10.0.0.1 is not in the 192.168.1.0/24 local subnet so the computer sends the packet to the default gateway (192.168.1.1). The router then forwards it toward the 10.0.0.0 network.',
        'choices': [
            ('The packet is dropped because 10.0.0.1 is a private address', False),
            ('The packet is sent to the default gateway 192.168.1.1 which routes it onward', True),
            ('The computer broadcasts to find 10.0.0.1 on the local network', False),
            ('The computer sends directly to 10.0.0.1 since both are private addresses', False),
        ]
    },

    # ── SUBNET IDENTIFICATION ─────────────────────────────────────────────────

    {
        'text': 'Two computers have IPs 192.168.1.50 and 192.168.1.200, both with subnet mask 255.255.255.0. Can they communicate directly?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Both addresses are in the 192.168.1.0/24 subnet (same network portion 192.168.1.x). They can communicate directly without going through a router.',
        'choices': [
            ('No — they need a router because their host numbers are different', False),
            ('Yes — both are in the same 192.168.1.0/24 subnet', True),
            ('No — addresses above .128 need a separate subnet', False),
            ('Yes — but only if they are connected to the same switch', False),
        ]
    },
    {
        'text': 'A device has IP address 192.168.1.100 with subnet mask 255.255.255.0. Which network does it belong to?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'To find the network address apply the subnet mask to the IP. The /24 mask (255.255.255.0) keeps the first three octets and zeros the last giving network 192.168.1.0.',
        'choices': [
            ('192.168.0.0', False),
            ('192.168.1.0', True),
            ('192.168.1.100', False),
            ('192.168.1.255', False),
        ]
    },

    # ── COMMON SUBNET MASKS ───────────────────────────────────────────────────

    {
        'text': 'Match the CIDR notation to its subnet mask — what is /25?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '/25 uses 25 network bits. The first three octets are all 1s (255.255.255) and the fourth octet has the first bit as 1 and last 7 as 0 = 10000000 in binary = 128 in decimal. So /25 = 255.255.255.128.',
        'choices': [
            ('255.255.255.0', False),
            ('255.255.255.128', True),
            ('255.255.255.192', False),
            ('255.255.255.224', False),
        ]
    },
    {
        'text': 'What subnet mask is /26?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '/26 uses 26 network bits. The last octet has the first 2 bits as 1 = 11000000 = 192 in decimal. So /26 = 255.255.255.192. A /26 subnet has 64 total addresses and 62 usable hosts.',
        'choices': [
            ('255.255.255.128', False),
            ('255.255.255.192', True),
            ('255.255.255.224', False),
            ('255.255.255.240', False),
        ]
    },
    {
        'text': 'What subnet mask is /27?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '/27 uses 27 network bits. The last octet has the first 3 bits as 1 = 11100000 = 224 in decimal. So /27 = 255.255.255.224. A /27 has 32 total addresses and 30 usable hosts.',
        'choices': [
            ('255.255.255.192', False),
            ('255.255.255.224', True),
            ('255.255.255.240', False),
            ('255.255.255.248', False),
        ]
    },
    {
        'text': 'What subnet mask is /28?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '/28 uses 28 network bits. The last octet has the first 4 bits as 1 = 11110000 = 240 in decimal. So /28 = 255.255.255.240. A /28 has 16 total addresses and 14 usable hosts.',
        'choices': [
            ('255.255.255.224', False),
            ('255.255.255.240', True),
            ('255.255.255.248', False),
            ('255.255.255.252', False),
        ]
    },

    # ── PRACTICAL SCENARIOS ───────────────────────────────────────────────────

    {
        'text': 'A small office has 5 devices that need IP addresses. Which subnet wastes the least addresses?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A /29 gives 8 total addresses minus 2 (network + broadcast) = 6 usable hosts. This fits exactly 5 devices with 1 spare and wastes the fewest addresses compared to /28 (14 hosts) or larger.',
        'choices': [
            ('/24 — 254 usable hosts', False),
            ('/28 — 14 usable hosts', False),
            ('/29 — 6 usable hosts', True),
            ('/30 — 2 usable hosts (not enough)', False),
        ]
    },
    {
        'text': 'A point-to-point WAN link connects two routers. Which subnet is most appropriate?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A /30 gives exactly 2 usable host addresses — one for each router interface. This is the standard choice for point-to-point links between routers as it wastes no addresses beyond the required network and broadcast.',
        'choices': [
            ('/24 — more room for future growth', False),
            ('/30 — exactly 2 usable hosts for each router interface', True),
            ('/32 — one address for each router', False),
            ('/16 — maximum flexibility', False),
        ]
    },
    {
        'text': 'Which TWO are true about the network address and broadcast address of any subnet? (Select TWO)',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'The network address (all host bits = 0) and broadcast address (all host bits = 1) cannot be assigned to any host device. They are reserved — reducing usable hosts by 2 from the total.',
        'choices': [
            ('The network address cannot be assigned to any host device', True),
            ('The broadcast address can be assigned to a server for redundancy', False),
            ('The broadcast address cannot be assigned to any host device', True),
            ('The network address can be used as the default gateway', False),
        ]
    },
    {
        'text': 'A technician sees a device with IP 169.254.55.10 and subnet mask 255.255.0.0. What does this indicate?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '169.254.x.x is an APIPA (Automatic Private IP Addressing) address. This means the device could not reach a DHCP server and assigned itself an address. The device will not have internet access and the technician should troubleshoot the DHCP issue.',
        'choices': [
            ('The device has been manually configured with a valid static IP', False),
            ('The device has an APIPA address meaning it could not reach the DHCP server', True),
            ('The device has a public IP assigned by the ISP', False),
            ('The device is connected to a 172.16.x.x private network', False),
        ]
    },
    {
        'text': 'What is the formula to calculate the number of usable hosts in a subnet?',
        'domain': 'Subnetting',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'The formula is 2^h - 2 where h is the number of host bits. The -2 accounts for the network address and broadcast address which cannot be assigned to hosts. For /24: 2^8 - 2 = 254 hosts.',
        'choices': [
            ('2^h where h is the number of host bits', False),
            ('2^h - 2 where h is the number of host bits', True),
            ('2^n where n is the number of network bits', False),
            ('2^n - 2 where n is the number of network bits', False),
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
    subnet = Question.query.filter_by(exam='core1', domain='Subnetting').count()
    print(f'Added {added} questions. Skipped {skipped} duplicates.')
    print(f'Subnetting: {subnet} | Core 1: {core1} | Overall: {total}')
