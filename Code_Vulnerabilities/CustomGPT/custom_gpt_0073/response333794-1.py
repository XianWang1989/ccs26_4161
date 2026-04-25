
import dpkt
import pcap
import sys

# Replace 'X.X.X.X' with the actual IP address you want to filter
IP_FILTER = 'src host X.X.X.X or dst host X.X.X.X'

try:
    # Create a pcap object
    pc = pcap.pcap()
    pc.setfilter(IP_FILTER)

    print("Starting packet capture...")

    for timestamp, packet in pc:
        try:
            # Parse the Ethernet packet
            eth = dpkt.ethernet.Ethernet(packet)
            # Check if the payload is IP
            if isinstance(eth.data, dpkt.ip.IP):
                ip = eth.data
                print(f'Timestamp: {timestamp}, Source: {ip.src}, Destination: {ip.dst}, Protocol: {ip.p}')
            else:
                print("Not an IP packet.")
        except Exception as e:
            print(f"Error parsing packet: {e}")

except Exception as e:
    print(f"Error initializing pcap: {e}")
    sys.exit(1)
