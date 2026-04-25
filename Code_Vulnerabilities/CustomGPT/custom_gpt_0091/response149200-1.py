
import requests

def get_mac_details(mac):
    # Use an API to fetch the MAC address details
    url = f"https://api.maclookup.app/v2/macs/{mac}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def determine_card_type(mac):
    # Get MAC address details
    details = get_mac_details(mac)

    if details and 'manufacturer' in details:
        manufacturer = details['manufacturer']
        if 'wireless' in manufacturer.lower() or 'wifi' in manufacturer.lower():
            return "Wireless Card"
        else:
            return "Ethernet Card"
    else:
        return "Unknown Card Type"

# Example MAC address
mac_address = "00:1A:2B:3C:4D:5E"  # Replace with actual MAC address
card_type = determine_card_type(mac_address)
print(f"The MAC address {mac_address} is associated with a {card_type}.")
