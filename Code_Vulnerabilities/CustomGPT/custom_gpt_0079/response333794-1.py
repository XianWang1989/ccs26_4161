
import dpkt
import pcap

def main():
    # Initialize the pcap object
    pc = pcap.pcap()  # Open a live pcap session
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')  # Set the filter to capture packets

    try:
        # Loop through captured packets
        for timestamp, packet in pc:
            # Parse Ethernet frames
            eth = dpkt.ethernet.Ethernet(packet)
            print(eth)  # Print the Ethernet frame
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
