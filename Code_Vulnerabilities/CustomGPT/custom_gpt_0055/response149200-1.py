
import nmap

def check_interface_type(mac_address):
    nm = nmap.PortScanner()

    # Scan the network (adjust the target as needed)
    nm.scan('192.168.1.0/24')  # Replace with your subnet

    for host in nm.all_hosts():
        if 'mac' in nm[host]['addresses']:
            mac = nm[host]['addresses']['mac']
            if mac_address.lower() == mac.lower():
                # Example heuristics based on MAC OUI (Organizationally Unique Identifier)
                # Check if the MAC indicates a known wireless manufacturer
                ouis = {
                    '00:1A:7D': 'Ethernet',
                    '00:1B:44': 'Wireless',
                    'F4:5C:89': 'Wireless',
                    '00:15:5D': 'Ethernet'
                    # Add more OUI checks here
                }
                prefix = mac_address.upper()[:8]
                if prefix in ouis:
                    return ouis[prefix]

    return 'Unknown'

# Example usage
mac_address = '00:1A:7D:DA:71:13'  # Replace with your MAC address
interface_type = check_interface_type(mac_address)
print(f"The interface type for {mac_address} is: {interface_type}")
