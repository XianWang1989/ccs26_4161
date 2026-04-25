
import dpkt
import pcap

# Adjust this to your network interface
interface = 'en0'  # Change to your relevant interface

# Create a pcap object and set a filter
pc = pcap.pcap(name=interface)  
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # Replace with your IP

# Sniff packets
for timestamp, packet in pc:
    eth = dpkt.ethernet.Ethernet(packet)
    if isinstance(eth.data, dpkt.ip.IP):
        ip = eth.data
        print(f'Timestamp: {timestamp} | Source IP: {ip.src} | Destination IP: {ip.dst} | Protocol: {ip.p}')
