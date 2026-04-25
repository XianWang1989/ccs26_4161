
import sys
import time
import libtorrent as lt

# Create a file storage object and add files
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")

# Create a torrent object and set properties
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.opentrackr.org:1337", 0)  # Updated tracker
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")

# Generate the torrent file
torrent = t.generate()

# Save the torrent file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Create a session
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent and set it to seed mode
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '/tmp', 'seed_mode': True})

# Loop to maintain seeding status
try:
    while True:
        s = h.status()
        state_str = ['queued', 'checking', 'downloading metadata', 
                     'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

        print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % \
              (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
        sys.stdout.flush()

        time.sleep(1)
except KeyboardInterrupt:
    print("\nSeeding stopped.")
