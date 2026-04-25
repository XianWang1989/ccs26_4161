
import requests

def get_mac_details(mac_address):
    # Extract the first three octets (OUI)
    oui = mac_address.upper()[:8]
    try:
        # Fetch the OUI data from an online database
        response = requests.get(f'https://api.maclookup.app/api/v2/macs/{oui}')
        data = response.json()

        if 'vendor' in data['data']:
            vendor = data['data']['vendor']
            # Example logic: Identify if vendor is typically used for wireless or Ethernet
            wireless_vendors = ['D-Link', 'Linksys', 'Netgear']  # Add more as needed
            ethernet_vendors = ['Cisco', 'Dell', 'HP']  # Add more as needed

            if any(vendor in wireless_vendors for vendor in vendor):
                return "Wireless Card"
            elif any(vendor in ethernet_vendors for vendor in vendor):
                return "Ethernet Card"
            else:
                return "Unknown Type"
        else:
            return "Vendor not found"
    except Exception as e:
        return str(e)

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"  # Example MAC address
card_type = get_mac_details(mac_address)
print(f"The MAC address {mac_address} is likely a: {card_type}")
