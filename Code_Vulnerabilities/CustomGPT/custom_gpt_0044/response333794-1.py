
import pcap
import dpkt

# Specify the packet capturing interface (e.g., 'en0' for Ethernet)
interface = 'en0'  # Change to your actual interface if needed

# Create a pcap object for the specified interface
pc = pcap.pcap(name=interface)

# Set filter for packets from/to specific IP address
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

print("Listening on interface:", interface)
print("Start sniffing...")

# Capture packets in a loop
for timestamp, packet in pc:
    # Parse Ethernet frame
    eth = dpkt.ethernet.Ethernet(packet)

    # Check if it's an IP packet
    if isinstance(eth.data, dpkt.ip.IP):
        ip = eth.data
        print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}')
