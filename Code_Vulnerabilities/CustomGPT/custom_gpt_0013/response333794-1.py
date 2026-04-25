
import dpkt
import pcap

def main():
    # Create pcap object
    try:
        pc = pcap.pcap()  # Default interface
        pc.setfilter('src host X.X.X.X or dst host X.X.X.X')
    except Exception as e:
        print(f"Error setting up pcap: {e}")
        return

    print("Listening for packets...")
    for timestamp, packet in pc:
        try:
            eth = dpkt.ethernet.Ethernet(packet)
            print(f"Timestamp: {timestamp}, Packet: {eth}")
        except dpkt.dpkt.NeedData:
            print("Received incomplete packet")
        except Exception as e:
            print(f"Error processing packet: {e}")

if __name__ == "__main__":
    main()
