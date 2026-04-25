
import requests

def get_mac_info(mac_address):
    # Clean the MAC address
    mac = mac_address.replace(":", "").upper()

    # OUI Lookup URL
    url = f"https://api.macaddress.io/v1?apiKey=at_YOUR_API_KEY&output=json&search={mac}"

    response = requests.get(url)
    data = response.json()

    if 'error' in data:
        return "Invalid MAC address or not found."

    # Extract OUI information
    oui = data['vendorDetails']['oui']
    vendor = data['vendorDetails']['companyName']

    # Determine the type of card
    if "wireless" in vendor.lower() or "wifi" in vendor.lower():
        card_type = "Wireless Card"
    else:
        card_type = "Ethernet Card"

    return {
        "MAC Address": mac_address,
        "OUI": oui,
        "Vendor": vendor,
        "Card Type": card_type
    }

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
result = get_mac_info(mac_address)
print(result)
