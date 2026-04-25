
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()

# Set the filter for the desired host
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Start sniffing packets
try:
    for timestamp, packet in pc:
        # Decode the Ethernet packet
        eth = dpkt.ethernet.Ethernet(packet)
        # Print the packet details
        print(eth)
except Exception as e:
    print("An error occurred: ", e)
