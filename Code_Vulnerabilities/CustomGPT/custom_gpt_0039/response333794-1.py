
import dpkt
import pcap

def packet_handler(timestamp, packet):
    # Parse the Ethernet packet
    eth = dpkt.ethernet.Ethernet(packet)
    print(f'Timestamp: {timestamp}')
    print(eth)

# Create a pcap object
pc = pcap.pcap()
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Start sniffing packets
print("Starting packet sniffing...")
pc.loop(packet_handler)  # Use the loop method with a handler
