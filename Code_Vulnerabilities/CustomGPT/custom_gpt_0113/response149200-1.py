
import requests

# Mock OUI database
oui_database = {
    "00:1A:2B": "Ethernet",
    "00:1B:3C": "Wi-Fi",
    "00:1C:4D": "Unknown",
    # Add more OUI mappings here
}

def get_device_type(mac_address):
    # Format MAC address to uppercase and split into OUI
    oui = mac_address.upper()[:8]  # Get the first 8 characters (OUI)

    # Check if OUI exists in our database
    device_type = oui_database.get(oui, "Unknown")
    return device_type

# Example MAC addresses
mac_addresses = [
    "00:1A:2B:4C:5D:6E",  # Ethernet
    "00:1B:3C:7D:8E:9F",  # Wi-Fi
    "00:1C:4D:1E:2F:3A"   # Unknown
]

for mac in mac_addresses:
    print(f"MAC Address: {mac} -> Device Type: {get_device_type(mac)}")
