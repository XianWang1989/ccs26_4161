
import requests

def get_mac_vendor(mac_address):
    """Get vendor information from MAC address."""
    url = f"http://api.macvendors.com/{mac_address}"
    response = requests.get(url)
    return response.text if response.status_code == 200 else "Unknown Vendor"

def check_card_type(mac_address):
    """Determine if MAC address is for a wireless or Ethernet card."""
    vendor = get_mac_vendor(mac_address)

    # Example logic to infer card type based on vendor
    wireless_vendors = ["Apple", "Intel", "Qualcomm"]
    ethernet_vendors = ["Realtek", "Broadcom"]

    for vendor_name in wireless_vendors:
        if vendor_name.lower() in vendor.lower():
            return "Wireless card"

    for vendor_name in ethernet_vendors:
        if vendor_name.lower() in vendor.lower():
            return "Ethernet card"

    return "Unknown card type"

# Example MAC address
mac_address = "00:1A:2B:3C:4D:5E"
card_type = check_card_type(mac_address)
print(f"The card type for MAC {mac_address} is: {card_type}")
