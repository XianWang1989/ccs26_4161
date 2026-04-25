
import sys
import binascii
import urllib.parse
import urllib.request
from bcode import bdecode

def announce(inputurl):
    with urllib.request.urlopen(inputurl) as url:
        response = url.read()
        decoded = bdecode(response)
        print(decoded)

        # Decode peer list
        peers = decoded.get(b'peers', b'')
        if isinstance(peers, bytes):
            # Convert peer list from binary to list of addresses
            peer_list = [f"{peers[i]}.{peers[i+1]}.{peers[i+2]}.{peers[i+3]}:{(peers[i+4] << 8) + peers[i+5]}" 
                         for i in range(0, len(peers), 6)]
            print("Peer list:", peer_list)

infohash = sys.argv[1]  # Read info hash from command line
encoded_infohash = urllib.parse.quote(binascii.a2b_hex(infohash))  # Encode info_hash
announce_url = f"http://my_tracker_ip:6969/announce?info_hash={encoded_infohash}"
announce(announce_url)
