
import dpkt
import pcap

# List available devices
devices = pcap.findalldevs()
print("Available devices:")
for device in devices:
    print(device)

# Choose the device you want to listen on
device_name = 'en0'  # Example: replace with your actual device name

# Construct pcap object
pc = pcap.pcap(device=device_name)  
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Start sniffing
for timestamp, packet in pc:
    eth = dpkt.ethernet.Ethernet(packet)
    print(eth)
