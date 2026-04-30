import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app import app, db
from models import Question, Choice

questions_data = [

    # Q2 - After factory reset (multi-select 3)
    {
        'text': 'Which activities will be required after performing a factory reset on a mobile device? (Select THREE)',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': True,
        'explanation': 'After a factory reset the OS needs updating personal data must be restored and security settings must be reconfigured. The SIM card does not need replacing and Bluetooth re-pairing is optional.',
        'choices': [
            ('Update the operating system', True),
            ('Physically replace the SIM card', False),
            ('Restore personal data and settings', True),
            ('Pair a new Bluetooth headset for the first time', False),
            ('Reconfigure security settings', True),
        ]
    },

    # Q3 - Wi-Fi frequencies (multi-select 2)
    {
        'text': 'Which frequency bands do Wi-Fi networks use? (Select TWO)',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': True,
        'explanation': 'Wi-Fi networks operate on 2.4 GHz and 5 GHz bands. The newer Wi-Fi 6E also uses 6 GHz but 2.4 GHz and 5 GHz are the standard bands tested on the exam.',
        'choices': [
            ('5 GHz', True),
            ('700 MHz', False),
            ('2.4 GHz', True),
            ('28 GHz', False),
            ('900 MHz', False),
        ]
    },

    # Q4 - App-specific sync
    {
        'text': 'What type of synchronization is exemplified by syncing only your photos to Google Photos?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'Syncing only photos to a single service like Google Photos is app-specific sync — it only synchronizes data for that one application rather than a full device or cloud-to-cloud backup.',
        'choices': [
            ('Full device backup', False),
            ('Cloud-to-cloud sync', False),
            ('Desktop-based sync', False),
            ('App-specific sync', True),
            ('Carrier sync', False),
        ]
    },

    # Q6 - iTunes backup type
    {
        'text': 'What type of backup is an iPhone backup created using iTunes on a desktop computer?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'Backing up an iPhone using iTunes on a desktop is a computer-based (local) backup. The data is stored on the computer rather than in the cloud or on a carrier server.',
        'choices': [
            ('Cloud-based backup', False),
            ('App-specific backup', False),
            ('Carrier backup', False),
            ('Computer-based backup', True),
            ('MDM-managed backup', False),
        ]
    },

    # Q7 - BYOD benefits (multi-select 3)
    {
        'text': 'What are the potential primary benefits of BYOD? (Select THREE)',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': True,
        'explanation': 'BYOD benefits include increased productivity (employees use familiar devices), employee satisfaction (personal device preference), and reduced costs (company does not purchase hardware).',
        'choices': [
            ('Full corporate control of the device', False),
            ('Increased productivity', True),
            ('Guaranteed data security', False),
            ('Employee satisfaction', True),
            ('Reduced costs', True),
        ]
    },

    # Q10 - Causes of overheating (multi-select 3)
    {
        'text': 'Which activities are more likely to cause a mobile device to overheat? (Select THREE)',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': True,
        'explanation': 'Video streaming gaming and charging all generate significant heat. Reading a text document uses minimal CPU resources and enabling airplane mode reduces radio activity.',
        'choices': [
            ('Reading a text document', False),
            ('Video streaming', True),
            ('Gaming', True),
            ('Charging', True),
            ('Enabling airplane mode', False),
        ]
    },

    # Q12 - Battery failure symptoms (multi-select 3)
    {
        'text': 'Which of the following are symptoms of a failing mobile device battery? (Select THREE)',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': True,
        'explanation': 'A failing battery shows overheating rapid battery drain and physical swelling or unexpected shutdowns. GPS accuracy and screen brightness are unrelated to battery health.',
        'choices': [
            ('Improved GPS accuracy', False),
            ('Overheating', True),
            ('Rapid battery drain', True),
            ('Increased screen brightness', False),
            ('Device swelling or unexpected shutdowns', True),
        ]
    },

    # Q13 - RAM replacement order
    {
        'text': 'What is the correct order for replacing RAM in an upgradable mobile device?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'The correct order is: Power down first → remove back cover → disconnect battery → replace module. Always power off before opening and disconnect the battery before touching components.',
        'choices': [
            ('Remove back cover → replace module → disconnect battery → power down', False),
            ('Power down → remove back cover → disconnect battery → replace module', True),
            ('Disconnect battery → power down → replace module → remove back cover', False),
            ('Replace module → power down → remove back cover → disconnect battery', False),
            ('Power down → replace module → remove back cover → disconnect battery', False),
        ]
    },

    # Q16 - Cellular standard unified GSM/CDMA
    {
        'text': 'Which cellular standard eliminated the need for both GSM and CDMA by introducing a single unified standard?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': '4G LTE introduced a single unified standard replacing the previous GSM and CDMA divide. All 4G LTE carriers use the same standard making devices more universally compatible.',
        'choices': [
            ('2G', False),
            ('3G', False),
            ('4G LTE', True),
            ('5G', False),
            ('WiMAX', False),
        ]
    },

    # Q17 - 5G capabilities
    {
        'text': 'Which statement best describes 5G network capabilities?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': '5G can be up to 100x faster than 4G with potential speeds up to 20 Gbps on higher frequencies. It offers dramatically lower latency and greater device density support.',
        'choices': [
            ('Maximum speed of 300 Mbps same as LTE Advanced', False),
            ('Designed only for voice calls', False),
            ('Up to 100x faster than 4G with potential speeds up to 20 Gbps', True),
            ('Based on CDMA technology', False),
            ('Requires a physical SIM card', False),
        ]
    },

    # Q18 - Bluetooth pairing sequence
    {
        'text': 'What is the correct sequence for pairing a Bluetooth device to a mobile phone?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'The correct sequence is: Enable Bluetooth on both devices → set to discoverable mode → select the device from the list → confirm the PIN to complete pairing.',
        'choices': [
            ('Enter PIN → enable Bluetooth → set discoverable → select device', False),
            ('Enable Bluetooth → enter PIN → set discoverable → select device', False),
            ('Enable Bluetooth → set discoverable → select device → confirm PIN', True),
            ('Set discoverable → select device → enable Bluetooth → confirm PIN', False),
            ('Select device → enable Bluetooth → confirm PIN → set discoverable', False),
        ]
    },

    # Q19 - SIM card contents (multi-select 3)
    {
        'text': 'Which of the following are stored on a physical SIM card? (Select THREE)',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': True,
        'explanation': 'A SIM card stores carrier and subscriber information contacts and messages and the phone number. BIOS settings and the OS are stored on the device hardware not the SIM.',
        'choices': [
            ('The device BIOS settings', False),
            ('Carrier and subscriber information', True),
            ('Contacts and messages', True),
            ('The phone operating system', False),
            ('Phone number', True),
        ]
    },

    # Q22 - COPE definition
    {
        'text': 'What does COPE stand for in mobile device management?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'COPE stands for Corporate Owned Personally Enabled. The company owns the device but allows personal use. This gives the company more control than BYOD while allowing employee flexibility.',
        'choices': [
            ('Company Operated Personal Equipment', False),
            ('Corporate Owned Personally Enabled', True),
            ('Choose Owned Personal Environment', False),
            ('Corporate Optimized Portable Equipment', False),
            ('Company Owned Protected Environment', False),
        ]
    },

    # Q23 - HDD/SSD replacement symptoms (multi-select 3)
    {
        'text': 'Which symptoms suggest an HDD or SSD replacement may be needed on a mobile workstation? (Select THREE)',
        'domain': 'Laptops', 'exam': 'core1', 'multi_select': True,
        'explanation': 'Slow boot times clicking sounds from storage and missing OS or storage errors all indicate drive failure. Bluetooth pairing failures and battery overheating are unrelated to storage.',
        'choices': [
            ('Bluetooth pairing failures', False),
            ('Slow boot times', True),
            ('Clicking sounds from storage', True),
            ('Overheating battery', False),
            ('Missing OS or storage errors', True),
        ]
    },

    # Q24 - MDM data sync types (multi-select 3)
    {
        'text': 'Which types of data can typically be synchronized through an MDM or account setup? (Select THREE)',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': True,
        'explanation': 'MDM can synchronize contacts calendar and mail. SIM card firmware and cellular tower data are hardware and network infrastructure items not synchronized through MDM.',
        'choices': [
            ('SIM card firmware', False),
            ('Contacts', True),
            ('Calendar', True),
            ('Cellular tower data', False),
            ('Mail', True),
        ]
    },

    # Q25 - GPS how it works
    {
        'text': 'How does GPS determine a device\'s location?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'GPS uses signal differences from at least four satellites to calculate longitude latitude and altitude. This process is called trilateration and requires four satellites for accurate 3D positioning.',
        'choices': [
            ('By scanning nearby Wi-Fi networks only', False),
            ('By using signal differences from at least four satellites to calculate longitude latitude and altitude', True),
            ('By pinging the nearest cellular tower', False),
            ('By reading the device SIM card', False),
            ('By using NFC tags in the environment', False),
        ]
    },

    # Q26 - Cellular coverage cells
    {
        'text': 'How do cellular networks provide coverage to mobile devices?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'Cellular networks divide land areas into cells each served by its own antenna or tower. As a device moves between cells it hands off seamlessly providing continuous coverage.',
        'choices': [
            ('Using a single central antenna for an entire country', False),
            ('By dividing land areas into cells each served by its own antenna', True),
            ('Through satellite signals only', False),
            ('By connecting devices directly to each other', False),
            ('Using only underground fiber optic cables', False),
        ]
    },

    # Q28 - 3G capabilities (multi-select 3)
    {
        'text': 'Which features became possible thanks to 3G technology? (Select THREE)',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': True,
        'explanation': '3G enabled GPS functionality video conferencing and mobile television. Basic SMS was already available on 2G networks and 10 Gbps speeds are associated with 5G.',
        'choices': [
            ('Basic SMS text messaging', False),
            ('GPS functionality', True),
            ('Video conferencing', True),
            ('10 Gbps data speeds', False),
            ('Mobile television', True),
        ]
    },

    # Q30 - LTE Advanced throughput
    {
        'text': 'What maximum throughput does LTE Advanced (LTE-A) support?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'LTE Advanced (LTE-A) supports a maximum throughput of 300 Mbps — double the 150 Mbps of standard LTE. It achieves this through carrier aggregation and other improvements.',
        'choices': [
            ('150 Mbps', False),
            ('300 Mbps', True),
            ('600 Mbps', False),
            ('1 Gbps', False),
            ('10 Gbps', False),
        ]
    },

    # Q31 - 5G introduced year
    {
        'text': 'When was 5G officially introduced?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': '5G was introduced in 2020. It brought dramatically higher speeds lower latency and the ability to connect many more devices simultaneously compared to 4G LTE.',
        'choices': [
            ('2015', False),
            ('2017', False),
            ('2018', False),
            ('2019', False),
            ('2020', True),
        ]
    },

    # Q32 - 5G speed higher frequencies
    {
        'text': 'What maximum speed is 5G designed to support over higher frequencies?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': '5G over higher mmWave frequencies is designed to support up to 10 Gbps. Over other frequencies 5G delivers 100 to 900 Mbps. The theoretical maximum of 20 Gbps applies to the overall standard.',
        'choices': [
            ('300 Mbps', False),
            ('1 Gbps', False),
            ('5 Gbps', False),
            ('10 Gbps', True),
            ('20 Gbps', False),
        ]
    },

    # Q33 - 5G speed non-high frequencies
    {
        'text': 'What throughput range can 5G deliver over non-high (sub-6GHz) frequencies?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': '5G over sub-6GHz frequencies delivers between 100 and 900 Mbps. This is slower than mmWave 5G but covers much greater distances and is the most common 5G deployment.',
        'choices': [
            ('10 to 50 Mbps', False),
            ('50 to 150 Mbps', False),
            ('100 to 900 Mbps', True),
            ('1 to 5 Gbps', False),
            ('5 to 10 Gbps', False),
        ]
    },

    # Q35 - Wi-Fi vs cellular range
    {
        'text': 'What is a key limitation of 802.11 Wi-Fi compared to cellular networks?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'Wi-Fi has a limited range typically 30-100 metres and requires a local access point. Cellular networks cover much larger areas through towers making cellular far better for wide-area connectivity.',
        'choices': [
            ('Lower data speeds', False),
            ('Limited range requiring a local access point', True),
            ('No support for voice communication', False),
            ('Incompatibility with mobile phones', False),
            ('Only supports 2.4 GHz frequency', False),
        ]
    },

    # Q38 - Physical SIM card info (multi-select 3)
    {
        'text': 'What information is stored on a SIM card? (Select THREE)',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': True,
        'explanation': 'A SIM card stores carrier and subscriber information the SIM ID and phone number and contacts and messages. Device screen resolution and app installation history are stored on the device not the SIM.',
        'choices': [
            ('Device screen resolution', False),
            ('Carrier and subscriber information', True),
            ('SIM ID and phone number', True),
            ('App installation history', False),
            ('Contacts and messages', True),
        ]
    },

    # Q39 - Moving SIM between phones
    {
        'text': 'What is the result of moving a physical SIM card from one phone to another?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'Moving a SIM card transfers your phone number and any stored contacts and messages to the new device. The IMEI stays with the hardware and the OS does not transfer.',
        'choices': [
            ('The IMEI number transfers to the new phone', False),
            ('Only the carrier settings transfer', False),
            ('Your phone number and stored contacts and messages move to the new device', True),
            ('The new phone inherits the old phone operating system', False),
            ('The SIM must be reprogrammed by the carrier first', False),
        ]
    },

    # Q40 - eSIM advantage
    {
        'text': 'What is the main advantage of an eSIM over a physical SIM card?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'An eSIM can be transferred between devices using software without physically swapping a card. This makes switching carriers or devices much easier and allows multiple carrier profiles on one device.',
        'choices': [
            ('It stores more contacts than a physical SIM', False),
            ('It supports more cellular frequencies', False),
            ('It can be transferred between devices using software without physically swapping a card', True),
            ('It is compatible with older 3G networks only', False),
            ('It eliminates the need for a carrier plan', False),
        ]
    },

    # Q41 - Multiple SIMs benefit
    {
        'text': 'What benefit does a phone with multiple SIM support provide?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'Multiple SIM support allows having multiple phone numbers or profiles on the same device. This is useful for separating personal and work lines or using a local SIM while travelling.',
        'choices': [
            ('Faster GPS lock', False),
            ('Longer battery life', False),
            ('The ability to have multiple phone numbers or profiles on the same device', True),
            ('Stronger Wi-Fi signal', False),
            ('Automatic switching between 4G and 5G', False),
        ]
    },

    # Q42 - Bluetooth PIN purpose
    {
        'text': 'What is the purpose of the PIN in the Bluetooth pairing process?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'The PIN verifies connectivity and ensures security during the initial pairing setup. It confirms that the correct devices are being paired and prevents unauthorized connections.',
        'choices': [
            ('To encrypt data during every Bluetooth session', False),
            ('To verify connectivity and ensure security during initial setup', True),
            ('To assign a static IP address to the Bluetooth device', False),
            ('To register the device with the manufacturer', False),
            ('To enable NFC on the device', False),
        ]
    },

    # Q43 - Bluetooth re-pairing
    {
        'text': 'How many times do you need to go through the Bluetooth pairing process for the same device?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'Bluetooth pairing only needs to happen once. After that both devices store the link key and automatically reconnect whenever they are within range of each other.',
        'choices': [
            ('Every time you reconnect', False),
            ('Once per day', False),
            ('Once per software update', False),
            ('Only once — after that it connects automatically', True),
            ('Twice — once for each direction of communication', False),
        ]
    },

    # Q44 - GPS satellites needed
    {
        'text': 'How many satellites must a device be able to see to get accurate GPS readings?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'A GPS device needs to see at least four satellites for accurate positioning. Three satellites can determine longitude and latitude but a fourth is needed to also calculate altitude and improve accuracy.',
        'choices': [
            ('One', False),
            ('Two', False),
            ('Three', False),
            ('Four', True),
            ('Six', False),
        ]
    },

    # Q45 - GPS origin
    {
        'text': 'Who originally created GPS technology?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'GPS was created by the United States Department of Defense originally for military navigation. It was later made available for civilian use and is now the most widely used global navigation system.',
        'choices': [
            ('NASA', False),
            ('The European Space Agency', False),
            ('The United States Department of Defense', True),
            ('Google', False),
            ('The United Nations', False),
        ]
    },

    # Q46 - GPS data points (multi-select 3)
    {
        'text': 'What location data does GPS provide? (Select THREE)',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': True,
        'explanation': 'GPS provides longitude latitude and altitude above sea level. These three data points give a complete 3D position. IP address and carrier name are network data not GPS data.',
        'choices': [
            ('Device IP address', False),
            ('Longitude', True),
            ('Altitude above sea level', True),
            ('Cellular carrier name', False),
            ('Latitude', True),
        ]
    },

    # Q47 - Alternative location methods (multi-select 2)
    {
        'text': 'If GPS signals are unavailable what other methods can determine a device\'s location? (Select TWO)',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': True,
        'explanation': 'Wi-Fi network triangulation and cellular tower triangulation are both used as fallback location methods when GPS is unavailable such as indoors or in areas with poor satellite visibility.',
        'choices': [
            ('Bluetooth scanning', False),
            ('Wi-Fi network triangulation', True),
            ('NFC tag reading', False),
            ('Cellular tower triangulation', True),
            ('HDMI signal detection', False),
        ]
    },

    # Q48 - MDM policy control (multi-select 3)
    {
        'text': 'Which of the following can a system administrator control through an MDM? (Select THREE)',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': True,
        'explanation': 'MDM allows administrators to disable the camera require screen locks with PIN and specify which applications are allowed or forbidden. Physical hardware and cellular towers cannot be controlled through MDM.',
        'choices': [
            ('Replace physical hardware', False),
            ('Disable the camera', True),
            ('Require screen locks with PIN', True),
            ('Upgrade cellular network towers', False),
            ('Specify which applications are allowed or forbidden', True),
        ]
    },

    # Q49 - BYOD data protection
    {
        'text': 'What challenge does BYOD create that MDM helps address?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'BYOD creates the challenge of protecting corporate data on a personally owned device while keeping personal data private. MDM containerization helps separate and protect corporate data.',
        'choices': [
            ('Employees bringing incompatible phone models', False),
            ('Phones connecting to the wrong cellular towers', False),
            ('Protecting corporate data on a personally owned device while keeping personal data private', True),
            ('Preventing employees from making personal calls', False),
            ('Ensuring phones support 5G', False),
        ]
    },

    # Q50 - BYOD vs COPE
    {
        'text': 'What is the key difference between BYOD and COPE?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'In BYOD the employee owns the device and the company manages corporate data on it. In COPE the company owns the device but allows personal use. Ownership is the key difference.',
        'choices': [
            ('BYOD uses MDM while COPE does not', False),
            ('COPE only allows Android devices while BYOD allows any device', False),
            ('In BYOD the employee owns the device while in COPE the company owns it', True),
            ('COPE does not allow personal use of the device', False),
            ('BYOD gives the company full control while COPE gives the employee full control', False),
        ]
    },

    # Q51 - CYOD definition
    {
        'text': 'What does CYOD (Choose Your Own Device) allow employees to do?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'CYOD allows employees to choose from a selection of company-approved devices. The company maintains control and support while giving employees some flexibility in device choice.',
        'choices': [
            ('Use any personal device without MDM restrictions', False),
            ('Choose from a selection of company-approved devices', True),
            ('Connect personal devices to the corporate network without enrollment', False),
            ('Customize MDM policies on their device', False),
            ('Opt out of corporate security requirements', False),
        ]
    },

    # Q52 - MDM email configuration
    {
        'text': 'How does MDM simplify corporate email setup for employees?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'MDM configures email settings centrally and pushes them to all enrolled devices automatically. This eliminates the need for individual manual setup and ensures consistent configuration.',
        'choices': [
            ('It installs a custom email app on every device manually', False),
            ('Employees configure email individually using a printed guide', False),
            ('Email settings are configured centrally in MDM and pushed to all devices automatically', True),
            ('It replaces email with internal messaging only', False),
            ('It requires each employee to visit IT for email setup', False),
        ]
    },

    # Q53 - MDM two-factor authentication
    {
        'text': 'What can the MDM security team enforce regarding authentication?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'MDM allows the security team to require two-factor authentication and specify the type of MFA to use across all managed devices ensuring consistent strong authentication.',
        'choices': [
            ('Require employees to memorize complex passwords', False),
            ('Disable biometric login on all devices', False),
            ('Require two-factor authentication and specify the type of MFA to use', True),
            ('Restrict devices to PIN-only authentication', False),
            ('Allow only fingerprint authentication', False),
        ]
    },

    # Q54 - MDM sync settings (multi-select 3)
    {
        'text': 'Which data types can be selectively configured for synchronization through MDM? (Select THREE)',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': True,
        'explanation': 'MDM can selectively sync calendar settings contact details and mail. Cellular tower firmware and SIM card data are network and hardware items that cannot be configured through MDM sync.',
        'choices': [
            ('Cellular tower firmware', False),
            ('Calendar settings', True),
            ('Contact details', True),
            ('SIM card data', False),
            ('Mail', True),
        ]
    },

    # Q55 - MDM Wi-Fi only sync
    {
        'text': 'Why might an organization configure MDM to sync only over Wi-Fi rather than cellular?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'Syncing over Wi-Fi only controls costs by avoiding cellular data charges. Corporate sync operations can transfer large amounts of data and cellular data plans may have usage limits or costs.',
        'choices': [
            ('Wi-Fi is always faster than cellular', False),
            ('Cellular networks do not support data sync', False),
            ('To control costs by avoiding cellular data charges', True),
            ('Because MDM does not support cellular syncing', False),
            ('To comply with 5G frequency regulations', False),
        ]
    },

    # Q56 - MDM IMEI purpose
    {
        'text': 'What is the IMEI visible in the MDM console used for?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'The IMEI (International Mobile Equipment Identity) uniquely identifies the mobile device hardware. It is used to track manage and identify specific devices in the MDM system.',
        'choices': [
            ('Identifying which Wi-Fi network the device is on', False),
            ('Tracking the device GPS location in real time', False),
            ('Uniquely identifying the mobile device', True),
            ('Storing the user SIM card number', False),
            ('Verifying the device OS version', False),
        ]
    },

    # Q57 - MDM restrictions tab (multi-select 3)
    {
        'text': 'Which of the following can be enabled or disabled from the MDM Restrictions tab? (Select THREE)',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': True,
        'explanation': 'The MDM Restrictions tab allows disabling Camera FaceTime and Siri. GPS satellite access and cellular tower selection are infrastructure elements that cannot be controlled from MDM restrictions.',
        'choices': [
            ('GPS satellite access', False),
            ('Camera', True),
            ('FaceTime', True),
            ('Cellular tower selection', False),
            ('Siri', True),
        ]
    },

    # Q58 - 2G capabilities (multi-select 2)
    {
        'text': 'What were 2G networks primarily capable of? (Select TWO)',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': True,
        'explanation': '2G networks supported phone calls and SMS text messaging. Video conferencing mobile TV and internet browsing required 3G and later technology.',
        'choices': [
            ('Video conferencing', False),
            ('Phone calls', True),
            ('Mobile television', False),
            ('SMS text messaging', True),
            ('Mobile internet browsing', False),
        ]
    },

    # Q59 - GSM carriers (multi-select 2)
    {
        'text': 'Which carriers historically used GSM technology? (Select TWO)',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': True,
        'explanation': 'AT&T and T-Mobile historically used GSM technology. Verizon and Sprint used CDMA technology. 4G LTE unified both into a single standard.',
        'choices': [
            ('Verizon', False),
            ('Sprint', False),
            ('AT&T', True),
            ('T-Mobile', True),
            ('Boost Mobile', False),
        ]
    },

    # Q60 - PRL CDMA
    {
        'text': 'What does the PRL (Preferred Roaming List) in a CDMA network determine?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'The PRL determines which radio bands and service provider IDs the phone will search for to connect to the correct tower. It controls roaming behaviour and tower selection priority.',
        'choices': [
            ('The maximum data speed allowed on the network', False),
            ('Which applications can be installed on the device', False),
            ('Which radio bands and service provider IDs the phone will search for to connect to the correct tower', True),
            ('The encryption method used for voice calls', False),
            ('The PIN required for SIM unlocking', False),
        ]
    },

    # Q61 - Connection methods (multi-select 3)
    {
        'text': 'Which of the following are valid connection methods for mobile devices? (Select THREE)',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': True,
        'explanation': 'USB NFC and Bluetooth are all valid mobile device connection methods. HDMI direct and coaxial cable are not standard mobile device connection types.',
        'choices': [
            ('HDMI direct', False),
            ('USB including USB-C microUSB and miniUSB', True),
            ('NFC', True),
            ('Coaxial cable', False),
            ('Bluetooth', True),
        ]
    },

    # Q63 - Docking station vs port replicator
    {
        'text': 'What makes a docking station different from a port replicator?',
        'domain': 'Laptops', 'exam': 'core1', 'multi_select': False,
        'explanation': 'A docking station can include drive bays expansion slots optical drives and additional ports beyond what the laptop offers. A port replicator simply replicates existing ports via USB.',
        'choices': [
            ('A docking station only works with Apple devices', False),
            ('A port replicator offers more ports than a docking station', False),
            ('A docking station can include drive bays expansion slots optical drives and additional ports beyond what the laptop offers', True),
            ('A docking station connects wirelessly while a port replicator uses cables', False),
            ('There is no difference between the two', False),
        ]
    },

    # Q64 - Wi-Fi antenna symptoms (multi-select 2)
    {
        'text': 'Which symptoms suggest a problem with a laptop\'s Wi-Fi antenna? (Select TWO)',
        'domain': 'Laptops', 'exam': 'core1', 'multi_select': True,
        'explanation': 'A damaged or disconnected Wi-Fi antenna causes weak Wi-Fi signal and frequent connection drops. Battery and display issues are unrelated to the antenna.',
        'choices': [
            ('Overheating battery', False),
            ('Weak Wi-Fi signal', True),
            ('Cracked display', False),
            ('Dropping Wi-Fi connection frequently', True),
            ('NFC payment failures', False),
        ]
    },

    # Q65 - Camera troubleshooting before replacement
    {
        'text': 'What should you do before replacing a mobile device camera module?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'Before replacing hardware always test the camera in multiple apps to rule out a software issue. If it works in one app but not another the problem is likely software not hardware.',
        'choices': [
            ('Immediately order a replacement part', False),
            ('Perform a factory reset', False),
            ('Test the camera in multiple apps first to rule out a software issue', True),
            ('Replace the flex cable assembly first', False),
            ('Update the cellular firmware', False),
        ]
    },

    # Q66 - Microphone symptoms (multi-select 2)
    {
        'text': 'Which symptoms indicate a potential microphone issue on a mobile device? (Select TWO)',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': True,
        'explanation': 'Muffled audio and no audio input detected are direct microphone symptoms. Screen flickering GPS inaccuracy and battery drain are unrelated to microphone function.',
        'choices': [
            ('Screen flickering', False),
            ('Muffled audio during calls', True),
            ('GPS inaccuracy', False),
            ('No audio input detected', True),
            ('Rapid battery drain', False),
        ]
    },

    # Q67 - Biometrics after replacement
    {
        'text': 'What must be done after replacing a biometric sensor module on a mobile device?',
        'domain': 'Mobile Devices', 'exam': 'core1', 'multi_select': False,
        'explanation': 'After replacing a biometric sensor such as a fingerprint reader or face scanner biometrics must be reconfigured because the new sensor needs to learn the user\'s biometric data again.',
        'choices': [
            ('Flash new firmware to the motherboard', False),
            ('Replace the SIM card', False),
            ('Reconfigure biometrics after replacement', True),
            ('Re-enroll in the MDM', False),
            ('Reinstall the operating system', False),
        ]
    },

    # Q68 - Wireless card antenna leads
    {
        'text': 'What must you be careful about when replacing a wireless card in a laptop?',
        'domain': 'Laptops', 'exam': 'core1', 'multi_select': False,
        'explanation': 'Wireless cards have fragile snap-on antenna leads that connect the card to the antenna wires routed around the display. These must be gently disconnected and reconnected to avoid damage.',
        'choices': [
            ('Removing the SIM card first', False),
            ('Disconnecting the battery last', False),
            ('Gently disconnecting the fragile snap-on antenna leads', True),
            ('Disabling Bluetooth before removal', False),
            ('Formatting the SSD before replacement', False),
        ]
    },

    # Q69 - RAM compatibility (multi-select 3)
    {
        'text': 'When replacing RAM in an upgradable mobile device what must you verify? (Select THREE)',
        'domain': 'Laptops', 'exam': 'core1', 'multi_select': True,
        'explanation': 'When replacing RAM you must verify the RAM type (DDR4 DDR5 etc) the RAM speed (MHz) and the form factor (SO-DIMM for laptops). Screen resolution and GPS module version are irrelevant to RAM.',
        'choices': [
            ('Screen resolution compatibility', False),
            ('RAM type', True),
            ('RAM speed', True),
            ('GPS module version', False),
            ('Form factor', True),
        ]
    },

    # Q70 - SSD form factors (multi-select 3)
    {
        'text': 'Which SSD form factors may be used in mobile workstations? (Select THREE)',
        'domain': 'Storage', 'exam': 'core1', 'multi_select': True,
        'explanation': 'Mobile workstations and laptops use M.2 SATA M.2 NVMe and 2.5-inch drives. The 3.5-inch desktop drive and 5.25-inch optical bay are full desktop form factors not used in laptops.',
        'choices': [
            ('3.5 inch desktop drive', False),
            ('M.2 SATA', True),
            ('M.2 NVMe', True),
            ('5.25 inch optical bay', False),
            ('2.5 inch drive', True),
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