
import requests

def get_device_type(mac_address):
    # Convert MAC address to uppercase and remove colons or dashes
    mac_address = mac_address.upper().replace(':', '').replace('-', '')

    # Extract the first 6 characters (OUI)
    oui = mac_address[:6]

    # Query the OUI database
    url = f"https://api.macvendors.com/{oui}"
    response = requests.get(url)

    if response.status_code == 200:
        vendor_info = response.text
        if 'wireless' in vendor_info.lower():
            return "Wireless Card"
        elif 'ethernet' in vendor_info.lower() or 'wired' in vendor_info.lower():
            return "Ethernet Card"
        else:
            return "Unknown Type"
    else:
        return "Unable to retrieve vendor information"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
device_type = get_device_type(mac_address)
print(f"The device type for MAC address {mac_address} is: {device_type}")
