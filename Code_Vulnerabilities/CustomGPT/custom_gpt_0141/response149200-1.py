
import requests

def get_oui_info(mac_address):
    # Extract OUI (first 6 characters of MAC address)
    oui = mac_address.upper().replace(':', '')[:6]

    # OUI lookup API (change if you have a local database)
    url = f"https://api.macvendors.com/{mac_address}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Assume the response is in the format: {"vendor": "VendorName"}
            vendor_info = response.json()
            vendor_name = vendor_info.get("vendor", "Unknown")
            if "wireless" in vendor_name.lower():
                return "Wireless Card"
            elif "ethernet" in vendor_name.lower() or "wired" in vendor_name.lower():
                return "Ethernet Card"
            else:
                return "Could not determine card type"
        else:
            return "Failed to retrieve vendor information"
    except Exception as e:
        return f"Error: {e}"

# Example MAC addresses
mac_address_1 = "00:1A:2B:3C:4D:5E"
mac_address_2 = "00:1F:AA:BB:CC:DD"

print(f"{mac_address_1}: {get_oui_info(mac_address_1)}")
print(f"{mac_address_2}: {get_oui_info(mac_address_2)}")
