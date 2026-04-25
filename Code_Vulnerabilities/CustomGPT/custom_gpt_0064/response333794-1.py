
import dpkt
import pcap

# Create a pcap object
pc = pcap.pcap()

# Set a filter for the specific host
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop to capture packets
for timestamp, packet in pc:
    try:
        # Parse the Ethernet packet
        eth = dpkt.ethernet.Ethernet(packet)

        # Print the Ethernet frame details
        print('Timestamp:', timestamp)
        print('Source:', eth.src)
        print('Destination:', eth.dst)
        print('Protocol:', eth.type)

        # If the packet has an IP layer, parse and print additional details
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print('IP Source:', ip.src)
            print('IP Destination:', ip.dst)
            print('IP Protocol:', ip.p)
    except Exception as e:
        print('Error parsing packet:', e)
