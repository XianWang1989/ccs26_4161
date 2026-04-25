
import dpkt
import pcap

# Create pcap object
pc = pcap.pcap()
# Set filter for specific source or destination IP
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

print("Starting packet capture...")

# Loop to read packets
for timestamp, packet in pc:
    try:
        # Decode the Ethernet packet
        ethernet = dpkt.ethernet.Ethernet(packet)
        # Print the decoded packet
        print(ethernet)
    except Exception as e:
        print(f"Error decoding packet: {e}")
