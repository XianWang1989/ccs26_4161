
import dpkt
import pcap

def packet_callback(timestamp, packet):
    try:
        eth = dpkt.ethernet.Ethernet(packet)
        ip = eth.data
        if isinstance(ip, dpkt.ip.IP):
            print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}')
    except Exception as e:
        print(f'Error processing packet: {e}')

def main():
    pc = pcap.pcap()  # Create a pcap object
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # Set your filter here

    # Start sniffing packets
    for timestamp, packet in pc:
        packet_callback(timestamp, packet)

if __name__ == "__main__":
    main()
