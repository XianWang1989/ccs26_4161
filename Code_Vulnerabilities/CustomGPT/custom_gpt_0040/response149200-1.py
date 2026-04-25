
import requests

def get_oui_info(mac_address):
    # Get the first three octets from the MAC address
    oui_prefix = mac_address[:8]

    # OUI database URL (this is a sample URL, use a real database in production)
    oui_db_url = f"https://api.macaddress.io/v1?apiKey=YOUR_API_KEY&output=json&search={oui_prefix}"

    response = requests.get(oui_db_url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def is_wireless_or_ethernet(mac_address):
    info = get_oui_info(mac_address)

    if info and 'vendorDetails' in info:
        manufacturer = info['vendorDetails']['companyName']
        # Check typical patterns for wireless and Ethernet
        if "wireless" in manufacturer.lower():
            return "Wireless Card"
        elif "ethernet" in manufacturer.lower() or "network" in manufacturer.lower():
            return "Ethernet Card"

    return "Unknown Card Type"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
card_type = is_wireless_or_ethernet(mac_address)
print(f"The card type for {mac_address} is: {card_type}")
