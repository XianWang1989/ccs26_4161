
import dpkt
import pcap

# List available devices
devices = pcap.findalldevs()
print("Available devices:")
for device in devices:
    print(device)

# Create a pcap object for a specific device, e.g., 'en0'
pc = pcap.pcap('en0')  # Replace 'en0' with your device name
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # Filter for specific IP

# Sniff packets
for timestamp, packet in pc:
    eth = dpkt.ethernet.Ethernet(packet)
    print(eth)  # Print Ethernet packet details
