
import dpkt
import pcap

def packet_sniffer():
    pc = pcap.pcap()  # Create pcap object
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # Set filter

    for timestamp, packet in pc:
        try:
            eth = dpkt.ethernet.Ethernet(packet)
            print(f'Timestamp: {timestamp}')
            print(eth)
        except (dpkt.dpkt.NeedData, IndexError) as e:
            print(f'Error processing packet: {e}')

if __name__ == "__main__":
    packet_sniffer()
