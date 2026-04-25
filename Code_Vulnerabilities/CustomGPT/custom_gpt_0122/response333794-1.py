
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()

# Set the filter for the desired host
filter_str = 'src host X.X.X.X or dst host X.X.X.X'
pc.setfilter(filter_str)

try:
    print("Listening on network for packets...")
    for timestamp, packet in pc:
        # Parse Ethernet frame
        eth = dpkt.ethernet.Ethernet(packet)
        print(f'Timestamp: {timestamp}, Ethernet Frame: {eth}')
except Exception as e:
    print(f"An error occurred: {e}")
