
import requests
from getmac import get_mac_address

def get_oui(mac):
    # Extract the first three bytes of the MAC address (OUI)
    oui = ':'.join(mac.split(':')[:3]).upper()
    return oui

def check_mac_type(mac):
    # Request OUI information from a public OUI lookup service
    url = f"https://api.maclookup.app/v2/macs/{mac}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'result' in data:
            vendor = data['result']['vendor']
            # Heuristic to decide if the device is likely a laptop or workstation
            if 'laptop' in vendor.lower() or 'notebook' in vendor.lower():
                return "Wireless Card - Likely a Laptop"
            elif 'desktop' in vendor.lower():
                return "Ethernet Card - Likely a Workstation"
            else:
                return "Unknown type, but vendor is: " + vendor
        else:
            return "MAC address not found in the database"
    else:
        return "Error fetching data from lookup service"

# Example MAC address for testing
mac_address = "00:1A:2B:3C:4D:5E"
print(check_mac_type(mac_address))
