
import dpkt
import pcap

# Create pcap object on a specific interface, e.g., 'en0'
pc = pcap.pcap(name='en0')  
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

for timestamp, packet in pc:
    eth = dpkt.ethernet.Ethernet(packet)
    print(eth)
