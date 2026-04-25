
import dpkt
import pcap

# Initialize pcap object
pc = pcap.pcap() 
# Set filter for the specific host
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop through the packets
for timestamp, packet in pc:
    try:
        # Parse the Ethernet packet
        eth = dpkt.ethernet.Ethernet(packet)
        # Print the source and destination MAC addresses
        print(f"Timestamp: {timestamp}, Source: {eth.src.hex()}, Destination: {eth.dst.hex()}")
    except Exception as e:
        print(f"Error parsing packet: {e}")
