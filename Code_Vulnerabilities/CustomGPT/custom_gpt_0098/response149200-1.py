
import subprocess
import re

def get_mac_info(mac_address):
    # Extract the OUI from the MAC address
    oui = mac_address[:8].upper()
    return oui

def check_interface_type(mac_address):
    # Use nmap to report network interface types
    try:
        nmap_command = f"nmap -p 80 --script=mac-addr {mac_address}"
        result = subprocess.run(nmap_command, shell=True, text=True, capture_output=True)

        if "wireless" in result.stdout.lower():
            return "Wireless Interface"
        elif "ethernet" in result.stdout.lower():
            return "Ethernet Interface"
        else:
            return "Interface type unknown"
    except Exception as e:
        return f"Error: {e}"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
oui = get_mac_info(mac_address)
interface_type = check_interface_type(mac_address)

print(f"OUI: {oui}")
print(f"Interface Type: {interface_type}")
