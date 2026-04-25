
import dpkt
import pcap

# Choose the correct network interface
# Replace 'en0' with your actual interface name if needed
interface = 'en0'
pc = pcap.pcap(name=interface)

# Set a filter to capture packets from/to the specified IP address
filter_string = 'src host X.X.X.X or dst host X.X.X.X'
pc.setfilter(filter_string)

try:
    print("Starting packet capture on {}...".format(interface))
    for timestamp, packet in pc:
        eth = dpkt.ethernet.Ethernet(packet)
        print(eth)
except Exception as e:
    print("An error occurred: {}".format(e))
