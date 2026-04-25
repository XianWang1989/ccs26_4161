
import getmac
import requests

def get_card_type(mac):
    # Get the OUI from the MAC address
    oui = mac[:8].upper()
    url = f'https://api.thepowerbase.com/api/v1/ouis/{oui}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Check the category of the vendor
        if 'vendor' in data:
            vendor_info = data['vendor'].lower()
            if 'wireless' in vendor_info or 'wifi' in vendor_info:
                return "Wireless Card"
            else:
                return "Ethernet Card"
        else:
            return "Unknown Card Type"

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
card_type = get_card_type(mac_address)
print(f"The card type for MAC {mac_address} is: {card_type}")
