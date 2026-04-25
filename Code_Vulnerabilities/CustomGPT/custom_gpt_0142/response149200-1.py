
import requests

def get_mac_info(mac_address):
    # Get the first three octets of the MAC address
    mac_prefix = ':'.join(mac_address.split(':')[:3]).upper()  # e.g., '00:1A:2B'

    # Query the MAC address lookup API
    response = requests.get(f'https://api.macvendors.com/{mac_prefix}')

    if response.status_code == 200:
        return response.json()
    else:
        return None

def determine_card_type(mac_address):
    mac_info = get_mac_info(mac_address)

    if mac_info:
        manufacturer = mac_info.get('result', {}).get('company', '').lower()

        # Simplified logic: Check manufacturer for wireless or ethernet keywords
        if 'wireless' in manufacturer or 'wifi' in manufacturer:
            return "Wireless Card"
        elif 'ethernet' in manufacturer or 'cable' in manufacturer:
            return "Ethernet Card"
        else:
            return "Unknown Card Type"
    else:
        return "Could not retrieve MAC information"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
card_type = determine_card_type(mac_address)
print(f"The card type for MAC address {mac_address} is: {card_type}")
