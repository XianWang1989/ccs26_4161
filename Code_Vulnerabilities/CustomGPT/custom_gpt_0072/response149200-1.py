
import requests

# Example lists of known OUIs (can be updated with real data)
wireless_oui_list = [
    "00:1A:2B",  # Example wireless OUI
    "00:1C:DF",
    # Add other known wireless OUIs
]

ethernet_oui_list = [
    "00:1A:3F",  # Example Ethernet OUI
    "00:1E:C0",
    # Add other known Ethernet OUIs
]

def get_device_type(mac_address):
    """Determine if the MAC address belongs to a wireless or Ethernet card."""
    oui = ":".join(mac_address.split(":")[:3])  # Get the first three octets
    if oui in wireless_oui_list:
        return "Wireless"
    elif oui in ethernet_oui_list:
        return "Ethernet"
    else:
        return "Unknown"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"  # Example MAC address
device_type = get_device_type(mac_address)
print(f"The device type for MAC {mac_address} is: {device_type}")
