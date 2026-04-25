
import dpkt
import pcap

def main():
    # Construct pcap object
    pc = pcap.pcap()

    # Set filter to capture packets for the specified IP address
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    # Loop through packets
    for timestamp, packet in pc:
        try:
            eth = dpkt.ethernet.Ethernet(packet)
            # Check for IP packets
            if isinstance(eth.data, dpkt.ip.IP):
                ip = eth.data
                print(f'Timestamp: {timestamp}, Source: {dpkt.utils.inet_to_str(ip.src)}, Destination: {dpkt.utils.inet_to_str(ip.dst)}')
        except Exception as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    main()
