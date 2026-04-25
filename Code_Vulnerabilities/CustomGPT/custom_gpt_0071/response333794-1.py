
import dpkt
import pcap

def main():
    # Create a pcap object
    pc = pcap.pcap()

    # Set a filter for the desired IP address
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    print("Packet sniffing started...")

    try:
        for timestamp, packet in pc:
            # Decode the Ethernet packet
            eth = dpkt.ethernet.Ethernet(packet)
            print(eth)
    except Exception as e:
        print("An error occurred: {}".format(e))

if __name__ == "__main__":
    main()
