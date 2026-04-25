
import sys
import time
import libtorrent as lt

# Create a file storage for the torrent metadata
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")  # Ensure the file path is correct

# Create the torrent
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.opentrackr.org:1337")  # Try a different tracker
t.set_creator("My Torrent")
t.set_comment("Test Torrent")
lt.set_piece_hashes(t, ".")
torrent = t.generate()

# Write the .torrent file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Create a session and listen for incoming connections
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent to the session with seed mode enabled
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '/tmp', 'seed_mode': True})

print("Seeding started...")

# Loop to monitor the seeding status
while not h.is_seed():  # Changed condition to wait until seeding starts
    time.sleep(1)

# Display the seeding status
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', 
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']
    print(f'\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % 
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]), end='')
    sys.stdout.flush()

    time.sleep(1)
