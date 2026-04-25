
import requests

def get_mac_info(mac_address):
    """Fetch MAC address information using the MAC address."""
    url = f'https://api.macvendors.com/{mac_address}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def identify_card_type(mac_address):
    """Determine if MAC address is likely to be associated with an Ethernet or Wireless card."""
    # Fetch MAC info from external API
    vendor_info = get_mac_info(mac_address)

    if vendor_info:
        vendor = vendor_info.get('vendor', '')
        if 'wireless' in vendor.lower() or 'wifi' in vendor.lower():
            return "Wireless Card"
        else:
            return "Ethernet Card"
    else:
        return "Unknown vendor or failed to retrieve info"

# Example usage
mac = "00:1A:2B:3C:4D:5E"
card_type = identify_card_type(mac)
print(f"The MAC address {mac} is associated with a: {card_type}")
