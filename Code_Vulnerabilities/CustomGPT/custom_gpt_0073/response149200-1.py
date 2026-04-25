
import requests

def get_oui_category(mac_address):
    try:
        # Extract the first three octets (OUI) from the MAC address
        oui = mac_address.upper()[0:8]  # Format: XX:XX:XX
        response = requests.get(f'https://api.macvendors.com/{oui.replace(":", "")}')

        if response.status_code == 200:
            vendor_info = response.json()
            return vendor_info.get("category", "Unknown")
        else:
            return "Error fetching info"
    except Exception as e:
        return str(e)

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
category = get_oui_category(mac_address)
print(f"The MAC address {mac_address} belongs to: {category}")
