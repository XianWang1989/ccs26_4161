
import requests

def get_mac_vendor(mac_address):
    # Normalize the MAC address
    mac_address = mac_address.replace(":", "-").upper()

    # API endpoint for OUI lookup
    url = f"https://api.macvendors.com/{mac_address}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        return None

def determine_card_type(mac_address):
    vendor = get_mac_vendor(mac_address)

    if vendor:
        # Check for known wireless and Ethernet vendors
        wireless_vendors = ["APPLE", "LINKSYS", "NETGEAR", "TP-LINK", "D-LINK"]
        ethernet_vendors = ["INTEL", "REALTEK", "MARVELL", "CISCO"]

        # Check if the vendor belongs to either category
        if any(v in vendor for v in wireless_vendors):
            return "Wireless Card"
        elif any(v in vendor for v in ethernet_vendors):
            return "Ethernet Card"
        else:
            return "Unknown Card Type"
    else:
        return "Vendor not found"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
card_type = determine_card_type(mac_address)
print(f"The MAC address {mac_address} is associated with a {card_type}.")
