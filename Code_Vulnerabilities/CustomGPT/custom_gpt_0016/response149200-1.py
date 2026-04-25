
import requests

def get_mac_vendor(mac_address):
    # Format MAC address
    mac_address = mac_address.replace(":", "").upper()
    url = f"https://api.macvendors.com/{mac_address}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        vendor = response.text

        # Check the vendor name to infer the type of card
        if "wireless" in vendor.lower() or "wifi" in vendor.lower():
            return "Wireless Card", vendor
        else:
            return "Ethernet Card", vendor

    except requests.exceptions.RequestException as e:
        return "Error fetching data", str(e)

# Example MAC Addresses
mac_address_1 = "00:1A:2B:3C:4D:5E"  # Example MAC address (replace with actual)
mac_address_2 = "00:1A:2B:3C:4D:5F"  # Another example

# Usage
card_type_1, vendor_1 = get_mac_vendor(mac_address_1)
card_type_2, vendor_2 = get_mac_vendor(mac_address_2)

print(f"MAC Address: {mac_address_1}, Type: {card_type_1}, Vendor: {vendor_1}")
print(f"MAC Address: {mac_address_2}, Type: {card_type_2}, Vendor: {vendor_2}")
