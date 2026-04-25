
import dpkt
import pcap

# Specify your network interface here
interface = 'en0'  # Change this to your interface (use 'ifconfig' to find)

# Create a pcap object with the specified interface
pc = pcap.pcap(interface)     
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Sniff packets
for timestamp, packet in pc:
    eth_packet = dpkt.ethernet.Ethernet(packet)
    print(eth_packet)
