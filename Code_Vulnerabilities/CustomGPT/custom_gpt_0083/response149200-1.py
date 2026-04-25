
import requests

# Sample OUI lists (these should be expanded for more accuracy)
WIRELESS_OUIS = [
    # Add known wireless OUI prefixes
    "00:1A:2B", "00:1E:4F", "00:24:D7"
]
ETHERNET_OUIS = [
    # Add known Ethernet OUI prefixes
    "00:14:22", "00:05:5D", "00:01:6C"
]

def get_device_type(mac):
    # Normalize MAC address
    mac = mac.upper()
    for oui in WIRELESS_OUIS:
        if mac.startswith(oui):
            return "Wireless Card"
    for oui in ETHERNET_OUIS:
        if mac.startswith(oui):
            return "Ethernet Card"
    return "Unknown"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
device_type = get_device_type(mac_address)
print(f"The device with MAC {mac_address} is connected via: {device_type}")

# Optionally, you can use a public API to get the manufacturer's info
def get_manufacturer(mac):
    api_url = f"https://api.macvendors.com/{mac.replace(':', '')}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.text
    return "Manufacturer not found"

# Get manufacturer information
manufacturer = get_manufacturer(mac_address)
print(f"Manufacturer: {manufacturer}")
