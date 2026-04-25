
import dpkt
import pcap

def main():
    # Create a pcap object
    pc = pcap.pcap()

    # Set the filter for the desired IP address
    try:
        pc.setfilter('host X.X.X.X')  # Replace X.X.X.X with your target IP
    except pcap.PcapError as e:
        print(f"Error setting filter: {e}")
        return

    print("Starting packet capture...")

    # Loop through packets
    for timestamp, packet in pc:
        try:
            eth = dpkt.ethernet.Ethernet(packet)
            # Process only IP packets
            if isinstance(eth.data, dpkt.ip.IP):
                ip = eth.data
                print(f"{timestamp}: {ip.src} -> {ip.dst}")
        except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError) as e:
            print(f"Error unpacking packet: {e}")

if __name__ == "__main__":
    main()
