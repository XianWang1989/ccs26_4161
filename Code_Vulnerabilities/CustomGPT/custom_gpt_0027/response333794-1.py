
import dpkt
import pcap

# Create a pcap object and set the filter
pc = pcap.pcap()
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # Replace with your IP

print("Starting packet capture...")

# Loop through packets
for timestamp, packet in pc:
    try:
        eth = dpkt.ethernet.Ethernet(packet)
        ip = eth.data
        print(f'Time: {timestamp}, Src: {ip.src}, Dst: {ip.dst}, Protocol: {ip.p}')
    except (dpkt.dpkt.NeedData, IndexError):
        continue
