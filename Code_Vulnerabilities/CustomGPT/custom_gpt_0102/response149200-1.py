
import requests

def get_vendor(mac_address):
    # Format MAC address
    mac_address = mac_address.replace(":", "").replace("-", "").upper()
    url = f"https://api.macvendors.com/{mac_address}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['result']
        else:
            return None
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def determine_card_type(mac_address):
    vendor = get_vendor(mac_address)

    if vendor:
        wireless_keywords = ['WIFI', 'WIRELESS', 'BLUETOOTH']
        if any(keyword in vendor.upper() for keyword in wireless_keywords):
            return "Wireless Card"
        else:
            return "Ethernet Card"
    else:
        return "Vendor not found"

# Example usage
mac = "00:1A:2B:3C:4D:5E"
card_type = determine_card_type(mac)
print(f"The card type for MAC address {mac} is: {card_type}")
