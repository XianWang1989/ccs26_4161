
from getmac import get_mac_address

def get_device_type(mac_address):
    # Get the MAC OUI
    oui = mac_address[:8].replace(':', '').upper()

    # A sample mapping of OUIs to device types
    oui_mapping = {
        '00:1A:2B': 'Ethernet',
        '00:1A:3C': 'Wireless',
        '00:1B:4D': 'Wireless',
        # Add more OUIs here
    }

    # Check if the OUI exists in our mapping
    device_type = oui_mapping.get(oui, 'Unknown')

    return device_type

# Example MAC address
mac_address = "00:1A:2B:3C:4D:5E"
device_type = get_device_type(mac_address)
print(f'Device type for {mac_address}: {device_type}')
