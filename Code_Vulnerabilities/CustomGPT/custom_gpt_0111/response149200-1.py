
import requests

def get_mac_info(mac_address):
    url = f"https://api.macvendors.com/{mac_address}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        return None

def determine_card_type(mac_address):
    vendor_info = get_mac_info(mac_address)

    if vendor_info:
        # A basic heuristic can be applied based on known vendors
        wireless_vendors = ['Apple', 'Intel', 'Broadcom']
        ethernet_vendors = ['Realtek', 'Intel', 'Cisco']

        for vendor in wireless_vendors:
            if vendor in vendor_info:
                return "Wireless Card"

        for vendor in ethernet_vendors:
            if vendor in vendor_info:
                return "Ethernet Card"

        return "Unknown Card Type"
    else:
        return "MAC Address not found"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"  # Example MAC address
card_type = determine_card_type(mac_address)
print(f"The card type for MAC address {mac_address} is: {card_type}")
