
import requests

def get_mac_address_info(mac_address):
    # Use an online OUI database to fetch information
    url = f"https://api.macaddress.io/v1?apiKey=YOUR_API_KEY&output=json&search={mac_address}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def determine_card_type(mac_address):
    info = get_mac_address_info(mac_address)

    if info and 'vendorDetails' in info:
        vendor = info['vendorDetails']['companyName']
        print(f"MAC Address: {mac_address}, Vendor: {vendor}")

        # Here you can add specific conditions based on vendor signature
        if "Wireless" in vendor:
            return "Wireless Card"
        else:
            return "Ethernet Card"
    else:
        return "Unknown"

# Example usage
mac = "00:1A:2B:3C:4D:5E"  # Replace with actual MAC address
card_type = determine_card_type(mac)
print(f"Card Type: {card_type}")
