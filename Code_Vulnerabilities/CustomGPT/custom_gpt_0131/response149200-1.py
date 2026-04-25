
import requests

def get_mac_type(mac_address):
    mac_address = mac_address.replace(":", "-").upper()  # Format the MAC address
    url = f"https://api.macaddress.io/v1?apiKey=YOUR_API_KEY&output=json&search={mac_address}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        manufacturer = data.get("vendorDetails", {}).get("companyName", "")

        # Common criteria to differentiate
        wireless_manufacturers = ["Cisco", "Netgear", "TP-Link", "Qualcomm"]
        ethernet_manufacturers = ["Intel", "Realtek", "Broadcom", "Atheros"]

        # Check if manufacturer is in wireless or ethernet category
        if any(manufacturer in m for m in wireless_manufacturers):
            return "Wireless Card"
        elif any(manufacturer in m for m in ethernet_manufacturers):
            return "Ethernet Card"
        else:
            return "Unknown Type"

    return "Error fetching data"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
card_type = get_mac_type(mac_address)
print(f"The MAC address {mac_address} is associated with a {card_type}.")
