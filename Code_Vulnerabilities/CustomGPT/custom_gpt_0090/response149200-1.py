
import requests
from getmac import get_mac_address

def get_mac_type(mac_address):
    # Fetch the MAC address vendor information
    url = f"https://api.macvendors.com/{mac_address}"
    try:
        response = requests.get(url)
        vendor = response.text
        wireless_vendors = ['Apple', 'Intel', 'Broadcom', 'Qualcomm', 'Atheros']  # Common wireless vendors

        if any(vendor in wireless for wireless in wireless_vendors):
            return 'Wireless'
        else:
            return 'Ethernet'
    except Exception as e:
        return f"Error fetching MAC info: {e}"

# Example MAC address
mac_address = "00:1A:2B:3C:4D:5E"  # Replace with the actual MAC address
mac_type = get_mac_type(mac_address)
print(f"The MAC address {mac_address} is likely: {mac_type}")
