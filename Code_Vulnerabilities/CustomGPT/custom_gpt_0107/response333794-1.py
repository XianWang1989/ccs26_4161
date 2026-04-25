
import dpkt
import pcap

# Create a pcap object and specify the device to use
pc = pcap.pcap(name=None)  # None uses the default device
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # Replace with your IP

try:
    for timestamp, packet in pc:
        # Parse the packet
        eth = dpkt.ethernet.Ethernet(packet)
        print(f'Time: {timestamp}, Packet: {eth}')
except Exception as e:
    print(f'An error occurred: {e}')
