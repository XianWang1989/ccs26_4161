
import dpkt
import pcap

# Set your interface name (use 'ifconfig' to find it)
interface = 'en0'  # Change to your active interface

# Create pcap object with the specified interface
pc = pcap.pcap(name=interface)

# Set the filter for the packets you want to capture
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

print("Listening on interface:", interface)

# Start capturing packets
for timestamp, packet in pc:
    try:
        eth = dpkt.ethernet.Ethernet(packet)
        ip = eth.data
        print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}')
    except Exception as e:
        print('Error parsing packet:', e)
