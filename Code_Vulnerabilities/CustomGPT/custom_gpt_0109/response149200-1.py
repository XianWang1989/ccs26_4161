
import requests

def get_mac_type(mac_address):
    # Remove any delimiters
    mac = mac_address.replace(":", "").replace("-", "").upper()

    if len(mac) != 12:
        raise ValueError("Invalid MAC address")

    # Extract OUI (first 6 characters)
    oui = mac[:6]

    # Use an OUI lookup service
    response = requests.get(f'https://api.macvendors.com/{oui}')

    if response.status_code == 200:
        vendor = response.text
        print(f"Vendor: {vendor}")

        # List of common wireless vendors (example)
        wireless_vendors = ['APPLE', 'CISCO', 'LINKSYS', 'TP-LINK']

        if any(vendor.upper() in v for v in wireless_vendors):
            return 'Wireless Card'
        else:
            return 'Ethernet Card'
    else:
        return "OUI Not Found"

mac_address = "00:1A:2B:3C:4D:5E"
card_type = get_mac_type(mac_address)
print(f"The MAC address {mac_address} is associated with a {card_type}.")
