
import requests

def get_mac_info(mac_address):
    # Remove any non-hexadecimal characters
    mac = mac_address.replace(":", "").replace("-", "").upper()

    # Get OUI from the MAC address
    oui = mac[:6]

    # Use an online OUI database
    url = f"https://api.maclookup.app/v2/macs/{oui}"

    try:
        response = requests.get(url)
        data = response.json()

        if data['found']:
            return data['vendor_details']
        else:
            return "No details found for this MAC address."
    except Exception as e:
        return f"Error: {e}"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
info = get_mac_info(mac_address)
print(info)
