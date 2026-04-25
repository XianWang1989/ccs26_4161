
from getmac import get_mac_address

def get_device_type(mac_address):
    # OUI prefixes for common manufacturers
    wireless_ouis = ['00:1A:2B', '00:1E:10', '00:14:22']  # Add more as needed
    ethernet_ouis = ['00:12:34', '00:1B:44', '00:1D:A8']  # Add more as needed

    # Check if the MAC address belongs to a known wireless OUI
    for oui in wireless_ouis:
        if mac_address.startswith(oui):
            return "Wireless Card"

    # Check if the MAC address belongs to a known Ethernet OUI
    for oui in ethernet_ouis:
        if mac_address.startswith(oui):
            return "Ethernet Card"

    return "Unknown Card Type"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"  # Replace with your MAC address
device_type = get_device_type(mac_address)
print(f"The device type for MAC {mac_address} is: {device_type}")
