
import dpkt
import pcap

# Create the pcap object
pc = pcap.pcap()     
# Set the filter for the desired host
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Process packets
for timestamp, packet in pc:
    try:
        eth = dpkt.ethernet.Ethernet(packet)
        print(f'Timestamp: {timestamp}, src: {eth.src}, dst: {eth.dst}')
    except Exception as e:
        print(f'Error processing packet: {e}')
