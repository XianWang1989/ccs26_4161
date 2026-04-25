
import requests

def get_mac_vendor(mac_address):
    # Convert MAC address to the OUI format
    oui = mac_address[:8].upper()  # First 6 characters (3 octets)

    # OUI lookup through an online API
    response = requests.get(f"https://api.macvendors.com/{oui}")
    if response.status_code == 200:
        return response.json().get('result', '')
    return ''

def check_card_type(mac_address):
    vendor = get_mac_vendor(mac_address)
    wireless_vendors = ['INTEL', 'LINKSYS', 'TP-LINK', 'BELKIN', 'NETGEAR']
    ethernet_vendors = ['REALTEK', 'MARVELL', 'Atheros', 'Broadcom']

    for vendor_name in wireless_vendors:
        if vendor_name in vendor.upper():
            return 'Wireless Card'

    for vendor_name in ethernet_vendors:
        if vendor_name in vendor.upper():
            return 'Ethernet Card'

    return 'Unknown'

# Example usage
mac = '00:1A:2B:3C:4D:5E'
card_type = check_card_type(mac)
print(f'The MAC address {mac} is associated with: {card_type}')
