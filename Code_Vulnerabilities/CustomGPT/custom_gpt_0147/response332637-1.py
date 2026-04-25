
import sys
import time
import libtorrent as lt

# Create file storage and add files
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")

# Create torrent and set metadata
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")

# Generate the torrent
torrent = t.generate()

# Save torrent to file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Set up the libtorrent session
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent in seed mode
params = {
    'ti': lt.torrent_info(torrent),
    'save_path': '/tmp',  # Ensure this path is correct for your environment
    'seed_mode': True
}
h = ses.add_torrent(params)

# Check the seeding status
try:
    print("Seeding...")
    while True:
        # Get the status of the torrent
        s = h.status()
        state_str = ['queued', 'checking', 'downloading metadata', 
                     'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

        # Output the status
        print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % 
              (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
        sys.stdout.flush()

        # Sleep to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("\nStopping seeding...")
