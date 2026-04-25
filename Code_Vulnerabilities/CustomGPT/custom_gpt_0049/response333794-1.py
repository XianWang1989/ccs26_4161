
import dpkt
import pcap

def packet_sniffer():
    pc = pcap.pcap()  # create a pcap object
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # set the filter for specific IPs

    print("Starting packet sniffing...")

    for timestamp, packet in pc:
        eth = dpkt.ethernet.Ethernet(packet)  # decode the ethernet packet
        if not isinstance(eth.data, dpkt.ip.IP):
            # If it's not an IP packet, skip it
            continue

        ip = eth.data  # get the IP data
        print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}')

if __name__ == "__main__":
    packet_sniffer()
