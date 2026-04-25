
import dpkt
import pcap

# Open the pcap object
pc = pcap.pcap()  # construct pcap object

# Set filter for a specific IP address
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop through captured packets
for timestamp, packet in pc:
    try:
        eth = dpkt.ethernet.Ethernet(packet)
        ip = eth.data  # This should typically be an IP packet
        if isinstance(ip, dpkt.ip.IP):
            print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}')
    except Exception as e:
        print(f'Error processing packet: {e}')
