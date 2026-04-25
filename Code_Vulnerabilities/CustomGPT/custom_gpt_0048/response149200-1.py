
import requests

# Sample OUI database
# In a real application, this should be more comprehensive.
known_wireless_ouis = {
    "00:1A:2B",  # Example OUI for wireless
    "00:1B:44",  # Another example
}

known_ethernet_ouis = {
    "00:1C:B3",  # Example OUI for Ethernet
    "00:1D:A1",  # Another example
}

def get_oui(mac_address):
    return mac_address[:8].upper()  # Get the first 3 bytes

def identify_card_type(mac_address):
    oui = get_oui(mac_address)

    if oui in known_wireless_ouis:
        return "Wireless Card"
    elif oui in known_ethernet_ouis:
        return "Ethernet Card"
    else:
        return "Unknown Card Type"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
card_type = identify_card_type(mac_address)
print(f"The MAC address {mac_address} is associated with: {card_type}")
