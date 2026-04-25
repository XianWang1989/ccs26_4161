
import requests

def get_device_type(mac_address):
    # Make sure to format MAC address (remove colons or dashes)
    formatted_mac = mac_address.replace(':', '').replace('-', '').upper()
    if len(formatted_mac) < 6:
        return "Invalid MAC address"

    oui = formatted_mac[:6]

    # Using a public API to get OUI details
    try:
        response = requests.get(f'https://api.macvendors.com/{formatted_mac}')
        if response.status_code == 200:
            vendor_info = response.json()
            if 'type' in vendor_info:
                return vendor_info['type']
            else:
                return "Unknown device type"
        else:
            return "Could not retrieve vendor information"
    except Exception as e:
        return f"Error: {e}"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
device_type = get_device_type(mac_address)
print(f"The device type for MAC {mac_address} is: {device_type}")
