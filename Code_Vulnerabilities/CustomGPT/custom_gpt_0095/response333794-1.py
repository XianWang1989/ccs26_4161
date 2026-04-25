
import dpkt
import pcap

def main():
    try:
        # Create pcap object
        pc = pcap.pcap()  
        # Set filter for your specific IP address
        pc.setfilter('src host X.X.X.X or dst host X.X.X.X')

        print("Sniffing packets...")

        for timestamp, packet in pc:
            try:
                # Parse Ethernet frame
                eth = dpkt.ethernet.Ethernet(packet)
                print(f'Time: {timestamp}, Source: {eth.src}, Destination: {eth.dst}')

                # If you want to further analyze the packet, you can check for IP packets
                if isinstance(eth.data, dpkt.ip.IP):
                    ip = eth.data
                    print(f'Protocol: {ip.p}, Length: {len(ip)}')

            except Exception as e:
                print(f'Error processing packet: {e}')

    except Exception as e:
        print(f'Error initializing pcap: {e}')

if __name__ == "__main__":
    main()
