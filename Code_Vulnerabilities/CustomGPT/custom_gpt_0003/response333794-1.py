
import dpkt
import pcap

# List available devices
def list_devices():
    devices = pcap.findalldevs()
    for i, device in enumerate(devices):
        print(f"{i}: {device.name}")
    return devices

# Sniff packets
def sniff_packets():
    pc = pcap.pcap()  # Construct pcap object
    # Optionally set a specific interface
    # pc = pcap.pcap(name='your_interface') 
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # Set filter for specific IPs

    print("Sniffing packets...")
    for timestamp, packet in pc:
        eth = dpkt.ethernet.Ethernet(packet)
        print(f'Timestamp: {timestamp}, Packet: {eth}')

if __name__ == "__main__":
    list_devices()  # List network interfaces (optional)
    sniff_packets()  # Start sniffing
