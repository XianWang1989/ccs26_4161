
import requests

def get_mac_info(mac_address):
    # Fetch OUI information from the IEEE website
    try:
        response = requests.get(f'https://api.macvendors.com/{mac_address}')
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print(f"Error fetching MAC info: {e}")
        return None

def determine_interface_type(mac_address):
    info = get_mac_info(mac_address)

    if info is not None:
        if 'wireless' in info['category'].lower():
            return 'Wireless Card'
        elif 'ethernet' in info['category'].lower():
            return 'Ethernet Card'
        else:
            return 'Unknown Card Type'
    return 'Unable to determine card type'

# Example usage
mac = '00:1A:2B:3C:4D:5E'  # Replace with your MAC address
card_type = determine_interface_type(mac)
print(f"The MAC address {mac} is likely associated with a: {card_type}")
