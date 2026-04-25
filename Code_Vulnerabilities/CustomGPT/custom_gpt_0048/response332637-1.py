
import sys
import time
import libtorrent as lt

# Create a file storage for the torrent
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")  # Specify the file to be shared
t = lt.create_torrent(fs)

# Add a tracker
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test comment")
lt.set_piece_hashes(t, ".")

# Generate the torrent
torrent = t.generate()

# Write the torrent to a file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Set up a session and start seeding
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent
h = ses.add_torrent({
    'ti': lt.torrent_info(torrent),
    'save_path': '/tmp',  # Ensure this path exists
    'seed_mode': True
})

# Run the seeder loop
print("Seeding... Press Ctrl+C to stop.")
try:
    while not h.is_seed():
        s = h.status()
        state_str = ['queued', 'checking', 'downloading metadata',
                     'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

        print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
              (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
        sys.stdout.flush()

        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopping seed.")
