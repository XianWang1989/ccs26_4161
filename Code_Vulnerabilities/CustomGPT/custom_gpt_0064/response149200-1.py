
# OUI database sample (you can expand this with real data)
oui_database = {
    "00:1A": "Ethernet",
    "00:1B": "Wifi",
    "00:1C": "Wifi",
    "00:1D": "Ethernet",
    "00:1E": "Ethernet",
    "00:1F": "Wifi"
}

def get_device_type(mac_address):
    # Extract the first three octets (OUI)
    oui = mac_address.upper()[:8]  # Format: XX:XX:XX
    # Check the OUI in the database
    return oui_database.get(oui, "Unknown")

# Example MAC addresses
mac_addresses = [
    "00:1A:2B:3C:4D:5E",
    "00:1B:2A:3C:4D:5F",
]

for mac in mac_addresses:
    device_type = get_device_type(mac)
    print(f"MAC Address: {mac} is likely a {device_type} device.")
