
import dpkt
import pcap

def main():
    # Create pcap object to capture packets
    pc = pcap.pcap()

    # Set a filter for specific IP addresses
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    print("Listening for packets...")

    # Iterate over captured packets
    for timestamp, packet in pc:
        try:
            eth = dpkt.ethernet.Ethernet(packet)  # Decode Ethernet packet
            print(f'Time: {timestamp}, Source: {eth.src}, Destination: {eth.dst}, Type: {eth.type}')
            # Further processing can be done here (e.g., IP analysis)
        except Exception as e:
            print(f'Error processing packet: {e}')

if __name__ == "__main__":
    main()
