
import dpkt
import pcap

# Construct pcap object
pc = pcap.pcap()

# Set your filter for specific IP addresses
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop to capture packets
for timestamp, packet in pc:
    try:
        # Parse Ethernet frame
        eth = dpkt.ethernet.Ethernet(packet)

        # Print packet information
        print(f'Timestamp: {timestamp}')
        print(eth)

        # Additional parsing for IP packets
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f'IP Source: {ip.src}, IP Destination: {ip.dst}')
    except Exception as e:
        print(f'Error processing packet: {e}')
