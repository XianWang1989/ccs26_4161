
import dpkt
import pcap

# Create a pcap object and set the filter
try:
    pc = pcap.pcap(name='en0')  # Replace 'en0' with your network interface
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

    print("Listening for packets...")
    for timestamp, packet in pc:
        # Parse the Ethernet packet
        eth = dpkt.ethernet.Ethernet(packet)
        print(eth)

except Exception as e:
    print(f"An error occurred: {e}")
