import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app import app, db
from models import Question, Choice

questions_data = [

    # ── USB — Video 2 ─────────────────────────────────────────────────────────

    {
        'text': 'What was the maximum data transfer speed of USB 1.0 when it was introduced in 1996?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'USB 1.0 supported a maximum of 12 Mbps and was primarily used for basic peripherals like keyboards and mice.',
        'choices': [
            ('480 Mbps', False),
            ('5 Gbps', False),
            ('12 Mbps', True),
            ('1.5 Mbps', False),
        ]
    },
    {
        'text': 'What key feature was introduced with USB 2.0 around the year 2000?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'USB 2.0 increased speeds to 480 Mbps and introduced support for USB hubs allowing multiple devices to connect through a single port.',
        'choices': [
            ('Reversible connector design', False),
            ('Support for USB hubs and increased speed to 480 Mbps', True),
            ('Power delivery up to 240W', False),
            ('Thunderbolt 3 compatibility', False),
        ]
    },
    {
        'text': 'What is the data transfer speed of USB 3.0 introduced in 2008?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'USB 3.0 boosted speeds to 5 Gbps and enhanced power efficiency compared to USB 2.0.',
        'choices': [
            ('480 Mbps', False),
            ('10 Gbps', False),
            ('5 Gbps', True),
            ('20 Gbps', False),
        ]
    },
    {
        'text': 'What maximum speed does USB 4 Version 2.0 (released 2022) support?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'USB 4 Version 2.0 doubles the previous standard to 80 Gbps and is optimized for AI gaming and data-intensive applications.',
        'choices': [
            ('40 Gbps', False),
            ('20 Gbps', False),
            ('80 Gbps', True),
            ('60 Gbps', False),
        ]
    },
    {
        'text': 'What shape is a USB-B connector and where is it commonly found?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'USB-B is more square-shaped and is commonly found on printers and scanners at the device end of the cable.',
        'choices': [
            ('Rectangular — found on computers and chargers', False),
            ('Square-shaped — commonly found on printers and scanners', True),
            ('Oval-shaped — found on mobile devices', False),
            ('Reversible oval — found on laptops', False),
        ]
    },
    {
        'text': 'What distinguishes USB-C from all previous USB connector types?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'USB-C was the first USB connector with a fully reversible design meaning there is no up or down orientation. It also supports data power and display functions.',
        'choices': [
            ('It is the smallest USB connector ever made', False),
            ('It supports reversible insertion and handles data power and display in one connector', True),
            ('It only works with USB 4 devices', False),
            ('It has more pins than any previous USB connector', False),
        ]
    },
    {
        'text': 'What is the maximum power delivery supported by USB PD 3.1?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'USB PD 3.1 enables power transfers up to 240W and supports intelligent power negotiation between devices.',
        'choices': [
            ('100W', False),
            ('180W', False),
            ('240W', True),
            ('65W', False),
        ]
    },
    {
        'text': 'How can you visually distinguish a Thunderbolt port from a regular USB-C port?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'The connectors look identical but Thunderbolt ports have a small lightning bolt icon next to them. This is the only visual distinguishing characteristic.',
        'choices': [
            ('Thunderbolt ports are larger than USB-C ports', False),
            ('Thunderbolt ports have a small lightning bolt icon next to them', True),
            ('Thunderbolt ports are gold-coloured', False),
            ('Thunderbolt ports have more physical pins visible', False),
        ]
    },
    {
        'text': 'What maximum speed does Thunderbolt 3 or 4 support over its USB-C connector?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Thunderbolt 3 and 4 use the USB-C connector but allow speeds up to 40 Gbps. With USB4 Version 2.0 over Thunderbolt speeds can reach 80 Gbps.',
        'choices': [
            ('10 Gbps', False),
            ('20 Gbps', False),
            ('40 Gbps', True),
            ('5 Gbps', False),
        ]
    },

    # ── LIGHTNING — Video 3 ───────────────────────────────────────────────────

    {
        'text': 'Who developed the Lightning connector and on which devices was it primarily used?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Lightning is a proprietary connector developed by Apple found on many iPhones iPads and iPods particularly older models before Apple moved to USB-C.',
        'choices': [
            ('Google — used on Android phones and tablets', False),
            ('Apple — used on iPhones iPads and iPods particularly older models', True),
            ('Samsung — used on Galaxy smartphones', False),
            ('Microsoft — used on Surface tablets', False),
        ]
    },
    {
        'text': 'How many pins does the Lightning connector have and what does it support?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'The Lightning connector features 8 pins carrying power data audio and accessory signals. It is entirely digital-based enabling a wide range of functionality.',
        'choices': [
            ('30 pins — power and data only', False),
            ('8 pins — carrying power data audio and accessory signals', True),
            ('4 pins — power and charging only', False),
            ('16 pins — power data and video output', False),
        ]
    },
    {
        'text': 'What does MFi stand for and why is it important for Lightning cables?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'MFi stands for Made for iPhone/iPod/iPad. Using MFi-certified cables ensures full functionality best performance and avoids accessory error warnings on Apple devices.',
        'choices': [
            ('Mobile Fast Interface — ensures maximum charging speed', False),
            ('Made for iPhone/iPod/iPad — ensures full functionality and avoids accessory error warnings', True),
            ('Modular Firmware Interface — required for firmware updates', False),
            ('Multi-Function Integration — supports all Apple accessories', False),
        ]
    },
    {
        'text': 'What data transfer speed does the Lightning connector support?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Lightning for the most part matched USB 2.0 speeds. Now that Apple has moved to USB-C the newer devices support USB 3.0 and higher transfer rates.',
        'choices': [
            ('USB 3.0 speeds — 5 Gbps', False),
            ('USB 2.0 speeds — up to 480 Mbps', True),
            ('USB 4 speeds — 40 Gbps', False),
            ('USB 1.0 speeds — 12 Mbps', False),
        ]
    },
    {
        'text': 'What is a key difference between Lightning and Micro-USB connectors?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Lightning is reversible with a more robust pin design. Micro-USB was orientation-specific meaning you had to align it correctly before inserting it.',
        'choices': [
            ('Lightning is larger and sturdier than Micro-USB', False),
            ('Lightning is reversible while Micro-USB was orientation-specific and had to be aligned correctly', True),
            ('Micro-USB supports faster data transfer than Lightning', False),
            ('Lightning only works with Apple chargers while Micro-USB is universal', False),
        ]
    },
    {
        'text': 'How should you clean a Lightning port that has debris blocking it?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'The Lightning port should be cleaned carefully using compressed air or an ESD-safe brush. Avoid metal objects that could damage the pins.',
        'choices': [
            ('Use a metal pin or toothpick to remove debris', False),
            ('Use compressed air or an ESD-safe brush to carefully clear debris', True),
            ('Rinse with water and allow to dry completely', False),
            ('Use isopropyl alcohol applied with a cotton swab directly into the port', False),
        ]
    },
    {
        'text': 'Which Apple devices have moved away from Lightning to USB-C?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Apple has moved to USB-C on newer iPads Macs and other devices. The Lightning connector is now primarily found on older legacy Apple devices.',
        'choices': [
            ('Only MacBook laptops have moved to USB-C', False),
            ('Newer iPads Macs and Apple devices — Lightning remains only on older legacy devices', True),
            ('No Apple devices have moved to USB-C yet', False),
            ('Only iPhones have moved to USB-C', False),
        ]
    },

    # ── SERIAL CONNECTIONS — Video 4 ──────────────────────────────────────────

    {
        'text': 'How does serial communication transmit data?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Serial communication transmits data one bit at a time over a single channel. This differs from parallel communication which transmits 8 bits simultaneously.',
        'choices': [
            ('8 bits at a time over multiple parallel wires', False),
            ('One bit at a time over a single channel or wire', True),
            ('In packets of 64 bits using error correction', False),
            ('Wirelessly using radio frequency modulation', False),
        ]
    },
    {
        'text': 'What does RS-232 stand for and what type of devices used it?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'RS stands for Recommended Standard and 232 is an index number. It was one of the earliest serial standards used for connecting computers to modems printers and industrial equipment.',
        'choices': [
            ('Remote Serial 232 — used for wireless communications', False),
            ('Recommended Standard 232 — used for connecting computers to modems printers and industrial equipment', True),
            ('Rapid Synchronous 232 — used for high-speed network devices', False),
            ('Regulated Serial 232 — used exclusively in military applications', False),
        ]
    },
    {
        'text': 'What are the physical connector types used by RS-232 serial connections?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'RS-232 used DB-9 and DB-25 connectors. DB stands for D-subminiature (D-sub) and the number indicates the pin count. The D shape comes from the connector resembling the letter D when stood vertically.',
        'choices': [
            ('USB-A and USB-B', False),
            ('RJ-45 and RJ-11', False),
            ('DB-9 and DB-25', True),
            ('Mini-DIN and PS/2', False),
        ]
    },
    {
        'text': 'What is the maximum distance RS-232 signals can travel before degrading?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'RS-232 signals can travel approximately 50 feet (about 15 metres) before the signal degrades and would require repeating.',
        'choices': [
            ('1,200 metres', False),
            ('50 feet (approximately 15 metres)', True),
            ('500 feet', False),
            ('10 metres', False),
        ]
    },
    {
        'text': 'What improvement does RS-422 offer over RS-232?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'RS-422 uses differential signaling to reduce noise and supports up to 10 Mbps speeds and distances up to 1200 metres compared to RS-232\'s 50 feet and very low speeds.',
        'choices': [
            ('RS-422 supports wireless communication unlike RS-232', False),
            ('RS-422 uses differential signaling supporting up to 10 Mbps and distances up to 1200 metres', True),
            ('RS-422 supports multiple devices on the same bus', False),
            ('RS-422 uses USB connectors for modern compatibility', False),
        ]
    },
    {
        'text': 'What does RS-485 add over RS-422 and what is SCADA?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'RS-485 extends RS-422 with multi-point capability allowing multiple devices on the same bus. SCADA stands for Supervisory Control and Data Acquisition used in industrial applications like HVAC and factory automation.',
        'choices': [
            ('RS-485 adds encryption and is used in banking systems', False),
            ('RS-485 adds multi-device support on the same bus and is used in SCADA systems for industrial applications like HVAC', True),
            ('RS-485 adds Bluetooth capability to serial communications', False),
            ('RS-485 increases speed to 100 Mbps for industrial networks', False),
        ]
    },
    {
        'text': 'What is the purpose of a USB-to-serial adapter?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Most modern devices lack dedicated serial ports. A USB-to-serial adapter maintains compatibility allowing modern computers to connect to legacy devices that still have serial interfaces.',
        'choices': [
            ('Converts USB data to a format readable by older hard drives', False),
            ('Allows modern computers without serial ports to connect to legacy devices that use serial interfaces', True),
            ('Speeds up serial communications to match USB 3.0 speeds', False),
            ('Converts serial cables to work with USB-C ports', False),
        ]
    },
    {
        'text': 'What is the difference between baud rate and bits per second (bps)?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Baud rate refers to the number of signal state changes per second. For purely digital transmissions baud rate and bps are the same but other methods can carry more than one bit per state change making bps higher than baud rate.',
        'choices': [
            ('Baud rate and bps always mean exactly the same thing', False),
            ('Baud rate measures signal state changes per second while bps can be higher if multiple bits are carried per state change', True),
            ('Baud rate is always faster than bps in modern systems', False),
            ('Bps measures analog signals while baud rate measures digital signals', False),
        ]
    },

    # ── BLUETOOTH — Video 5 ───────────────────────────────────────────────────

    {
        'text': 'What is Bluetooth pairing and what does it create between two devices?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Bluetooth pairing establishes a trusted connection between two devices by creating a unique link key stored on both devices. This allows them to automatically reconnect without manual intervention each time.',
        'choices': [
            ('A temporary connection that must be re-established every session', False),
            ('A trusted connection that creates a unique link key stored on both devices for automatic future reconnection', True),
            ('A wired backup connection used when wireless fails', False),
            ('A one-time code that expires after 24 hours', False),
        ]
    },
    {
        'text': 'What is "bluejacking" in the context of Bluetooth security?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Bluejacking is sending unsolicited messages to a nearby Bluetooth device. It is considered a nuisance attack rather than a data theft attack.',
        'choices': [
            ('Unauthorized access to data stored on a Bluetooth device', False),
            ('Sending unsolicited messages to a nearby Bluetooth device', True),
            ('Intercepting Bluetooth communications in a stealth manner', False),
            ('Taking control of a Bluetooth device remotely', False),
        ]
    },
    {
        'text': 'What is "bluesnarfing"?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Bluesnarfing is unauthorized access to data stored on a Bluetooth device. This is more serious than bluejacking as actual data is stolen.',
        'choices': [
            ('Sending spam messages over Bluetooth', False),
            ('Unauthorized access to data stored on a Bluetooth-enabled device', True),
            ('Disrupting Bluetooth connections between paired devices', False),
            ('Cloning a Bluetooth device identity', False),
        ]
    },
    {
        'text': 'What are the range and speed specifications of Bluetooth 5.0?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Bluetooth 5.0 increased range to up to 40 metres and doubled speed to 2 Mbps compared to Bluetooth 4.0\'s 10 metres and 1 Mbps.',
        'choices': [
            ('10 metres range and 1 Mbps speed', False),
            ('60 metres range and 3 Mbps speed', False),
            ('40 metres range and 2 Mbps speed', True),
            ('100 metres range and 5 Mbps speed', False),
        ]
    },
    {
        'text': 'What new feature does Bluetooth 5.4 introduce compared to 5.0?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Bluetooth 5.4 extends range to 60 metres and introduces Low Energy Audio (LEA) periodic advertising and improved stability enabling larger lower-power networks.',
        'choices': [
            ('Higher data speed of 10 Mbps', False),
            ('Range up to 60 metres with Low Energy Audio and periodic advertising for larger lower-power networks', True),
            ('Support for USB-C direct pairing', False),
            ('Full HD video streaming capability', False),
        ]
    },
    {
        'text': 'What is Secure Simple Pairing (SSP) and why is it preferred over PIN-based pairing?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'SSP creates a shared secret or link key between devices used for authentication and encryption. It is more secure than PIN-based pairing and makes connections easier while protecting data.',
        'choices': [
            ('A PIN system that generates longer codes than standard pairing', False),
            ('A pairing method that creates a shared link key for authentication and encryption replacing the less secure PIN method', True),
            ('A simplified pairing process with no security for convenience', False),
            ('A pairing method exclusive to Bluetooth 5.4', False),
        ]
    },
    {
        'text': 'Which radio frequency bands does Bluetooth use that can cause interference with Wi-Fi?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Bluetooth uses the 2.4 GHz band (and 5 GHz depending on device and version) which are the same bands used by Wi-Fi causing potential channel conflicts and interference.',
        'choices': [
            ('900 MHz and 1.8 GHz', False),
            ('2.4 GHz and 5 GHz — the same bands as Wi-Fi', True),
            ('13.56 MHz like NFC', False),
            ('60 GHz exclusively', False),
        ]
    },
    {
        'text': 'What are the range and speed specifications of Bluetooth 4.0?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Bluetooth 4.0 had a range of only 10 metres and a data speed of 1 Mbps. It also only offered moderate power efficiency compared to newer versions.',
        'choices': [
            ('40 metres range and 2 Mbps speed', False),
            ('10 metres range and 1 Mbps speed', True),
            ('60 metres range and 1 Mbps speed', False),
            ('30 metres range and 3 Mbps speed', False),
        ]
    },

    # ── NFC/BLUETOOTH/HOTSPOTS — Video 6 ──────────────────────────────────────

    {
        'text': 'What frequency does NFC operate at and what spectrum does it belong to?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'NFC operates at 13.56 MHz within the RFID (Radio Frequency Identification) spectrum.',
        'choices': [
            ('2.4 GHz within the Wi-Fi spectrum', False),
            ('13.56 MHz within the RFID spectrum', True),
            ('900 MHz within the cellular spectrum', False),
            ('5 GHz within the Wi-Fi spectrum', False),
        ]
    },
    {
        'text': 'What are the three operating modes of NFC?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'NFC has three modes: peer-to-peer (devices communicate directly), reader/writer (device reads or writes to NFC tags), and card emulation (device acts as a payment card).',
        'choices': [
            ('Active passive and standby modes', False),
            ('Peer-to-peer reader/writer and card emulation', True),
            ('Transmit receive and relay modes', False),
            ('Secure standard and legacy modes', False),
        ]
    },
    {
        'text': 'What are the data transfer speeds supported by NFC?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'NFC supports data transfer speeds of 106 kbps 212 kbps and 424 kbps. These are very slow but sufficient since NFC typically only transfers small amounts of data.',
        'choices': [
            ('1 Mbps 2 Mbps and 5 Mbps', False),
            ('106 kbps 212 kbps and 424 kbps', True),
            ('10 Mbps 20 Mbps and 40 Mbps', False),
            ('480 Mbps matching USB 2.0 speeds', False),
        ]
    },
    {
        'text': 'What is a "relay attack" in NFC security?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A relay attack is when NFC data is intercepted and forwarded to a different device in an unauthorized manner allowing transactions to be performed without the owner\'s knowledge.',
        'choices': [
            ('Blocking NFC signals to prevent payments', False),
            ('Forwarding intercepted NFC data to a different device in an unauthorized manner', True),
            ('Replaying old NFC transactions repeatedly', False),
            ('Corrupting NFC data during transmission', False),
        ]
    },
    {
        'text': 'Comparing NFC Bluetooth and Wi-Fi hotspots which requires the most power?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Wi-Fi requires much higher power than Bluetooth which uses moderate power. NFC has the lowest power consumption of the three.',
        'choices': [
            ('NFC uses the most power due to its electromagnetic field', False),
            ('Bluetooth uses the most power due to constant pairing', False),
            ('Wi-Fi uses the most power followed by Bluetooth then NFC', True),
            ('All three use identical amounts of power', False),
        ]
    },
    {
        'text': 'What is tokenization in NFC payments and what security benefit does it provide?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Tokenization replaces sensitive payment data with a one-time code for each transaction. Even if intercepted the token cannot be reused making it much more secure.',
        'choices': [
            ('Encrypting the NFC signal so it cannot be read by other devices', False),
            ('Replacing payment data with a one-time code making intercepted data useless for future transactions', True),
            ('Converting payment data into a QR code format', False),
            ('Requiring a PIN for every NFC payment regardless of amount', False),
        ]
    },

    # ── MOBILE ACCESSORIES — Video 7 ──────────────────────────────────────────

    {
        'text': 'What is a "folio case" for a mobile device?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A folio case typically has a cover that folds over the screen and often includes slots for holding payment cards. It is usually a softer case design.',
        'choices': [
            ('A rigid hard case made from carbon fibre', False),
            ('A case with a cover that folds over the screen often with card slots', True),
            ('A case that only covers the back of the device', False),
            ('A waterproof case for underwater use', False),
        ]
    },
    {
        'text': 'What is a mobile power bank and what are its key considerations?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A power bank is a portable charging station that allows you to charge devices when no wall outlet is available. Key considerations include capacity number of ports and device compatibility.',
        'choices': [
            ('A high-capacity battery that replaces the internal battery', False),
            ('A portable charging device for when no wall outlet is available — key considerations include capacity ports and device compatibility', True),
            ('A solar-powered charging mat for outdoor use', False),
            ('A charging dock that only works at home', False),
        ]
    },
    {
        'text': 'What is the key difference between Virtual Reality (VR) and Augmented Reality (AR) headsets?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'VR is entirely digitally generated — everything you see is artificial. AR overlays digital information onto the real world that you are actually looking at.',
        'choices': [
            ('VR is wireless while AR requires a cable connection', False),
            ('VR is entirely digitally generated while AR overlays digital information onto the real world', True),
            ('VR is more expensive than AR in all cases', False),
            ('AR is only used for gaming while VR is used for productivity', False),
        ]
    },
    {
        'text': 'What connector types might wired headphones use for a mobile device connection?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Wired headphones for mobile devices may use a 3.5mm audio jack USB-C or Lightning (for older Apple devices). The correct type must match the device port.',
        'choices': [
            ('Only USB-A for all modern devices', False),
            ('3.5mm audio jack USB-C or Lightning depending on the device', True),
            ('Only RJ11 connectors for audio devices', False),
            ('Micro-USB exclusively on all Android devices', False),
        ]
    },
    {
        'text': 'What are the two main types of screen protectors and what distinguishes them?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Solid glass protectors offer high clarity smooth touch and better durability but are more bulky. Thin flexible film protectors are lighter and less noticeable but provide less protection.',
        'choices': [
            ('Plastic and metal — plastic is cheaper while metal is more protective', False),
            ('Solid glass (more durable but bulkier) and thin flexible film (lighter and less noticeable but less protective)', True),
            ('UV-coated and anti-glare — UV protects from sunlight while anti-glare reduces reflections', False),
            ('Tempered and laminated — tempered shatters safely while laminated holds together', False),
        ]
    },

    # ── APP CONNECTIVITY TROUBLESHOOTING — Video 8 ────────────────────────────

    {
        'text': 'A mobile app is not connecting properly. What should be checked regarding app permissions?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Certain apps need permission to access device features like photos camera or location. If permissions have not been granted the relevant features will not work.',
        'choices': [
            ('Check if the app has been purchased with a valid license', False),
            ('Verify the app has been granted the necessary permissions to access required device features', True),
            ('Check if the app is compatible with the screen resolution', False),
            ('Verify the app developer is registered with the app store', False),
        ]
    },
    {
        'text': 'Why might an app fail to connect when using an unsecured public Wi-Fi network?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Some applications especially on corporate-managed devices have policies that deny connections when an unsecured Wi-Fi is detected. Using secured networks or a VPN is recommended.',
        'choices': [
            ('Public Wi-Fi always has lower bandwidth preventing app connections', False),
            ('Corporate apps may have policies that block connections from unsecured networks — use secured Wi-Fi or a VPN', True),
            ('Public Wi-Fi uses IPv6 which some apps do not support', False),
            ('Apps require a static IP address that public Wi-Fi cannot provide', False),
        ]
    },
    {
        'text': 'What is the purpose of clearing an app\'s cache when troubleshooting connectivity issues?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Clearing the cache removes stale or unnecessary information from previous connections. This can resolve connectivity issues caused by corrupted or outdated cached data.',
        'choices': [
            ('It deletes all app data and resets the app to factory defaults', False),
            ('It removes stale or corrupted cached data from previous connections that may be causing issues', True),
            ('It reinstalls the app from the app store automatically', False),
            ('It clears the device RAM to free up memory for the app', False),
        ]
    },
    {
        'text': 'What roaming setting consideration is important for mobile connectivity when travelling?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'When travelling without Wi-Fi access data roaming must be enabled in device settings to allow cellular connectivity. Without it the device will not connect to foreign cellular networks.',
        'choices': [
            ('Airplane mode should be enabled while travelling', False),
            ('Data roaming must be enabled to allow cellular connectivity when not on your home network', True),
            ('GPS must be enabled for apps to connect while roaming', False),
            ('Bluetooth must be disabled to preserve cellular connection strength', False),
        ]
    },
    {
        'text': 'What does a cloud-based VPN provide for mobile app security?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A cloud-based VPN encrypts all communications coming in and out of the device. Once connected all traffic is encrypted providing security especially on public or unsecured Wi-Fi.',
        'choices': [
            ('It speeds up app connections by routing through faster servers', False),
            ('It encrypts all device communications providing security especially on public or unsecured networks', True),
            ('It automatically fixes app configuration errors', False),
            ('It blocks ads within mobile applications', False),
        ]
    },

    # ── UPDATING MOBILE DEVICES — Video 9 ─────────────────────────────────────

    {
        'text': 'What is the difference between a major and minor mobile OS update?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A major update increments the main version number (e.g. iOS 17 to iOS 18) and includes new features. Minor updates increment smaller numbers and typically address security fixes and bug patches.',
        'choices': [
            ('Major updates are free while minor updates require payment', False),
            ('Major updates increment the main version number with new features while minor updates address security fixes and patches', True),
            ('Major updates require a new device while minor updates work on any device', False),
            ('There is no practical difference between major and minor updates', False),
        ]
    },
    {
        'text': 'Why should mobile device updates be applied over Wi-Fi rather than cellular data?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Updates can be quite large and downloading them over cellular service could incur significant data charges. Wi-Fi avoids these charges and is typically faster.',
        'choices': [
            ('Cellular networks are too slow to download updates', False),
            ('Updates downloaded over cellular can be very large incurring significant data charges', True),
            ('Updates only work when connected to the manufacturer\'s Wi-Fi', False),
            ('Cellular updates are less secure than Wi-Fi updates', False),
        ]
    },
    {
        'text': 'What should be done to prepare a mobile device before applying a major OS update?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Before a major update you should back up the device and plug it into power. Updates require sufficient storage to download before applying and the battery should not drain during the process.',
        'choices': [
            ('Factory reset the device to ensure a clean installation', False),
            ('Back up the device and plug it into power to prevent battery drain during the update', True),
            ('Uninstall all apps to free up storage before updating', False),
            ('Disable all network connections before starting the update', False),
        ]
    },
    {
        'text': 'What typically happens if a mobile OS update fails to install?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'If an update fails the device will typically revert to its previous state leaving it in a consistent working condition. It will usually notify the user and ask to retry.',
        'choices': [
            ('The device becomes permanently bricked and must be repaired', False),
            ('The device reverts to its previous state and notifies the user to retry', True),
            ('The update is applied partially leaving the device in an unstable state', False),
            ('The device automatically contacts the manufacturer for support', False),
        ]
    },
    {
        'text': 'Why should security updates be applied as soon as they are available?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Security updates address vulnerabilities that have been discovered. Delaying installation leaves the device exposed to known exploits that attackers can take advantage of.',
        'choices': [
            ('Security updates always improve battery life significantly', False),
            ('Security updates address discovered vulnerabilities — delaying leaves the device exposed to known exploits', True),
            ('Security updates are required to keep the device warranty valid', False),
            ('Security updates improve app compatibility with newer services', False),
        ]
    },
    {
        'text': 'Why is insufficient storage a potential problem when updating a mobile OS?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'The update file must be downloaded and temporarily stored on the device before being applied. If there is not enough free space the update cannot be downloaded even if the new OS is the same size as the old one.',
        'choices': [
            ('The OS takes up more space after installation leaving less for apps', False),
            ('The update file must be temporarily stored on the device before being applied requiring sufficient free space', True),
            ('Storage affects update speed not whether the update can run', False),
            ('Insufficient storage only affects app updates not OS updates', False),
        ]
    },

    # ── MOBILE SECURITY — Video 10 ────────────────────────────────────────────

    {
        'text': 'Why is malware considered less likely on mobile devices compared to desktop computers?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Mobile platforms like iOS and Android typically only allow app installations from their official stores (App Store and Google Play) which vet apps for malware. Desktop computers allow installation from anywhere.',
        'choices': [
            ('Mobile devices run slower processors that prevent malware execution', False),
            ('Mobile platforms restrict app installations to official vetted stores unlike desktops which allow installation from anywhere', True),
            ('Mobile devices use a different type of memory that malware cannot infect', False),
            ('Mobile devices are too small to store malware files', False),
        ]
    },
    {
        'text': 'What is "jailbreaking" a mobile device and what security risk does it introduce?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Jailbreaking removes the manufacturer\'s restrictions allowing installation of apps from outside the official store. This significantly increases the risk of malware infection since apps are no longer vetted.',
        'choices': [
            ('Replacing the battery without manufacturer approval — increases warranty risk', False),
            ('Removing manufacturer restrictions to install unapproved apps — significantly increases malware risk', True),
            ('Unlocking a device for use on any carrier — increases cost of repairs', False),
            ('Overclocking the device CPU — increases heat and battery drain', False),
        ]
    },
    {
        'text': 'What mobile security feature allows you to protect a lost or stolen device remotely?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Remote lock and wipe allows you to sign into your account from any other device via a browser and lock or erase the lost device preventing unauthorized access.',
        'choices': [
            ('Two-factor authentication which locks the device after failed attempts', False),
            ('Remote lock and wipe — sign into your account from any browser to lock or erase the device remotely', True),
            ('Device encryption which requires a PIN even after a factory reset', False),
            ('Biometric authentication which only responds to the owner\'s face', False),
        ]
    },
    {
        'text': 'Why is public Wi-Fi a greater security risk for mobile devices than for desktop computers?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Mobile devices almost entirely rely on wireless connections and we frequently use them on public Wi-Fi. Data interception is easier on wireless networks especially unsecured ones compared to wired corporate networks.',
        'choices': [
            ('Mobile devices have weaker processors that cannot handle encryption', False),
            ('Mobile devices rely entirely on wireless connections making data interception easier especially on unsecured public Wi-Fi', True),
            ('Public Wi-Fi providers specifically target mobile devices', False),
            ('Mobile devices broadcast their identity making them easier to find', False),
        ]
    },
    {
        'text': 'What is data interception on mobile devices and how can it be prevented?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Data interception occurs when someone captures your wireless communications. It can be prevented by using apps that support encrypted communications enabling a VPN and avoiding unsecured public Wi-Fi.',
        'choices': [
            ('Physical theft of the device — prevented by cable locks', False),
            ('Capturing wireless communications — prevented by using encrypted apps VPNs and avoiding unsecured Wi-Fi', True),
            ('Accessing device storage — prevented by screen locks', False),
            ('Shoulder surfing at the screen — prevented by privacy filters', False),
        ]
    },
    {
        'text': 'Why should Bluetooth be disabled when not in use on a mobile device?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'When Bluetooth is active others may be able to attempt to establish a connection to your device even without your knowledge. Disabling it when not in use removes this attack surface.',
        'choices': [
            ('Bluetooth drains the battery significantly even when idle', False),
            ('When Bluetooth is active others may attempt unauthorized connections — disabling it removes this risk', True),
            ('Bluetooth interferes with cellular signals reducing call quality', False),
            ('Bluetooth causes overheating on modern mobile devices', False),
        ]
    },

    # ── WIRED VS WIRELESS — Video 11 ──────────────────────────────────────────

    {
        'text': 'What is the charging efficiency of wired charging compared to wireless charging?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Wired charging achieves about 90-95% efficiency. Wireless charging is only about 75-85% efficient with lost energy dissipated as heat which can affect battery longevity.',
        'choices': [
            ('Wired 50-60% vs wireless 90-95%', False),
            ('Wired 90-95% vs wireless 75-85%', True),
            ('Both achieve approximately 95% efficiency', False),
            ('Wired 75% vs wireless 99%', False),
        ]
    },
    {
        'text': 'What problem can fast wired charging (over 50W) cause for a mobile battery?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Fast wired charging over 50W generates more heat which can increase wear on the lithium-ion cells and shorten overall battery lifespan despite the convenience of faster charging.',
        'choices': [
            ('It causes the phone to overheat immediately and shut down', False),
            ('It generates more heat which increases wear on lithium-ion cells and can shorten battery lifespan', True),
            ('It damages the charging port from excessive current', False),
            ('It overloads the wireless charging coil causing permanent damage', False),
        ]
    },
    {
        'text': 'Why might a phone case prevent wireless charging from working?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'If the case is not designed to pass the magnetic charging field through it the case can block the connection entirely. Cases must be compatible with wireless charging to work.',
        'choices': [
            ('Cases cause static electricity that interferes with wireless charging', False),
            ('A case not designed to pass the magnetic field through it can block wireless charging entirely', True),
            ('Cases block the Wi-Fi signal required for wireless charging', False),
            ('Thick cases prevent the charging pad from detecting the device', False),
        ]
    },
    {
        'text': 'What is a key limitation of wireless headphones compared to wired headphones?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Wireless headphones must be charged separately. If they run out of power you lose audio completely. Wired headphones draw power from the device itself and never need charging.',
        'choices': [
            ('Wireless headphones always have lower audio quality than wired', False),
            ('Wireless headphones must be charged separately and will lose audio if the battery runs out', True),
            ('Wireless headphones cannot connect to multiple devices simultaneously', False),
            ('Wireless headphones only work within 1 metre of the device', False),
        ]
    },
    {
        'text': 'How does wireless charging physically work on a mobile device?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Wireless charging does not mean the device charges from a distance. The device must be placed on a specific cradle or platform that makes a magnetic connection at the base or back of the device.',
        'choices': [
            ('The device receives power through Wi-Fi radio waves from a router', False),
            ('The device must be placed on a specific cradle or platform that makes a magnetic connection to charge', True),
            ('The device charges through Bluetooth from a nearby charging hub', False),
            ('The device charges from any surface using static electricity', False),
        ]
    },

    # ── BATTERY LIFE MANAGEMENT — Video 12 ────────────────────────────────────

    {
        'text': 'What is a charge cycle for a lithium-ion battery and how many can it typically handle?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'A charge cycle is one full recharge of the battery. Most lithium-ion batteries can handle between 300 and 500 charge cycles before significant degradation occurs.',
        'choices': [
            ('One hour of charging — batteries handle 1000 to 2000 hours', False),
            ('One full recharge — most batteries handle 300 to 500 charge cycles', True),
            ('One discharge to zero — batteries handle up to 100 deep cycles', False),
            ('One week of normal use — batteries last 2 to 3 years', False),
        ]
    },
    {
        'text': 'What is the recommended charge level range for maximizing lithium-ion battery lifespan?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Keeping the battery between 20% and 80% has been shown to be ideal for most modern lithium-ion batteries. Repeatedly charging to 100% and draining to 0% accelerates degradation.',
        'choices': [
            ('0% to 100% for maximum capacity', False),
            ('50% to 100% to avoid deep discharge', False),
            ('20% to 80% as the optimal range for longevity', True),
            ('10% to 90% for the widest usable range', False),
        ]
    },
    {
        'text': 'What is "smart charging" on a mobile device?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Smart charging automatically stops charging at around 80-85% rather than always charging to 100%. This helps preserve battery health by keeping the charge within the optimal range.',
        'choices': [
            ('A feature that charges the battery faster using AI to detect device usage', False),
            ('Automatically stops charging at around 80-85% to preserve battery health within the optimal range', True),
            ('Wireless charging that adjusts power based on the surrounding temperature', False),
            ('A feature that allows charging from multiple sources simultaneously', False),
        ]
    },
    {
        'text': 'What is battery calibration and when is it recommended?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Battery calibration involves occasionally letting the battery run down to zero. This helps recalibrate the usage statistics for more accurate battery percentage readings. It is not recommended regularly but occasionally is fine.',
        'choices': [
            ('Charging to exactly 50% every day to keep the battery centred', False),
            ('Occasionally letting the battery run to zero to recalibrate usage statistics for more accurate percentage readings', True),
            ('Replacing the battery every 6 months regardless of condition', False),
            ('Resetting battery settings in the device configuration menu monthly', False),
        ]
    },
    {
        'text': 'What environmental factor can significantly reduce a mobile device battery performance?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Exposure to extreme temperatures both hot and cold can significantly affect battery performance and lifespan. Avoid leaving the device in direct sunlight or in very cold conditions.',
        'choices': [
            ('Using the device while it is charging', False),
            ('Exposure to extreme temperatures both hot and cold', True),
            ('Running multiple apps simultaneously for extended periods', False),
            ('Using maximum screen brightness indoors', False),
        ]
    },
    {
        'text': 'What display setting adjustment can most directly extend mobile battery life?',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': False,
        'explanation': 'Reducing screen brightness is one of the most direct ways to extend battery life since the display is one of the highest power consumers on a mobile device.',
        'choices': [
            ('Changing the screen resolution to a lower setting', False),
            ('Reducing screen brightness as the display is one of the highest power consumers', True),
            ('Switching from portrait to landscape orientation', False),
            ('Disabling auto-rotate to save processing power', False),
        ]
    },

    # ── MULTI SELECT QUESTIONS ────────────────────────────────────────────────

    {
        'text': 'Which TWO of the following are correct about USB-C connectors? (Select TWO)',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'USB-C introduced a reversible connector design and supports multiple functions including data transfer power delivery and video output in one connector.',
        'choices': [
            ('USB-C has a fully reversible design with no up or down orientation', True),
            ('USB-C only supports data transfer not power delivery', False),
            ('USB-C supports data power and display functions in one connector', True),
            ('USB-C is identical to Lightning and they are interchangeable', False),
        ]
    },
    {
        'text': 'Which TWO of the following are Bluetooth security threats? (Select TWO)',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Bluejacking sends unsolicited messages to nearby devices. Bluesnarfing is unauthorized access to data on a Bluetooth device. Both are specific Bluetooth attack types.',
        'choices': [
            ('Bluejacking — sending unsolicited messages to a nearby Bluetooth device', True),
            ('Bluesnarfing — unauthorized access to data on a Bluetooth device', True),
            ('Bluefire — corrupting Bluetooth firmware remotely', False),
            ('Bluecloning — creating a duplicate of a Bluetooth device', False),
        ]
    },
    {
        'text': 'Which TWO of the following are best practices for mobile device security? (Select TWO)',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Keeping software updated patches security vulnerabilities. Enabling remote wipe protects data if the device is lost or stolen. Both are essential mobile security practices.',
        'choices': [
            ('Keep all apps and OS updated to patch security vulnerabilities', True),
            ('Always connect to any available open Wi-Fi to conserve cellular data', False),
            ('Enable remote lock and wipe in case the device is lost or stolen', True),
            ('Jailbreak the device for better app selection', False),
        ]
    },
    {
        'text': 'Which TWO factors negatively impact lithium-ion battery health over time? (Select TWO)',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Repeatedly fully charging to 100% and discharging to 0% (deep discharge cycles) and exposure to extreme temperatures both degrade lithium-ion battery health over time.',
        'choices': [
            ('Repeatedly charging to 100% and discharging to 0%', True),
            ('Keeping the device screen brightness at 50%', False),
            ('Exposure to extreme temperatures hot or cold', True),
            ('Using Bluetooth headphones instead of wired headphones', False),
        ]
    },
    {
        'text': 'Which TWO of the following correctly compare NFC to Bluetooth? (Select TWO)',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'NFC has a much shorter range (4cm) versus Bluetooth (10-100m). NFC also has much lower power consumption than Bluetooth making it suitable for always-on passive tags.',
        'choices': [
            ('NFC has a much shorter range than Bluetooth — approximately 4cm vs 10-100 metres', True),
            ('NFC is faster than Bluetooth for data transfers', False),
            ('NFC consumes less power than Bluetooth', True),
            ('NFC requires device pairing just like Bluetooth', False),
        ]
    },
    {
        'text': 'Which TWO of the following are advantages of wired charging over wireless charging? (Select TWO)',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Wired charging is more efficient (90-95% vs 75-85%) and generally charges the device faster. Wireless charging loses energy as heat which also affects battery longevity.',
        'choices': [
            ('Wired charging is more energy efficient at 90-95% vs 75-85% for wireless', True),
            ('Wired charging requires a special compatible case', False),
            ('Wired charging generally charges the device faster than wireless', True),
            ('Wired charging works at any distance from the power source', False),
        ]
    },
    {
        'text': 'Which TWO of the following are true about the Lightning connector? (Select TWO)',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Lightning is a proprietary Apple connector with a reversible design. It is not compatible with USB-C and the two cannot be used interchangeably.',
        'choices': [
            ('Lightning is a proprietary Apple connector not an open standard', True),
            ('Lightning and USB-C are interchangeable with an adapter included in the box', False),
            ('Lightning has a reversible design with no top or bottom orientation', True),
            ('Lightning supports faster speeds than USB-C', False),
        ]
    },
    {
        'text': 'Which TWO of the following are best practices when updating a mobile device? (Select TWO)',
        'domain': 'Mobile Devices',
        'exam': 'core1',
        'multi_select': True,
        'explanation': 'Connecting to Wi-Fi avoids cellular data charges for large updates. Plugging in to power prevents the battery from draining during the update process.',
        'choices': [
            ('Use Wi-Fi instead of cellular data for downloading updates', True),
            ('Update while on 1% battery to force a full calibration cycle', False),
            ('Plug the device into power before starting a major update', True),
            ('Uninstall all apps before applying OS updates', False),
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
    multi = Question.query.filter_by(exam='core1', multi_select=True).count()
    print(f'Added {added} questions. Skipped {skipped} duplicates.')
    print(f'Core 1 total: {core1} | Multi-select Core 1: {multi} | Overall: {total}')