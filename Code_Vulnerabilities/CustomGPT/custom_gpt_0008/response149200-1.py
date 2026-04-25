
import subprocess
import re

def get_mac_type(mac_address):
    # Convert MAC address to ensure it's in the proper format
    mac_address = mac_address.lower()

    # Using nmap to fetch MAC address details
    try:
        output = subprocess.check_output(['nmap', '-sn', '192.168.1.0/24']).decode('utf-8')
        mac_info = re.findall(r'(?i)(?<=mac addr: )([\da-f:]{17})\s+\((.*?)\)', output)

        for mac, vendor in mac_info:
            if mac_address == mac:
                if 'wireless' in vendor.lower():
                    return 'Wireless Card'
                elif 'ethernet' in vendor.lower() or 'wired' in vendor.lower():
                    return 'Ethernet Card'
                else:
                    return 'Unknown type'

        return 'MAC address not found'

    except subprocess.CalledProcessError as e:
        return f"Error: {str(e)}"

# Example usage
mac = '00:1A:2B:3C:4D:5E'  # Replace with the actual MAC address
print(get_mac_type(mac))
