
import dpkt
import pcap

def packet_callback(timestamp, packet):
    # Parse Ethernet frame
    eth = dpkt.ethernet.Ethernet(packet)
    print(f'Timestamp: {timestamp}, Ethernet Frame: {eth}')

    # Here you can add more parsing based on the protocols (IP, TCP, etc.)
    if isinstance(eth.data, dpkt.ip.IP):
        ip = eth.data
        print(f'IP Packet: {ip}')

        if isinstance(ip.data, dpkt.tcp.TCP):
            tcp = ip.data
            print(f'TCP Segment: {tcp}')

def main():
    # Construct pcap object
    pc = pcap.pcap(name=None, promisc=True, immediate=True, timeout_ms=50)

    # Set the filter for the specific address
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    # Start capturing packets
    try:
        print('Starting packet capture...')
        for timestamp, packet in pc:
            packet_callback(timestamp, packet)
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()
