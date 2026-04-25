
import dpkt
import pcap

# Set your target IP address
target_ip = 'X.X.X.X'  # replace with your target IP

# Create a pcap object
pc = pcap.pcap()

# Set the filter for the target IP address
pc.setfilter(f'src host {target_ip} or dst host {target_ip}')

# Start sniffing packets
for timestamp, packet in pc:
    eth = dpkt.ethernet.Ethernet(packet)  # Parse the Ethernet frame
    print(eth)  # Print the Ethernet frame
