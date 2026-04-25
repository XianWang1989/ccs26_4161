
import subprocess

# Sample mapping of MAC prefixes
mac_prefix_mapping = {
    "00:1A": "Wireless",
    "00:1B": "Ethernet",
    # Additional mappings can be added here
}

def get_card_type(mac_address):
    # Normalize MAC address
    mac_address = mac_address.upper()
    prefix = mac_address[:5]  # Get the first 5 characters (OUI)

    card_type = mac_prefix_mapping.get(prefix, "unknown")

    return card_type

def check_device_type(mac_address):
    card_type = get_card_type(mac_address)
    if card_type == "Wireless":
        return "Likely a laptop"
    elif card_type == "Ethernet":
        return "Likely a workstation"
    else:
        return "Unknown device type"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
device_type = check_device_type(mac_address)
print(f"The device with MAC {mac_address} is: {device_type}")
