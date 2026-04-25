
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()     
# Set a filter for the desired source or destination IP
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop over captured packets
for timestamp, packet in pc:
    try:
        eth = dpkt.ethernet.Ethernet(packet)
        ip = eth.data

        # Check if the packet is an IP packet
        if isinstance(ip, dpkt.ip.IP):
            print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}')
    except Exception as e:
        print(f'Error processing packet: {e}')
