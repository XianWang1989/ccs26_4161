
import dpkt
import pcap

# Create a pcap object and specify the interface
pc = pcap.pcap(name=None)  # None uses the default interface
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

print("Starting to sniff packets...\n")

# Loop to read packets
for timestamp, packet in pc:
    ether = dpkt.ethernet.Ethernet(packet)
    # Check if the packet contains an IP layer
    if isinstance(ether.data, dpkt.ip.IP):
        ip = ether.data
        print("Time: {}, Source: {}, Destination: {}".format(timestamp, ip.src, ip.dst))
    else:
        print("Non-IP Packet: {}".format(ether.data))
