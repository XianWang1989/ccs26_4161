
import dpkt
import pcap

def main():
    # Construct pcap object
    pc = pcap.pcap()     
    # Set filter for capturing packets
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    print("Listening on network...")

    for timestamp, packet in pc:
        try:
            # Parse the Ethernet packet
            eth = dpkt.ethernet.Ethernet(packet)
            print(f'Timestamp: {timestamp}, Packet: {eth}')
        except Exception as e:
            print(f"Error parsing packet: {e}")

if __name__ == "__main__":
    main()
