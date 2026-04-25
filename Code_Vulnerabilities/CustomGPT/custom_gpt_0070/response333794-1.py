
import dpkt
import pcap

def main():
    pc = pcap.pcap()  # construct pcap object
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # replace X.X.X.X with the actual IP

    print("Listening for packets...")

    for timestamp, packet in pc:
        try:
            eth = dpkt.ethernet.Ethernet(packet)
            print(eth)
        except (dpkt.dpkt.NeedData, ValueError) as e:
            print("Error parsing packet: ", e)

if __name__ == "__main__":
    main()
