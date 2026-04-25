
import dpkt
import pcap

def main():
    # Create pcap object
    pc = pcap.pcap()

    # Set filter for specific IP
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    print("Listening for packets...")

    for timestamp, packet in pc:
        try:
            # Parse Ethernet frame
            eth = dpkt.ethernet.Ethernet(packet)

            # Check if it contains an IP packet
            if isinstance(eth.data, dpkt.ip.IP):
                ip = eth.data
                print(f"Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}")
        except Exception as e:
            print(f"Error parsing packet: {e}")

if __name__ == '__main__':
    main()
