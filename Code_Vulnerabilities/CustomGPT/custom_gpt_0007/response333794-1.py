
import dpkt
import pcap

# Select the appropriate network interface
pc = pcap.pcap(name=None)  # use None to select the default interface
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

print("Starting packet sniffing...")

# Process packets
for timestamp, packet in pc:
    try:
        ether = dpkt.ethernet.Ethernet(packet)
        print(ether)
    except Exception as e:
        print(f"Error parsing packet: {e}")
