
import nmap

def get_interface_type(mac_address):
    # Initialize the nmap PortScanner
    nm = nmap.PortScanner()

    # Scan the network to find devices
    # You can specify the target network in the format '192.168.1.0/24'
    target = '192.168.1.0/24'  # Change this to your network range
    nm.scan(hosts=target, arguments='-sn')

    # Iterate over all hosts found during the scan
    for host in nm.all_hosts():
        # Verify if we have an 'addresses' section
        if 'addresses' in nm[host]:
            # Check for the MAC address
            mac = nm[host]['addresses'].get('mac', None)
            # If present, check its type
            if mac and mac.lower() == mac_address.lower():
                # Return interface type based on the vendor OUI
                vendor = nm[host]['vendor'].get(mac)
                if vendor:
                    if 'WLAN' in vendor or 'Wireless' in vendor:
                        return 'Wireless'
                    else:
                        return 'Wired (Ethernet)'

    return 'Unknown'

# Example usage
mac_address = '00:1A:2B:3C:4D:5E'  # Replace with your MAC address
interface_type = get_interface_type(mac_address)
print(f'The interface type for MAC address {mac_address} is: {interface_type}')
