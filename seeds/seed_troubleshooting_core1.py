from app import app, db
from models import Question, Choice

questions_data = [

    # ── HARDWARE TROUBLESHOOTING SCENARIOS ───────────────────────────────────

    {
        'text': 'A technician turns on a desktop computer and hears a single long beep followed by two short beeps during POST. What does this most likely indicate?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The CPU has failed and needs to be replaced', False),
            ('A video card or display error has been detected during POST', True),
            ('The hard drive is not detected by the BIOS', False),
            ('The system is booting normally', False),
        ]
    },
    {
        'text': 'A desktop computer powers on, the fans spin, but there is no POST beep and no display output. What is the most likely cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The operating system is corrupted', False),
            ('A critical component such as RAM or CPU is faulty or not seated correctly', True),
            ('The monitor cable is the wrong type', False),
            ('The hard drive has failed', False),
        ]
    },
    {
        'text': 'After installing a second RAM stick, a computer no longer boots. What should you check first?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Update the BIOS to support more RAM', False),
            ('Ensure the new RAM is fully seated and is compatible with the motherboard and existing RAM', True),
            ('Reinstall the operating system', False),
            ('Replace the power supply as it cannot support more RAM', False),
        ]
    },
    {
        'text': 'A user reports their computer is running very slowly and the hard drive activity light is constantly on. What is the most likely cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The CPU is overclocked too high', False),
            ('The system is using excessive virtual memory due to insufficient RAM, causing constant disk paging', True),
            ('The monitor refresh rate is set too high', False),
            ('The network adapter is consuming too many resources', False),
        ]
    },
    {
        'text': 'A technician notices a capacitor on a motherboard is bulging at the top. What does this indicate?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The capacitor is fully charged and working correctly', False),
            ('The capacitor has failed and the motherboard may need to be replaced', True),
            ('The motherboard needs a BIOS update', False),
            ('The system needs more cooling', False),
        ]
    },
    {
        'text': 'A computer randomly freezes and requires a hard reset. After checking temperatures they are normal. What should you test next?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Replace the CPU immediately', False),
            ('Test the RAM using MemTest86 as faulty RAM is a common cause of random freezes', True),
            ('Reinstall the operating system', False),
            ('Replace the monitor', False),
        ]
    },
    {
        'text': 'A user reports that their computer screen shows artifacts — random colored pixels and distorted graphics. What is the most likely cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The hard drive is failing', False),
            ('The GPU is overheating or failing', True),
            ('The RAM needs to be upgraded', False),
            ('The monitor resolution is set incorrectly', False),
        ]
    },
    {
        'text': 'After a power outage, a computer will not turn on at all. What should you check first?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Replace the motherboard', False),
            ('Check the power supply — it may have been damaged by the power outage, and check that the surge protector or outlet is working', True),
            ('Reinstall the operating system', False),
            ('Replace the RAM', False),
        ]
    },
    {
        'text': 'A technician is troubleshooting a computer that shows no video output. They connect the monitor to the motherboard\'s integrated video port and it works. What does this tell them?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The motherboard needs to be replaced', False),
            ('The dedicated GPU is likely faulty or not receiving power', True),
            ('The monitor is incompatible with the system', False),
            ('The CPU needs to be reseated', False),
        ]
    },
    {
        'text': 'A user reports that USB devices stop working after a few minutes of use. What should the technician check?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Replace the USB devices', False),
            ('Check the USB power management settings — Windows may be turning off USB ports to save power', True),
            ('Reinstall the operating system', False),
            ('Replace the keyboard and mouse', False),
        ]
    },
    {
        'text': 'A computer is displaying a "CPU fan error" message during POST. What should the technician do?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Ignore the message and boot into the OS', False),
            ('Check that the CPU fan is properly connected to the motherboard fan header and is spinning', True),
            ('Replace the CPU immediately', False),
            ('Update the BIOS firmware', False),
        ]
    },
    {
        'text': 'A technician replaces a failed PSU. After installing the new PSU the computer still does not power on. What should be checked next?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Return the new PSU as it is also faulty', False),
            ('Verify the power connections from the PSU to the motherboard are fully seated, including both the 24-pin and CPU power connectors', True),
            ('Replace the motherboard', False),
            ('Reinstall the operating system', False),
        ]
    },
    {
        'text': 'A user complains that their computer is making a loud grinding noise. What is the most likely source?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The RAM is loose and vibrating', False),
            ('A cooling fan or HDD with failing bearings', True),
            ('The GPU is drawing too much power', False),
            ('The CPU is overclocked', False),
        ]
    },
    {
        'text': 'After upgrading a CPU, a computer POSTs successfully but runs slower than expected. What is the most likely cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The CPU is incompatible with the operating system', False),
            ('The BIOS may need to be updated to properly support the new CPU, or XMP/DOCP memory profiles need to be enabled', True),
            ('The hard drive is too slow for the new CPU', False),
            ('The monitor cannot display the higher performance', False),
        ]
    },
    {
        'text': 'A technician is troubleshooting a system that keeps losing the date and time after being powered off. What component is most likely failing?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The operating system clock service has stopped', False),
            ('The CMOS battery on the motherboard is dead and needs to be replaced', True),
            ('The power supply is not providing standby power', False),
            ('The hard drive is losing data when powered off', False),
        ]
    },
    {
        'text': 'A desktop computer works fine until a new PCIe expansion card is installed, after which it fails to boot. What is the most likely cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The expansion card is not compatible with any system', False),
            ('The new card is drawing more power than the PSU can supply, or the card is not fully seated in the slot', True),
            ('The operating system needs to be reinstalled to support new hardware', False),
            ('The BIOS settings are preventing the card from working', False),
        ]
    },
    {
        'text': 'A user reports that their computer produces a burning smell. What should the technician do immediately?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Open the case and identify the burning component while the system is running', False),
            ('Power off and unplug the computer immediately, then inspect for burnt components before attempting to power on again', True),
            ('Run a diagnostic tool to identify the overheating component', False),
            ('Increase fan speeds to cool down the burning component', False),
        ]
    },
    {
        'text': 'A laptop screen is very dim even when brightness is set to maximum. What is the most likely hardware cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The GPU has failed', False),
            ('The LCD backlight or inverter is failing', True),
            ('The RAM is insufficient for the display', False),
            ('The screen resolution is set too high', False),
        ]
    },
    {
        'text': 'A technician notices that a computer restarts every time a specific program is launched. What is the most likely cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The monitor is incompatible with the program', False),
            ('The program is causing a critical system error — possibly due to a driver conflict, corrupted program files, or hardware stress like GPU overload', True),
            ('The keyboard shortcut for restart is being triggered', False),
            ('The network connection drops when the program starts', False),
        ]
    },
    {
        'text': 'A user reports their laptop runs hot and shuts down during video playback but not during normal use. What is the most likely cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The video player software is corrupted', False),
            ('The GPU or CPU thermal paste has degraded and the cooling system cannot handle the increased load from video decoding', True),
            ('The laptop battery is failing', False),
            ('The screen brightness is too high during video playback', False),
        ]
    },

    # ── STORAGE TROUBLESHOOTING SCENARIOS ─────────────────────────────────────

    {
        'text': 'A user reports that their computer is very slow and they hear frequent clicking sounds from the PC. What should the technician do first?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Defragment the hard drive', False),
            ('Back up the data immediately and run a disk diagnostic as the HDD is showing signs of imminent failure', True),
            ('Add more RAM to reduce hard drive activity', False),
            ('Reinstall the operating system', False),
        ]
    },
    {
        'text': 'After cloning an HDD to a new SSD and installing it, the computer boots to a BIOS screen instead of Windows. What is the most likely cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The SSD is too fast for the motherboard', False),
            ('The boot order in BIOS needs to be changed to set the new SSD as the primary boot device', True),
            ('The clone process failed and Windows needs to be reinstalled', False),
            ('The SATA cable is not compatible with SSDs', False),
        ]
    },
    {
        'text': 'A technician runs chkdsk on a drive and it reports bad sectors. What should they do?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Defragment the drive to repair the bad sectors', False),
            ('Back up all data immediately and plan to replace the drive as bad sectors indicate physical drive failure', True),
            ('Format the drive to clear the bad sectors', False),
            ('Run a virus scan as viruses cause bad sectors', False),
        ]
    },
    {
        'text': 'A newly installed NVMe SSD is not showing up in Windows or BIOS. What should the technician check?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The SSD needs to be formatted before it appears in BIOS', False),
            ('Verify the SSD is fully seated in the M.2 slot, the slot supports NVMe, and check BIOS settings for M.2 configuration', True),
            ('The operating system does not support NVMe drives', False),
            ('The SSD needs a driver installed before it is detected', False),
        ]
    },
    {
        'text': 'A user deleted important files and emptied the Recycle Bin. What is the best course of action?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The files are permanently gone and cannot be recovered', False),
            ('Stop using the drive immediately and use data recovery software as the files may still be recoverable until the space is overwritten', True),
            ('Defragment the drive to recover the deleted files', False),
            ('Run chkdsk to restore the deleted files', False),
        ]
    },
    {
        'text': 'A RAID 1 array shows that one drive has failed. The system is still running normally. What should the technician do?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Shut down the system immediately as data loss is imminent', False),
            ('Replace the failed drive as soon as possible — the system is running on one drive with no redundancy and data is at risk', True),
            ('Ignore the warning as RAID 1 means the data is already backed up', False),
            ('Rebuild the RAID array from scratch', False),
        ]
    },

    # ── PRINTER TROUBLESHOOTING SCENARIOS ─────────────────────────────────────

    {
        'text': 'A laser printer is printing pages that are completely blank. What is the most likely cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The fuser assembly has failed', False),
            ('The toner cartridge is empty or the protective seal has not been removed from a new cartridge', True),
            ('The printer driver is outdated', False),
            ('The paper type is incompatible', False),
        ]
    },
    {
        'text': 'A printer is producing output with smeared toner that smudges when touched. What component is most likely failing?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The toner cartridge is overfilled', False),
            ('The fuser assembly is not heating properly and failing to bond the toner to the paper', True),
            ('The drum unit is worn out', False),
            ('The paper is damp', False),
        ]
    },
    {
        'text': 'Users report that print jobs are sent to a printer but nothing prints and the jobs disappear from the queue. What should the technician check?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Replace the printer immediately', False),
            ('Check the printer status — it may be set to offline, or the print spooler service may need to be restarted', True),
            ('Reinstall Windows on all affected computers', False),
            ('Check if the toner is low', False),
        ]
    },
    {
        'text': 'A thermal receipt printer is printing blank receipts. What is the most likely cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The printer driver needs to be updated', False),
            ('The thermal paper is loaded backwards — the thermal-coated side must face the print head', True),
            ('The print head temperature is too low', False),
            ('The printer needs to be recalibrated', False),
        ]
    },
    {
        'text': 'A laser printer consistently prints with a light vertical white streak down the same area of every page. What is the most likely cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The paper tray is not properly aligned', False),
            ('There is a scratch or worn spot on the drum, or a blockage preventing toner from reaching that area of the drum', True),
            ('The fuser temperature is too high', False),
            ('The printer resolution is set too low', False),
        ]
    },
    {
        'text': 'A network printer was working fine but after a power outage it is no longer accessible. Other network devices work normally. What should the technician check?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Replace the printer network card', False),
            ('Check if the printer received a different IP address from DHCP after the reboot and update the printer port settings on computers if needed', True),
            ('Reinstall printer drivers on all computers', False),
            ('Replace the network switch', False),
        ]
    },
    {
        'text': 'An inkjet printer is producing output where colors are incorrect — reds appear orange and blues appear green. What is the most likely cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The printer driver has the wrong color profile', False),
            ('One or more ink cartridges are empty or clogged, causing incorrect color mixing', True),
            ('The monitor color calibration is affecting the print output', False),
            ('The paper type setting is incorrect', False),
        ]
    },
    {
        'text': 'After replacing a toner cartridge in a laser printer, the printer shows a "cartridge not recognized" error. What should the technician try first?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Replace the new cartridge again with another one', False),
            ('Remove and reinstall the cartridge ensuring it is fully seated, and check if the cartridge is compatible with the printer model', True),
            ('Perform a factory reset of the printer', False),
            ('Update the printer firmware', False),
        ]
    },

    # ── NETWORK TROUBLESHOOTING SCENARIOS ─────────────────────────────────────

    {
        'text': 'A user can access local network resources but cannot access the internet. What is the most likely cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The network cable is faulty', False),
            ('The default gateway is incorrectly configured or the router has lost internet connectivity', True),
            ('The DNS server is configured incorrectly on the local network', False),
            ('The user\'s firewall is blocking all traffic', False),
        ]
    },
    {
        'text': 'A user receives an IP address of 169.254.x.x. What does this mean and what should you check?',
        'domain': 'Troubleshooting',
        'choices': [
            ('This is a valid static IP address assigned by the administrator', False),
            ('The computer could not reach the DHCP server and assigned itself an APIPA address — check the DHCP server and network connection', True),
            ('The computer is connected to a IPv6 network', False),
            ('The IP address is being blocked by the firewall', False),
        ]
    },
    {
        'text': 'Two computers on the same network cannot communicate with each other even though both can reach the internet. What is the most likely cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The internet router is blocking local traffic', False),
            ('The computers are on different VLANs or subnets, or a firewall is blocking local traffic between them', True),
            ('The computers need to be restarted simultaneously', False),
            ('The DNS server is down', False),
        ]
    },
    {
        'text': 'A wireless user reports slow internet speeds, but wired users are unaffected. What should the technician check?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Replace the router immediately', False),
            ('Check for Wi-Fi interference, the distance from the access point, the wireless channel being used, and the Wi-Fi standard supported by the device', True),
            ('Upgrade the internet plan', False),
            ('Replace the user\'s network adapter', False),
        ]
    },
    {
        'text': 'A technician runs a ping test and gets "Request timed out" responses. What could cause this?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The DNS server is not responding', False),
            ('The destination host is unreachable, powered off, blocking ICMP, or there is a routing problem between the two hosts', True),
            ('The network cable is the wrong category', False),
            ('The computer\'s IP address is incorrect', False),
        ]
    },
    {
        'text': 'After moving offices, a computer that was working fine now cannot connect to the network. What should the technician check first?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Reinstall the network adapter driver', False),
            ('Check the physical network cable connection and verify the wall port is active and patched correctly at the network switch', True),
            ('Replace the computer', False),
            ('Update the operating system', False),
        ]
    },
    {
        'text': 'A user reports intermittent network drops throughout the day. The problem affects only their computer. What should the technician check?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Replace the network switch', False),
            ('Check the network cable for damage, try a different cable, and check the NIC driver and power management settings that may be turning off the adapter', True),
            ('Increase the user\'s internet bandwidth', False),
            ('Restart the DHCP server', False),
        ]
    },
    {
        'text': 'A technician needs to find which switch port a specific computer is connected to. What tool should they use?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Cable tester', False),
            ('Toner probe — to trace the cable from the computer back to the switch', True),
            ('Loopback plug', False),
            ('Multimeter', False),
        ]
    },
    {
        'text': 'All computers in an office suddenly lose internet access but can still access local network resources. What is the most likely cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('All computers have been infected with malware simultaneously', False),
            ('The router or modem has lost its internet connection, or the ISP is experiencing an outage', True),
            ('The DNS server on each computer needs to be updated', False),
            ('A switch has failed', False),
        ]
    },
    {
        'text': 'A user connects a laptop to a wired network but gets no connectivity. The link light on the network port is not lit. What should the technician check?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Update the network adapter driver', False),
            ('Check that the network cable is properly connected at both ends, try a different cable, and verify the switch port is active', True),
            ('Disable and re-enable the network adapter', False),
            ('Assign a static IP address to the laptop', False),
        ]
    },
    {
        'text': 'A user reports their VoIP calls have poor quality with choppy audio. The internet speed tests are normal. What is most likely causing this?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The VoIP application needs to be reinstalled', False),
            ('High network latency or packet loss is affecting the real-time audio stream — QoS settings on the router may need to be configured', True),
            ('The internet plan does not support VoIP', False),
            ('The microphone driver needs to be updated', False),
        ]
    },
    {
        'text': 'A technician uses ping 127.0.0.1 and gets a successful reply, but cannot ping the default gateway. What does the successful loopback ping confirm?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The internet connection is working correctly', False),
            ('The local TCP/IP stack on the computer is functioning correctly, so the problem is with the physical network connection or configuration', True),
            ('The DNS server is working correctly', False),
            ('The default gateway IP address is correct', False),
        ]
    },
    {
        'text': 'After installing a new network switch, some computers can communicate but others cannot. What is the most likely cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The switch is defective and needs to be returned', False),
            ('Some ports on the switch may be configured for a different VLAN, or the switch needs to be configured to match the network settings', True),
            ('The computers that cannot communicate need new network cables', False),
            ('The DHCP server is assigning duplicate IP addresses', False),
        ]
    },

    # ── MOBILE DEVICE TROUBLESHOOTING SCENARIOS ───────────────────────────────

    {
        'text': 'A smartphone charges very slowly even with the original charger. What should the technician check?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Replace the battery immediately', False),
            ('Check the charging port for debris or damage, try a different cable, and check if a background process is consuming power while charging', True),
            ('Perform a factory reset', False),
            ('Replace the charger adapter', False),
        ]
    },
    {
        'text': 'A tablet touchscreen is responding to touches in the wrong location — tapping one area activates a different area. What should the technician do?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Replace the digitizer immediately', False),
            ('Recalibrate the touchscreen through the device settings', True),
            ('Perform a factory reset of the device', False),
            ('Update the operating system', False),
        ]
    },
    {
        'text': 'A laptop screen works fine when the lid is in one position but goes black when moved to a different angle. What is the most likely cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The screen brightness setting is linked to the lid angle', False),
            ('The video cable running through the hinge is damaged or loose and loses connection when the screen is moved', True),
            ('The GPU is overheating when the screen is at certain angles', False),
            ('The screen auto-brightness feature is malfunctioning', False),
        ]
    },
    {
        'text': 'A user reports that their laptop battery percentage jumps erratically — for example going from 60% to 20% without warning. What is the cause?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The power management software needs to be reinstalled', False),
            ('The battery is degraded and its cells are failing unevenly, causing inaccurate capacity readings', True),
            ('The laptop charger is providing inconsistent voltage', False),
            ('The operating system has a bug affecting battery readings', False),
        ]
    },
    {
        'text': 'A user dropped their laptop and now the display has a large dark blotch spreading from one corner. What has happened?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The GPU has failed due to the impact', False),
            ('The LCD panel is cracked internally and the liquid crystals are leaking — the screen needs to be replaced', True),
            ('The display cable has become loose from the impact', False),
            ('The backlight has failed on one side of the screen', False),
        ]
    },

    # ── ADDITIONAL CORE 1 HARDWARE SCENARIOS ──────────────────────────────────

    {
        'text': 'A technician installs a new GPU and connects the monitor to it, but the display still outputs from the motherboard\'s integrated graphics. What should they do?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Replace the GPU as it is not working', False),
            ('Enter BIOS settings and disable the integrated graphics or set the primary display adapter to the PCIe slot', True),
            ('Reinstall the operating system', False),
            ('Connect both the monitor and a second monitor to force GPU activation', False),
        ]
    },
    {
        'text': 'A computer that was working fine suddenly will not turn on. You press the power button and nothing happens — no fans, no lights. What should you check first?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Replace the motherboard immediately', False),
            ('Check the power source — verify the outlet is working, the power cable is connected, and the PSU switch on the back is set to on', True),
            ('Replace the power button', False),
            ('Reseat the RAM and GPU', False),
        ]
    },
    {
        'text': 'A user reports that their computer is running slowly and Task Manager shows CPU usage at 100% even when no applications are open. What should the technician investigate?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The CPU needs to be replaced with a faster model', False),
            ('Check for malware, a runaway background process, or Windows Update running in the background consuming resources', True),
            ('Add more RAM to reduce CPU load', False),
            ('The hard drive needs to be defragmented', False),
        ]
    },
    {
        'text': 'After adding a new hard drive to a desktop, the BIOS detects it but Windows does not show it. What should the technician do?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Reinstall Windows to detect the new drive', False),
            ('Open Disk Management and initialize, partition, and format the new drive so Windows can use it', True),
            ('Update the SATA driver', False),
            ('Move the drive to a different SATA port', False),
        ]
    },
    {
        'text': 'A technician is setting up a workstation and notices the system date resets to January 1, 2000 every time it is powered off. What component needs to be replaced?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The hard drive', False),
            ('The CMOS battery — it is responsible for maintaining BIOS settings including the system date and time when the computer is powered off', True),
            ('The power supply unit', False),
            ('The RAM', False),
        ]
    },
    {
        'text': 'A user reports that their second monitor is not being detected after connecting it via HDMI. The primary monitor works fine. What should the technician check?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Replace the second monitor', False),
            ('Check the HDMI cable connection, try a different port on the GPU, and use Windows display settings (Win+P) to detect and configure the second display', True),
            ('Reinstall the graphics driver', False),
            ('The GPU only supports one monitor', False),
        ]
    },
    {
        'text': 'A computer powers on normally but makes a continuous beeping sound with no display. What is this most likely indicating?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The hard drive is not detected', False),
            ('A RAM failure — RAM is not detected or has failed the POST memory test', True),
            ('The operating system files are corrupted', False),
            ('The GPU driver needs to be updated', False),
        ]
    },
    {
        'text': 'A technician replaces a failing laptop keyboard. After reassembly, some keys type the wrong characters. What most likely went wrong?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The replacement keyboard is defective', False),
            ('The keyboard ribbon cable may not be fully seated, or the replacement keyboard layout does not match the region settings', True),
            ('The operating system needs to be reinstalled', False),
            ('The laptop BIOS needs to be updated', False),
        ]
    },
    {
        'text': 'A laser printer is producing output where every page has a repeating mark at regular intervals down the page. What component is most likely causing this?',
        'domain': 'Troubleshooting',
        'choices': [
            ('The fuser is applying uneven heat', False),
            ('The drum unit has a scratch or foreign material on it that leaves a mark every time it completes one rotation', True),
            ('The paper tray is misaligned', False),
            ('The toner cartridge is nearly empty', False),
        ]
    },
    {
        'text': 'A user reports that when printing documents the text appears jagged and low quality despite the printer being set to high quality. What should the technician check?',
        'domain': 'Troubleshooting',
        'choices': [
            ('Replace the printer as it cannot print high quality', False),
            ('Check the printer driver settings — the print quality may be overridden in the application or driver, and verify the correct printer driver is installed', True),
            ('Replace the toner cartridge', False),
            ('The paper quality is too low for high resolution printing', False),
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