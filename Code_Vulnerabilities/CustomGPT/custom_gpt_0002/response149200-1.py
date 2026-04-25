
import getmac
import re

def identify_interface_type(mac_address):
    # Dictionary for known manufacturers
    known_makers = {
        'Wireless': [
            '00:1A:2B',  # Example OUI for wireless devices
            '00:1C:B3'
        ],
        'Ethernet': [
            '00:22:68',  # Example OUI for wired devices
            '00:40:9D'
        ]
    }

    for interface, ouis in known_makers.items():
        for oui in ouis:
            if mac_address.startswith(oui):
                return f'The MAC {mac_address} is associated with a {interface} card.'

    return 'The MAC address type could not be determined.'

# Example usage
mac_address = '00:1A:2B:3C:4D:5E'  # Replace with actual MAC address
print(identify_interface_type(mac_address))
