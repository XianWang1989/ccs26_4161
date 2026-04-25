
import requests

def get_device_type(mac_address):
    # Strip any hyphens or colons from the MAC address
    mac_address = mac_address.replace('-', '').replace(':', '').upper()

    # Ensure the MAC address is 6 bytes
    if len(mac_address) != 12:
        raise ValueError("Invalid MAC address format. Should be 12 hex digits.")

    # Extract the OUI (first 6 characters)
    oui = mac_address[:6]

    # You can use a public API to get manufacturer info
    response = requests.get(f'https://api.macaddress.io/v1?apiKey=YOUR_API_KEY_HERE&output=json&search={oui}')

    if response.status_code == 200:
        data = response.json()
        company = data.get('vendorDetails', {}).get('companyName', 'Unknown')

        # Example logic: You can refine the logic based on known manufacturers
        wireless_manufacturers = ['Apple', 'Intel', 'Atheros', 'Broadcom', 'Qualcomm']
        ethernet_manufacturers = ['Realtek', 'Marvell', 'Asus', 'TP-LINK']

        if any(manufacturer in company for manufacturer in wireless_manufacturers):
            return 'Wireless Card'
        elif any(manufacturer in company for manufacturer in ethernet_manufacturers):
            return 'Ethernet Card'
        else:
            return 'Unknown type'

    else:
        return 'Error accessing MAC address database'

# Example usage
mac = "00:1A:2B:3C:4D:5E"
device_type = get_device_type(mac)
print(f"The MAC address {mac} is likely to be from a {device_type}.")
