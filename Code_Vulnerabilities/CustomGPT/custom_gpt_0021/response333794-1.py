
import dpkt
import pcap

def main():
    # Initialize pcap object
    pc = pcap.pcap()

    # Set the filter for capturing specific traffic
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    try:
        for timestamp, packet in pc:
            # Parse the Ethernet frame
            eth = dpkt.ethernet.Ethernet(packet)

            # Check for IP packets
            if isinstance(eth.data, dpkt.ip.IP):
                ip = eth.data
                print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}')
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
