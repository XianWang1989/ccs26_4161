
import dpkt
import pcap

def sniff_packets():
    try:
        pc = pcap.pcap()  # Construct pcap object
        pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # Set filter

        print("Listening for packets...")
        for timestamp, packet in pc:
            eth = dpkt.ethernet.Ethernet(packet)
            print(eth)  # Print the Ethernet packet
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    sniff_packets()
