
import requests
from getmac import get_mac_address

def get_device_type(mac_address):
    try:
        # Extract the OUI (first 3 bytes)
        oui = mac_address[:8].upper()
        print(f"OUI: {oui}")

        # Use an external API to get vendor details
        response = requests.get(f"https://api.macvendors.com/{mac_address}")

        if response.status_code == 200:
            vendor_info = response.json()
            vendor = vendor_info.get('result', {}).get('company', 'Unknown')
            print(f"Vendor: {vendor}")

            # Implement logic to determine if the vendor is likely wireless or wired
            if 'wireless' in vendor.lower() or 'wifi' in vendor.lower():
                return "Wireless Card"
            else:
                return "Ethernet Card or Unknown"
        else:
            return "Vendor information not available"
    except Exception as e:
        return f"Error: {str(e)}"

# Example MAC address
mac_address = get_mac_address()  # Replace with your MAC address
device_type = get_device_type(mac_address)
print(f"Device Type: {device_type}")
