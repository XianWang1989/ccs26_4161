
from get_oui import get_oui

def get_network_card_type(mac_address):
    try:
        # Extract OUI from the MAC address
        oui = mac_address[:8]  # First 3 bytes in the MAC address

        # Get OUI details
        details = get_oui(oui)

        # Logic to determine the card type
        if 'wireless' in details.lower():
            return "Wireless Card"
        elif 'ethernet' in details.lower() or 'wired' in details.lower():
            return "Ethernet Card"
        else:
            return "Unknown Card Type"
    except Exception as e:
        return f"Error: {e}"

# Example usage
mac = "00:1A:2B:3C:4D:5E"
card_type = get_network_card_type(mac)
print(f"The MAC address {mac} is associated with: {card_type}")
