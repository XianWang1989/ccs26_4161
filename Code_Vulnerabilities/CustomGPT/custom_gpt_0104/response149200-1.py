
import subprocess
import re

def get_interface_type(mac_address):
    # Run the nmap command to discover devices on the network.
    process = subprocess.Popen(['nmap', '-sn', '192.168.0.0/24'], stdout=subprocess.PIPE)
    output, _ = process.communicate()

    # Decode the output
    text = output.decode()

    # Use regex to find the MAC address and associated interface type.
    # Note: nmap output provides 'MAC Address: <mac> (<vendor>) at <ip> on <interface>'
    pattern = re.compile(r'MAC Address: (.+?) \((.+?)\) at (.+?) on (.+)')

    for line in text.split('\n'):
        match = pattern.search(line)
        if match:
            mac, vendor, ip, interface = match.groups()
            if mac.lower() == mac_address.lower():
                if 'wireless' in interface.lower() or 'wlan' in interface.lower():
                    return 'Wireless Card'
                else:
                    return 'Ethernet Card'

    return 'Unknown'

# Example usage
mac_address = '00:1A:2B:3C:4D:5E'  # Replace with your MAC address
interface_type = get_interface_type(mac_address)
print(f'The interface type for MAC address {mac_address} is: {interface_type}')
