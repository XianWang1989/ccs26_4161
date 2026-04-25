
import re

# Sample data for demonstration purposes
known_wifi_ouis = [
    "00:1A:2B",  # Example OUI for wireless
    "00:1E:84",  # Example OUI for wireless
]

known_ethernet_ouis = [
    "00:0C:29",  # Example OUI for wired
    "00:50:56",  # Example OUI for wired
]

def get_device_type(mac_address):
    # Ensure valid MAC address format
    if not re.match(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', mac_address):
        raise ValueError("Invalid MAC address format")

    # Get OUI from the MAC address
    oui = mac_address[:8].upper()  # e.g. "00:1A:2B"

    # Determine device type
    if oui in known_wifi_ouis:
        return "Wireless"
    elif oui in known_ethernet_ouis:
        return "Ethernet"
    else:
        return "Unknown"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
device_type = get_device_type(mac_address)
print(f"The device with MAC address {mac_address} is of type: {device_type}")
