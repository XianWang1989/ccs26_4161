
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()

# Set filter for specific IP address
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

print("Listening for packets...")

# Loop through captured packets
for timestamp, packet in pc:
    try:
        # Parse the Ethernet frame
        eth = dpkt.ethernet.Ethernet(packet)

        # Check if the packet has an IP layer
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f"Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}")
    except Exception as e:
        print(f"Error processing packet: {e}")
