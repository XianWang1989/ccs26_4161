
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()  
# Set a filter for the packets you want to capture
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop through the packets
for timestamp, packet in pc:
    # Parse the Ethernet frame
    eth = dpkt.ethernet.Ethernet(packet)

    # Check if the Ethernet frame has an IP packet
    if isinstance(eth.data, dpkt.ip.IP):
        ip = eth.data
        print(f'Timestamp: {timestamp}')
        print(f'Source IP: {ip.src}')
        print(f'Destination IP: {ip.dst}')
        print(f'Protocol: {ip.p}')
        print(f'Packet Size: {len(packet)} bytes')
    else:
        print('Not an IP packet')
