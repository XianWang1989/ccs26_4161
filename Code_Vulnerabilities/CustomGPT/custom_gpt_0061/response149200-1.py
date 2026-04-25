
import requests

def get_oui_info(mac_address):
    # Extract the OUI from the MAC address (first 6 characters)
    oui_prefix = mac_address[:8].upper()

    # We'll use an online OUI lookup service
    response = requests.get(f'https://api.macvendors.com/{oui_prefix}')

    if response.status_code == 200:
        return response.json()
    else:
        return None

def infer_card_type(mac_address):
    oui_info = get_oui_info(mac_address)

    if oui_info:
        vendor = oui_info.get('company')
        print(f'MAC Address: {mac_address} | Vendor: {vendor}')

        # Basic inference logic (customize as needed)
        if 'wireless' in vendor.lower() or 'wifi' in vendor.lower():
            return "Likely a Wireless Card"
        else:
            return "Likely an Ethernet Card"
    else:
        return "OUI information not available"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
card_type = infer_card_type(mac_address)
print(card_type)
