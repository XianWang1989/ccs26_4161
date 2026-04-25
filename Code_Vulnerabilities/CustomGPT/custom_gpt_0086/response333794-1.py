
import dpkt
import pcap

# Initialize the pcap object
pc = pcap.pcap()

# Set the filter for the desired IP addresses
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

print("Starting packet sniffing...")

try:
    # Loop to capture packets
    for timestamp, packet in pc:
        # Parse the Ethernet frame
        eth = dpkt.ethernet.Ethernet(packet)

        # Check for IP packets
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print('Timestamp: {}, Source: {}, Destination: {}'.format(
                timestamp, 
                ip.src, 
                ip.dst
            ))
except KeyboardInterrupt:
    # Stop the sniffing on interrupt
    print("Sniffing stopped.")
except Exception as e:
    print("An error occurred: {}".format(e))
