
import dpkt
import pcap

def sniff_packets():
    # Create a pcap object
    pc = pcap.pcap()
    # Set filter for capturing packets from/to a specific IP address
    pc.setfilter('src host 192.168.1.1 or dst host 192.168.1.1')

    print("Listening for packets...")
    for timestamp, packet in pc:
        eth = dpkt.ethernet.Ethernet(packet)
        # Check if it's an IP packet
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f'Time: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}'
                  f', Length: {len(packet)}')

if __name__ == "__main__":
    sniff_packets()
