
import sys
import time
import libtorrent as lt

# Step 1: Generate the torrent file
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")  # Change the path to your file
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")
torrent = t.generate()

# Save the torrent to a file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Step 2: Setup the libtorrent session for seeding
ses = lt.session()
ses.listen_on(6881, 6891)  # Listen on the specified ports

# Start seeding the torrent
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '/tmp', 'seed_mode': True})

# Step 3: Monitor the seeding status
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', \
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    # Check if still seeding
    if not h.is_seed():
        print("Not seeding anymore!")
        break

    time.sleep(1)
