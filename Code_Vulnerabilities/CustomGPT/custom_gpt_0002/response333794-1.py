
import dpkt
import pcap

try:
    pc = pcap.pcap()  # construct pcap object
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # replace X.X.X.X with your IP
    for timestamp, packet in pc:
        eth = dpkt.ethernet.Ethernet(packet)
        print(eth)
except Exception as e:
    print("An error occurred:", e)
