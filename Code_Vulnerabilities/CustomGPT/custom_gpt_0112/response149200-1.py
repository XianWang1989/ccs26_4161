
import requests

def retrieve_oui_data():
    """
    Retrieve OUI data from an open database.
    This method fetches a JSON representation of known OUI types.
    """
    try:
        response = requests.get("https://api.macvendors.com/lookup")
        return response.json()
    except Exception as e:
        print(f"Error retrieving OUI data: {e}")
        return {}

def get_mac_type(mac_address):
    """
    Determine if the MAC address belongs to a wireless or Ethernet card.
    """
    oui = mac_address[:8]  # Get the OUI part of the MAC (first 3 bytes)

    oui_data = retrieve_oui_data()
    mac_type = oui_data.get(oui, {}).get("type", "Unknown")

    return mac_type

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
mac_type = get_mac_type(mac_address)
if mac_type == "unknown":
    print("MAC address type could not be determined.")
else:
    print(f"The MAC address {mac_address} is likely associated with a {mac_type} device.")
