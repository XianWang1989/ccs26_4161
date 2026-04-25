
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()

# Set the filter for source or destination IP
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop through captured packets
for timestamp, packet in pc:
    try:
        # Parse the Ethernet frame
        eth = dpkt.ethernet.Ethernet(packet)

        # Extract IP packet
        ip = eth.data

        # Print source and destination IPs
        print(f'Timestamp: {timestamp}')
        print(f'Source IP: {ip.src}')
        print(f'Destination IP: {ip.dst}')
    except dpkt.dpkt.NeedData:
        continue
    except Exception as e:
        print(f'Error: {e}')
