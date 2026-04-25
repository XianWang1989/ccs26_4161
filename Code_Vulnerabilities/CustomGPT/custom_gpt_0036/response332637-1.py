
import sys
import time
import libtorrent as lt

# Step 1: Create the torrent file
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")  # Ensure the file exists
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")  # Add a tracker
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")
torrent = t.generate()

with open("mytorrent.torrent", "wb") as f:  # Use a context manager to handle the file
    f.write(lt.bencode(torrent))

# Step 2: Set up the session and add the torrent for seeding
ses = lt.session()
ses.listen_on(6881, 6891)  # Listen on port range for incoming connections

# Add the torrent to the session
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': './', 'seed_mode': True})

print("Seeding...")

# Step 3: Monitor the seeding process
while True:
    if h.is_seed():
        print("Seeding completed.")
        break

    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata',
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    time.sleep(1)
