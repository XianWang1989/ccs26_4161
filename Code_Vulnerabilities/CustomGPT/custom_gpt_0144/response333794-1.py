import dpkt
import pcap

# List available interfaces
print("Available interfaces:")
for dev in pcap.findalldevs():
    print(dev)

# Select your interface (replace 'en0' with your active one)
interface = 'en0'
pc = pcap.pcap(name=interface, promisc=True, immediate=True, timeout_ms=50)
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # Replace X.X.X.X with the target IP

print("Starting packet capture on:", interface)
try:
    for timestamp, packet in pc:
        eth = dpkt.ethernet.Ethernet(packet)
        print(eth)
except KeyboardInterrupt:
    print("\nStopping capture.")
