
import dpkt
import pcap

# Function to process packets
def process_packet(ts, pkt):
    try:
        eth = dpkt.ethernet.Ethernet(pkt)
        print(f'Timestamp: {ts}, Packet: {eth}')
    except Exception as e:
        print(f'Error processing packet: {e}')

# Create pcap object
pc = pcap.pcap()

# Set a filter for specific host
filter_rule = 'src host X.X.X.X or dst host X.X.X.X'
pc.setfilter(filter_rule)

print(f'Starting packet capture on filter: {filter_rule}')

# Capture packets
for timestamp, packet in pc:
    process_packet(timestamp, packet)
