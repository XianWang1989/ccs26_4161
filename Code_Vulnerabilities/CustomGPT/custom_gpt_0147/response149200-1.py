
import os
from getmac import get_mac_address

def get_interface_type(mac_address):
    interface_info = os.popen(f"ip link show | grep {mac_address}").read()
    if "wl" in interface_info:  # Common identifier for wireless
        return "Wireless"
    elif "eth" in interface_info:  # Common identifier for Ethernet
        return "Ethernet"
    else:
        return "Unknown interface type"

mac_address = "XX:XX:XX:XX:XX:XX"  # Replace with actual MAC address
interface_type = get_interface_type(mac_address)
print(f"The MAC address {mac_address} is associated with a/an {interface_type} card.")
