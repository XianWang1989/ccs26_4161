
import dpkt
import pcap

def main():
    pc = pcap.pcap()  # Construct pcap object

    # Set the filter for the desired host
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    print("Listening for packets...")

    for timestamp, packet in pc:
        try:
            eth = dpkt.ethernet.Ethernet(packet)
            ip = eth.data
            print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Length: {len(packet)}')
        except (dpkt.dpkt.NeedData, IndexError):
            continue

if __name__ == "__main__":
    main()
