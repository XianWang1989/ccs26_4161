
import requests

def get_mac_vendor(mac_address):
    # Extract OUI from MAC address
    oui = mac_address.upper()[:8]
    response = requests.get(f'https://api.macvendors.com/{oui}')
    return response.text

def is_wireless_or_ethernet(mac_address):
    vendor_info = get_mac_vendor(mac_address)
    if 'wireless' in vendor_info.lower():
        return "Wireless card"
    elif 'ethernet' in vendor_info.lower():
        return "Ethernet card"
    else:
        return "Unknown type"

# Example usage
mac_address = '01:23:45:67:89:AB'
device_type = is_wireless_or_ethernet(mac_address)
print(device_type)
