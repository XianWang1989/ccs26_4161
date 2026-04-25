
import requests

def get_mac_vendor(mac):
    try:
        # Request the OUI from an online database
        response = requests.get(f"https://api.macvendors.com/{mac}")
        if response.status_code == 200:
            return response.text
        else:
            return "Vendor not found"
    except Exception as e:
        return str(e)

def is_wireless_mac(mac):
    vendor = get_mac_vendor(mac)
    # Check the vendor against known wireless manufacturers
    wireless_vendors = [
        'Apple', 'Intel', 'TP-Link', 'Netgear', 
        'Linksys', 'D-Link', 'Broadcom', 'Atheros'
    ]

    for vendor_name in wireless_vendors:
        if vendor_name.lower() in vendor.lower():
            return True

    return False

# Example usage
mac_address = "00:14:22:01:23:45"
if is_wireless_mac(mac_address):
    print(f"The MAC address {mac_address} is likely a wireless card.")
else:
    print(f"The MAC address {mac_address} is likely an Ethernet card.")
