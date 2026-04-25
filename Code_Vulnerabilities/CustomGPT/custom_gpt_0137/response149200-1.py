
import subprocess
import re

def get_mac_interface_type(mac_address):
    # Convert MAC address to appropriate format for grep
    mac_address_formatted = mac_address.lower()

    # Get the ARP table
    try:
        arp_output = subprocess.check_output(['arp', '-a']).decode('utf-8')
        for line in arp_output.splitlines():
            if mac_address_formatted in line.lower():
                # Print line showing the MAC address
                print(f"Found MAC address in ARP: {line}")

                # Check for keywords indicating interface type
                if 'wlan' in line.lower() or 'wifi' in line.lower():
                    return "Wireless Card (WiFi)"
                elif 'eth' in line.lower() or 'ethernet' in line.lower():
                    return "Ethernet Card"
                else:
                    return "Unknown Interface Type"
        return "MAC address not found in ARP table"
    except Exception as e:
        return f"Error occurred: {str(e)}"

# Example usage
mac_address = '00:1A:2B:3C:4D:5E'  # Replace with actual MAC address
interface_type = get_mac_interface_type(mac_address)
print(f"Interface Type for {mac_address}: {interface_type}")
