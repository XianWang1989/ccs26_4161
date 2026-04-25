
import dpkt
import pcap

try:
    pc = pcap.pcap()  # construct pcap object
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # Set your IP filter

    print("Listening on IP:", pc)
    for timestamp, packet in pc:
        # Parse the Ethernet header and the packet
        eth = dpkt.ethernet.Ethernet(packet)
        print(f'Timestamp: {timestamp}, Packet: {eth}')

except Exception as e:
    print(f"An error occurred: {e}")
