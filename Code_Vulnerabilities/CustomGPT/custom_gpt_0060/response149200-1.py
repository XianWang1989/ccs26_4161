
import requests

def get_mac_vendor(mac_address):
    # Normalize MAC address format
    mac_address = mac_address.replace(':', '').replace('-', '').upper()

    if len(mac_address) != 12:
        raise ValueError("Invalid MAC address format")

    oui = mac_address[:6]  # Get the first six characters for OUI
    url = f"https://api.macvendors.com/{oui}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

# Example usage
mac_example = "00:1A:2B:3C:4D:5E"
vendor = get_mac_vendor(mac_example)

if vendor:
    print(f"The MAC address {mac_example} is associated with the vendor: {vendor}")
else:
    print("Vendor not found.")
