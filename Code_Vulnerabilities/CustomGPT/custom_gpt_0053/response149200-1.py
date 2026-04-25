
import requests
from getmac import get_mac_address

def get_oui_info(mac):
    oui_url = f"https://api.macaddress.io/v1?apiKey=YOUR_API_KEY&output=json&search={mac}"
    response = requests.get(oui_url)
    data = response.json()

    if "vendorDetails" in data:
        return data["vendorDetails"]
    return None

def is_wireless_or_ethernet(mac):
    oui_info = get_oui_info(mac)

    if oui_info:
        # Check for known wireless manufacturers
        wireless_vendors = ["Apple", "Intel", "Broadcom", "Atheros", "Marvell"]

        vendor = oui_info.get("companyName", "").strip()
        if any(vendor in name for name in wireless_vendors):
            return "Wireless"
        else:
            return "Ethernet"
    return "Unknown"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"  # Replace with your MAC address
interface_type = is_wireless_or_ethernet(mac_address)
print(f"The interface with MAC address {mac_address} is likely: {interface_type}")
