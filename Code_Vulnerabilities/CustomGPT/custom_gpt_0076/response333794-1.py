
import pcap
import dpkt

def packet_sniffer():
    # Create a pcap object
    pc = pcap.pcap()

    # Set a filter for the specific IP address
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    print("Listening for packets...")

    # Loop through incoming packets
    for timestamp, packet in pc:
        # Parse the Ethernet packet
        eth = dpkt.ethernet.Ethernet(packet)

        # Check if the packet has an IP layer
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}')
        else:
            print("Non-IP Packet detected")

if __name__ == "__main__":
    packet_sniffer()
