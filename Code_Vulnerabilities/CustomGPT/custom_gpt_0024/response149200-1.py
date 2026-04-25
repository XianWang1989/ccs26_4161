
import requests

def get_mac_type(mac_address):
    # Strip MAC address of hyphens or colons and convert to uppercase
    mac_address = mac_address.replace(":", "").replace("-", "").upper()
    if len(mac_address) != 12:
        raise ValueError("Invalid MAC address format.")

    # Get the OUI (first 6 characters)
    oui = mac_address[:6]

    # URL to fetch OUI information
    url = f"https://api.ooi.io/lookup/{oui}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        if 'our_mac_type' in data:
            return data['our_mac_type']  # returns 'wireless' or 'ethernet'
        else:
            return "Unknown OUI type"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching OUI information: {e}")
        return None

# Example usage
mac = "00:1A:2B:3C:4D:5E"  # Replace with your MAC address
mac_type = get_mac_type(mac)
print(f"The MAC address {mac} is associated with a {mac_type} card.")
