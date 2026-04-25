
import sys
import time
import libtorrent as lt

# Create a file storage for the torrent
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")  # Path to the file you want to seed
t = lt.create_torrent(fs)

# Add a tracker to the torrent
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")

# Generate the torrent metadata
lt.set_piece_hashes(t, ".")
torrent = t.generate()

# Save the torrent file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Create a session
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent for seeding
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '/tmp', 'seed_mode': True})

# Ensure the file is present in the 'save_path'
file_path = '/tmp/test.txt'  # Ensure this file exists
with open(file_path, 'wb') as f:
    f.write(b'This is a test file for seeding.')

# Monitor the seeding process
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', 
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    time.sleep(1)
