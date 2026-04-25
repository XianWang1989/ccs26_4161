
import requests

def get_mac_info(mac):
    """Gets information about the MAC address using an OUI lookup."""
    url = f"https://api.oui.io/v1/lookup/{mac[:8].upper()}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def classify_mac_type(mac):
    """Classifies the MAC address as Ethernet or Wireless."""
    mac_info = get_mac_info(mac)

    if mac_info:
        vendor = mac_info.get('vendor', '')

        # Assuming you have a list of known wireless and Ethernet vendors
        wireless_vendors = ['NETGEAR', 'LINKSYS', 'TP-LINK', 'APPLE']
        ethernet_vendors = ['HUAWEI', 'D-LINK', 'CISCO', 'BELKIN']

        if any(vendor.startswith(wv) for wv in wireless_vendors):
            return 'Wireless Card'
        elif any(vendor.startswith(ev) for ev in ethernet_vendors):
            return 'Ethernet Card'
        else:
            return 'Unknown Type'
    return 'Lookup Failed'

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
card_type = classify_mac_type(mac_address)
print(f"The MAC address {mac_address} is associated with: {card_type}")
