
import dpkt
import pcap

# Create a pcap object
try:
    pc = pcap.pcap()  # construct pcap object
except Exception as e:
    print("Error initializing pcap: ", e)
    exit(1)

# Set the filter for capturing packets
try:
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')
except Exception as e:
    print("Error setting filter: ", e)
    exit(1)

# Start capturing packets
try:
    print("Listening on the network interface... Press Ctrl+C to stop.")
    for timestamp, packet in pc:
        # Parse the Ethernet packet
        eth = dpkt.ethernet.Ethernet(packet)
        print("Captured packet: ", eth)
except KeyboardInterrupt:
    print("Packet sniffing stopped by user.")
except Exception as e:
    print("Error during packet capturing: ", e)
