
import sys
import binascii
import urllib.parse
import urllib.request
from bcode import bdecode

def announce(inputurl):
    with urllib.request.urlopen(inputurl) as url:
        response_data = url.read()  # Read the response once
        print(response_data)  # Print raw response data
        decoded = bdecode(response_data)  # Decode the response
        print(decoded)  # Print the decoded data

if __name__ == "__main__":
    infohash = sys.argv[1]  # Read info hash from command line

    # Encode the infohash
    encoded_infohash = urllib.parse.quote(binascii.a2b_hex(infohash)) 
    announce_url = f"http://my_tracker_ip:6969/announce?info_hash={encoded_infohash}"
    announce(announce_url)
