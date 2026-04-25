
import sys
import time
import libtorrent as lt

# Function to create a torrent
def create_torrent(filepath, tracker_url):
    fs = lt.file_storage()
    lt.add_files(fs, filepath)
    t = lt.create_torrent(fs)
    t.add_tracker(tracker_url)
    t.set_creator("My Torrent")
    t.set_comment("Test")
    lt.set_piece_hashes(t, ".")
    return t.generate()

# Create the torrent
torrent = create_torrent("./test.txt", "udp://tracker.publicbt.com:80")

# Save it to a file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Set up the session and add the torrent
ses = lt.session()
ses.listen_on(6881, 6891)
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '/tmp', 'seed_mode': True})

# Start seeding the torrent
print("Seeding...")
while True:
    s = h.status()
    state_str = [
        'queued', 'checking', 'downloading metadata',
        'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume'
    ]

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % 
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    if s.is_seed():
        print("\nSeeding complete!")
        break

    time.sleep(1)
