
import sys
import time
import libtorrent as lt

# Create a file storage for the torrent
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")  # Path to the file to be included in the torrent
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test comment")
lt.set_piece_hashes(t, ".")

# Generate the torrent
torrent = t.generate()
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Start the session and listen on specific ports
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent to the session to seed it
info = lt.torrent_info(torrent)
h = ses.add_torrent({'ti': info, 'save_path': '/tmp', 'seed_mode': True})

# Keep seeding until manually terminated
try:
    while True:
        s = h.status()
        state_str = ['queued', 'checking', 'downloading metadata', 
                     'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

        print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
              (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
        sys.stdout.flush()

        time.sleep(1)
except KeyboardInterrupt:
    print("\nSeeding stopped.")
