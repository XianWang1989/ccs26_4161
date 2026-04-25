
import requests

# Known OUIs for wireless and Ethernet interfaces
wireless_ouis = ['00:1A:2B', '00:1B:44', '00:1C:BF']  # Add more as needed
ethernet_ouis = ['00:1A:3F', '00:1B:17', '00:1C:00']  # Add more as needed

def get_mac_type(mac):
    mac_prefix = mac.upper()[:8]  # Get the first 8 characters (e.g., '00:1A:2B')

    if mac_prefix in wireless_ouis:
        return "Wireless"
    elif mac_prefix in ethernet_ouis:
        return "Ethernet"
    else:
        return "Unknown"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"
device_type = get_mac_type(mac_address)
print(f"The device with MAC {mac_address} is a {device_type} interface.")
