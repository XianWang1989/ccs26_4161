
import pcap
import dpkt

# Create a pcap object
pc = pcap.pcap()
pc.setnonblock(True)  # Set non-blocking mode

# Apply a filter for your specific IP address
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

try:
    while True:
        # Read packets
        for timestamp, packet in pc:
            ether = dpkt.ethernet.Ethernet(packet)
            print ether
except KeyboardInterrupt:
    print("Exited by user.")
except Exception as e:
    print("Error: ", e)
