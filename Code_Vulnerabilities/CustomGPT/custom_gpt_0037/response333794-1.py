
import dpkt
import pcap

# Create pcap object
pc = pcap.pcap()  # This captures packets from the default interface

# Set the filter (adjust X.X.X.X to your target IP)
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop to process packets
for timestamp, packet in pc:
    try:
        eth = dpkt.ethernet.Ethernet(packet)
        ip = eth.data  # Access the IP layer
        print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}')
    except (dpkt.dpkt.NeedData, IndexError):
        continue  # Handle any parsing errors
