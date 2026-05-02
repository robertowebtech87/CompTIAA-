import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from app import app, db
from models import Question, Choice

questions_data = [

    # ── IPv4 BASICS ───────────────────────────────────────────────────────────

    {
        'text': 'What is an IP address and what is it used for?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'An IP (Internet Protocol) address is a unique numerical label assigned to every device on a network. It serves two purposes: identifying the device (who it is) and providing its location on the network (where it is) so data can be routed to it.',
        'choices': [
            ('A physical address burned into a network card at manufacture', False),
            ('A unique numerical label that identifies a device and its location on a network', True),
            ('A password used to authenticate devices on a network', False),
            ('A port number used to identify applications running on a device', False),
        ]
    },
    {
        'text': 'How many bits make up an IPv4 address and how is it written?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'An IPv4 address is 32 bits long written as four decimal numbers (octets) separated by dots. Each octet represents 8 bits and can range from 0 to 255. Example: 192.168.1.100.',
        'choices': [
            ('16 bits — written as two decimal numbers', False),
            ('32 bits — written as four decimal octets separated by dots', True),
            ('48 bits — written as six hexadecimal groups', False),
            ('64 bits — written as eight decimal numbers', False),
        ]
    },
    {
        'text': 'What is the maximum value of any single octet in an IPv4 address?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Each octet in an IPv4 address is 8 bits. The maximum value of 8 bits is 11111111 in binary which equals 255 in decimal. So no octet can ever exceed 255.',
        'choices': [
            ('128', False),
            ('255', True),
            ('256', False),
            ('512', False),
        ]
    },
    {
        'text': 'How many total IPv4 addresses are possible?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'IPv4 uses 32 bits giving 2^32 = approximately 4.29 billion possible addresses. This seemed sufficient when IPv4 was designed but internet growth has exhausted the available public addresses leading to IPv6.',
        'choices': [
            ('About 1 million', False),
            ('About 4.29 billion', True),
            ('About 10 billion', False),
            ('Unlimited', False),
        ]
    },

    # ── STATIC vs DYNAMIC ─────────────────────────────────────────────────────

    {
        'text': 'What is a static IP address?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A static IP address is one that is manually configured on a device and never changes. It is commonly used for servers printers and routers that need a consistent address. The downside is it must be manually updated if the network changes.',
        'choices': [
            ('An IP address that changes every time the device restarts', False),
            ('A manually configured IP address that stays the same permanently', True),
            ('An IP address assigned automatically by a DHCP server', False),
            ('A temporary IP address used only during bootup', False),
        ]
    },
    {
        'text': 'What is a dynamic IP address?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A dynamic IP address is automatically assigned by a DHCP server when a device joins the network. It may change over time as leases expire. Dynamic addressing is used for most client devices like laptops and phones.',
        'choices': [
            ('An IP address manually typed into a device that never changes', False),
            ('An IP address automatically assigned by a DHCP server that may change over time', True),
            ('An IPv6 address that automatically generates itself', False),
            ('An IP address used only for wireless connections', False),
        ]
    },
    {
        'text': 'Which devices should typically be configured with static IP addresses?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Servers printers routers switches and other infrastructure devices should have static IPs so their addresses are always predictable. Client devices like laptops and phones use DHCP since their addresses do not need to be remembered.',
        'choices': [
            ('Laptops and smartphones', False),
            ('Servers routers printers and network infrastructure devices', True),
            ('Only devices connected via Wi-Fi', False),
            ('All devices should always use static IPs', False),
        ]
    },
    {
        'text': 'What is a DHCP reservation and how does it differ from a static IP?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A DHCP reservation ties a specific IP address to a device MAC address on the DHCP server. The device uses DHCP but always gets the same IP. Unlike a static IP configured on the device DHCP reservations are managed centrally making changes easier.',
        'choices': [
            ('They are identical — DHCP reservation is just a newer term for static IP', False),
            ('A DHCP reservation is configured on the server and ties an IP to a MAC address while static IP is configured on the device itself', True),
            ('DHCP reservation gives a temporary address while static IP is permanent', False),
            ('Static IP supports IPv6 while DHCP reservation only supports IPv4', False),
        ]
    },

    # ── PRIVATE AND PUBLIC ────────────────────────────────────────────────────

    {
        'text': 'What is the difference between a private and public IP address?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Public IP addresses are globally unique and routable on the internet. Private IP addresses (RFC 1918) are used inside networks and cannot route on the public internet. NAT translates private addresses to a public IP for internet access.',
        'choices': [
            ('Public IPs are faster than private IPs', False),
            ('Public IPs are globally unique and routable on the internet while private IPs are used internally and require NAT to reach the internet', True),
            ('Private IPs are assigned by ISPs while public IPs are self-assigned', False),
            ('Public IPs support IPv6 while private IPs are IPv4 only', False),
        ]
    },
    {
        'text': 'Which of the following is a public IP address?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '8.8.8.8 is a public IP address (Google DNS). The others are private: 192.168.x.x is RFC 1918 private, 10.x.x.x is RFC 1918 private, and 169.254.x.x is APIPA.',
        'choices': [
            ('192.168.1.1', False),
            ('10.0.0.1', False),
            ('8.8.8.8', True),
            ('169.254.1.1', False),
        ]
    },
    {
        'text': 'What is NAT and why is it needed?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'NAT (Network Address Translation) allows multiple devices with private IP addresses to share a single public IP address for internet access. It is needed because there are not enough public IPv4 addresses for every device and private addresses cannot route on the internet.',
        'choices': [
            ('Network Authentication Tool — verifies device identity on the network', False),
            ('Network Address Translation — allows devices with private IPs to share a public IP for internet access', True),
            ('Node Assignment Table — tracks which IP addresses are in use', False),
            ('Network Access Terminal — the router interface for configuration', False),
        ]
    },

    # ── APIPA ─────────────────────────────────────────────────────────────────

    {
        'text': 'What is APIPA and when does a device use it?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'APIPA (Automatic Private IP Addressing) is a self-assigned IP address a device uses when it cannot reach a DHCP server. The address is in the 169.254.1.0 to 169.254.254.255 range. A device with APIPA cannot access the internet.',
        'choices': [
            ('A static IP assigned by the administrator for temporary use', False),
            ('A self-assigned address in the 169.254.x.x range used when no DHCP server is reachable', True),
            ('An IPv6 address automatically generated from the MAC address', False),
            ('A public IP provided by the ISP when DHCP fails', False),
        ]
    },
    {
        'text': 'A technician checks a computer and sees IP address 169.254.33.12. What is the most likely problem?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '169.254.x.x is an APIPA address meaning the device could not reach the DHCP server. The technician should check the network cable DHCP server availability and switch connectivity.',
        'choices': [
            ('The device has been manually configured with a valid static IP', False),
            ('The device could not reach the DHCP server and assigned itself an APIPA address', True),
            ('The device has a public IP from the ISP', False),
            ('The device is using IPv6 link-local addressing', False),
        ]
    },
    {
        'text': 'Can a device with an APIPA address access the internet?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'No. APIPA is a link-local address meaning it can only communicate with other devices on the same local subnet. It cannot be routed outside the local network so internet access is not possible.',
        'choices': [
            ('Yes — APIPA provides full network access', False),
            ('No — APIPA is link-local only and cannot route outside the local subnet', True),
            ('Yes — but only to IPv6 websites', False),
            ('No — but only because the firewall blocks APIPA addresses', False),
        ]
    },

    # ── IPv6 ──────────────────────────────────────────────────────────────────

    {
        'text': 'Why was IPv6 developed to replace IPv4?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'IPv4 only supports about 4.29 billion addresses which have been exhausted by the growth of internet-connected devices. IPv6 uses 128-bit addresses providing 340 undecillion addresses — effectively unlimited for the foreseeable future.',
        'choices': [
            ('IPv6 is faster than IPv4 because addresses are shorter', False),
            ('IPv4 addresses were exhausted — IPv6 provides 340 undecillion addresses solving the shortage', True),
            ('IPv6 was required to support wireless networks', False),
            ('IPv4 lacked encryption which IPv6 builds in by default', False),
        ]
    },
    {
        'text': 'How many bits make up an IPv6 address and how is it written?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'IPv6 addresses are 128 bits long written as eight groups of four hexadecimal digits separated by colons. Example: 2001:0db8:85a3:0000:0000:8a2e:0370:7334. Consecutive groups of zeros can be shortened with ::.',
        'choices': [
            ('32 bits — written as four decimal numbers', False),
            ('128 bits — written as eight groups of four hexadecimal digits separated by colons', True),
            ('64 bits — written as four hexadecimal groups', False),
            ('256 bits — written as a long hexadecimal string', False),
        ]
    },
    {
        'text': 'What is the default subnet prefix length for IPv6?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'The default subnet prefix for IPv6 is /64. The first 64 bits identify the network and the last 64 bits identify the host. This gives an enormous number of host addresses per subnet — 18 quintillion per network.',
        'choices': [
            ('/24', False),
            ('/32', False),
            ('/48', False),
            ('/64', True),
        ]
    },

    # ── LOOPBACK AND SPECIAL ADDRESSES ────────────────────────────────────────

    {
        'text': 'What is the loopback address in IPv4 and what is it used for?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'The IPv4 loopback address is 127.0.0.1 (the entire 127.0.0.0/8 range is reserved for loopback). It is used to test the network stack on the local device without sending traffic over the network. Pinging 127.0.0.1 tests that TCP/IP is working locally.',
        'choices': [
            ('192.168.0.1 — the default router address', False),
            ('127.0.0.1 — used to test the local network stack without sending traffic over the network', True),
            ('0.0.0.0 — used when a device has no IP address', False),
            ('255.255.255.255 — the broadcast address for all networks', False),
        ]
    },
    {
        'text': 'What does the IP address 0.0.0.0 represent?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '0.0.0.0 represents "no address" or "all addresses". It is used as the source IP by a DHCP client before it receives an address (DHCP Discover), and in routing it means the default route matching all destinations.',
        'choices': [
            ('The loopback address for testing the local network stack', False),
            ('No address — used by DHCP clients before receiving an IP and as the default route', True),
            ('The first usable address in any subnet', False),
            ('The broadcast address for the local network', False),
        ]
    },
    {
        'text': 'What is the broadcast address 255.255.255.255 used for?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': '255.255.255.255 is the limited broadcast address. Packets sent to this address are delivered to all devices on the local subnet. It is used by DHCP Discover messages since the client does not yet know the network address.',
        'choices': [
            ('To send traffic to all devices on the entire internet', False),
            ('To send traffic to all devices on the local subnet — used by DHCP Discover', True),
            ('To test the loopback interface on the local device', False),
            ('To identify the default gateway on a network', False),
        ]
    },

    # ── SCENARIOS ─────────────────────────────────────────────────────────────

    {
        'text': 'A laptop is configured with IP 192.168.1.50 subnet mask 255.255.255.0 but no default gateway. What can it do?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Without a default gateway the device can only communicate with other devices on its local subnet (192.168.1.x). It cannot reach any other network including the internet because it has no router to forward traffic to external destinations.',
        'choices': [
            ('Communicate normally including internet access', False),
            ('Only communicate with devices on the local 192.168.1.x subnet', True),
            ('Not communicate at all — a gateway is required for any communication', False),
            ('Access the internet but not local network resources', False),
        ]
    },
    {
        'text': 'A user reports they cannot access the internet but can access local network resources. What is the most likely IP configuration problem?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'If a user can access local resources but not the internet the default gateway is likely missing or incorrect. The gateway is needed to route traffic beyond the local subnet to the internet.',
        'choices': [
            ('The IP address is wrong', False),
            ('The default gateway is missing or incorrect', True),
            ('The subnet mask is wrong', False),
            ('The DNS server is unreachable', False),
        ]
    },
    {
        'text': 'Two devices have IPs 192.168.1.50/24 and 192.168.2.50/24. Can they communicate directly?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'No — they are on different subnets. 192.168.1.50/24 is on the 192.168.1.0 network and 192.168.2.50/24 is on the 192.168.2.0 network. A router is needed to route traffic between them.',
        'choices': [
            ('Yes — both use 192.168.x.x private addresses so they can communicate', False),
            ('No — they are on different subnets and need a router to communicate', True),
            ('Yes — as long as they are connected to the same switch', False),
            ('No — different third octets always means different buildings', False),
        ]
    },
    {
        'text': 'Which THREE pieces of information does a device need for basic network communication? (Select THREE)',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'For basic network communication a device needs an IP address (its identity), a subnet mask (to determine local vs remote destinations), and a default gateway (to reach devices outside the local subnet).',
        'choices': [
            ('IP address', True),
            ('MAC address', False),
            ('Subnet mask', True),
            ('Default gateway', True),
            ('DNS server', False),
        ]
    },
    {
        'text': 'A technician assigns IP 192.168.1.50 to two different computers on the same network. What happens?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'This creates an IP address conflict. Both devices will have connectivity problems — one or both will display an IP conflict warning and may lose network access. Every device on a network must have a unique IP address.',
        'choices': [
            ('Both computers share the connection and split the bandwidth', False),
            ('An IP conflict occurs causing connectivity problems for one or both devices', True),
            ('The second device automatically chooses a different IP', False),
            ('Only the first device to connect keeps the IP — the second is disconnected', False),
        ]
    },
    {
        'text': 'Which TWO statements about IPv4 and IPv6 are correct? (Select TWO)',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'IPv4 uses 32-bit addresses in dotted decimal format. IPv6 uses 128-bit addresses in hexadecimal colon notation. IPv6 was created to solve the IPv4 address exhaustion problem.',
        'choices': [
            ('IPv4 uses 32-bit addresses written in dotted decimal format', True),
            ('IPv6 uses 64-bit addresses written in decimal format', False),
            ('IPv6 uses 128-bit addresses written in hexadecimal with colons', True),
            ('IPv4 supports more addresses than IPv6', False),
        ]
    },
    {
        'text': 'A device is configured with the correct IP and subnet mask but has the wrong DNS server. What will happen?',
        'domain': 'IP Addressing',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'With a wrong DNS server the device can still communicate by IP address and access local resources. However it will fail to resolve domain names so web browsing by name and most internet services will not work.',
        'choices': [
            ('The device loses all network connectivity', False),
            ('The device can communicate by IP but cannot resolve domain names for web browsing', True),
            ('The device automatically finds the correct DNS server', False),
            ('Only secure HTTPS sites are affected — HTTP sites still work', False),
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
    ip = Question.query.filter_by(exam='core1', domain='IP Addressing').count()
    print(f'Added {added} questions. Skipped {skipped} duplicates.')
    print(f'IP Addressing: {ip} | Core 1: {core1} | Overall: {total}')