
import requests

def get_oui_info(mac_address):
    # Extract the OUI (first three bytes)
    oui = mac_address[:8].upper()

    # Use an OUI lookup API (for example, macvendors.com)
    response = requests.get(f'https://api.macaddress.io/v1?apiKey=at_your_api_key_here&output=json&search={mac_address}')
    data = response.json()

    if 'vendorDetails' in data:
        vendor = data['vendorDetails']['companyName']
        return vendor
    else:
        return None

def determine_interface_type(vendor):
    # Basic heuristic for determining interface type
    if vendor:
        # This can be expanded with more specific vendors
        wireless_vendors = ['Atheros', 'Intel', 'Broadcom', 'Qualcomm']
        ethernet_vendors = ['Realtek', 'Intel', 'Cisco']

        for wireless_vendor in wireless_vendors:
            if wireless_vendor in vendor:
                return 'Wireless Card'

        for ethernet_vendor in ethernet_vendors:
            if ethernet_vendor in vendor:
                return 'Ethernet Card'

    return 'Unknown'

# Example MAC address
mac_address = '00:1A:2B:3C:4D:5E'
vendor = get_oui_info(mac_address)
interface_type = determine_interface_type(vendor)

print(f'MAC Address: {mac_address}')
print(f'Vendor: {vendor}')
print(f'Interface Type: {interface_type}')
