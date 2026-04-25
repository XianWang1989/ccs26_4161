
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()

# Set the filter for the specific host
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Start sniffing
for timestamp, packet in pc:
    try:
        # Parse the Ethernet frame
        eth = dpkt.ethernet.Ethernet(packet)

        # Print relevant information
        print(f'Timestamp: {timestamp}')
        print(f'Source MAC: {eth.src.hex()}')
        print(f'Destination MAC: {eth.dst.hex()}')

        # Further packet details (like IP, TCP/UDP) can be added here if needed
    except Exception as e:
        print(f'Error processing packet: {e}')
