
import requests

def get_oui_info(oui):
    # Use an external API to get OUI information
    response = requests.get(f"https://api.macvendors.com/{oui}")

    if response.status_code == 200:
        return response.json()
    return None

def identify_card_type(mac_address):
    # Format the MAC address
    oui = mac_address[:8].upper()

    # Fetch OUI information
    info = get_oui_info(oui)
    if info:
        # A simple assumption based on the manufacturers
        manufacturer = info.get("result", "")
        if "wireless" in manufacturer.lower():
            return 'Wireless Card'
        elif "ethernet" in manufacturer.lower() or "wired" in manufacturer.lower():
            return 'Ethernet Card'
    return 'Unknown Card Type'

# Example MAC address
mac = "00:1A:2B:3C:4D:5E"
card_type = identify_card_type(mac)
print(f"The card type for MAC address {mac} is: {card_type}")
