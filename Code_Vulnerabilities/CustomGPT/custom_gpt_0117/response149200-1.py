
import requests

def get_mac_info(mac_address):
    url = f'https://api.macvendors.com/{mac_address}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def determine_interface_type(mac_address):
    mac_info = get_mac_info(mac_address)

    if mac_info:
        vendor = mac_info.get('result', {}).get('company', '').lower()

        # Add custom logic to determine type based on vendor
        wireless_vendors = ['netgear', 'linksys', 'broadcom', 'intel', 'tp-link']
        ethernet_vendors = ['realtek', 'broadcom', 'intel', 'qualcomm']

        for vendor in wireless_vendors:
            if vendor in vendor:
                return "Wireless Card"

        for vendor in ethernet_vendors:
            if vendor in vendor:
                return "Ethernet Card"

        return "Unknown Interface Type"

    return "MAC Address Not Found"

# Example usage
mac_address = "44:38:39:ff:ef:57"  # Replace with actual MAC address
interface_type = determine_interface_type(mac_address)
print(f"The MAC address {mac_address} is associated with a: {interface_type}")
