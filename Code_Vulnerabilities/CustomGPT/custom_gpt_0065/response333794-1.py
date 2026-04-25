
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()

# Set filter to capture traffic from/to specific IP (replace with actual IP)
pc.setfilter('host X.X.X.X')

print("Starting packet capture...")

# Capture packets
for timestamp, packet in pc:
    try:
        # Decode Ethernet frame
        eth = dpkt.ethernet.Ethernet(packet)
        print(eth)
    except Exception as e:
        print("Error processing packet: ", e)
