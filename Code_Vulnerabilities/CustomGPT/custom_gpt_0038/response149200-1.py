
import requests

def get_mac_details(mac_address):
    url = f"https://api.macaddress.io/v1?apiKey=YOUR_API_KEY&output=json&search={mac_address}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        vendor = data.get("vendorDetails", {}).get("companyName", "Unknown")
        if "Wireless" in vendor:
            return "Wireless Card"
        else:
            return "Ethernet Card"
    else:
        return "Error fetching MAC details"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"  # Replace with your MAC address
card_type = get_mac_details(mac_address)
print(f"The card type for MAC address {mac_address} is: {card_type}")
