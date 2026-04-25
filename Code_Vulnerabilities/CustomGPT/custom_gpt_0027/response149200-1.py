
import requests

# Sample known OUIs
ethernet_ouis = {
    "00:1A:2B": "Ethernet",
    "00:1D:A1": "Ethernet",
    "00:24:D7": "Ethernet"
}

wireless_ouis = {
    "00:11:22": "Wireless",
    "00:14:51": "Wireless",
    "00:BC:30": "Wireless"
}

def get_device_type(mac_address):
    # Normalize MAC address
    mac_prefix = mac_address[:8].upper()  # Get first three octets (e.g., '00:1A:2B')

    if mac_prefix in ethernet_ouis:
        return "Ethernet Card"
    elif mac_prefix in wireless_ouis:
        return "Wireless Card"
    else:
        return "Unknown Card Type"

# Example usage
mac = "00:1A:2B:3C:4D:5E"
device_type = get_device_type(mac)
print(f"The device type for MAC {mac} is: {device_type}")
