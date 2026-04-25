
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()
# Set the filter for the desired IP
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop through captured packets
for timestamp, packet in pc:
    try:
        # Parse the Ethernet frame
        eth = dpkt.ethernet.Ethernet(packet)
        # Print out the Ethernet frame
        print(eth)
    except Exception as e:
        print(f"Error processing packet: {e}")
