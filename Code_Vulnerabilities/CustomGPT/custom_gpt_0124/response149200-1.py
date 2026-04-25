
import requests

def get_mac_info(mac_address):
    # Convert MAC address to the appropriate format
    mac_address = mac_address.replace(':', '').upper()
    url = f'https://api.macvendors.com/{mac_address}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    return None

def is_wireless_mac(mac_address):
    info = get_mac_info(mac_address)

    if info:
        # Check OUI associated with the MAC address
        # This is a simplified check; further parsing may be required based on your data source
        if 'wireless' in info.get('category', '').lower():
            return True
        return False

# Example MAC address
mac_address = '00:1A:2B:3C:4D:5E'
if is_wireless_mac(mac_address):
    print(f"{mac_address} is likely a wireless card.")
else:
    print(f"{mac_address} is likely an Ethernet card.")
