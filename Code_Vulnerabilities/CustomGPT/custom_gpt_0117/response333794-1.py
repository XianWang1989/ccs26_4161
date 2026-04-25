
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()

# Set the filter to capture packets from a specific host
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

print("Capturing packets...")

try:
    for timestamp, packet in pc:
        eth = dpkt.ethernet.Ethernet(packet)
        ip = eth.data

        # Check if the packet contains an IP layer
        if isinstance(ip, dpkt.ip.IP):
            print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}')
except KeyboardInterrupt:
    print("Stopped capturing packets.")
