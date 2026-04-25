
import dpkt
import pcap

# Construct pcap object
pc = pcap.pcap()
# Set the filter to capture packets from or to a specific IP address
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Start sniffing packets
for timestamp, packet in pc:
    try:
        # Parse the Ethernet packet
        eth = dpkt.ethernet.Ethernet(packet)
        # Check if the packet has an IP layer
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f'Timestamp: {timestamp}, Source IP: {ip.src}, Destination IP: {ip.dst}, Protocol: {ip.p}')
    except Exception as e:
        print(f'Error processing packet: {e}')
