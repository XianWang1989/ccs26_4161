
import dpkt
import pcap

def main():
    pc = pcap.pcap()
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')
    print("Starting packet capture...")

    for timestamp, packet in pc:
        eth = dpkt.ethernet.Ethernet(packet)
        print(f'Timestamp: {timestamp}, Ethernet frame: {eth}')

if __name__ == "__main__":
    main()
