
import requests

def get_device_type(mac_address):
    # Get the first three octets (OUI) from the MAC address
    ouis = mac_address[:8].upper()

    # Fetch OUI data from a public OUI database
    url = f"https://api.macaddress.io/v1?apiKey=YOUR_API_KEY&output=json&search={ouis}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        manufacturer = data['vendorDetails']['companyName']

        # Lists (examples, should be expanded for more manufacturers)
        wireless_manufacturers = ['Atheros', 'Intel', 'Broadcom']
        ethernet_manufacturers = ['Realtek', 'TP-Link']

        # Determine the type based on the manufacturer
        for wm in wireless_manufacturers:
            if wm in manufacturer:
                return 'Wireless Card'
        for em in ethernet_manufacturers:
            if em in manufacturer:
                return 'Ethernet Card'

        return 'Unknown Type'
    else:
        return 'Error fetching data'

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
device_type = get_device_type(mac_address)
print(f"The device type for MAC {mac_address} is: {device_type}")
