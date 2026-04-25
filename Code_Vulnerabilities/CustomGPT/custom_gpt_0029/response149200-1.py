
import requests

def get_mac_info(mac_address):
    url = f"https://api.macvendors.com/{mac_address}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        return "MAC address not found."

# Example usage
mac_address = "00:14:22:01:23:45"  # Replace with your MAC address
vendor_info = get_mac_info(mac_address)
print(vendor_info)
