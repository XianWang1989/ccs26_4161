
import requests

def get_mac_info(mac_address):
    # Format MAC address
    mac_address = mac_address.replace(":", "").upper()
    oui = mac_address[:6]  # First 6 characters (3 bytes)

    # Use macaddress.io API to fetch details
    response = requests.get(f"https://api.macaddress.io/v1?apiKey=YOUR_API_KEY&output=json&search={oui}")

    if response.status_code == 200:
        data = response.json()
        return data.get('data')
    else:
        return None

def classify_device(mac_details):
    if mac_details:
        # Check for common wireless or Ethernet indicators
        if 'wireless' in mac_details.get('type', '').lower():
            return "This MAC address belongs to a wireless card."
        elif 'ethernet' in mac_details.get('type', '').lower():
            return "This MAC address belongs to an Ethernet card."
        else:
            return "Device type unclear."
    return "MAC address information not found."

# Example usage
mac = "00:1A:2B:3C:4D:5E"
mac_info = get_mac_info(mac)
device_type = classify_device(mac_info)
print(device_type)
