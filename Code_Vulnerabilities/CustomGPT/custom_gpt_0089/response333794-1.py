
import pcap
import dpkt

# Create a pcap object
pc = pcap.pcap()

# Set the filter for the specified IP address
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop through captured packets
for timestamp, packet in pc:
    try:
        # Parse the ethernet frame
        eth = dpkt.ethernet.Ethernet(packet)
        print(f'Timestamp: {timestamp}, Ethernet Frame: {eth}')
    except Exception as e:
        print(f'Error parsing packet: {e}')
