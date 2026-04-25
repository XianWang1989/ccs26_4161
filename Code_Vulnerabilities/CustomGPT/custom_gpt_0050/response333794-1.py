
import dpkt
import pcap

# Open the pcap object on a specific device
pc = pcap.pcap()
# Set a filter for specific IP addresses
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

print("Listening for packets...")

# Loop through captured packets
for timestamp, packet in pc:
    try:
        ethernet_frame = dpkt.ethernet.Ethernet(packet)
        # Print the Ethernet frame
        print(ethernet_frame)
    except dpkt.dpkt.NeedData:
        print("Not enough data in packet")
