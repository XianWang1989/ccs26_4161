
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()     

# Set the filter for the desired IP address
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop to capture packets
for timestamp, packet in pc:
    # Parse the Ethernet frame
    eth = dpkt.ethernet.Ethernet(packet)

    # Check for IPv4 packets
    if isinstance(eth.data, dpkt.ip.IP):
        ip = eth.data
        print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}')
