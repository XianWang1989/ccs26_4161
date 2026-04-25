
import requests

def get_mac_info(mac_address):
    # Format the MAC address
    mac_address = mac_address.replace(":", "-").upper()

    # OUI lookup URL
    url = f"https://api.maclookup.app/v2/macs/{mac_address}"

    try:
        response = requests.get(url)
        data = response.json()

        # Check if the request was successful
        if response.status_code == 200:
            oui = data['result']['oui']
            print(f"MAC Address: {mac_address}")
            print(f"OUI: {oui}")
            # Here, you can implement your own logic to differentiate between wireless and Ethernet
            if "WLAN" in oui.upper():
                return "Wireless Card"
            elif "ETH" in oui.upper():
                return "Ethernet Card"
            else:
                return "Unknown Type"
        else:
            return "MAC address not found"

    except Exception as e:
        return f"An error occurred: {e}"

# Example MAC address
mac = "00:1A:2B:3C:4D:5E"
result = get_mac_info(mac)
print(f"Network Interface Type: {result}")
