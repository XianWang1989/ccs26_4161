
import requests

# Sample MAC address for testing
mac_address = "00:14:22:01:23:45"

# OUI databases for Ethernet and Wireless
oui_wired = ['00:14:22', '00:1A:2B']  # Add more wired MAC prefixes
oui_wireless = ['00:1F:3B', '00:1B:77']  # Add more wireless MAC prefixes

def get_mac_type(mac_address):
    mac_prefix = mac_address.upper()[:8]  # Extract the first 8 characters (OUI)

    if mac_prefix in oui_wireless:
        return "Wireless"
    elif mac_prefix in oui_wired:
        return "Ethernet"
    else:
        return "Unknown"

# Example usage
interface_type = get_mac_type(mac_address)
print(f"The MAC address {mac_address} is associated with a {interface_type} card.")
