
import sys
import binascii
import urllib.parse
import urllib.request
from bcode import bdecode

def announce(inputurl):
    with urllib.request.urlopen(inputurl) as url:
        response = url.read()
        # Print raw response for debugging purposes
        print(response)

        # Decode the bencoded response
        decoded = bdecode(response)
        print(decoded)

if __name__ == "__main__":
    infohash = sys.argv[1]  # Read info hash from command line

    # Encode info hash
    encoded_infohash = urllib.parse.quote(binascii.a2b_hex(infohash))  
    announce_url = f"http://my_tracker_ip:6969/announce?info_hash={encoded_infohash}"

    announce(announce_url)
