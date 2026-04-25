
import dpkt
import pcap
import socket

# Create pcap object
pc = pcap.pcap()

# Set the filter for the desired IP address
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Function to convert IP to a readable format
def ip_to_str(ip):
    return socket.inet_ntoa(ip)

# Capture packets
for timestamp, packet in pc:
    ethernet = dpkt.ethernet.Ethernet(packet)

    # Check if the packet contains IPv4
    if isinstance(ethernet.data, dpkt.ip.IP):
        ip = ethernet.data
        print(f'Timestamp: {timestamp}, Source: {ip_to_str(ip.src)}, Destination: {ip_to_str(ip.dst)}')
