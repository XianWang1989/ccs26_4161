
import dpkt
import pcap
import socket

def get_ip_address(data):
    """Get the IP address from raw data."""
    return socket.inet_ntoa(data[26:30])

def main():
    # Create pcap object
    pc = pcap.pcap()
    # Set a filter to capture specific source and destination IPs
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    print("Listening on the network...")
    for timestamp, packet in pc:
        eth = dpkt.ethernet.Ethernet(packet)
        # Ensure we only process IP packets
        if isinstance(eth.data, dpkt.ip.IP):
            ip_data = eth.data
            print(f'Timestamp: {timestamp}, Source IP: {get_ip_address(ip_data)}, Length: {len(packet)}')

if __name__ == "__main__":
    main()
