
import dpkt
import pcap
import socket
import struct

def mac_addr(address):
    """Convert a MAC address to a readable/printable string"""
    return ':'.join('%02x' % b for b in address)

def ip_addr(address):
    """Convert an IP address to a readable string"""
    return socket.inet_ntoa(address)

# Initialize pcap
pc = pcap.pcap()
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

try:
    for timestamp, packet in pc:
        eth = dpkt.ethernet.Ethernet(packet)
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f'Timestamp: {timestamp}')
            print(f'Source MAC: {mac_addr(eth.src)}')
            print(f'Destination MAC: {mac_addr(eth.dst)}')
            print(f'Source IP: {ip_addr(ip.src)}')
            print(f'Destination IP: {ip_addr(ip.dst)}')
            print(f'Protocol: {ip.p}
