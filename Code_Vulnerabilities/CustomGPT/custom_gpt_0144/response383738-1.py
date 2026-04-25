import sys
import binascii
import urllib.parse
import urllib.request
from bcode import bdecode

def announce(inputurl):
    with urllib.request.urlopen(inputurl) as url:
        response_data = url.read()  # Read once and reuse
        print(response_data)
        decoded = bdecode(response_data)
        print(decoded)

infohash = sys.argv[1]  # Read info hash from command line

# Encode info_hash for URL (use urllib.parse.quote with safe='' to encode all bytes)
encoded_infohash = urllib.parse.quote(binascii.a2b_hex(infohash), safe='')

# Sample announce URL
announce_url = f"http://my_tracker_ip:6969/announce?info_hash={encoded_infohash}&peer_id=ABCDEFGHIJKLMNOPQRST&port=6881&uploaded=0&downloaded=0&left=0&event=started"

announce(announce_url)
