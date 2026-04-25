
import subprocess
from getmac import get_mac_address

# Example mapping of some OUIs
mac_type_mapping = {
    '00:1A:2B': 'Wireless',
    '00:1A:2C': 'Ethernet',
    '00:1D:A1': 'Wireless',
    '00:1E:4F': 'Ethernet'
}

def get_network_card_type(mac_address):
    # Extract OUI (first three bytes)
    oui = ':'.join(mac_address.split(':')[:3]).upper()

    # Check if OUI is in the mapping
    if oui in mac_type_mapping:
        return mac_type_mapping[oui]
    else:
        return 'Unknown'

# Function to use nmap to get additional info
def scan_network_with_nmap(ip):
    try:
        output = subprocess.check_output(["nmap", "-sP", ip]).decode()
        return output
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

# Example MAC address
mac_address = "00:1A:2B:3C:4D:5E"
card_type = get_network_card_type(mac_address)
print(f"The network card type for MAC {mac_address} is: {card_type}")

# Perform nmap scan (modify IP address as needed)
# nmap_info = scan_network_with_nmap("192.168.1.0/24")
# print(nmap_info)
