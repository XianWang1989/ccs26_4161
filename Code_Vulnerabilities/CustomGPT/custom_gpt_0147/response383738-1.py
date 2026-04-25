
import sys
import binascii
import urllib.parse
import urllib.request
from bcode import bdecode

def announce(inputurl):
    with urllib.request.urlopen(inputurl) as url:
        response_data = url.read()  # Read the response only once
        decoded = bdecode(response_data)  # Decode the bencoded data
        print(decoded)  # Print the decoded information

        # Example of extracting the peer list from the decoded response
        if b'peers' in decoded:
            peers = decoded[b'peers']
            print("Peers:")
            for i in range(0, len(peers), 6):  # Each peer takes 6 bytes (IPv4)
                # Extract IP and port
                ip = '.'.join(str(peers[i + j]) for j in range(4))  # First 4 bytes are IP
                port = (peers[i + 4] << 8) + peers[i + 5]  # Next 2 bytes are port
                print(f'{ip}:{port}')

infohash = sys.argv[1]  # Read info hash from command line

encoded_infohash = urllib.parse.quote(binascii.a2b_hex(infohash))  # Encode info_hash
announce_url = "http://my_tracker_ip:6969/announce?info_hash=" + encoded_infohash
announce(announce_url)
