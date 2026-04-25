
import dpkt
import pcap

def main():
    # Construct pcap object and set filter
    pc = pcap.pcap()
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    print("Starting packet capture...")

    # Loop to process packets
    for timestamp, packet in pc:
        try:
            eth = dpkt.ethernet.Ethernet(packet)
            ip = eth.data
            # Print source and destination IP addresses
            print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}')
        except Exception as e:
            print(f'Error processing packet: {e}')

if __name__ == "__main__":
    main()
