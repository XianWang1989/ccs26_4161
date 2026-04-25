
import subprocess

def get_interface_type(mac_address):
    # Run the `ip link` command to get the list of interfaces
    try:
        result = subprocess.run(['ip', 'link'], capture_output=True, text=True, check=True)
        interfaces = result.stdout.splitlines()

        for interface in interfaces:
            if mac_address.lower() in interface.lower():
                # Capture the interface name
                interface_name = interface.split(':')[1].strip()
                # Check if the interface is wireless or ethernet
                if 'wl' in interface_name:
                    return 'Wireless'
                elif 'eth' in interface_name or 'en' in interface_name:  # 'en' for newer naming conventions
                    return 'Ethernet'

        return 'Unknown'

    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        return None

# Example usage
mac_address = "00:11:22:33:44:55"  # Replace with your MAC address
interface_type = get_interface_type(mac_address)
print(f"The MAC address {mac_address} is associated with: {interface_type}")
