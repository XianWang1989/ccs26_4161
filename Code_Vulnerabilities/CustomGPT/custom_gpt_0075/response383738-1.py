
import sys
import binascii
import urllib.parse
import urllib.request
from bcode import bdecode

def announce(inputurl):
    try:
        with urllib.request.urlopen(inputurl) as url:
            response = url.read()  # Read the response once
            print("Raw response:", response)
            decoded = bdecode(response)  # Decode the raw response
            print("Decoded response:", decoded)
            # Extract peer list if available
            peers = decoded.get(b'peers', b'')
            print("Peers:", peers)

    except Exception as e:
        print("An error occurred:", e)

infohash = sys.argv[1]  # Read info hash from command line

# Encode info_hash
encoded_infohash = urllib.parse.quote(binascii.a2b_hex(infohash))
announce_url = f"http://my_tracker_ip:6969/announce?info_hash={encoded_infohash}"
announce(announce_url)
