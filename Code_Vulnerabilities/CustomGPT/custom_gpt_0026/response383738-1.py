
import sys
import binascii
import urllib.parse
import urllib.request
from bcode import bdecode

def announce(inputurl):
    with urllib.request.urlopen(inputurl) as url:
        response = url.read()  # Read the URL response once
        print(response)  # Print raw response
        decoded = bdecode(response)  # Decode the response
        print(decoded)  # Print the decoded response

        # Extracting peer list
        peers = decoded.get(b'peers')
        if peers:
            # If peers are in binary format, convert them to a list of addresses
            peer_list = []
            for i in range(0, len(peers), 6):  # Each peer is 6 bytes
                ip = f"{peers[i]}.{peers[i+1]}.{peers[i+2]}.{peers[i+3]}"
                port = (peers[i+4] << 8) + peers[i+5]  # Combine to form port
                peer_list.append((ip, port))
            print("Peers:", peer_list)

infohash = sys.argv[1]  # Read info hash from command line

encoded_infohash = urllib.parse.quote(binascii.a2b_hex(infohash))  # Encode info_hash
announce_url = f"http://my_tracker_ip:6969/announce?info_hash={encoded_infohash}"
announce(announce_url)
