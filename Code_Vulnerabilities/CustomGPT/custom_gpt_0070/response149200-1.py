
from scapy.all import ARP, Ether, srp, conf

def get_interface_type(mac_address):
    # You may want to replace this dictionary with a more comprehensive one.
    oui_map = {
        '00:1A:2B': 'Wireless',
        '00:1A:3C': 'Ethernet',
        '00:0C:29': 'Virtual',
        # Add more MAC prefixes as needed
    }

    # Normalize the MAC address
    mac_prefix = ':'.join(mac_address.split(':')[:3]).upper()

    return oui_map.get(mac_prefix, 'Unknown')

def scan_network(network):
    # Create ARP request to discover MAC addresses in the network
    arp = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=2, verbose=False)[0]

    devices = []

    for _, received in result:
        devices.append(received.hwsrc)  # MAC address

    return devices

# Example usage:
if __name__ == "__main__":
    network_to_scan = "192.168.1.0/24"  # Replace with your network
    mac_addresses = scan_network(network_to_scan)

    for mac in mac_addresses:
        interface_type = get_interface_type(mac)
        print(f"MAC Address: {mac} - Interface Type: {interface_type}")
