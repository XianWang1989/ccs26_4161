
import dpkt
import pcap

def packet_handler(timestamp, packet):
    try:
        eth = dpkt.ethernet.Ethernet(packet)
        print(eth)  # Print the Ethernet packet
    except Exception as e:
        print(f"Error processing packet: {e}")

def main():
    pc = pcap.pcap()  # Construct pcap object
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # Set your filter here

    for timestamp, packet in pc:
        packet_handler(timestamp, packet)

if __name__ == "__main__":
    main()
