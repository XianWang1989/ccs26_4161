
import requests

def get_oui(vendor_prefix):
    """Fetch OUI information from a public API."""
    url = f'https://api.macvendors.com/{vendor_prefix}'
    try:
        response = requests.get(url)
        return response.json() if response.ok else None
    except Exception as e:
        print(f"Error fetching OUI data: {e}")
        return None

def determine_interface_type(mac_address):
    """Determine if MAC address is likely an Ethernet or wireless interface."""
    # Extract OUI (first 3 bytes of MAC)
    vendor_prefix = mac_address.replace(":", "").upper()[:6]

    vendor_info = get_oui(vendor_prefix)

    if vendor_info:
        vendor = vendor_info.get('result', 'Unknown')
        print(f"Vendor: {vendor}")

        # Example heuristics based on vendor
        wireless_vendors = ['INTEL', 'Atheros', 'Broadcom', 'Qualcomm']
        if any(vendor.upper() in w for w in wireless_vendors):
            return "Wireless Card"
        return "Ethernet Card"
    return "Unknown"

# Example MAC address
mac = "00:1A:2B:3C:4D:5E"
interface_type = determine_interface_type(mac)
print(f"The interface type of {mac} is: {interface_type}")
