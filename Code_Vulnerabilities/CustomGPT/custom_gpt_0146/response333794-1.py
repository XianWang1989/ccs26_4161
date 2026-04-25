
import dpkt
import pcap

def main():
    # Specify the network interface to sniff on. Replace 'en0' with your interface.
    pc = pcap.pcap(name='en0')  # Adjust with the correct interface
    # Set your desired filter
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    try:
        print("Starting packet capture...")
        for timestamp, packet in pc:
            # Parse Ethernet frame
            eth = dpkt.ethernet.Ethernet(packet)
            print(f"Captured packet: {eth}")
    except KeyboardInterrupt:
        print("Stopping packet capture...")

if __name__ == "__main__":
    main()
