
import sys
import binascii
import urllib.parse
import urllib.request
from bcode import bdecode

def announce(inputurl):
    with urllib.request.urlopen(inputurl) as url:
        response = url.read()  # Read the response once
        print(response)  # Optionally print raw response
        decoded = bdecode(response)  # Decode the response
        print(decoded)  # Print the decoded output

infohash = sys.argv[1]  # Read info hash from command line

# Ensure your info_hash is 20 bytes long by passing in the correct hex
encoded_infohash = urllib.parse.quote(binascii.a2b_hex(infohash))  # Encode inf_hash
announce_url = "http://my_tracker_ip:6969/announce?info_hash=" + encoded_infohash
announce(announce_url)
