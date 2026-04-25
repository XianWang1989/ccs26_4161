
import requests
from getmac import get_mac_address

# A simple OUI lookup using an online API
def get_oui(mac):
    oui = mac[:8].upper()  # Extract OUI (first 3 octets)
    response = requests.get(f'https://api.macvendors.com/{oui}')
    if response.status_code == 200:
        return response.text  # Return manufacturer name
    return None

# Function to determine the type of network card
def determine_card_type(mac):
    manufacturer = get_oui(mac)

    if manufacturer:
        wireless_keywords = ['WIRELESS', 'BLUETOOTH', 'WIFI']
        ethernet_keywords = ['ETHERNET', 'LAN', 'NETWORK']

        if any(keyword in manufacturer.upper() for keyword in wireless_keywords):
            return "Wireless Card"
        elif any(keyword in manufacturer.upper() for keyword in ethernet_keywords):
            return "Ethernet Card"
        else:
            return "Unknown Card Type"
    else:
        return "Manufacturer not found."

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"  # Replace with your MAC address
card_type = determine_card_type(mac_address)
print(f"The card type for MAC address {mac_address} is: {card_type}")
