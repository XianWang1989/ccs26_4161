
import dpkt
import pcap

# Create pcap object
pc = pcap.pcap(name=None)  # 'name=None' uses the default interface

# Set filter for the desired host
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Start capturing packets
for timestamp, packet in pc:
    try:
        # Parse Ethernet packet
        eth = dpkt.ethernet.Ethernet(packet)
        # Print packet info
        print(f'Time: {timestamp}, Source: {eth.src}, Destination: {eth.dst}, Type: {eth.type}')
    except dpkt.dpkt.NeedData:
        continue
