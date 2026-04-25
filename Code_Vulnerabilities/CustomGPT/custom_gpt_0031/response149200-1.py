
import psutil

def get_interface_type(mac_address):
    # Normalize MAC address
    mac_address = mac_address.lower()

    # Get network interfaces
    interfaces = psutil.net_if_addrs()

    for interface, addrs in interfaces.items():
        for addr in addrs:
            if addr.family == psutil.AF_LINK and addr.address.lower() == mac_address:
                # Check interface type
                interface_type = 'Ethernet' if 'eth' in interface or 'en' in interface else 'Wireless'
                return interface_type
    return None

# Example usage
mac = '00:1A:2B:3C:4D:5E'  # Replace with your MAC address
interface_type = get_interface_type(mac)

if interface_type:
    print(f"The MAC address {mac} is associated with a {interface_type} card.")
else:
    print(f"The MAC address {mac} was not found.")
