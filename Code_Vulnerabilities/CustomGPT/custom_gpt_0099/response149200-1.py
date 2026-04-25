
import requests

def get_oui_info(mac_address):
    """
    Get OUI information from MAC address.
    """
    try:
        response = requests.get(f'https://api.macaddress.io/v1?apiKey=<YOUR_API_KEY>&output=json&search={mac_address}')
        data = response.json()
        return data['vendorDetails'] if 'vendorDetails' in data else None
    except Exception as e:
        print(f"Error fetching OUI info: {e}")
        return None

def determine_interface_type(mac_address):
    oui_info = get_oui_info(mac_address)
    if oui_info:
        manufacturer = oui_info.get('companyName', 'Unknown')
        # Example list of wireless and ethernet manufacturers
        wireless_manufacturers = ['Intel', 'Cisco', 'TP-Link', 'Netgear']
        ethernet_manufacturers = ['Realtek', 'Broadcom', 'Qualcomm']

        for manufacturer in wireless_manufacturers:
            if manufacturer in oui_info['companyName']:
                return "Wireless Card"

        for manufacturer in ethernet_manufacturers:
            if manufacturer in oui_info['companyName']:
                return "Ethernet Card"

    return "Unknown Interface Type"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
interface_type = determine_interface_type(mac_address)
print(f"The MAC address {mac_address} is associated with a: {interface_type}")
