
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()

# Set the filter for the desired host IP address
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop through packets
for timestamp, packet in pc:
    try:
        # Parse the Ethernet packet
        eth = dpkt.ethernet.Ethernet(packet)

        # Print out the packet details
        print(f'Time: {timestamp}, Packet: {eth}')

        # Check if it's an IP packet
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f'IP Source: {ip.src}, IP Destination: {ip.dst}')
    except Exception as e:
        print(f'Error processing packet: {e}')
