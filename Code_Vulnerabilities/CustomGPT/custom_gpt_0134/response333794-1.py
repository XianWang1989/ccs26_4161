
import dpkt
import pcap

# Create pcap object
pc = pcap.pcap()     
# Set filter for specific IP
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop over the packets
for timestamp, packet in pc:
    try:
        eth = dpkt.ethernet.Ethernet(packet)
        ip = eth.data
        print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}')
    except (dpkt.dpkt.NeedData, AttributeError) as e:
        print(f'Error processing packet: {e}')
