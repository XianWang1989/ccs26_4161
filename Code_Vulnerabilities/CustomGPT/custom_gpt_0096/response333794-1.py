
import dpkt
import pcap

# Create a pcap object to capture packets.
pc = pcap.pcap()

# Set the filter for the specified IP address.
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Start capturing packets.
for timestamp, packet in pc:
    try:
        # Parse the packet from Ethernet layer.
        eth = dpkt.ethernet.Ethernet(packet)
        # Print out the Ethernet frame.
        print(eth)
    except Exception as e:
        print(f"Error parsing packet: {e}")
