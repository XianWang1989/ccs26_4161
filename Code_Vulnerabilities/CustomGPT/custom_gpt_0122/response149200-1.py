
import requests

def get_mac_info(mac_addr):
    # Ensure the MAC address is in valid format (XX:XX:XX:XX:XX:XX)
    if len(mac_addr) != 17:
        return "Invalid MAC address format"

    # Get the OUI (first three octets) from the MAC address
    oui = mac_addr[:8].replace(':', '').upper()

    # OUI database URL (you can use other OUI sources if needed)
    url = f"https://api.macvendors.com/{mac_addr}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            vendor_info = response.text
            # Check if it mentions 'Wireless' or 'Ethernet'
            if 'Wireless' in vendor_info:
                return "Wireless card"
            elif 'Ethernet' in vendor_info:
                return "Ethernet card"
            else:
                return "Unknown type"
        else:
            return "Could not retrieve OUI information"
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
result = get_mac_info(mac_address)
print(result)
