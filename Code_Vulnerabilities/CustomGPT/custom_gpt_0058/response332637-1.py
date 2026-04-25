
import sys
import time
import libtorrent as lt

# Step 1: Create the torrent
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")
torrent = t.generate()

# Step 2: Write the torrent to a file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Step 3: Start a session
ses = lt.session()
ses.listen_on(6881, 6891)

# Step 4: Add the torrent to the session
params = {
    'ti': lt.torrent_info(torrent),
    'save_path': '/tmp',
    'seed_mode': True
}
h = ses.add_torrent(params)

# Step 5: Allow the torrent to seed
print("Seeding...")
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', 'downloading',
                 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    # Sleep for 1 second to avoid excessive printing
    time.sleep(1)
