
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()

# Set the filter for source and destination IP
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

try:
    print("Listening for packets...")
    for timestamp, packet in pc:
        eth = dpkt.ethernet.Ethernet(packet)
        # Check for IP packets
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f'Timestamp: {timestamp}, Source IP: {ip.src}, Destination IP: {ip.dst}, Protocol: {ip.p}')
except Exception as e:
    print(f"An error occurred: {e}")
