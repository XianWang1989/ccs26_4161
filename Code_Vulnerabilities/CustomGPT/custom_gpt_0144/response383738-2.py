import socket
import struct

def parse_peers(peers_binary):
    peers = []
    for i in range(0, len(peers_binary), 6):
        ip = socket.inet_ntoa(peers_binary[i:i+4])
        port = struct.unpack(">H", peers_binary[i+4:i+6])[0]
        peers.append(f"{ip}:{port}")
    return peers
