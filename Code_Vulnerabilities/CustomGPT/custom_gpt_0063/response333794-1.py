
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()

# Set the filter for specific IP addresses
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Start sniffing packets
for timestamp, packet in pc:
    try:
        # Parse the ethernet frame
        eth = dpkt.ethernet.Ethernet(packet)

        # Check if it's an IP packet
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}')
    except Exception as e:
        print(f'Error processing packet: {e}')
