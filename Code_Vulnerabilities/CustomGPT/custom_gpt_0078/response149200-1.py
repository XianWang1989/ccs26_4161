
import requests

def get_mac_type(mac_address):
    # Ensure MAC address is formatted correctly
    mac_address = mac_address.lower().replace(":", "").replace("-", "")
    if len(mac_address) != 12:
        return "Invalid MAC address format."

    # Extract the OUI (first 6 characters)
    oui = mac_address[:6]

    # Example: Using an OUI lookup API
    response = requests.get(f"https://api.macaddress.io/v1?apiKey=YOUR_API_KEY&output=json&search={oui}")
    if response.status_code != 200:
        return "Error fetching OUI information."

    data = response.json()

    if "vendorDetails" in data:
        vendor = data["vendorDetails"]["companyName"]
        # Add your logic to categorize vendors as Ethernet or Wireless
        wireless_vendors = ["Intel Corporation", "Atheros Communications"]
        ethernet_vendors = ["Broadcom", "Realtek", "NVIDIA"]

        if vendor in wireless_vendors:
            return "Wireless Card"
        elif vendor in ethernet_vendors:
            return "Ethernet Card"
        else:
            return "Unknown type"
    else:
        return "Vendor information not found."

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
card_type = get_mac_type(mac_address)
print(f"The MAC address {mac_address} is associated with: {card_type}")
