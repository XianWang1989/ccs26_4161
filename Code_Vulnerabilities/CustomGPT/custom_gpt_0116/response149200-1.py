
import requests

def get_mac_info(mac):
    """Get MAC address information."""
    # Assuming MAC address is in the format XX:XX:XX:XX:XX:XX
    oui = mac.upper()[:8]  # Take the first 8 characters (first 3 bytes)

    # A simple list of known OUIs for Ethernet and Wireless
    ethernet_ouis = {
        '00:1A:2B', '00:3C:9F', '00:0C:29',  # Add more known Ethernet OUIs here
    }

    wireless_ouis = {
        '00:1F:33', '00:18:4D', '00:0C:41',  # Add more known Wireless OUIs here
    }

    if oui in ethernet_ouis:
        return 'Ethernet Card'
    elif oui in wireless_ouis:
        return 'Wireless Card'
    else:
        return 'Unknown'

# Example usage
mac_address = '00:1A:2B:3C:4D:5E'
card_type = get_mac_info(mac_address)
print(f'The card type for MAC {mac_address} is: {card_type}')
