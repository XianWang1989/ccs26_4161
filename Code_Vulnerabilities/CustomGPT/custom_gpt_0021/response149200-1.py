
import requests

def get_card_type(mac_address):
    # Validate MAC address format
    if not validate_mac(mac_address):
        return "Invalid MAC address format."

    # Extract OUI (first 3 bytes)
    oui = mac_address.upper().replace(":", "")[:6]

    # OUI lookup URL
    url = f"https://api.macvendors.com/{oui}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        # Get the vendor details
        vendor_info = response.text
        if "wireless" in vendor_info.lower():
            return "Wireless Card"
        elif "ethernet" in vendor_info.lower():
            return "Ethernet Card"
        else:
            return "Unknown or Unclassified Card Type"

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def validate_mac(mac):
    # Basic MAC address format validation
    import re
    return bool(re.match(r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", mac))

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
card_type = get_card_type(mac_address)
print(f"The card type for {mac_address} is: {card_type}")
