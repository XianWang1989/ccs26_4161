
import dpkt
import pcap

# Set your network interface here (e.g., 'en0' for Wi-Fi)
interface = 'en0'
# Create pcap object, specifying the interface
pc = pcap.pcap(name=interface)
# Set the filter for the packets
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

print("Listening for packets on {}...".format(interface))

# Start sniffing packets
for timestamp, packet in pc:
    try:
        eth = dpkt.ethernet.Ethernet(packet)
        ip = eth.data
        if isinstance(ip, dpkt.ip.IP):
            print("Timestamp: {}, Source: {}, Destination: {}".format(
                timestamp, 
                dpkt.utils.inet_to_str(ip.src), 
                dpkt.utils.inet_to_str(ip.dst)
            ))
    except (dpkt.dpkt.NeedData, IndexError):
        continue
