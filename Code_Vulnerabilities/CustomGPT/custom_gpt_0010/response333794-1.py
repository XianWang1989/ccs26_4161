
import dpkt
import pcap

def main():
    # Create pcap object
    pc = pcap.pcap()

    # Set filter for the specific IP address
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    print("Listening on %s..." % pc.name)
    try:
        # Loop through captured packets
        for timestamp, packet in pc:
            # Decode Ethernet packet
            eth = dpkt.ethernet.Ethernet(packet)
            print(eth)
    except KeyboardInterrupt:
        print("Sniffing stopped.")

if __name__ == "__main__":
    main()
