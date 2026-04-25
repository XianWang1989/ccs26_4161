
import dpkt
import pcap

pc = pcap.pcap()  # Construct pcap object
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # Set filter for your specific hosts

try:
    for timestamp, packet in pc:
        eth = dpkt.ethernet.Ethernet(packet)  # Decode Ethernet packet

        # Check if it contains an IP packet and print it
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f'Timestamp: {timestamp}, Source IP: {ip.src}, Destination IP: {ip.dst}')
except Exception as e:
    print(f'Error: {e}')
