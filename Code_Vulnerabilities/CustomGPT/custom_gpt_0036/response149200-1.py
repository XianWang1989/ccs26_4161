
import subprocess
import re

def get_interface_type(mac_address):
    try:
        # Run nmap command to scan the local network for the MAC address
        result = subprocess.run(['nmap', '-sn', '192.168.1.0/24'], capture_output=True, text=True)

        # Look for the MAC address in nmap output
        if mac_address.lower() in result.stdout.lower():
            # Find the line with the MAC address
            for line in result.stdout.splitlines():
                if mac_address.lower() in line.lower():
                    if "wlan" in line.lower():
                        return "Wireless"
                    elif "eth" in line.lower():
                        return "Ethernet"

        return "Unknown interface type"

    except Exception as e:
        return str(e)

# Replace with the MAC address you want to check
mac_address = "00:1A:2B:3C:4D:5E"
interface_type = get_interface_type(mac_address)

print(f"The interface type for MAC address {mac_address} is: {interface_type}")
