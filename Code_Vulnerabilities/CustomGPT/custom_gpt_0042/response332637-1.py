
import sys
import time
import libtorrent as lt

# Create a file storage object
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")  # Add the file to the torrent

# Create a torrent object
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")  # Add a tracker
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")  # Set the piece hashes
torrent = t.generate()

# Write the torrent file to disk
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Create a session and listen for connections
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent to the session in seed mode
h = ses.add_torrent({
    'ti': lt.torrent_info(torrent),
    'save_path': '/tmp',
    'seed_mode': True  # Ensure we're in seed mode
})

# Wait until the torrent is seeded
while not h.is_seed():
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata',
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))

    sys.stdout.flush()
    time.sleep(1)

print("Seeding complete!")
