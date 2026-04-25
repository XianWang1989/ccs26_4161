
import nmap

def get_interface_type(mac_address):
    # Initialize the Nmap scanner
    nm = nmap.PortScanner()

    # Scan local network (adjust the target as necessary)
    nm.scan('192.168.1.0/24')  # Replace with your local network range

    for host in nm.all_hosts():
        # Check if the MAC address matches
        if 'mac' in nm[host]['addresses']:
            if nm[host]['addresses']['mac'] == mac_address:
                # Check the interface type
                for interface in nm[host]['interfaces']:
                    if interface['mac'] == mac_address:
                        return 'Wireless' if 'wireless' in interface['name'].lower() else 'Ethernet'

    return 'Unknown'

# Example usage
mac_address = '00:1A:2B:3C:4D:5E'  # Replace with your MAC address
interface_type = get_interface_type(mac_address)
print(f'The interface type for MAC address {mac_address} is: {interface_type}')
