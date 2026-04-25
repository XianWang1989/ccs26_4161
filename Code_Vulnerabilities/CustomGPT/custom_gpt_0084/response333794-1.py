
import dpkt
import pcap

# Construct pcap object
pc = pcap.pcap()

# Set filter for specific IP
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Start sniffing packets
for timestamp, packet in pc:
    try:
        eth = dpkt.ethernet.Ethernet(packet)
        ip = eth.data
        print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}')
    except (dpkt.dpkt.NeedData, AttributeError):
        continue  # Continue if there's an error in parsing
