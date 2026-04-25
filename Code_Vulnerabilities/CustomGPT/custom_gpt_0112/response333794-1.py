
import dpkt
import pcap

# Construct pcap object
pc = pcap.pcap()
# Set your filter
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

print("Starting packet capture...")
for timestamp, packet in pc:
    try:
        # Parse Ethernet frame
        eth = dpkt.ethernet.Ethernet(packet)
        print(f'Timestamp: {timestamp}, Source: {eth.src}, Destination: {eth.dst}')

        # Optional: Further decode packet types (e.g., IP, TCP)
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f'IP source: {ip.src}, IP destination: {ip.dst}')
    except Exception as e:
        print(f'Error processing packet: {e}')
