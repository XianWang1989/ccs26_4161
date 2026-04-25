
def decode_peers(peers):
    peer_list = []
    for i in range(0, len(peers), 6):
        ip = '.'.join(str(peers[i + j]) for j in range(4))
        port = (peers[i + 4] << 8) + peers[i + 5]
        peer_list.append((ip, port))
    return peer_list
