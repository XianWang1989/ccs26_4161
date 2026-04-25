
import pcap
import dpkt

# Create a PCAP object and set the filter for the desired IP
pc = pcap.pcap(name=None)  # Specify None to use the default interface
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # Replace with your target IP

# Loop to capture packets
for timestamp, packet in pc:
    try:
        eth = dpkt.ethernet.Ethernet(packet)  # Decode Ethernet frame
        ip = eth.data  # Get the IP layer from the Ethernet frame

        # Basic check to ensure it is an IP packet
        if isinstance(ip, dpkt.ip.IP):
            print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}')
    except (dpkt.dpkt.NeedData, IndexError) as e:
        # Handle potential packet decode errors
        print(f'Decoding error: {e}')
