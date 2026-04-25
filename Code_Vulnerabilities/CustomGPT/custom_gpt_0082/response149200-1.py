
import requests

def get_mac_type(mac_address):
    # Clean the MAC address format
    mac_address = mac_address.upper().replace('-', ':')

    # OUI Lookup API
    url = f"https://api.macvendors.com/{mac_address}"

    try:
        # Making a request to the OUI API
        response = requests.get(url)
        if response.status_code == 200:
            vendor = response.text
            if "wireless" in vendor.lower():
                return "Wireless card"
            elif "ethernet" in vendor.lower() or "network" in vendor.lower():
                return "Ethernet card"
            else:
                return "Unknown type"
        else:
            return "Failed to fetch vendor information"
    except Exception as e:
        return str(e)

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
mac_type = get_mac_type(mac_address)
print(f"The MAC address {mac_address} is likely an: {mac_type}")
