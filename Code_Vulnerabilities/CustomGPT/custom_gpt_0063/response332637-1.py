
import sys
import time
import libtorrent as lt

# Create a .torrent file
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")  # Path to file you want to seed
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")

# Save the torrent file
torrent = t.generate()
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Create a session and seed
ses = lt.session()
ses.listen_on(6881, 6891)

# Load the torrent and start seeding
h = ses.add_torrent({
    'ti': lt.torrent_info(torrent),
    'save_path': '/tmp',  # Directory where the files are stored
    'seed_mode': True     # Set to seed mode
})

# Start the event loop
print("Seeding... (press Ctrl+C to stop)")
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
