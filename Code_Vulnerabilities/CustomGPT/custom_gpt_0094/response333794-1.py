
import dpkt
import pcap

# Construct pcap object
pc = pcap.pcap()
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop through captured packets
for timestamp, packet in pc:
    try:
        # Parse the Ethernet packet
        ethernet = dpkt.ethernet.Ethernet(packet)
        # Print source and destination MAC addresses
        print(f"Timestamp: {timestamp}")
        print(f"Source MAC: {ethernet.src.hex()}")
        print(f"Destination MAC: {ethernet.dst.hex()}")
    except Exception as e:
        print(f"Error processing packet: {e}")
