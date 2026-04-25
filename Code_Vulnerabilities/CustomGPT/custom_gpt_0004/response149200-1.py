
import requests

def get_oui_details(mac_address):
    # Clean the MAC address
    mac = mac_address.replace(":", "").replace("-", "").upper()[:6]

    # OUI lookup API
    url = f"https://api.maclookup.app/v2/macs/{mac}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'vendor_details' in data:
            vendor = data['vendor_details']['company']
            category = data['vendor_details']['type']
            return vendor, category
        else:
            return None, "OUI not found"
    else:
        return None, "Error fetching data"

# Example MAC Address
mac_address = "00:1A:2B:3C:4D:5E"
vendor, category = get_oui_details(mac_address)

if category:
    print(f"Vendor: {vendor}, Type: {category}")
    if "wireless" in category.lower():
        print("This is likely a wireless card.")
    elif "ethernet" in category.lower():
        print("This is likely an Ethernet card.")
    else:
        print("Unknown type of network card.")
