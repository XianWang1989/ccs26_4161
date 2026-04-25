
import sys
import time
import libtorrent as lt

# Create a torrent
def create_torrent(file_path):
    fs = lt.file_storage()
    lt.add_files(fs, file_path)
    t = lt.create_torrent(fs)
    t.add_tracker("udp://tracker.publicbt.com:80")
    t.set_creator("My Torrent")
    t.set_comment("Test")
    lt.set_piece_hashes(t, ".")
    torrent = t.generate()

    with open("mytorrent.torrent", "wb") as f:
        f.write(lt.bencode(torrent))

    return torrent

# Function to seed the torrent
def seed_torrent(torrent):
    ses = lt.session()
    ses.listen_on(6881, 6891)

    # Add torrent to session
    h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '/tmp', 'seed_mode': True})

    while True:  # Loop indefinitely to seed
        s = h.status()
        state_str = ['queued', 'checking', 'downloading metadata',
                     'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

        print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
              (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
        sys.stdout.flush()

        if s.state == lt.torrent_status.seeding:
            print("\nSeeding...")
            # Optionally, you could implement a stopping condition here

        time.sleep(1)

if __name__ == "__main__":
    file_path = "./test.txt"  # Path to the file you want to torrent
    torrent = create_torrent(file_path)
    seed_torrent(torrent)
