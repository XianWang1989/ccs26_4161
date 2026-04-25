
import requests

def get_mac_info(mac_address):
    # Normalize the MAC address
    mac_address = mac_address.replace(":", "").replace("-", "").upper()

    # OUI Lookup URL
    url = f"https://api.macaddress.io/v1?apiKey=YOUR_API_KEY&output=json&search={mac_address}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        vendor = data.get('vendorDetails', {}).get('orgName', 'Unknown')
        return vendor
    else:
        return None

def determine_card_type(vendor):
    # List of known wireless vendors
    wireless_vendors = [
        "Apple", "Cisco", "Intel",
        "Netgear", "TP-Link", "D-Link", 
        # Add other known vendors as needed
    ]

    if any(v in vendor for v in wireless_vendors):
        return "Wireless Card"
    else:
        return "Ethernet Card"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
vendor = get_mac_info(mac_address)

if vendor:
    card_type = determine_card_type(vendor)
    print(f"MAC Address: {mac_address} is associated with a {card_type}.")
else:
    print("Vendor information not found.")
