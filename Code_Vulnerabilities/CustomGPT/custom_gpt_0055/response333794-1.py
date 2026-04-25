
import dpkt
import pcap

def packet_sniffer():
    # Create a pcap object for capturing packets
    pc = pcap.pcap()

    # Set the filter for the desired IP address
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    # Capture packets
    for timestamp, packet in pc:
        try:
            # Decode the Ethernet packet
            eth_pkt = dpkt.ethernet.Ethernet(packet)
            # Print the source and destination MAC addresses
            print(f"Source MAC: {eth_pkt.src}, Destination MAC: {eth_pkt.dst}")
        except (dpkt.dpkt.NeedData, ValueError) as e:
            print(f"Error processing packet: {e}")

if __name__ == "__main__":
    packet_sniffer()
