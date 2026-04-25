
import subprocess
import re

def get_interface_type(mac_address):
    # Use the subprocess to execute `ip` command to get interfaces
    try:
        interfaces = subprocess.check_output(["ip", "link"], universal_newlines=True)

        # Search for the MAC address in the interface details
        for line in interfaces.splitlines():
            if mac_address in line:
                interface_name = re.search(r'^\d+: (\w+):', line).group(1)
                interface_details = subprocess.check_output(["cat", f"/sys/class/net/{interface_name}/type"], universal_newlines=True).strip()

                # determine if it's wireless or ethernet based on type
                if interface_details == '1':  # Ethernet
                    return "Ethernet Card"
                elif interface_details == '2':  # Wireless
                    return "Wireless Card"

    except Exception as e:
        return str(e)

# Example MAC address
mac_address = "00:1A:2B:3C:4D:5E"
interface_type = get_interface_type(mac_address)
print(f"The interface type for MAC address {mac_address} is: {interface_type}")
