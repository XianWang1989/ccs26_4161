
import sys
import binascii
import urllib.parse
import urllib.request
from bcode import bdecode

def announce(inputurl):
    with urllib.request.urlopen(inputurl) as url:
        response = url.read()
        print(f"Raw response: {response}")
        decoded = bdecode(response)
        print(f"Decoded response: {decoded}")

infohash = sys.argv[1] 

encoded_infohash = urllib.parse.quote(binascii.a2b_hex(infohash)) 
announce_url = "http://my_tracker_ip:6969/announce?info_hash=" + encoded_infohash
announce(announce_url)
