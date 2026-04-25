
import dpkt
import pcap

# Specify the network device (replace 'en0' with your actual device)
device = 'en0'  
pc = pcap.pcap(device)  # construct pcap object for the specified device

# Set capture filter for specific IP address
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop through captured packets
for timestamp, packet in pc:
    try:
        ethernet = dpkt.ethernet.Ethernet(packet)
        print(ethernet)
    except Exception as e:
        print(f"Error parsing packet: {e}")
