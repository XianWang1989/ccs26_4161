
import dpkt
import pcap

# Set up the pcap object
pc = pcap.pcap()

# Set the filter for sniffing (replace X.X.X.X with your target IP)
filter_expr = 'src host X.X.X.X or dst host X.X.X.X'
try:
    pc.setfilter(filter_expr)
except Exception as e:
    print("Error setting filter: ", e)

# Start sniffing packets
print("Sniffing packets... Press Ctrl+C to stop.")
try:
    for timestamp, packet in pc:
        eth = dpkt.ethernet.Ethernet(packet)
        # Check for IP packets
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f"Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}")
except KeyboardInterrupt:
    print("Stopped sniffing.")
except Exception as e:
    print("Error: ", e)
