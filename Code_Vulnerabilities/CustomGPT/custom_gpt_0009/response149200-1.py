
from getmac import get_mac_address

def get_card_info(mac_address):
    # Get the MAC prefix (first three octets)
    ouis = mac_address.split(':')[:3]
    prefix = ':'.join(ouis).upper()

    # A basic example mapping of OUI prefixes to types
    # This is not exhaustive; you may want to expand this based on your needs
    device_types = {
        '00:1A:2B': 'Ethernet',
        '00:1C:42': 'Wireless',
        '00:1F:16': 'Wireless',
        '00:24:D7': 'Ethernet'
        # Add more OUI mappings as needed
    }

    card_type = device_types.get(prefix, 'Unknown')

    return card_type

# Example MAC address
mac_address = "00:1A:2B:3C:4D:5E"
card_info = get_card_info(mac_address)

print(f"The card type for MAC {mac_address} is likely: {card_info}")
