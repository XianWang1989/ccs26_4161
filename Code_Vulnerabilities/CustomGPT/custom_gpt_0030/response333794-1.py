
import pcap
import dpkt

# Function to process packets
def packet_handler(timestamp, packet):
    try:
        eth = dpkt.ethernet.Ethernet(packet)
        print(f'Timestamp: {timestamp}, Ethernet Frame: {eth}')
    except Exception as e:
        print(f'Error processing packet: {e}')

# Main function to set up the sniffer
def main():
    try:
        # Create a pcap object and set the appropriate filter
        pc = pcap.pcap()
        pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # Replace with valid IP

        print("Sniffing packets...")
        # Start sniffing packets
        for timestamp, packet in pc:
            packet_handler(timestamp, packet)
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()
