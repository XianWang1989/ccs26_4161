
import dpkt
import pcap

# List available network interfaces
devices = pcap.findalldevs()
for i, device in enumerate(devices):
    print(f"{i}: {device}")

# Select the interface you want to use
interface_index = int(input("Choose the interface index: "))
pc = pcap.pcap(devices[interface_index])  # construct pcap object for selected interface
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

try:
    for timestamp, packet in pc:
        eth = dpkt.ethernet.Ethernet(packet)
        print(eth)
except KeyboardInterrupt:
    print("Packet sniffing stopped.")
