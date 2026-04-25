
import dpkt
import pcap

# Construct pcap object
pc = pcap.pcap()     
# Set filter for specified IP address
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

try:
    for timestamp, packet in pc:
        # Decode Ethernet frame
        eth = dpkt.ethernet.Ethernet(packet)
        print(eth)
except Exception as e:
    print(f"An error occurred: {e}")
