
import requests

# Sample OUI lists (in practice, use a comprehensive list)
WIFI_OUIS = {
    '00:1A:2B', '00:1C:DF', '00:24:D7', # Add more OUI for wireless cards
}

ETHERNET_OUIS = {
    '00:0A:E6', '00:1C:42', '00:1D:A1', # Add more OUI for Ethernet cards
}

def get_oui(mac):
    return mac[:8].upper()  # Get the first three octets

def determine_interface_type(mac):
    oui = get_oui(mac)

    if oui in WIFI_OUIS:
        return "Wireless"
    elif oui in ETHERNET_OUIS:
        return "Ethernet"
    else:
        return "Unknown"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
interface_type = determine_interface_type(mac_address)
print(f"The MAC address {mac_address} is associated with: {interface_type}")
