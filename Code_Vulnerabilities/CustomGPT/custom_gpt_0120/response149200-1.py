
import requests
from getmac import get_mac_address

def get_mac_info(mac):
    # Get MAC address details from the maclookup API
    response = requests.get(f"https://api.maclookup.app/lookup/{mac}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def determine_card_type(mac):
    mac_info = get_mac_info(mac)

    if mac_info and 'data' in mac_info:
        manufacturer = mac_info['data']['company']
        # Add conditions to classify the manufacturer's MAC addresses
        # This is a simplified example; real classification might require a detailed database
        if 'wireless' in manufacturer.lower():
            return 'Wireless Card'
        elif 'ethernet' in manufacturer.lower() or 'network' in manufacturer.lower():
            return 'Ethernet Card'
        else:
            return 'Unknown Card Type'
    return 'MAC address not found'

# Example MAC address
mac_address = "44:38:39:ff:ef:57"
card_type = determine_card_type(mac_address)
print(f"The MAC address {mac_address} is likely a {card_type}.")
