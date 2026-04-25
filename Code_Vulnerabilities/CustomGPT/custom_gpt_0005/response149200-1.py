
import requests
from getmac import get_mac_address

def get_oui(mac_address):
    # Retrieve OUI from an online database
    oui_url = f"https://api.macaddress.io/v1?apiKey=at_your_api_key&output=json&search={mac_address}"
    response = requests.get(oui_url)
    data = response.json()
    return data['vendorDetails']['oui'] if 'vendorDetails' in data else None

def classify_mac(mac_address):
    oui = get_oui(mac_address)
    if oui:
        # Example conditions (customize this based on the OUI data you gather)
        wireless_ouis = ['00:1A:2B', '00:1C:DF']  # Add known wireless OUIs
        ethernet_ouis = ['00:1D:8D', '00:1E:C2']  # Add known Ethernet OUIs

        if any(oui.startswith(w) for w in wireless_ouis):
            return "Wireless Card"
        elif any(oui.startswith(e) for e in ethernet_ouis):
            return "Ethernet Card"
        else:
            return "Unknown Type"
    return "Invalid MAC Address"

# Example usage
mac = get_mac_address()  # Replace with your MAC address
card_type = classify_mac(mac)
print(f"The MAC address {mac} is classified as: {card_type}")
