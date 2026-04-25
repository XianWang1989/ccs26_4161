
from getmac import get_mac_address

def get_interface_type(mac_address):
    # Get network interface details
    interface = get_mac_address(mac=mac_address, network_request=True)

    if interface:
        if 'wlan' in interface.lower() or 'wireless' in interface.lower():
            return 'Wireless Card'
        elif 'eth' in interface.lower() or 'ethernet' in interface.lower():
            return 'Ethernet Card'
    return 'Unknown Card Type'

# Example MAC address
mac = "00:1A:2B:3C:4D:5E"
interface_type = get_interface_type(mac)
print(f"The MAC address {mac} is associated with: {interface_type}")
