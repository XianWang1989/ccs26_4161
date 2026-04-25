
import requests
from getmac import get_mac_address

# List of common wireless manufacturers
wireless_manufacturers = {
    '00:1A:11',  # Example prefixes
    '00:1B:44',
    '00:1C:BF',
}

def get_interface_type(mac_address):
    # Get the first three octets of the MAC address
    prefix = ':'.join(mac_address.split(':')[:3]).upper()

    if prefix in wireless_manufacturers:
        return "Wireless Card"
    else:
        return "Ethernet Card"

# Example MAC address
mac_address = get_mac_address()  # Replace with actual MAC address if necessary

interface_type = get_interface_type(mac_address)
print(f"The interface type for MAC {mac_address} is: {interface_type}")
