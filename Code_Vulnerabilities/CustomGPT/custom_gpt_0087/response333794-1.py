
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()     
# Set a filter for specific source or destination IP addresses
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Start sniffing packets
for timestamp, packet in pc:
    ethernet = dpkt.ethernet.Ethernet(packet)
    print(ethernet)
