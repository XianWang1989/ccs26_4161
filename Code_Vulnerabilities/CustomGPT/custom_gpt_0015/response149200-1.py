
import requests

# Predefined lists of OUIs for Ethernet and Wireless cards
ethernet_ouis = {
    "00:1A:2B", "00:1B:3C", "00:1C:4D",  # Add more OUIs as per your research
}

wireless_ouis = {
    "00:24:D7", "00:15:6D", "B8:27:EB",  # Add more OUIs as per your research
}

def get_card_type(mac_address):
    # Normalize MAC address
    mac_address = mac_address.upper()
    oui = mac_address[:8]  # Get the OUI part of the MAC address

    if oui in ethernet_ouis:
        return "Ethernet card"
    elif oui in wireless_ouis:
        return "Wireless card"
    else:
        return "Unknown card type"

# Example usage:
mac = "00:1A:2B:3C:4D:5E"
card_type = get_card_type(mac)
print(f"The MAC address {mac} is associated with a {card_type}.")
