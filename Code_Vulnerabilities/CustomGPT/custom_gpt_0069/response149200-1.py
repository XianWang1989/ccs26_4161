
import requests

def get_mac_details(mac_address):
    # Clean and format MAC address
    mac_address = mac_address.strip().upper().replace(':', '')

    # Open OUI lookup service
    url = f"https://api.macvendors.com/{mac_address}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            vendor_info = response.json()
            # Example vendor-based checks (you can customize this list)
            wireless_vendors = ["APPLE", "CISCO", "D-LINK", "LINKSYS"]
            ethernet_vendors = ["INTEL", "REALTEK", "BROADCOM"]

            vendor = vendor_info.get('result', 'Unknown Vendor')
            print(f"Vendor: {vendor}")

            if any(v in vendor for v in wireless_vendors):
                return "Likely a Wireless Card"
            elif any(v in vendor for v in ethernet_vendors):
                return "Likely an Ethernet Card"
            else:
                return "Type Unknown"
        else:
            return "Failed to retrieve vendor information"

    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
result = get_mac_details(mac_address)
print(result)
