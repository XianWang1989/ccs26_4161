
import sys
import time
import libtorrent as lt

# Step 1: Create a torrent file
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")  # Add your file here
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")  # Add a tracker
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")
torrent = t.generate()

# Save the generated torrent file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Step 2: Start the session and add the torrent
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent to the session in seed mode
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '/tmp', 'seed_mode': True})

# Step 3: Seed the torrent
print("Seeding the torrent...")
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', 'downloading', 
                 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % 
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, 
           s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    # Check if we need to break the loop
    if s.state == lt.torrent_status.seeding:
        break

    time.sleep(1)
