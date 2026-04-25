
import re
import requests

def get_mac_vendor(mac):
    """Get the vendor for the MAC address."""
    mac = mac.lower()
    if not re.match(r'([0-9a-f]{2}[:-]){5}([0-9a-f]{2})$', mac):
        return None

    try:
        # Fetch OUI information from a public API
        response = requests.get(f'https://api.macvendors.com/{mac}')
        return response.text
    except Exception as e:
        print(f"Error retrieving vendor data: {e}")
        return None

def determine_interface_type(mac):
    """Determine if MAC is associated with Ethernet or Wireless."""
    vendor = get_mac_vendor(mac)
    if not vendor:
        return "Invalid MAC address or vendor not found."

    # You can refine this list based on known vendors
    wireless_vendors = ['broadcom', 'intel', 'atheros', 'qualcomm', 'linksys']
    ethernet_vendors = ['realtek', 'marvell', 'nvidia', 'cisco']

    # Check if the vendor belongs to known wireless or ethernet groups
    if any(vendor.lower().startswith(v) for v in wireless_vendors):
        return "Wireless Card"
    elif any(vendor.lower().startswith(v) for v in ethernet_vendors):
        return "Ethernet Card"

    return "Unknown type"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
interface_type = determine_interface_type(mac_address)
print(f"{mac_address} is associated with a: {interface_type}")
