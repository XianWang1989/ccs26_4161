
import dpkt
import pcap

# Construct pcap object
pc = pcap.pcap()

# Set a filter for specific source or destination IP
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

print("Starting packet sniffing...")

try:
    for timestamp, packet in pc:
        # Parse the Ethernet frame
        eth = dpkt.ethernet.Ethernet(packet)

        # Check for IP layer
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print('Timestamp: {} | Source: {} | Destination: {}'.format(
                timestamp, 
                ip.src, 
                ip.dst
            ))
except KeyboardInterrupt:
    print("Stopped by user.")
