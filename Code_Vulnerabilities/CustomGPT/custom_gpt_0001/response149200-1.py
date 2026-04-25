
import subprocess
import re

def get_interface_type(mac_address):
    # Run nmap command to get the interface type
    try:
        # Replace '192.168.1.0/24' with your target network
        output = subprocess.check_output(['nmap', '-sP', '192.168.1.0/24']).decode()

        # Regex to search for the MAC address and its details
        mac_pattern = r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})\s+\((.*)\)'
        matches = re.findall(mac_pattern, output)

        for match in matches:
            found_mac = match[0]
            device_info = match[2].strip()
            if found_mac.lower() == mac_address.lower():
                if 'wireless' in device_info.lower():
                    return 'Wireless Card'
                elif 'ethernet' in device_info.lower() or 'wired' in device_info.lower():
                    return 'Ethernet Card'
                else:
                    return 'Unknown Card Type'

    except subprocess.CalledProcessError as e:
        print(f"Error during nmap execution: {e}")

    return 'MAC Address not found'

# Example usage
mac_address = "00:1A:2B:3C:4D:5E"  # Replace with your MAC address
interface_type = get_interface_type(mac_address)
print(f"The MAC Address {mac_address} is connected via: {interface_type}")
