
import sys
import time
import libtorrent as lt

# Step 1: Create a torrent file
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")  # Path to your file
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")
torrent = t.generate()

# Write the torrent file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Step 2: Initialize the session
ses = lt.session()
ses.listen_on(6881, 6891)

# Step 3: Add the torrent to the session in seed mode
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '/tmp', 'seed_mode': True})

# Step 4: Seed the torrent
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', 
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    if s.state == lt.torrent_status.seeding:
        print("\nSeeding...")
        break

    time.sleep(1)

# Keep the script running to allow seeding
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting...")
