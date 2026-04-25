
import dpkt
import pcap

def packet_handler(timestamp, packet):
    # Handle the packet and try to decode it
    try:
        eth = dpkt.ethernet.Ethernet(packet)
        # Check if the packet is an IP packet
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}')
    except Exception as e:
        print(f'Error processing packet: {e}')

def main():
    # Create a pcap object
    pc = pcap.pcap()
    # Set a filter for packets coming from/to a specific host
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    # Start capturing packets
    try:
        print("Listening for packets...")
        for timestamp, packet in pc:
            packet_handler(timestamp, packet)
    except KeyboardInterrupt:
        print("Stopped packet capture")

if __name__ == "__main__":
    main()
