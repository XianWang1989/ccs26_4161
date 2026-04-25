
import dpkt
import pcap

def main():
    # Initialize pcap object
    pc = pcap.pcap()

    # Set a filter for the specified IP addresses
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    print("Listening for packets...")

    for timestamp, packet in pc:
        try:
            # Parse the packet using dpkt
            eth = dpkt.ethernet.Ethernet(packet)
            # Check if it's an IP packet
            if isinstance(eth.data, dpkt.ip.IP):
                ip = eth.data
                print(f'Time: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}')
            else:
                print("Not an IP packet")
        except Exception as e:
            print(f"Error processing packet: {e}")

if __name__ == "__main__":
    main()
