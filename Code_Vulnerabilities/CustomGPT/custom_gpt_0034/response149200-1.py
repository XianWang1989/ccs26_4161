
import requests

def get_mac_details(mac_address):
    # Format MAC address
    mac_address = mac_address.replace(":", "").upper()[:6]
    url = f"https://api.macvendors.com/{mac_address}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return "Unknown manufacturer"
    except requests.RequestException as e:
        return f"Error: {e}"

def determine_device_type(mac_address):
    manufacturer = get_mac_details(mac_address)

    # List of known manufacturers for wireless adapters
    wireless_makers = [
        "Apple", "Intel", "Broadcom", "Atheros", "Realtek", "Qualcomm", 
        "TP-Link", "Netgear"
    ]

    for maker in wireless_makers:
        if maker in manufacturer:
            return "Wireless Card detected"

    return "Ethernet Card or Unknown type"

# Example usage
mac = "00:1A:2B:3C:4D:5E"  # Replace with your MAC address
device_type = determine_device_type(mac)
print(device_type)
