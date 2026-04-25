
from get_mac_address import get_mac_info

def is_wireless_or_ethernet(mac_address):
    mac_info = get_mac_info(mac_address)

    if mac_info and 'category' in mac_info:
        if mac_info['category'] == 'Wireless':
            return "Wireless Card"
        elif mac_info['category'] == 'Ethernet':
            return "Ethernet Card"
    return "Unknown Card Type"

# Example usage:
mac_address = "00:1A:2B:3C:4D:5E"
card_type = is_wireless_or_ethernet(mac_address)
print(f"The card type for MAC {mac_address} is: {card_type}")
