
import requests

# Function to get OUI information from an online database
def get_oui_info(mac_address):
    try:
        # Extract the first three octets (OUI) of the MAC address
        oui = mac_address[:8].upper()  # Format: 'XX:XX:XX'
        response = requests.get(f'https://api.macaddress.io/v1?apiKey=YOUR_API_KEY&output=json&search={oui}')
        data = response.json()
        return data.get('vendorDetails', {}).get('company', 'Unknown')
    except Exception as e:
        print(f"Error fetching OUI info: {e}")
        return None

# Check if a MAC address is likely for Ethernet or Wireless
def check_card_type(mac_address):
    vendor = get_oui_info(mac_address)
    if vendor:
        # Define common manufacturers for wireless and Ethernet cards
        wireless_vendors = ['Apple', 'Atheros', 'Broadcom', 'Intel', 'Cisco']
        ethernet_vendors = ['Realtek', 'Intel', 'Broadcom']

        # Determine card type based on the vendor
        if any(vendor in w for w in wireless_vendors):
            return 'Wireless Card'
        elif any(vendor in e for e in ethernet_vendors):
            return 'Ethernet Card'

    return 'Unknown Card Type'

# Example MAC address for testing
mac = '00:1A:2B:3C:4D:5E'
card_type = check_card_type(mac)
print(f'The card type for MAC address {mac} is: {card_type}')
