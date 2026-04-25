
import requests

def get_mac_vendor(mac):
    """Fetch the vendor information based on the MAC address."""
    url = f"https://api.macvendors.com/{mac}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def is_wireless_vendor(vendor):
    """Determine if the vendor typically produces wireless cards."""
    wireless_vendors = [
        "Apple", "Intel", "TP-Link", "Netgear", "Cisco", "Linksys", "Broadcom"
    ]
    return any(wireless in vendor for wireless in wireless_vendors)

def determine_card_type(mac):
    """Determine if the MAC address belongs to a wireless or Ethernet card."""
    vendor_info = get_mac_vendor(mac)
    if vendor_info:
        vendor = vendor_info.get("company")
        return "Wireless" if is_wireless_vendor(vendor) else "Ethernet"
    return "Unknown"

# Example usage
mac_address = "44:38:39:ff:ef:57"
card_type = determine_card_type(mac_address)
print(f"The card type for MAC address {mac_address} is: {card_type}")
