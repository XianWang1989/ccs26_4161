
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()

# Set a filter for specific source and destination IPs
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop through the packets captured
try:
    for timestamp, packet in pc:
        # Decode the Ethernet packet
        eth = dpkt.ethernet.Ethernet(packet)

        # Print packet details
        print(f'Timestamp: {timestamp}')
        print(f'Ethernet Frame: {eth}')
except Exception as e:
    print(f'Error: {e}')
