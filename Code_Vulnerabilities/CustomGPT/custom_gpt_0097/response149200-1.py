
from get_oui import OUI

def determine_interface_type(mac_address):
    oui = OUI()
    manufacturer_info = oui.lookup(mac_address)

    if manufacturer_info:
        if 'wireless' in manufacturer_info.lower() or 'wifi' in manufacturer_info.lower():
            return "Wireless Card"
        elif 'ethernet' in manufacturer_info.lower():
            return "Ethernet Card"
        else:
            return "Unknown Card Type"
    else:
        return "Invalid MAC Address"

# Example usage
mac = "00:1A:2B:3C:4D:5E"
card_type = determine_interface_type(mac)
print(f"The MAC address {mac} is associated with: {card_type}")
