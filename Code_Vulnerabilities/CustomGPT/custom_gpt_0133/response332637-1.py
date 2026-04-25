
import sys
import time
import libtorrent as lt

# Step 1: Create the torrent file
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")
torrent = t.generate()

# Save the created torrent file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Step 2: Start session and add torrent to it
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent to the session in seed mode
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': './', 'seed_mode': True})

# Step 3: Run the loop to display seeding status
print("Seeding...")
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata',
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    # Check if the seeding is complete. You might want to adjust this condition.
    if s.state != lt.torrent_status.seeding:
        time.sleep(1)
        continue

    time.sleep(5)  # Sleep longer after reaching seeding state

# Important: Ensure to keep the program running while seeding
