
import requests

# Mapping of known OUIs for wireless and Ethernet cards
# This is a partial list; for complete mapping, consider using a comprehensive database.
known_ouis = {
    'Wireless': ['00:1A:2B', '00:1E:C2', '00:1A:11'],  # Add more known OUI prefixes for wireless
    'Ethernet': ['00:04:20', '00:14:22', '00:1A:8C'],  # Add more known OUI prefixes for Ethernet
}

def get_device_type(mac_address):
    # Normalize the MAC address (remove colons or dashes)
    mac_address = mac_address.upper().replace(':', '').replace('-', '')
    oui = mac_address[:6]  # Get the first 6 characters (OUI)

    # Check against known OUIs
    for device_type, ouis in known_ouis.items():
        if oui in ouis:
            return device_type

    return 'Unknown'

# Example MAC addresses
mac_addresses = [
    '00:1A:2B:3C:4D:5E',
    '00:14:22:01:23:45',
    '00:04:20:AB:CD:EF',
]

for mac in mac_addresses:
    device_type = get_device_type(mac)
    print(f"MAC Address: {mac} is a {device_type} device.")
