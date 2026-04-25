
import dpkt
import pcap

def main():
    pc = pcap.pcap()  # construct pcap object
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    for timestamp, packet in pc:
        eth = dpkt.ethernet.Ethernet(packet)
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}')

if __name__ == "__main__":
    main()
