
import dpkt
import pcap

def packet_sniffer():
    pc = pcap.pcap()  # Create a pcap object
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # Set filter for specific IP

    for timestamp, packet in pc:
        try:
            eth = dpkt.ethernet.Ethernet(packet)  # Parse Ethernet frame
            ip = eth.data  # Get the IP layer
            if isinstance(ip, dpkt.ip.IP):  # Ensure it's an IP packet
                print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Length: {len(packet)} bytes')
        except (dpkt.dpkt.NeedData, AttributeError) as e:
            print(f"Error parsing packet: {e}")

if __name__ == "__main__":
    packet_sniffer()
