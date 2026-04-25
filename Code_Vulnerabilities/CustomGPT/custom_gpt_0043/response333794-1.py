
import dpkt
import pcap

# Change 'en0' to the correct interface if needed
interface = 'en0'
pc = pcap.pcap(name=interface)  # construct pcap object

# Set a filter for packets from/to a specific IP address
filter_rule = 'src host X.X.X.X or dst host X.X.X.X'
pc.setfilter(filter_rule)

print("Listening on interface:", interface)
try:
    for timestamp, packet in pc:
        eth = dpkt.ethernet.Ethernet(packet)  # Parse Ethernet packet
        print(eth)  # Print the entire Ethernet packet
except Exception as e:
    print("An error occurred: ", e)
