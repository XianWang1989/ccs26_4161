
import sys
import binascii
import urllib.parse
import urllib.request
from bcode import bdecode

def announce(inputurl):
    with urllib.request.urlopen(inputurl) as response:
        data = response.read()  # Read once and store data
        print(data)  # Print raw response
        decoded = bdecode(data)  # Decode the data
        print(decoded)  # Print decoded response

if __name__ == "__main__":
    infohash = sys.argv[1]  # Read info hash from command line

    # Encode info_hash
    encoded_infohash = urllib.parse.quote(binascii.a2b_hex(infohash))
    announce_url = f"http://my_tracker_ip:6969/announce?info_hash={encoded_infohash}"
    announce(announce_url)
