
import dpkt
import pcap

# Select the appropriate interface
interface = 'en0'  # Replace with your network interface if needed
pc = pcap.pcap(name=interface)  # Construct pcap object
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # Set your filter

# Start sniffing
print("Listening on", interface, "...")

for timestamp, packet in pc:
    try:
        eth = dpkt.ethernet.Ethernet(packet)  # Decode packet
        ip = eth.data  # Get IP layer
        if isinstance(ip, dpkt.ip.IP):
            print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}')
    except Exception as e:
        print(f'Error processing packet: {e}')
