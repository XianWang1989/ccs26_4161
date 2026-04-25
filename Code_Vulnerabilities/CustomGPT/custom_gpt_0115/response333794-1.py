
import dpkt
import pcap

# Create pcap object
pc = pcap.pcap()

# Set the filter for the specified IP address
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop through captured packets
for timestamp, packet in pc:
    try:
        # Parse the packet
        eth = dpkt.ethernet.Ethernet(packet)

        # Check if the packet contains IP data
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f'Timestamp: {timestamp}, Source IP: {ip.src}, Destination IP: {ip.dst}, Protocol: {ip.p}')
    except Exception as e:
        print(f'Error processing packet: {e}')
