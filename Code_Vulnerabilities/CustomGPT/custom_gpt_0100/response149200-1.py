
import requests

# Function to get MAC address type
def get_mac_type(mac_address):
    # Extract the OUI from the MAC address (first 3 octets)
    oui = mac_address[:8].upper()  # e.g., '00:1A:2B'

    # Use a public API to fetch manufacturer data
    response = requests.get(f'https://api.macvendors.com/{mac_address}')

    if response.status_code == 200:
        vendor_info = response.json()
        vendor = vendor_info.get('result', {}).get('company', 'Unknown')

        # Check for common wireless vs. Ethernet vendor types
        wireless_vendors = ['Atheros', 'Broadcom', 'Intel']
        ethernet_vendors = ['Realtek', 'Intel', 'Marvell']

        if any(vendor in vendor_info['result'] for vendor in wireless_vendors):
            return "Wireless"
        elif any(vendor in vendor_info['result'] for vendor in ethernet_vendors):
            return "Ethernet"
        else:
            return "Unknown"
    else:
        return "Error fetching data"

# Example usage
mac_address = '00:1A:2B:3C:4D:5E'  # Replace with a valid MAC address
mac_type = get_mac_type(mac_address)
print(f'The MAC address {mac_address} is associated with a {mac_type} card.')
