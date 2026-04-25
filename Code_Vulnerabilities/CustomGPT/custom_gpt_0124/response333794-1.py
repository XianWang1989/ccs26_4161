
import pcap
import dpkt

# Create a pcap object
pc = pcap.pcap()

# Set a BPF filter for the desired IP address
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Capture packets
for timestamp, packet in pc:
    # Parse the Ethernet frame
    eth = dpkt.ethernet.Ethernet(packet)

    # Check if it has an IP layer
    if isinstance(eth.data, dpkt.ip.IP):
        ip = eth.data
        print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}')
