
import sys
import binascii
import urllib.parse
import urllib.request
from bcode import bdecode

def announce(inputurl):
    with urllib.request.urlopen(inputurl) as url:
        response_data = url.read()  # Read the data once and store it in a variable
        print(response_data)          # Print the raw response
        decoded = bdecode(response_data)  # Decode the response using the stored data
        print(decoded)                # Print the decoded dictionary

infohash = sys.argv[1]  # Read info hash from command line

encoded_infohash = urllib.parse.quote(binascii.a2b_hex(infohash))  # Encode info_hash
announce_url = f"http://my_tracker_ip:6969/announce?info_hash={encoded_infohash}"
announce(announce_url)
