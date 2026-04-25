
import requests

# Sample OUI list (you may need a full list)
oui_list = {
    '00:1A:2B': 'Ethernet',
    '00:1C:DF': 'Wireless',
    '00:1A:11': 'Wireless',
    '00:1E:52': 'Wireless',
    # Add more OUIs as needed
}

def get_device_type(mac_address):
    # Normalize MAC address format
    mac_parts = mac_address.upper().split(':')[:3]
    oui = ':'.join(mac_parts)

    return oui_list.get(oui, 'Unknown')

# Example usage
mac_address = '00:1A:2B:3C:4D:5E'
device_type = get_device_type(mac_address)
print(f"The device type for MAC {mac_address} is: {device_type}")
