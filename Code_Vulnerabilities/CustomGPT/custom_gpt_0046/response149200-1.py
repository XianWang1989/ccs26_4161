
from get_mac_ooui import OUI
import requests

# Function to determine the interface type based on MAC address
def get_interface_type(mac_address):
    # Normalize the MAC address
    mac_address = mac_address.lower().replace(':', '')

    # Get the OUI information
    oui_info = OUI.lookup(mac_address[:6])  # First 6 characters are the OUI
    iface_type = "unknown"

    # Check known manufacturers (typically, you may need a more comprehensive list)
    wireless_vendors = ['00:1A:11', '00:1B:77', 'F8:3D:8C']  # Add more known wireless OUIS
    ethernet_vendors = ['00:1C:C0', '00:24:D7', 'A0:36:9F']  # Add more known ethernet OUIS

    if oui_info:
        vendor = oui_info['name']
        print(f"Vendor: {vendor}")

        # Determine interface type based on vendor
        if any(mac_address.startswith(vendor[:6].lower()) for vendor in wireless_vendors):
            iface_type = "Wireless"
        elif any(mac_address.startswith(vendor[:6].lower()) for vendor in ethernet_vendors):
            iface_type = "Ethernet"

    return iface_type

# Example usage
mac_address = "00:1A:11:FF:EE:DD"
interface_type = get_interface_type(mac_address)
print(f"The interface type for {mac_address} is: {interface_type}")
