
import requests

def get_mac_details(mac):
    # Format the MAC address
    mac = mac.strip().replace(":", "").replace("-", "").upper()

    # Check the OUI from the MAC address
    url = f"https://api.maclookup.app/v2/macs/{mac}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data.get("result")
    else:
        return None

def determine_card_type(mac):
    details = get_mac_details(mac)

    if details:
        category = details.get("category")
        if "wireless" in category.lower():
            return "Wireless card"
        elif "ethernet" in category.lower():
            return "Ethernet card"
        else:
            return "Unknown card type"
    else:
        return "MAC address not found in database"

# Example MAC address
mac_address = "00:1A:2B:3C:4D:5E"
card_type = determine_card_type(mac_address)
print(f"The card type for MAC {mac_address} is: {card_type}")
