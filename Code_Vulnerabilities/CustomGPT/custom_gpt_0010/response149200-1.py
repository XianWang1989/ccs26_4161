
import subprocess
import requests

def get_mac_type(mac_address):
    # Use the maclookup API to get MAC info
    response = requests.get(f'https://api.maclookup.app/api/v2/macs/{mac_address}')

    if response.status_code == 200:
        data = response.json()
        if data['data']:
            mac_info = data['data']
            vendor = mac_info.get('company', 'Unknown')
            if 'wireless' in vendor.lower():
                return 'Wireless Card'
            elif 'ethernet' in vendor.lower():
                return 'Ethernet Card'
            else:
                return 'Unknown type'
    return 'Invalid MAC address'

# Example MAC address
mac_address = "00:1A:2B:3C:4D:5E"
mac_type = get_mac_type(mac_address)
print(f'The MAC address {mac_address} is associated with: {mac_type}')
