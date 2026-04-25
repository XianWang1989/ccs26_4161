
import requests

def get_oui_info(mac_address):
    # Extract the OUI from the MAC address
    oui = mac_address[:8].upper()  # Format: XX:XX:XX

    # Use a public API to get details about the OUI
    response = requests.get(f'https://api.macvendors.com/{oui}')

    if response.status_code == 200:
        return response.json()
    else:
        return None

def is_wireless_or_ethernet(mac_address):
    oui_info = get_oui_info(mac_address)

    if oui_info:
        vendor = oui_info.get('vendor')
        # Add specific vendors you know to be wireless
        wireless_vendors = ["Apple", "Atheros", "Broadcom", "Intel"]

        if any(vendor in wireless_vendors for vendor in oui_info.values()):
            return "Wireless Card"
        else:
            return "Ethernet Card"
    else:
        return "Unknown OUI"

# Sample MAC Address
mac_address = "00:1A:2B:3C:4D:5E"
result = is_wireless_or_ethernet(mac_address)
print(f'The MAC address {mac_address} is likely a: {result}')
