
import dpkt
import pcap

# Specify the network interface (e.g., 'en0' for Wi-Fi or 'en1' for Ethernet)
interface = 'en0'

# Create pcap object
pc = pcap.pcap(name=interface)  
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Start sniffing packets
for timestamp, packet in pc:
    try:
        eth = dpkt.ethernet.Ethernet(packet)
        print(eth)  # Use parentheses for print
    except Exception as e:
        print("Error processing packet: {}".format(e))
