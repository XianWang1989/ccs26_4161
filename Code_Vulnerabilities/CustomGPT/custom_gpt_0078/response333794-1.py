
import dpkt
import pcap
import socket

def print_packet_data(timestamp, packet):
    try:
        eth = dpkt.ethernet.Ethernet(packet)
        ip = eth.data
        if isinstance(ip, dpkt.ip.IP):
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print(f"Timestamp: {timestamp}, Source: {src}, Destination: {dst}")
        else:
            print("Not an IP packet")
    except Exception as e:
        print(f"Error processing packet: {e}")

def main():
    # Create pcap object
    pc = pcap.pcap()

    # Set filter for the desired IP address (replace with X.X.X.X)
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    print("Starting to sniff packets...")

    for timestamp, packet in pc:
        print_packet_data(timestamp, packet)

if __name__ == "__main__":
    main()
