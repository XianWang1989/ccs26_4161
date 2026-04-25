
import dpkt
import pcap

def main():
    # Create a pcap object.
    pc = pcap.pcap()

    # Set the filter for the source or destination host.
    filter_str = 'src host X.X.X.X or dst host X.X.X.X'
    pc.setfilter(filter_str)

    print(f"Listening on: {filter_str}")

    # Continuous loop to capture packets.
    try:
        for timestamp, packet in pc:
            # Decode the Ethernet packet.
            eth = dpkt.ethernet.Ethernet(packet)

            # Check if the packet has an IP layer.
            if isinstance(eth.data, dpkt.ip.IP):
                ip = eth.data
                print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Length: {len(ip.data)}')

            else:
                print(f'Timestamp: {timestamp}, Non-IP Packet captured.')
    except KeyboardInterrupt:
        print("Packet capture stopped.")

if __name__ == "__main__":
    main()
