
# Dictionary of known OUIs
oui_dict = {
    "00:1A:2B": "Ethernet",
    "00:1A:2C": "Wireless",
    "00:1B:44": "Ethernet",
    "00:1B:57": "Wireless",
    "00:1C:DF": "Wireless",
    # Add more known OUIs as needed
}

def get_oui_type(mac_address):
    # Normalize MAC address
    mac_address = mac_address.upper().replace('-', ':').split(':')
    if len(mac_address) < 3:
        return "Invalid MAC address"

    oui = ':'.join(mac_address[:3])  # Get the OUI (first 3 octets)
    return oui_dict.get(oui, "Unknown OUI")

# Example usage
mac = "00:1A:2B:3C:4D:5E"
card_type = get_oui_type(mac)

print(f"The MAC address {mac} is associated with a {card_type} card.")
