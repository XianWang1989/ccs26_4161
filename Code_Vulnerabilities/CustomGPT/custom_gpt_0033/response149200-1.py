
import nmap

def get_device_type(mac_address):
    # Initialize the scanner
    nm = nmap.PortScanner()

    # Scan the local network (replace '192.168.1.0/24' with your subnet)
    nm.scan(hosts='192.168.1.0/24', arguments='-sn')

    for host in nm.all_hosts():
        # Retrieve MAC address and vendor information
        if 'mac' in nm[host]['addresses']:
            if nm[host]['addresses']['mac'] == mac_address:
                return nm[host]['vendor'].get(mac_address, "Unknown")

    return "Not Found"

# Example usage
mac_address = '00:1A:2B:3C:4D:5E'  # Replace with your MAC address
device_vendor = get_device_type(mac_address)

if "wireless" in device_vendor.lower():
    print("This MAC address is likely associated with a wireless card.")
else:
    print("This MAC address is likely associated with an Ethernet card or not identifiable.")
