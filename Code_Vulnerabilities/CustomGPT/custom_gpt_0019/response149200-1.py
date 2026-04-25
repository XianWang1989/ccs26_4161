
import requests

# Function to determine card type from MAC address
def get_mac_info(mac):
    # Usually, the first three octets (first 6 characters) represent the OUI
    oui = mac[:8].upper()

    # OUI mapping (this is a simplified example)
    ouis = {
        '00:1A:2B': 'Wireless',
        '00:1C:4D': 'Ethernet',
        '00:24:D7': 'Wireless',
        # Add more OUIs as necessary
    }

    # Fetch MAC address info from a public API (if needed)
    # response = requests.get(f'https://api.macaddress.io/v1?apiKey=YOUR_API_KEY&output=json&search={mac}')
    # info = response.json()

    # Determine type based on OUI
    card_type = ouis.get(oui, 'Unknown')

    return card_type

# Example usage
mac_address = '00:1A:2B:3C:4D:5E'  # Replace with actual MAC address
print(f'MAC Address {mac_address} is associated with a {get_mac_info(mac_address)} card.')
