
import requests

def get_mac_info(mac_address):
    # Format MAC address for API
    mac_formatted = mac_address.replace(':', '').upper()
    api_url = f'https://api.macvendors.com/{mac_formatted}'

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            vendor_info = response.text
            print(f'MAC Address: {mac_address} is associated with vendor: {vendor_info}')
            return vendor_info
        else:
            print(f'Could not retrieve information for MAC address: {mac_address}')
    except Exception as e:
        print(f'Error occurred: {e}')

def determine_card_type(vendor_info):
    wireless_vendors = [
        "Atheros", "Broadcom", "Intel", "Realtek", "Qualcomm", "TP-LINK"  # Add more as needed
    ]
    ethernet_vendors = [
        "Intel", "Realtek", "Broadcom", "Marvell", "TP-LINK"  # Add more as needed
    ]

    if any(vendor in vendor_info for vendor in wireless_vendors):
        return "Wireless Card"
    elif any(vendor in vendor_info for vendor in ethernet_vendors):
        return "Ethernet Card"
    else:
        return "Unknown Type"

# Example usage
mac_address = '00:14:22:01:23:45'
vendor_info = get_mac_info(mac_address)

if vendor_info:
    card_type = determine_card_type(vendor_info)
    print(f'The card type for MAC {mac_address} is: {card_type}')
