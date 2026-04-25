
import sys
import binascii
import urllib.parse
import urllib.request
from bcode import bdecode

def announce(inputurl):
    with urllib.request.urlopen(inputurl) as url:
        response = url.read()  # Read the response once
        print(response)
        decoded = bdecode(response)  # Decode the stored response
        print(decoded)

infohash = sys.argv[1]  # Read info hash from command line

encoded_infohash = urllib.parse.quote(binascii.a2b_hex(infohash))  # Encode infohash
announce_url = f"http://my_tracker_ip:6969/announce?info_hash={encoded_infohash}"
announce(announce_url)
