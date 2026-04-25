
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()

# Set filter for specific IP
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

print("Listening for packets...")

# Loop through captured packets
for timestamp, packet in pc:
    try:
        eth = dpkt.ethernet.Ethernet(packet)
        print(eth)  # Display the Ethernet frame
    except Exception as e:
        print("Error processing packet: {}".format(e))
