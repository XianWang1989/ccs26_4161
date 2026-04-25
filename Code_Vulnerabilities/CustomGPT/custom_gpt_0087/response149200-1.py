
import re
import requests

# Function to get device type from MAC address
def get_device_type(mac_address):
    # Ensure the MAC address is in the correct format
    if not re.match(r'^([0-9a-fA-F]{2}[:-]){5}([0-9a-fA-F]{2})$', mac_address):
        return "Invalid MAC address format"

    # Extract the OUI from the MAC address
    oui = mac_address[:8].replace(':', '').replace('-', '').upper()

    # OUI database URL (for demonstration, replace with actual OUI lookup source)
    oui_database_url = f"https://api.macvendors.com/{mac_address}"

    try:
        response = requests.get(oui_database_url)
        if response.status_code == 200:
            vendor_info = response.json()
            vendor_name = vendor_info.get("company", "Unknown")
            if "Wi-Fi" in vendor_name or "Wireless" in vendor_name:
                return "Wireless card"
            else:
                return "Ethernet card"
    except Exception as e:
        return f"Error retrieving vendor info: {e}"

    return "Unknown type"

# Example usage
mac_address = "00:14:22:01:23:45"
device_type = get_device_type(mac_address)
print(f"The device type for MAC address {mac_address} is: {device_type}")
