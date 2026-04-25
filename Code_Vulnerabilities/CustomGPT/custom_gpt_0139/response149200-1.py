
import requests
from getmac import get_mac_address

def get_mac_type(mac):
    # Convert MAC address to upper case to maintain standard format
    mac = mac.upper().replace(":", "").replace("-", "")

    # Get OUI from the MAC address
    oui = mac[:6]
    response = requests.get(f'https://api.maclookup.app/api/v1/macs/{oui}')

    if response.status_code == 200:
        data = response.json()
        if data['success']:
            mac_info = data['data']
            # Print the manufacturer and type (if available)
            print(f"Manufacturer: {mac_info.get('company')}")

            # Check if the type is wireless or ethernet (often inferred from device type)
            device_type = mac_info.get('type', 'Unknown')
            if 'wireless' in device_type.lower():
                return 'Wireless'
            elif 'ethernet' in device_type.lower():
                return 'Ethernet'
            else:
                return 'Unknown'
        else:
            return "MAC address not found."   
    else:
        return "Error fetching data."

# Example Usage
mac_address = get_mac_address()  # Or you can use a specific MAC address
print(f"The MAC address {mac_address} is associated with: {get_mac_type(mac_address)}")
