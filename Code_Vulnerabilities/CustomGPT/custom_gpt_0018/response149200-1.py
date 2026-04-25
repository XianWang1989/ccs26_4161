
import subprocess

def get_interface_type(mac_address):
    # Run nmap to get interface information
    result = subprocess.run(['nmap', '-sP', '192.168.1.0/24'], capture_output=True, text=True)

    # Check if the MAC address is present in the nmap output
    if mac_address in result.stdout:
        # Infer type from the output (simplified)
        for line in result.stdout.splitlines():
            if mac_address in line:
                if "wlan" in line or "wireless" in line:
                    return "Wireless Card"
                elif "eth" in line or "ethernet" in line:
                    return "Ethernet Card"

    return "Unknown Type"

# Example usage
mac = "00:1A:2B:3C:4D:5E"  # Replace with the target MAC address
interface_type = get_interface_type(mac)
print(f'The interface type for MAC {mac} is: {interface_type}')
