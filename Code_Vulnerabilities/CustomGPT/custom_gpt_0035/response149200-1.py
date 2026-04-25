
import requests

def get_device_type(mac_address):
    url = f"https://api.maclookup.app/v2/macs/{mac_address}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'company' in data:
            return data['type'], data['company']
    return None, None

def main(mac_address):
    device_type, manufacturer = get_device_type(mac_address)

    if device_type:
        print(f"MAC Address: {mac_address}\nType: {device_type}\nManufacturer: {manufacturer}")
        if 'WLAN' in device_type:
            print("This device is likely a wireless card.")
        else:
            print("This device is likely an Ethernet card.")
    else:
        print("Could not retrieve information for this MAC address.")

# Example usage
mac = "00:14:22:01:23:45"  # Replace with your MAC address
main(mac)
