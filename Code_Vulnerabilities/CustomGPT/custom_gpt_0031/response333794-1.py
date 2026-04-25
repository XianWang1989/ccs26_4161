
import pcap
import dpkt

# Create a pcap object
pc = pcap.pcap()

# Set a filter for the specified IP address
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

try:
    # Iterate through captured packets
    for timestamp, packet in pc:
        # Decode the Ethernet packet
        eth = dpkt.ethernet.Ethernet(packet)

        # Check for IP layer and print relevant information
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print('Timestamp: {}, Source: {}, Destination: {}'.format(
                timestamp, 
                ip.src, 
                ip.dst
            ))

except Exception as e:
    print('Error: {}'.format(e))
