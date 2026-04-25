
import dpkt
import pcap

# Set your target IP address here
TARGET_IP = 'X.X.X.X'

# Create the pcap object
pc = pcap.pcap()

# Set the filter for incoming or outgoing packets
pc.setfilter(f'src host {TARGET_IP} or dst host {TARGET_IP}')

try:
    print("Starting packet sniffing...")
    for timestamp, packet in pc:
        # Parse the Ethernet frame
        eth = dpkt.ethernet.Ethernet(packet)

        # Display the packet if it's an IP packet
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}')
except Exception as e:
    print(f'An error occurred: {e}')
