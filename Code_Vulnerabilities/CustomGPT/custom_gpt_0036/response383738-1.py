
import sys
import binascii
import urllib.parse
import urllib.request
from bcode import bdecode

def announce(inputurl):
    with urllib.request.urlopen(inputurl) as response:
        data = response.read()  # Read the response once
        print("Raw Response: ", data)

        decoded = bdecode(data)  # Decode the response
        print("Decoded Response: ", decoded)

        # Extract the peers
        if b'peers' in decoded:
            if isinstance(decoded[b'peers'], bytes):
                # Convert byte string to list of peers
                num_peers = len(decoded[b'peers']) // 6
                peers = [
                    (decoded[b'peers'][i:i+6][0:4], decoded[b'peers'][i:i+6][4:6]) 
                    for i in range(0, num_peers * 6, 6)
                ]
                print("Peer List: ", peers)
            else:
                print("Peers format unexpected.")
        else:
            print("No peers found in response.")

infohash = sys.argv[1]  # Read info hash from command line
encoded_infohash = urllib.parse.quote(binascii.a2b_hex(infohash))  # Encode info_hash
announce_url = f"http://my_tracker_ip:6969/announce?info_hash={encoded_infohash}"
announce(announce_url)
