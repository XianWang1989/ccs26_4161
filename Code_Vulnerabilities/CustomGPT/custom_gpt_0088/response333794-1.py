
import dpkt
import pcap

# Create a pcap instance
pc = pcap.pcap()

# Set the packet filter for the desired IP
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop to capture packets
for timestamp, packet in pc:
    try:
        # Parse the Ethernet frame
        eth = dpkt.ethernet.Ethernet(packet)
        # Print source and destination MAC addresses
        print(f"Source MAC: {eth.src}, Destination MAC: {eth.dst}")

        # Additional parsing for IP packets if needed
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f"Source IP: {ip.src}, Destination IP: {ip.dst}")
    except dpkt.dpkt.UnpackError:
        print("Could not unpack the packet")
