
import dpkt
import pcap

# Create a pcap object and open a specific interface
# Replace 'en0' with your actual network interface name if necessary
interface = 'en0'
pc = pcap.pcap(name=interface)

# Set a filter for the desired IP address
filter_string = 'src host X.X.X.X or dst host X.X.X.X'
pc.setfilter(filter_string)

print(f"Listening on {interface} with filter '{filter_string}'...")

for timestamp, packet in pc:
    # Unpack the Ethernet frame
    eth = dpkt.ethernet.Ethernet(packet)

    # Display the Ethernet frame
    print(f"Timestamp: {timestamp}")
    print(eth)
