
import requests

def get_oui_type(mac_address):
    # Extract OUI (first three octets)
    oui = mac_address[:8].replace(":", "").upper()

    # Use a public OUI lookup API
    url = f"https://api.macvendors.com/{mac_address}"
    response = requests.get(url)

    if response.status_code == 200:
        manufacturer = response.text
        # You can maintain a list of known wireless manufacturers
        wireless_manufacturers = [
            "APPLE", "INTEL", "LINKSYS", "NETGEAR", "TP-LINK", 
            "D-LINK", "BELKIN", "HUAWEI", "SAMSUNG", "XIAOMI"
        ]

        # Check if manufacturer is in the wireless list
        if any(wireless in manufacturer.upper() for wireless in wireless_manufacturers):
            return "Wireless Card"
        else:
            return "Ethernet Card or Unknown Card"
    else:
        return "Unable to determine card type"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
print(f"The MAC address {mac_address} corresponds to a: {get_oui_type(mac_address)}")
