
import requests

def get_oui_info(mac_address):
    # Normalize MAC address
    mac_address = mac_address.replace(":", "").lower()
    oui = mac_address[:6]  # Get the first three bytes (6 hex digits)

    # Fetch OUI data from an online service
    response = requests.get(f"https://api.macvendors.com/{mac_address}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def is_wireless_or_ethernet(mac_address):
    oui_info = get_oui_info(mac_address)

    if not oui_info:
        return "Unknown"

    # Check for common wireless vendors
    wireless_vendors = [
        "00:1A:11",  # Example OUI of a wireless vendor
        "00:1B:44",  # Another example
        # Add more OUIs as needed
    ]

    for vendor in wireless_vendors:
        if mac_address.startswith(vendor):
            return "Wireless Card"

    return "Ethernet Card"

# Example usage
mac_address = "00:1A:11:FF:EE:DD"  # Replace with your MAC address
result = is_wireless_or_ethernet(mac_address)
print(f"The MAC address {mac_address} is associated with: {result}")
