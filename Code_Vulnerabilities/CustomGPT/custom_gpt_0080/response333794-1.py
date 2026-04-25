
import dpkt
import pcap

# Initialize the pcap object
pc = pcap.pcap()

# Set the filter for the desired IP
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

try:
    for timestamp, packet in pc:
        # Parse the Ethernet frame
        eth = dpkt.ethernet.Ethernet(packet)

        # Check if it's an IP packet
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f"Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}")
except KeyboardInterrupt:
    print("Sniffer stopped.")
except Exception as e:
    print(f"An error occurred: {e}")
