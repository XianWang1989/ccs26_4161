
import sys
import dpkt
import pcap

# If needed, specify your network interface name here
interface = 'en0'  # Modify this to your active interface if necessary

try:
    # Create a pcap object with the specified interface
    pc = pcap.pcap(name=interface)

    # Set a filter for the specific host
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    print(f"Listening on interface {interface} for packets...")

    # Capture packets in a loop
    for timestamp, packet in pc:
        # Parse the ethernet packet
        eth_packet = dpkt.ethernet.Ethernet(packet)

        # Print source and destination MAC addresses
        if isinstance(eth_packet.data, dpkt.ip.IP):
            ip_packet = eth_packet.data
            print(f"Timestamp: {timestamp}, Src: {ip_packet.src}, Dst: {ip_packet.dst}")
        else:
            print("Not an IP packet, skipping...")

except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
