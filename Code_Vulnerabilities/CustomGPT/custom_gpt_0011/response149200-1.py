
import requests

def get_device_type(mac_address):
    # Extract the OUI from the MAC address
    oui = mac_address[:8].upper()  # MAC address format should be xx:xx:xx
    url = f"https://api.macvendors.com/{mac_address}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            manufacturer_info = response.text
            # Determine if the manufacturer commonly produces WLAN or Wired devices
            # This part may require a predefined list based on known manufacturers
            wireless_manufacturers = ["Apple", "TP-Link", "Intel", "Netgear"]
            if any(manufacturer in manufacturer_info for manufacturer in wireless_manufacturers):
                return "Wireless Card"
            else:
                return "Ethernet Card"
        else:
            return "Unknown device type"
    except Exception as e:
        return f"Error: {e}"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"  # Replace with the target MAC address
device_type = get_device_type(mac_address)
print(f"The device type for MAC address {mac_address} is: {device_type}")
