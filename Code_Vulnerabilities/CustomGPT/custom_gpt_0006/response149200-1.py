
import requests

# Function to get OUI details
def get_oui_data(mac_prefix):
    try:
        response = requests.get(f"https://api.macvendors.com/{mac_prefix}")
        return response.text
    except Exception as e:
        print(f"Error retrieving data: {e}")
        return None

# Function to determine card type from MAC address
def determine_card_type(mac_address):
    # Extract OUI (first 6 characters of MAC in uppercase)
    mac_prefix = mac_address[:8].upper()

    # Get vendor info
    vendor_info = get_oui_data(mac_prefix)

    if vendor_info:
        if "wireless" in vendor_info.lower():
            return "Wireless Card"
        elif "ethernet" in vendor_info.lower() or "wired" in vendor_info.lower():
            return "Ethernet Card"
        else:
            return "Unknown Card Type"
    else:
        return "Could not determine card type"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
card_type = determine_card_type(mac_address)
print(f"The card type for MAC address {mac_address} is: {card_type}")
