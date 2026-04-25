
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()

# Set up a filter for the desired IP address (replace 'X.X.X.X' with the actual IP)
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

print("Listening for packets...")

# Iterate over the captured packets
for timestamp, packet in pc:
    try:
        # Parse the Ethernet frame
        eth = dpkt.ethernet.Ethernet(packet)

        # Check if the packet contains an IP packet
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f'Timestamp: {timestamp}')
            print(f'Source IP: {ip.src}')
            print(f'Destination IP: {ip.dst}')
            print(f'Protocol: {ip.p}')
            print('---')

    except Exception as e:
        print(f'Error processing packet: {e}')
