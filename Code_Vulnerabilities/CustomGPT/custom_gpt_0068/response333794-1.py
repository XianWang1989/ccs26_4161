
import dpkt
import pcap

# Make sure your interface is correct
pc = pcap.pcap(name=None)  # Use None to select default interface
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop over packets
for timestamp, packet in pc:
    try:
        eth = dpkt.ethernet.Ethernet(packet)  # Parse the Ethernet frame
        print(eth)  # Print the Ethernet frame
    except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError) as e:
        print("Packet could not be parsed:", e)
