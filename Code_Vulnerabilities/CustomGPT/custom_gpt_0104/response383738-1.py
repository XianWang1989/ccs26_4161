
import sys
import binascii
import urllib.parse
import urllib.request
from bcode import bdecode

def announce(inputurl):
    with urllib.request.urlopen(inputurl) as url:
        data = url.read()  # Read the response data once
        print(data)  # Print the raw response
        decoded = bdecode(data)  # Decode the response
        print(decoded)  # Print the decoded data

infohash = sys.argv[1]  # Read info hash from command line

# Ensure that the info hash is a valid hex string and correctly encode it
if len(infohash) != 40:  # Check for valid length of an infohash
    raise ValueError("The infohash must be a 40 character hexadecimal string.")

encoded_infohash = urllib.parse.quote(binascii.a2b_hex(infohash))  # Encode info_hash
announce_url = "http://my_tracker_ip:6969/announce?info_hash=" + encoded_infohash
announce(announce_url)
