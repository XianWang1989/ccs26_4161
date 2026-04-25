
from getmac import get_mac_address

def get_interface_type(mac_address):
    interface_info = get_mac_address(mac=mac_address, physical=True)

    if interface_info:
        # Check if the interface is wireless or wired
        if "wlan" in interface_info.lower():
            return "Wireless (Wi-Fi)"
        elif "eth" in interface_info.lower():
            return "Ethernet"
        else:
            return "Unknown interface type"
    else:
        return "MAC address not found"

# Example usage:
mac_address = '00:1A:2B:3C:4D:5E'  # Replace with your MAC address
interface_type = get_interface_type(mac_address)
print(f"The MAC address {mac_address} is associated with: {interface_type}")
