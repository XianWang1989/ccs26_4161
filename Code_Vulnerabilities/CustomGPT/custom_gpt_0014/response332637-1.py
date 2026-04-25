
import sys
import time
import libtorrent as lt

# Create file storage and add files
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")

# Generate the torrent
torrent = t.generate()

# Write the torrent file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Start the session and add the torrent for seeding
ses = lt.session()
ses.listen_on(6881, 6891)

# Set the save path and add the torrent
h = ses.add_torrent({
    'ti': lt.torrent_info(torrent),
    'save_path': '/tmp',
    'seed_mode': True
})

# Ensure the file exists at save_path before seeding
with open('./test.txt', 'wb') as f:
    f.write(b'This is a test file for seeding.')

# Seeding loop
while True:
    s = h.status()
    state_str = [
        'queued', 'checking', 'downloading metadata',
        'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume'
    ]

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    if s.state == lt.torrent_status.seeding:
        print("Seeding...")

    time.sleep(1)
