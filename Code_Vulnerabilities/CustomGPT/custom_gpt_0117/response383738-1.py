
import sys
import binascii
import urllib.parse
import urllib.request
from bcode import bdecode

def announce(inputurl):
    with urllib.request.urlopen(inputurl) as url:
        response = url.read()  # Read the response once
        print(f"Raw response: {response}")
        decoded = bdecode(response)  # Decode the response
        print(f"Decoded response: {decoded}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python announce.py <info_hash>")
        sys.exit(1)

    infohash = sys.argv[1]  # Read info hash from command line

    # Ensure the infohash is valid (40 hex characters)
    if len(infohash) != 40 or not all(c in '0123456789abcdefABCDEF' for c in infohash):
        print("Invalid info hash.")
        sys.exit(1)

    encoded_infohash = urllib.parse.quote(binascii.a2b_hex(infohash))  # Encode info_hash
    announce_url = f"http://my_tracker_ip:6969/announce?info_hash={encoded_infohash}"
    announce(announce_url)
