
import dpkt
import pcap

# Initialize pcap object
pc = pcap.pcap()

# Set the filter for the specific IP address
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Start sniffing packets
try:
    print("Starting packet capture...")
    for timestamp, packet in pc:
        eth = dpkt.ethernet.Ethernet(packet)

        # Check for IP packets
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print('Timestamp: {}, Source: {}, Destination: {}'.format(
                timestamp, 
                dpkt.utils.inet_to_str(ip.src), 
                dpkt.utils.inet_to_str(ip.dst)
            ))
except Exception as e:
    print(f"An error occurred: {e}")
