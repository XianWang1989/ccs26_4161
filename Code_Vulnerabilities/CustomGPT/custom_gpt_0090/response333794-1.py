
import pcap
import dpkt

# Create a pcap object
pc = pcap.pcap()

# Set a filter for specific IP addresses
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Start sniffing packets
try:
    for timestamp, packet in pc:
        eth = dpkt.ethernet.Ethernet(packet)
        print(eth)
except Exception as e:
    print(f"Error: {e}")
