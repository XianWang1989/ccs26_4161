
import requests

def get_mac_vendor(mac_address):
    # Ensure the MAC address is in the proper format (remove dashes, colons)
    mac_address = mac_address.replace('-', '').replace(':', '').upper()
    if len(mac_address) != 12:
        raise ValueError("Invalid MAC address format")

    # Get the first three octets (OUI)
    oui = mac_address[:6]

    # Query the MAC address API (example: macvendors.com)
    response = requests.get(f"http://api.macvendors.com/{oui}")

    if response.status_code == 200:
        return response.text.strip()
    else:
        return None

def determine_card_type(mac_address):
    vendor = get_mac_vendor(mac_address)
    if vendor:
        wireless_vendors = ['Atheros', 'Intel', 'Broadcom', 'Ralink', 'Realtek']
        # Check if the vendor indicates a wireless card
        for wireless_vendor in wireless_vendors:
            if wireless_vendor.lower() in vendor.lower():
                return 'Wireless Card'
        return 'Ethernet Card or Unknown'
    else:
        return 'Vendor Not Found'

# Example usage
mac_address = '00:14:22:01:23:45'  # Replace with your MAC address
card_type = determine_card_type(mac_address)
print(f"The card type for MAC {mac_address} is: {card_type}")
