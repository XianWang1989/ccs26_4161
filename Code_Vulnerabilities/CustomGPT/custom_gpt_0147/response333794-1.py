
import dpkt
import pcap

# Function to handle capturing of packets
def packet_sniffer():
    try:
        pc = pcap.pcap()  # Create a pcap object
        # Set filter for the desired source or destination IP
        pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

        for timestamp, packet in pc:  # Iterate over captured packets
            eth = dpkt.ethernet.Ethernet(packet)  # Parse Ethernet
            # Only proceed if the packet contains an IP
            if isinstance(eth.data, dpkt.ip.IP):
                ip = eth.data
                print(f'Timestamp: {timestamp}, Source IP: {ip.src}, Destination IP: {ip.dst}, Protocol: {ip.p}')

    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    packet_sniffer()  # Start sniffing packets
