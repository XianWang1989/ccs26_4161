
import dpkt
import pcap

# Create pcap object
pc = pcap.pcap(name=None)  # Use default interface; set name to None for this

# Set the filter to capture the desired packets
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # Replace with actual IPs

# Loop through captured packets
for timestamp, packet in pc:
    try:
        eth = dpkt.ethernet.Ethernet(packet)
        print('Captured packet: {}'.format(eth))
    except dpkt.dpkt.NeedData:
        print('Incomplete packet data')
    except Exception as e:
        print(f'Error processing packet: {e}')
