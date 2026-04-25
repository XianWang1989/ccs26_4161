
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()

# Set a filter for the desired IP address
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Start sniffing packets
try:
    for timestamp, packet in pc:
        # Parse the Ethernet frame
        eth = dpkt.ethernet.Ethernet(packet)

        # Check if the packet has an IP layer
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f'Timestamp: {timestamp}, Source: {ip.src.encode("hex")}, Destination: {ip.dst.encode("hex")}')
except Exception as e:
    print(f'Error: {e}')
