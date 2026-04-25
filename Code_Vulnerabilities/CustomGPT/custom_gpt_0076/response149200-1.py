
import requests

def get_mac_details(mac_address):
    # Use the OUI lookup to get organizational details
    url = f"https://api.macvendors.com/{mac_address}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    return None

def determine_card_type(mac_address):
    mac_prefix = mac_address.upper()[:8]  # Get the first 8 characters (OUI)
    vendor_info = get_mac_details(mac_prefix)

    if vendor_info:
        if "WIRELESS" in vendor_info.upper():
            return "Wireless Card"
        elif "ETHERNET" in vendor_info.upper():
            return "Ethernet Card"
        else:
            return "Unknown Card Type"
    return "Invalid MAC Address"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"  # Replace with the MAC address you want to check
card_type = determine_card_type(mac_address)
print(f"The card type for {mac_address} is: {card_type}")
