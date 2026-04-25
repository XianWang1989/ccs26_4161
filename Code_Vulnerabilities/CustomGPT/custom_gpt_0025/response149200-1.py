
import requests

def get_oui_info(mac_address):
    try:
        # Extract the OUI (first 6 characters)
        oui = mac_address.replace(":", "").upper()[:6]

        # Use an API to get OUI details (example API)
        response = requests.get(f'https://api.macvendors.com/{oui}')

        if response.status_code == 200:
            return response.json()  # Assuming the API returns JSON
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def determine_device_type(mac_address):
    oui_info = get_oui_info(mac_address)

    if oui_info:
        # Check if the device is typically associated with Ethernet or Wi-Fi
        if "wireless" in oui_info.get('type', '').lower():
            return "Wireless Card"
        elif "ethernet" in oui_info.get('type', '').lower():
            return "Ethernet Card"
        else:
            return "Unknown"
    else:
        return "OUI not found"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
device_type = determine_device_type(mac_address)
print(f"The MAC address {mac_address} is associated with a: {device_type}")
