
import requests

def get_device_type(mac_address):
    if not validate_mac(mac_address):
        print("Invalid MAC address format.")
        return None

    oui = mac_address[:8].upper()
    url = f"https://api.macvendors.com/{oui}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            vendor_info = response.json()
            return classify_device(vendor_info)
        else:
            print("OUI lookup failed.")
            return None
    except Exception as e:
        print(f"Error during OUI lookup: {e}")
        return None

def validate_mac(mac):
    return len(mac) == 17 and all(c in '0123456789ABCDEF:' for c in mac)

def classify_device(vendor_info):
    # Example heuristic classification
    wireless_keywords = ['wireless', 'wifi', 'broadband']
    ethernet_keywords = ['ethernet', 'wired', 'network']

    for key in wireless_keywords:
        if key in vendor_info.lower():
            return "Wireless Card"

    for key in ethernet_keywords:
        if key in vendor_info.lower():
            return "Ethernet Card"

    return "Unknown Type"

if __name__ == "__main__":
    mac_address = "XX:XX:XX:XX:XX:XX"  # Replace this with your MAC address
    device_type = get_device_type(mac_address)
    if device_type:
        print(f"The device type for MAC {mac_address} is: {device_type}")
