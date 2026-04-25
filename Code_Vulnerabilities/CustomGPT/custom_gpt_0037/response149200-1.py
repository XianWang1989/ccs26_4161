
import requests

def get_oui_type(mac_address):
    # Strip the MAC address of any colons or dashes
    mac = mac_address.replace(':', '').replace('-', '').upper()
    oui = mac[:6]  # Get the first 6 characters (OUI)

    # URL to a public OUI lookup service
    url = f'https://api.macvendors.com/{oui}'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            vendor_info = response.json()
            return vendor_info.get('result', 'Unknown vendor')
        else:
            return 'Failed to retrieve data.'
    except Exception as e:
        return str(e)

# Example Usage
mac_address = '00:1A:2B:3C:4D:5E'
device_type = get_oui_type(mac_address)
print(f'The device type for MAC {mac_address} is: {device_type}')
