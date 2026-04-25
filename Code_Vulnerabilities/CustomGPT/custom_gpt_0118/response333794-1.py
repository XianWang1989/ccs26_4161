
import dpkt
import pcap

# Initialize pcap object
pc = pcap.pcap()

# Set the filter for the specific IP address
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Start sniffing
for timestamp, packet in pc:
    try:
        eth = dpkt.ethernet.Ethernet(packet)  # Parse Ethernet frame
        ip = eth.data  # Get the IP layer
        if isinstance(ip, dpkt.ip.IP):  # Check if it is an IP packet
            print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}')
    except Exception as e:
        print(f'Error: {e}')
