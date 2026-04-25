
import sys
import time
import libtorrent as lt

# Function to create a torrent
def create_torrent(file_path, torrent_filename):
    fs = lt.file_storage()
    lt.add_files(fs, file_path)
    t = lt.create_torrent(fs)
    t.add_tracker("udp://tracker.publicbt.com:80")
    t.set_creator("My Torrent")
    t.set_comment("Test")
    lt.set_piece_hashes(t, ".")

    torrent = t.generate()

    with open(torrent_filename, "wb") as f:
        f.write(lt.bencode(torrent))

# Function to seed the torrent
def seed_torrent(torrent_filename):
    ses = lt.session()
    ses.listen_on(6881, 6891)

    # Add the torrent
    h = ses.add_torrent({'ti': lt.torrent_info(torrent_filename), 'save_path': '/tmp', 'seed_mode': True})

    print("Seeding...")
    while True:
        s = h.status()
        state_str = ['queued', 'checking', 'downloading metadata', 
                     'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

        print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % 
              (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]), end='')
        sys.stdout.flush()

        if s.state == lt.torrent_status.seeding:
            print("\nSeeding is active!")

        time.sleep(1)

if __name__ == "__main__":
    file_path = "./test.txt"
    torrent_filename = "mytorrent.torrent"

    # Create the torrent
    create_torrent(file_path, torrent_filename)

    # Seed the torrent
    seed_torrent(torrent_filename)
