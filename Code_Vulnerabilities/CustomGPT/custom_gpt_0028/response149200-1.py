
import requests

# Sample OUI database (you can update/add to this as needed)
oui_database = {
    "00:1A:2B": "Ethernet",        # Example OUI for Ethernet
    "00:1A:2C": "Wireless",        # Example OUI for Wireless
    "00:1B:3C": "Wireless",
    "00:1B:4D": "Ethernet",
}

def get_device_type(mac):
    # Normalize MAC address format
    mac = mac.upper()
    mac_prefix = mac[:8]  # Get the first 8 characters (OUI)

    # Check if the OUI is in the database
    device_type = oui_database.get(mac_prefix, "Unknown")

    return device_type

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
device_type = get_device_type(mac_address)

print(f"The device type for MAC address {mac_address} is: {device_type}")
