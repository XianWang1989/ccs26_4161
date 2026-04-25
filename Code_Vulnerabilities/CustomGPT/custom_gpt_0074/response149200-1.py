
import requests

def get_mac_details(mac_address):
    # Clean the input MAC address
    mac_address = mac_address.replace(":", "").replace("-", "").upper()

    # URL for the MAC address lookup API
    url = f"https://api.macaddress.io/v1?apiKey=YOUR_API_KEY&output=json&search={mac_address}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad status

        data = response.json()
        vendor = data.get('vendorDetails', {}).get('companyName', 'Unknown')

        # You can maintain a list of known OUI for Ethernet and Wireless adapters
        if 'Wireless' in vendor:
            return f"The MAC Address {mac_address} is likely associated with a Wireless card."
        else:
            return f"The MAC Address {mac_address} is likely associated with an Ethernet card."

    except requests.RequestException as e:
        return f"An error occurred: {e}"

# Example MAC Address
mac_example = "00:1A:2B:3C:4D:5E"
print(get_mac_details(mac_example))
