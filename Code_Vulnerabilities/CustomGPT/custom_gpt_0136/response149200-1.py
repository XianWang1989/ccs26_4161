
import subprocess
import json

def get_mac_info(mac_address):
    # Get vendor info using an external API (e.g. macvendors.com)
    try:
        result = subprocess.check_output(
            ['curl', '-s', f'https://api.macvendors.com/{mac_address}']
        )
        return result.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        return None

def identify_card_type(mac_address):
    vendor = get_mac_info(mac_address)

    if vendor:
        # Simple keyword check (you may refine this list)
        if "wireless" in vendor.lower() or "wifi" in vendor.lower():
            return "Wireless Card"
        elif "ethernet" in vendor.lower() or "wired" in vendor.lower():
            return "Ethernet Card"
        else:
            return "Unknown Card Type"
    return "Vendor Not Found"

# Example MAC address
mac_address = "00:1A:2B:3C:4D:5E"
card_type = identify_card_type(mac_address)
print(f"The MAC address {mac_address} is associated with a: {card_type}")
