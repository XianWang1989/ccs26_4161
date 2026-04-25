
import dpkt
import pcap

def main():
    # Construct pcap object
    pc = pcap.pcap()
    # Set filter for the pcap object
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    print("Listening for packets...")

    # Loop through packets
    for timestamp, packet in pc:
        try:
            # Parse Ethernet frame
            eth = dpkt.ethernet.Ethernet(packet)
            # Only process IP packets
            if isinstance(eth.data, dpkt.ip.IP):
                ip = eth.data
                print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Length: {len(packet)} bytes')
        except (dpkt.dpkt.NeedData, IndexError):
            continue  # Skip packets that cannot be parsed

if __name__ == "__main__":
    main()
