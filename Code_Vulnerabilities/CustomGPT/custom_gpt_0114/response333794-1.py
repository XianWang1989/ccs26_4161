
import dpkt
import pcap

def packet_sniffer():
    pc = pcap.pcap()  # Construct pcap object
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # Replace X.X.X.X with your IP

    for timestamp, packet in pc:
        eth = dpkt.ethernet.Ethernet(packet)
        # Checking if it's an IP packet
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Length: {len(packet)} bytes')

if __name__ == '__main__':
    packet_sniffer()
