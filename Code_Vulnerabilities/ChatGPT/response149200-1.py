
import requests

def is_wireless_card(mac_address):
    # Format MAC address (remove non-alphanumerics and convert to uppercase)
    formatted_mac = mac_address.replace(':', '').replace('-', '').upper()

    # Validate MAC address
    if len(formatted_mac) != 12:
        return None  # Invalid MAC address format

    # Use an API to get manufacturer details
    url = f"https://api.macaddress.io/v1?apiKey=YOUR_API_KEY&output=json&search={formatted_mac}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        manufacturer = data.get("vendorDetails", {}).get("companyName", "")

        # Example logic to determine if it's likely a wireless card
        wireless_manufacturers = ['Apple', 'Intel', 'Qualcomm', 'Broadcom', 'Atheros']

        for wireless in wireless_manufacturers:
            if wireless in manufacturer:
                return "Wireless Card"

        return "Ethernet Card or Unknown"
    else:
        return "Error fetching data"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
result = is_wireless_card(mac_address)
print(f'The MAC address {mac_address} is likely associated with a: {result}')
