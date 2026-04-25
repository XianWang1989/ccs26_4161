
import sys
import binascii
import urllib.parse
import urllib.request
from bcode import bdecode

def announce(inputurl):
    with urllib.request.urlopen(inputurl) as response:
        data = response.read()  # Read once
        decoded = bdecode(data)  # Decode the response

        # Print complete response for debugging
        print(f"Decoded Response: {decoded}")

        # Extract peers
        peers_binary = decoded.get(b'peers')
        if peers_binary:
            peers = []
            # Convert binary peers to IP:port format
            for i in range(0, len(peers_binary), 6):  # 4 bytes for IP, 2 bytes for port
                ip = '.'.join(str(peers_binary[j]) for j in range(i, i + 4))
                port = (peers_binary[i + 4] << 8) + peers_binary[i + 5]
                peers.append(f"{ip}:{port}")
            print("Peers found:")
            for peer in peers:
                print(peer)
        else:
            print("No peers found.")

infohash = sys.argv[1]  # Read info hash from command line

encoded_infohash = urllib.parse.quote(binascii.a2b_hex(infohash))  # Encode info_hash
announce_url = "http://my_tracker_ip:6969/announce?info_hash=" + encoded_infohash
announce(announce_url)
