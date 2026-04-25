
import dpkt
import pcap

def main():
    try:
        # Create a pcap object
        pc = pcap.pcap()  # This opens the default network interface

        # Set the filter for the specific IP address
        pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

        print("Listening for packets...")
        for timestamp, packet in pc:
            try:
                # Parse the packet
                eth = dpkt.ethernet.Ethernet(packet)
                # Print packet info
                print(f"Timestamp: {timestamp}, Packet: {eth}")
            except (dpkt.dpkt.NeedData, dpkt.dpkt.Error) as e:
                print(f"Error parsing packet: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
