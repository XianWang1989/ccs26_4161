
import requests

def get_oui_info(mac_address):
    # Get the first three bytes of the MAC address
    oui = mac_address[:8].upper()
    url = f"https://api.macvendors.com/{oui}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print(f"Error fetching OUI information: {e}")
        return None

def determine_device_type(mac_address):
    oui_info = get_oui_info(mac_address)

    if oui_info:
        vendor = oui_info.get('result', 'Unknown')
        print(f"Vendor: {vendor}")

        # Check vendor information (this is a simplified example)
        wireless_vendors = ['NETGEAR', 'TP-LINK', 'ASUS', 'D-Link']
        ethernet_vendors = ['Cisco', 'Intel', 'Broadcom']

        if any(vendor.startswith(w) for w in wireless_vendors):
            return "Wireless Card"
        elif any(vendor.startswith(e) for e in ethernet_vendors):
            return "Ethernet Card"
        else:
            return "Unknown Type"
    else:
        return "Could not determine type"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
device_type = determine_device_type(mac_address)
print(f"The MAC address {mac_address} is associated with a: {device_type}")
