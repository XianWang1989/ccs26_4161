
import pcap
import dpkt

# Create a pcap object for packet capturing
pc = pcap.pcap()

# Set the filter for specified IP address
filter_str = 'src host X.X.X.X or dst host X.X.X.X'
pc.setfilter(filter_str)

# Loop to capture packets
for timestamp, packet in pc:
    try:
        # Decode the ethernet frame
        eth = dpkt.ethernet.Ethernet(packet)

        # Print the decoded packet
        print(f'Timestamp: {timestamp}')
        print(eth)

    except Exception as e:
        print(f'Error parsing packet: {e}')
