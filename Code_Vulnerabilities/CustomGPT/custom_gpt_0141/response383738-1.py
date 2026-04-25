
import sys
import binascii
import urllib.parse
import urllib.request
from bcode import bdecode

def announce(inputurl):
    with urllib.request.urlopen(inputurl) as url:
        # Read the response only once
        response = url.read()
        print("Raw response:", response)

        # Decode the response using bdecode
        decoded = bdecode(response)
        print("Decoded response:", decoded)

        # Extracting peer list
        if b'peers' in decoded:
            peers = decoded[b'peers']
            # Check if peers is a byte string (compact format)
            if isinstance(peers, bytes):
                # Convert byte string to a list of (ip, port) tuples
                peer_list = []
                for i in range(0, len(peers), 6):  # 4 bytes for IP, 2 bytes for port
                    ip = peers[i:i+4]
                    port = int.from_bytes(peers[i+4:i+6], "big")  # Convert to integer
                    peer = f"{ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}:{port}"
                    peer_list.append(peer)
                print("Peer list:", peer_list)
            else:
                print("Peers list is not in compact format:", peers)
        else:
            print("No peers found in response.")

if __name__ == "__main__":
    infohash = sys.argv[1]  # Read info hash from command line
    encoded_infohash = urllib.parse.quote(binascii.a2b_hex(infohash))  # Encode info_hash
    announce_url = f"http://my_tracker_ip:6969/announce?info_hash={encoded_infohash}"
    announce(announce_url)
