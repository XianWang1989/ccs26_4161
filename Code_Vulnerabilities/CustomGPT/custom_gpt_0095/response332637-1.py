
import sys
import time
import libtorrent as lt

# Step 1: Create a torrent file
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")
torrent = t.generate()

# Save the torrent file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Step 2: Set up the session and add the torrent
ses = lt.session()
ses.listen_on(6881, 6891)

# Make sure the directory exists
save_path = '/tmp/test_torrent'
import os
if not os.path.exists(save_path):
    os.makedirs(save_path)

# Add the torrent in seed mode
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': save_path, 'seed_mode': True})

# Step 3: Seed and monitor
print("Seeding... (Press Ctrl+C to stop)")
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', 'downloading', 
                 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, 
           s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    time.sleep(1)
