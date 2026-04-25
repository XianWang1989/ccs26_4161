
import dpkt
import pcap

# Initialize pcap
pc = pcap.pcap()
pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

# Loop through packets
for timestamp, packet in pc:
    try:
        eth = dpkt.ethernet.Ethernet(packet)
        if isinstance(eth.data, dpkt.ip.IP):
            ip = eth.data
            print(f"{timestamp}: {ip.src} -> {ip.dst}: {ip.p}",
                  f"Length: {len(packet)}")
    except dpkt.UnpackError as e:
        print(f"Unpack error: {e}")
