
import dpkt
import pcap
import sys

def main():
    try:
        # Create pcap object
        pc = pcap.pcap(name='en0')  # Change 'en0' to your active interface
        pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

        print("Listening for packets...")

        for timestamp, packet in pc:
            ether = dpkt.ethernet.Ethernet(packet)  # Parse the packet
            print(f'Time: {timestamp}, Packet: {ether}')

    except Exception as e:
        print(f'An error occurred: {e}')
        sys.exit(1)

if __name__ == "__main__":
    main()
