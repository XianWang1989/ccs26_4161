
import dpkt
import pcap

def packet_sniffer():
    # Create a pcap object
    pc = pcap.pcap()

    # Set the filter for specific host IPs
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    print("Sniffing packets:")
    try:
        for timestamp, packet in pc:
            # Parse Ethernet frame
            eth = dpkt.ethernet.Ethernet(packet)
            # Check if it's IPv4
            if isinstance(eth.data, dpkt.ip.IP):
                ip = eth.data
                print(f'Timestamp: {timestamp}, Src: {ip.src}, Dst: {ip.dst}, Protocol: {ip.p}')
            else:
                print('Non-IP packet')
    except KeyboardInterrupt:
        print("Exiting packet sniffer.")

if __name__ == "__main__":
    packet_sniffer()
