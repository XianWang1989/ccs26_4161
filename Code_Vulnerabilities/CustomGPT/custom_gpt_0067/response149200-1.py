
import requests

# Sample OUI data; ideally, load from a file instead
OUI_DATA = {
    '00:1A:2B': 'Ethernet',
    '00:1C:43': 'Wireless',
    # Add more OUI values...
}

def get_card_type(mac):
    # Format MAC address to match OUI format
    oui = mac.upper()[:8]  # Get the first 3 bytes

    # Look up the OUI
    return OUI_DATA.get(oui, 'Unknown')

# Example usage
mac_address = '00:1A:2B:3C:4D:5E'
card_type = get_card_type(mac_address)

print(f'The card type for {mac_address} is: {card_type}')
