
import pcap

# Print out all available network interfaces
devices = pcap.findalldevs()
for device in devices:
    print(device)
