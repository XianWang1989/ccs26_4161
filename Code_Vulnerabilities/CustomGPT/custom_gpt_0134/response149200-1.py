
import requests

def get_mac_info(mac_address):
    # OUI lookup service
    url = f"https://api.macvendors.com/{mac_address}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching MAC info: {e}")
        return None

def is_wireless_mac(mac_address):
    mac_info = get_mac_info(mac_address)

    if mac_info:
        # Check common identifiers for wireless and Ethernet
        if "wireless" in mac_info['category'].lower():
            return True
        else:
            return False
    return None

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
if is_wireless_mac(mac_address):
    print(f"The MAC address {mac_address} is likely for a wireless card.")
else:
    print(f"The MAC address {mac_address} is likely for an Ethernet card.")
