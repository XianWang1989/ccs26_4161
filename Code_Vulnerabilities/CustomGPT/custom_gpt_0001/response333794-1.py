
import dpkt
import pcap

def main():
    # Create a pcap object
    pc = pcap.pcap()

    # List available devices and select the right one
    print("Available devices:")

    for device in pcap.findalldevs():
        print(device)

    # Set the filter for the specific IP address (replace with actual IP)
    ip_address = 'X.X.X.X'  # Replace with your desired IP
    pc.setfilter(f'src host {ip_address} or dst host {ip_address}')

    print(f"Sniffing packets to/from {ip_address}...")

    try:
        for timestamp, packet in pc:
            eth = dpkt.ethernet.Ethernet(packet)
            print(f"Timestamp: {timestamp}, Packet: {eth}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
