
import dpkt
import pcap

def main():
    try:
        # Create a pcap object
        pc = pcap.pcap()

        # Set a filter for the specific source or destination IP
        pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

        print("Listening for packets...")
        for timestamp, packet in pc:
            # Parse the packet using dpkt
            eth = dpkt.ethernet.Ethernet(packet)
            ip = eth.data
            if isinstance(ip, dpkt.ip.IP):
                print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Length: {len(packet)}')
            else:
                print(f'Timestamp: {timestamp}, Non-IP packet received.')

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
