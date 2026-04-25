
import requests

def get_mac_vendor(mac_address):
    # Format the MAC address (remove colons or dashes)
    mac_address = mac_address.replace(":", "").replace("-", "").upper()
    if len(mac_address) != 12:
        raise ValueError("Invalid MAC address format")

    # Get the first three bytes (OUI)
    oui = mac_address[:6]

    # Query the OUI database
    url = f"https://api.macvendors.com/{oui}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        return None

def identify_network_card(mac_address):
    vendor = get_mac_vendor(mac_address)

    if vendor:
        # Example list of known vendors with wireless and Ethernet products
        wireless_vendors = ['APPLE', 'INTEL', 'LINKSYS']
        ethernet_vendors = ['CISCO', 'TP-LINK', 'D-LINK']

        # Check if vendor matches known wireless or Ethernet vendors
        if any(vendor.upper() in name for name in wireless_vendors):
            return "Wireless Card"
        elif any(vendor.upper() in name for name in ethernet_vendors):
            return "Ethernet Card"
        else:
            return "Unknown Card Type"
    else:
        return "Vendor not found"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
card_type = identify_network_card(mac_address)
print(f"The MAC address {mac_address} is associated with: {card_type}")
