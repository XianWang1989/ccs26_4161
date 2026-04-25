
import sys
import time
import libtorrent as lt

# Create file storage and add files
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")  # Ensure this file exists
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")

# Generate the torrent
torrent = t.generate()

# Save the torrent file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Start the session for seeding
ses = lt.session()
ses.listen_on(6881, 6891)
h = ses.add_torrent({
    'ti': lt.torrent_info(torrent),
    'save_path': '/tmp',  # Ensure this path is valid
    'seed_mode': True
})

# Ensure the file is in the specified save path
with open("/tmp/test.txt", "wb") as f:  # Create the file if it doesn't exist
    f.write(b"Testing seeding functionality.")

# Monitor seeding status
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', 
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % (
        s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    time.sleep(1)
