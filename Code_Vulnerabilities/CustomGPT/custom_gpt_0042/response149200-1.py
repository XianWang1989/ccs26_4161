
import requests

def get_mac_info(mac_address):
    # Extract the OUI (first 3 octets)
    oui = mac_address.replace(':', '').upper()[:6]
    url = f"https://api.theaufs.com/oi/{oui}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        return {
            'manufacturer': data.get('manufacturer', 'Unknown'),
            'type': data.get('type', 'Unknown'),  # Example field, depends on the API
        }

    except requests.RequestException as e:
        print(f"Error retrieving data: {e}")
        return None

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
mac_info = get_mac_info(mac_address)

if mac_info:
    print(f"Manufacturer: {mac_info['manufacturer']}")
    print(f"Type: {mac_info['type']}")
