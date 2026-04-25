
import requests

def get_mac_info(mac_address):
    # Format MAC address
    mac = mac_address.replace(":", "").upper()

    # Request MAC address information from an API
    url = f"https://api.macvendors.com/{mac}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def is_wireless(mac_info):
    # Known wireless manufacturers (this is a simplified list; you may expand it)
    wireless_ouls = [
        "00:0A:95",  # Example OUI for wireless devices
        "00:1A:2B",  # Expand with more known OUIs
        # Add more known wireless OUIs
    ]

    # Check if OUI is in known wireless manufacturers
    oui = mac_info['mac_address'][:8].upper()  # First 8 characters
    return oui in wireless_ouls

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
mac_info = get_mac_info(mac_address)

if mac_info:
    if is_wireless(mac_info):
        print(f"{mac_address} is likely a wireless card.")
    else:
        print(f"{mac_address} is likely an Ethernet card.")
else:
    print("MAC address information not found.")
