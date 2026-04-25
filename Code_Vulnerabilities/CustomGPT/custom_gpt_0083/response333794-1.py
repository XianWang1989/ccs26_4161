
import dpkt
import pcap

# Create a pcap object and set the filter
pc = pcap.pcap()
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Start sniffing
try:
    for timestamp, packet in pc:
        # Parse the Ethernet frame
        eth = dpkt.ethernet.Ethernet(packet)
        print(f'Timestamp: {timestamp}')
        print(f'Destination: {eth.dst}')
        print(f'Source: {eth.src}')
        print(f'Type: {eth.type}')
except Exception as e:
    print(f'Error: {e}')
