
import dpkt
import pcap

def main():
    pc = pcap.pcap()  # create pcap object
    # Set the filter to capture packets from or to the specified IP address
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    for timestamp, packet in pc:
        try:
            eth = dpkt.ethernet.Ethernet(packet)  # decode Ethernet packet
            ip = eth.data  # get the IP layer
            print('Timestamp: {}, Source: {}, Destination: {}'.format(
                timestamp,
                dpkt.utils.inet_to_str(ip.src),
                dpkt.utils.inet_to_str(ip.dst)
            ))
        except dpkt.dpkt.NeedData:
            print("Packet truncated")

if __name__ == "__main__":
    main()
