
import dpkt
import pcap

def packet_sniffer():
    try:
        # Create a pcap object
        pc = pcap.pcap()

        # Set a filter for specific IP
        pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

        # Loop through packets
        for timestamp, packet in pc:
            eth = dpkt.ethernet.Ethernet(packet)
            print(f'Timestamp: {timestamp}, Packet: {eth}')

    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    packet_sniffer()
