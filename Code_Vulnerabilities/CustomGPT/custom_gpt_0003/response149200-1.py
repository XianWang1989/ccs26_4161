
import getmac
import subprocess
import re

def get_interface_type(mac_address):
    # Get all network interfaces using a subprocess call
    try:
        output = subprocess.check_output("ip link show", shell=True, universal_newlines=True)
        interfaces = output.split('\n')
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return None

    for interface in interfaces:
        # Look for the MAC address in the interface details
        if mac_address in interface:
            if 'state UP' in output:
                # For Linux systems, check if the interface is flagged as UP
                interface_name = re.search(r'(\w+):', interface).group(1)
                interface_info = subprocess.check_output(f'iw dev {interface_name} info', shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
                if 'type managed' in interface_info:
                    return "Wireless"
                else:
                    return "Ethernet"

    return "Unknown Interface Type"

# Example usage
mac_address = '00:11:22:33:44:55'  # Replace with the actual MAC address you want to check
interface_type = get_interface_type(mac_address)
print(f"The interface type for MAC address {mac_address} is: {interface_type}")
