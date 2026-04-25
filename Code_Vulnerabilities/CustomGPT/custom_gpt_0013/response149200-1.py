
import requests

def get_mac_details(mac_address):
    # Normalize MAC address format
    mac_address = mac_address.replace(":", "").upper()

    # API to get MAC address details
    url = f'https://api.macaddress.io/v1?apiKey=YOUR_API_KEY&output=json&search={mac_address}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['vendorDetails']['companyName'], data['vendorDetails']['cage']
    else:
        print("Error fetching MAC details")
        return None, None

def identify_card_type(mac_address):
    company_name, cage = get_mac_details(mac_address)

    wireless_vendors = [
        "Atheros", "Broadcom", "Cisco", "Intel", "Realtek"
    ]  # Add common wireless vendors

    ethernet_vendors = [
        "Intel", "Broadcom", "Realtek"
    ]  # Add common ethernet vendors

    if company_name:
        if any(vendor in company_name for vendor in wireless_vendors):
            return "Wireless Card"
        elif any(vendor in company_name for vendor in ethernet_vendors):
            return "Ethernet Card"
        else:
            return "Unknown Card Type"
    return "Error retrieving information"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"  # Replace with actual MAC address
card_type = identify_card_type(mac_address)
print(f"MAC Address {mac_address} is connected through: {card_type}")
