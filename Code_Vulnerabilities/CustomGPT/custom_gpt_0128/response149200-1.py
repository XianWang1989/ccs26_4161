
import requests

def get_vendor(mac_address):
    """Fetch vendor information from MAC address."""
    url = f"https://api.maclookup.app/api/v2/macs/{mac_address}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()
    return data.get("vendor_name"), data.get("type")

def identify_card_type(mac_address):
    """Identify if the MAC address belongs to a wireless or Ethernet card."""
    vendor, card_type = get_vendor(mac_address)

    if vendor:
        print(f"Vendor: {vendor}, Type: {card_type}")
        if "wireless" in card_type.lower():
            return "Wireless Card"
        elif "ethernet" in card_type.lower():
            return "Ethernet Card"
        else:
            return "Unknown Card Type"
    else:
        return "Could not retrieve vendor information"

# Example usage
mac_address = "00:14:22:01:23:45"  # Replace with your MAC address
card_type = identify_card_type(mac_address)
print(f"The MAC address {mac_address} is associated with: {card_type}")
