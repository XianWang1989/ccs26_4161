
import requests

def get_mac_info(mac_address):
    # Format the MAC address
    oui = mac_address.upper()[:8]  # Take only the first 6 characters
    url = f"https://api.macaddress.io/v1?apiKey=YOUR_API_KEY&output=json&search={oui}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        manufacturer = data.get('vendorDetails', {}).get('companyName', 'Unknown')
        return manufacturer
    else:
        return None

def determine_card_type(mac_address):
    manufacturer = get_mac_info(mac_address)
    if manufacturer:
        # Simple heuristic based on known manufacturers
        if "Wireless" in manufacturer or "Wi-Fi" in manufacturer:
            return "Wireless Card"
        else:
            return "Ethernet Card or Unknown Type"
    else:
        return "Could not retrieve data"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
card_type = determine_card_type(mac_address)
print(f"The MAC address {mac_address} is likely a: {card_type}")
