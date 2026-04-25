
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()

# List available interfaces
print("Available interfaces:")
for iface in pcap.findalldevs():
    print(iface)

# Set the desired filter; replace 'X.X.X.X' with your actual target IP
target_ip = 'X.X.X.X'
pc.setfilter(f'src host {target_ip} or dst host {target_ip}')

# Capture packets
print(f"Sniffing packets for {target_ip}...")
for timestamp, packet in pc:
    try:
        # Parse Ethernet frame
        eth = dpkt.ethernet.Ethernet(packet)
        # Check if the payload is IP
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Length: {len(packet)}')
    except Exception as e:
        print(f'Error parsing packet: {e}')
