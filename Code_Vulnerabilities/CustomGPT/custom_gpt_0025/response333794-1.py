
import dpkt
import pcap

# Set the IP address to filter
IP_ADDRESS = 'X.X.X.X'

def main():
    # Create a pcap object
    pc = pcap.pcap()

    # Set a filter for incoming and outgoing packets
    filter_str = f'src host {IP_ADDRESS} or dst host {IP_ADDRESS}'
    pc.setfilter(filter_str)

    print(f'Starting to sniff packets for {IP_ADDRESS}...')

    try:
        for timestamp, packet in pc:
            # Parse the Ethernet frame
            ethernet = dpkt.ethernet.Ethernet(packet)

            # Print packet details
            print(f'Timestamp: {timestamp}')
            print(ethernet)

    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    main()
