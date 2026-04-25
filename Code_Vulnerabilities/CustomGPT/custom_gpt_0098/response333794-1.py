
import dpkt
import pcap

# Initialize pcap object
pc = pcap.pcap()  
# Set a filter for packets from or to a specific IP
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop through captured packets
for timestamp, packet in pc:
    # Convert the packet to an Ethernet frame
    eth = dpkt.ethernet.Ethernet(packet)

    # Extract the IP layer
    if isinstance(eth.data, dpkt.ip.IP):
        ip = eth.data
        print(f'Time: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}')

    else:
        print(f'Time: {timestamp}, Unsupported Ethernet frame: {eth}')
