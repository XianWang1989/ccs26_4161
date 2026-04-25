
import dpkt
import pcap

# Set up the pcap object
pc = pcap.pcap()  # create pcap object
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # filter packets

# Loop through captured packets
for timestamp, packet in pc:
    try:
        eth = dpkt.ethernet.Ethernet(packet)  # parse Ethernet packet
        ip = eth.data  # get IP data

        if isinstance(ip, dpkt.ip.IP):
            print('Timestamp: {}, Source: {}, Destination: {}'.format(
                timestamp, 
                ip.src, 
                ip.dst
            ))
    except (dpkt.dpkt.NeedData, ValueError) as e:
        print('Error parsing packet: {}'.format(e))
