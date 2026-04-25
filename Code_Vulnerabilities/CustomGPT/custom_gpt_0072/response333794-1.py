
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()  # Construct pcap object

# Set the filter for the specified IP address
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop through captured packets
for timestamp, packet in pc:
    try:
        ethernet = dpkt.ethernet.Ethernet(packet)
        # Check for IP in the Ethernet frame
        if isinstance(ethernet.payload, dpkt.ip.IP):
            ip = ethernet.payload
            print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}')
    except Exception as e:
        print(f'Error processing packet: {e}')
