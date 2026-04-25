
import dpkt
import pcap

def packet_handler(ts, pkt):
    try:
        eth = dpkt.ethernet.Ethernet(pkt)
        ip = eth.data
        if isinstance(ip, dpkt.ip.IP):
            print(f'Time: {ts}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}')
    except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
        pass

def main():
    pc = pcap.pcap()  # construct pcap object
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # replace with your IP

    print("Starting packet capture...")
    pc.loop(packet_handler)

if __name__ == "__main__":
    main()
