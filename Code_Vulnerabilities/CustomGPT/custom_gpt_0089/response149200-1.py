
from getmac import get_mac_address
import subprocess

def get_interface_type(mac_address):
    # Use the nmap command to check the interface type
    result = subprocess.run(['nmap', '-sn', '192.168.1.0/24'], capture_output=True, text=True)

    if mac_address in result.stdout:
        if "wlan" in result.stdout:
            return "Wireless"
        elif "eth" in result.stdout:
            return "Ethernet"

    return "Unknown"

# Example MAC address
mac_address = "00:1A:2B:3C:4D:5E"
interface_type = get_interface_type(mac_address)
print(f"The interface type for MAC {mac_address} is: {interface_type}")
