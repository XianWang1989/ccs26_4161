
import dpkt
import pcap

# Create a pcap object and set the filter
pc = pcap.pcap()  # Use default network interface

# Set a filter to capture packets from a specific source or destination IP
try:
    pc.setfilter('src host X.X.X.X or dst host X.X.X.X')
except Exception as e:
    print(f"Error setting filter: {e}")

# Loop through the captured packets
for timestamp, packet in pc:
    try:
        # Parse the Ethernet packet
        eth = dpkt.ethernet.Ethernet(packet)

        # Print the packet information
        print('Timestamp:', timestamp)
        print('Ethernet Packet:', eth)
    except dpkt.dpkt.NeedData:
        print("Incomplete packet captured.")
    except Exception as e:
        print(f"Error processing packet: {e}")
