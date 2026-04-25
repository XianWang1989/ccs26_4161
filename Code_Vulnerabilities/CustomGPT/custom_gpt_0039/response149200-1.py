
import getmac
import subprocess
import re

def get_interface_type(mac_address):
    # Use a command like `iwconfig` to check for wireless interfaces
    try:
        iwconfig_output = subprocess.check_output("iwconfig", stderr=subprocess.STDOUT, shell=True).decode()
        if mac_address in iwconfig_output:
            return "Wireless"
    except Exception as e:
        print(f"Error checking wireless interfaces: {e}")

    # Use `ifconfig` or `ip link` command to check for ethernet interfaces
    try:
        ifconfig_output = subprocess.check_output("ifconfig", stderr=subprocess.STDOUT, shell=True).decode()
        if mac_address in ifconfig_output:
            return "Ethernet"
    except Exception as e:
        print(f"Error checking ethernet interfaces: {e}")

    return "Unknown"

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"  # Replace with your MAC address
interface_type = get_interface_type(mac_address)
print(f"The interface type for MAC address {mac_address} is: {interface_type}")
