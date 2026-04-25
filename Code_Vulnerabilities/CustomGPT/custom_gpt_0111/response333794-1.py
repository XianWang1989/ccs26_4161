
import dpkt
import pcap

def packet_handler(timestamp, packet):
    try:
        eth = dpkt.ethernet.Ethernet(packet)
        print(f'Timestamp: {timestamp}, Ethernet Frame: {eth}')
    except Exception as e:
        print(f'Error handling packet: {e}')

def main():
    # Create pcap object
    pc = pcap.pcap()
    # Set filter for specific IP
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    print('Starting packet sniffing...')
    # Loop through packets
    for timestamp, packet in pc:
        packet_handler(timestamp, packet)

if __name__ == '__main__':
    main()
