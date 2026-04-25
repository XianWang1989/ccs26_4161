
import dpkt
import pcap

# Construct pcap object
pc = pcap.pcap()
# Set filter for the desired IP address
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

try:
    for timestamp, packet in pc:
        eth = dpkt.ethernet.Ethernet(packet)
        # Check if the Ethernet packet has an IP layer
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f'Timestamp: {timestamp}, Source IP: {ip.src}, Destination IP: {ip.dst}')
except Exception as e:
    print(f'Error: {e}')
