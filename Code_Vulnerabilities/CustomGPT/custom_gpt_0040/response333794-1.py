
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()     
# Set filter for specified source and destination IP
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

print("Listening for packets...")
for timestamp, packet in pc:
    try:
        # Unpack the Ethernet frame
        eth = dpkt.ethernet.Ethernet(packet)
        # Check if the packet has an IP layer
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f'Timestamp: {timestamp}')
            print(f'Source: {ip.src}')
            print(f'Destination: {ip.dst}')
            print(f'Protocol: {ip.p}')
    except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
        print("Error unpacking packet")
