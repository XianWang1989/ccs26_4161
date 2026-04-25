
import requests

def get_oui_details(mac_address):
    # Strip any formatting from MAC address
    clean_mac = mac_address.replace(":", "").replace("-", "").upper()[:6]

    # Fetch OUI data
    url = f"https://api.maclookup.app/api/v2/macs/{clean_mac}"
    response = requests.get(url).json()

    return response

def identify_interface_type(mac_address):
    oui_details = get_oui_details(mac_address)

    # Check if the API call was successful
    if oui_details.get('success'):
        device_type = oui_details.get('vendor_details', {}).get('type')
        print(f"MAC Address: {mac_address}")
        print(f"Vendor: {oui_details['vendor_details']['company']}")
        print(f"Device Type: {device_type}")

        # Check interface type based on common categorizations
        if 'wireless' in device_type.lower():
            return "Wireless Card"
        elif 'ethernet' in device_type.lower() or 'wired' in device_type.lower():
            return "Ethernet Card"
    else:
        print("Error fetching OUI details.")
        return None

# Example MAC address
mac_address = "00:1A:2B:3C:4D:5E"
interface_type = identify_interface_type(mac_address)
print(f"Interface Type: {interface_type}")
