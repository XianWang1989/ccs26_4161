
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()

# Set the filter for the desired IP address
filter_expression = 'src host X.X.X.X or dst host X.X.X.X'
pc.setfilter(filter_expression)

# Start sniffing packets
try:
    for timestamp, packet in pc:
        # Parse the Ethernet frame
        ethernet = dpkt.ethernet.Ethernet(packet)

        # Check for IP packets
        if isinstance(ethernet.data, dpkt.ip.IP):
            ip = ethernet.data
            print(f'Timestamp: {timestamp}, Source IP: {ip.src}, Destination IP: {ip.dst}, Length: {len(packet)}')
except Exception as e:
    print(f'Error: {e}')
