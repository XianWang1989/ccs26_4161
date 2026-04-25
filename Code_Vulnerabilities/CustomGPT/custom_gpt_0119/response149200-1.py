
import requests

def get_oui_type(mac_address):
    # Extract the OUI (first 6 characters of the MAC address)
    oui = mac_address[:8].upper()

    # Use an OUI lookup API (e.g. macvendors.com)
    url = f"https://api.macvendors.com/{oui}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            manufacturer = response.text
            print(f"Manufacturer: {manufacturer}")
            # Check if the manufacturer is associated with wireless devices
            wireless_manufacturers = ["Atheros", "Broadcom", "Intel", "Realtek"]
            if any(man in manufacturer for man in wireless_manufacturers):
                return "Wireless Card"
            else:
                return "Ethernet Card"
        else:
            print("OUI not found.")
            return "Unknown Type"
    except Exception as e:
        print(f"Error: {e}")
        return "Error fetching OUI data"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
card_type = get_oui_type(mac_address)
print(f"The card type for MAC {mac_address} is: {card_type}")
