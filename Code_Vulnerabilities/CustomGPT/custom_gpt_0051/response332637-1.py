
import sys
import time
import libtorrent as lt

# Create a file storage and add a file
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")

# Generate the torrent
torrent = t.generate()
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Initialize the session and add the torrent
ses = lt.session()
ses.listen_on(6881, 6891)
params = {
    'ti': lt.torrent_info(torrent),
    'save_path': '/tmp',
    'seed_mode': True
}
h = ses.add_torrent(params)

# Seed the torrent
print("Seeding... Press Ctrl+C to quit.")
while True:
    s = h.status()
    state_str = [
        'queued', 'checking', 'downloading metadata',
        'downloading', 'finished', 'seeding',
        'allocating', 'checking fastresume'
    ]

    print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000,
           s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    time.sleep(1)
