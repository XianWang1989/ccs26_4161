
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()

# Set filter to capture traffic for a specific IP address
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop through captured packets
for timestamp, packet in pc:
    # Parse Ethernet frame
    eth = dpkt.ethernet.Ethernet(packet)

    # Handle only IP packets
    if isinstance(eth.data, dpkt.ip.IP):
        ip = eth.data
        print('Timestamp: {}'.format(timestamp))
        print('Source IP: {}'.format(ip.src))
        print('Destination IP: {}'.format(ip.dst))
        print('---')
