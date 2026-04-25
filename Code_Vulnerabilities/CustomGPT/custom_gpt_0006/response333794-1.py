
import dpkt
import pcap

# Initialize pcap
pc = pcap.pcap()
# Set filter for the desired IP address
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop through packets
for timestamp, packet in pc:
    try:
        # Attempt to parse the Ethernet packet
        eth = dpkt.ethernet.Ethernet(packet)
        print(f"Timestamp: {timestamp}, Packet: {eth}")
    except dpkt.dpkt.NeedData:
        # Handle case where packet is not complete
        print("Packet not complete, skipping...")
    except Exception as e:
        print(f"Error processing packet: {e}")
