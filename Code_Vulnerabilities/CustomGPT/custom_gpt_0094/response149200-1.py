
import requests

def get_mac_info(mac):
    # Use a public OUI lookup service
    url = f"https://api.macaddress.io/v1?apiKey=<your_api_key>&output=json&search={mac}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data.get('vendorDetails', {})
    return {}

def is_wireless(mac):
    info = get_mac_info(mac)
    if not info:
        return None

    # Example OUIs typically associated with wireless cards
    wireless_ouies = ['00:1A:2B', '00:1A:4A', '00:1F:33', '00:24:6C']

    # Check if the details indicate wireless capability
    return any(mac.startswith(oui) for oui in wireless_ouies)

# Sample MAC address
mac_address = "00:1A:2B:FF:EE:DD"

if is_wireless(mac_address):
    print(f"{mac_address} is a wireless card.")
else:
    print(f"{mac_address} is likely an Ethernet card or unknown.")
