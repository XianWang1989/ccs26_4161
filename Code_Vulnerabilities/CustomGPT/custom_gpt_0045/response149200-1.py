
import re

# Sample OUI database (for demonstration)
# Normally, you would use a complete database or an API for this purpose.
oui_database = {
    "00:1A:2B": "Ethernet",
    "00:1A:2C": "Wireless",
    "00:1A:2D": "Wireless",
    "00:1A:2E": "Ethernet",
    # Add more known OUIs as needed
}

def get_card_type(mac_address):
    # Validate MAC address format
    if not re.match("^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", mac_address):
        return "Invalid MAC address format"

    # Extract the OUI (first three octets)
    oui = mac_address[:8]  # Extracts first 8 characters (e.g., "00:1A:2B")

    # Lookup the type in OUI database
    card_type = oui_database.get(oui.upper(), "Unknown OUI")

    return card_type

# Example usage
mac_address = "00:1A:2B:03:04:05"
card_type = get_card_type(mac_address)
print(f"The card type for MAC address {mac_address} is: {card_type}")
