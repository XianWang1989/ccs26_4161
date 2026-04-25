
import dpkt
import pcap

# Initialize pcap
pc = pcap.pcap()
# Set a filter for the desired IP address
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

try:
    print("Starting packet capture... Press Ctrl+C to stop.")
    for timestamp, packet in pc:
        ethernet = dpkt.ethernet.Ethernet(packet)  # Parse Ethernet frame
        ip = ethernet.data  # Get the IP layer
        if isinstance(ip, dpkt.ip.IP):
            # Print the source and destination IPs
            print(f'Timestamp: {timestamp}, Src: {dpkt.utils.inet.ntoa(ip.src)}, Dst: {dpkt.utils.inet.ntoa(ip.dst)}')
except KeyboardInterrupt:
    print("\nCapture stopped by user.")
except Exception as e:
    print(f"An error occurred: {e}")
