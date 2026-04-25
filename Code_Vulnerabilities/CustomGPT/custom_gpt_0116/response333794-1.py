
import dpkt
import pcap

def main():
    # Create a pcap object
    pc = pcap.pcap()  # You may need to specify an interface
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    for timestamp, packet in pc:
        try:
            eth = dpkt.ethernet.Ethernet(packet)
            print(eth)
        except Exception as e:
            print("Error decoding packet:", e)

if __name__ == "__main__":
    main()
