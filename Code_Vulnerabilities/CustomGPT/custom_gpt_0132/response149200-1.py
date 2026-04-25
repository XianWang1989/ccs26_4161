
import requests
import re

def get_device_type(mac_address):
    # Validate MAC address format
    if not re.match(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', mac_address):
        raise ValueError("Invalid MAC address format")

    # Send request to OUI database
    url = f'https://api.macaddress.io/v1?apiKey=YOUR_API_KEY&output=json&search={mac_address}'
    response = requests.get(url)
    data = response.json()

    # Check if response is valid
    if 'vendorDetails' in data and data['vendorDetails']:
        vendor = data['vendorDetails'][0]
        mac_type = vendor['companyAddress']

        # Heuristic based on known patterns in company addresses
        if 'wireless' in mac_type.lower() or 'wifi' in mac_type.lower():
            return 'Wireless'
        elif 'ethernet' in mac_type.lower():
            return 'Ethernet'

    return 'Unknown or not determined'

# Example usage
try:
    mac = '00:1A:2B:3C:4D:5E'
    device_type = get_device_type(mac)
    print(f'MAC address {mac} is associated with a: {device_type} card')
except Exception as e:
    print(f'Error: {e}')
