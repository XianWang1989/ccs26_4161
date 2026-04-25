
import sys
import time
import libtorrent as lt

# Create a file storage object and add a file
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")
t = lt.create_torrent(fs)

# Add a tracker
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")

# Generate the torrent
torrent = t.generate()

# Write the torrent file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Set up the session
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent for seeding
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '/tmp', 'seed_mode': True})

# Keep seeding and reporting status
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata',
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print(f'\r{100*s.progress:.2f}% complete (down: {s.download_rate/1000:.1f} kb/s up: {s.upload_rate/1000:.1f} kB/s peers: {s.num_peers}) {state_str[s.state]}', end='')

    # Sleep for a while before checking the status again
    time.sleep(1)
