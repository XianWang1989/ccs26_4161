
import sys
import time
import libtorrent as lt

# Create the file storage
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

# Save the torrent file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Start a session
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent to the session with seed mode
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '/tmp', 'seed_mode': True})

# Wait for seeding
print("Seeding...")

while True:
    s = h.status()
    state_str = [
        'queued', 'checking', 'downloading metadata',
        'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume'
    ]

    # Print status
    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % 
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]), end='')

    # Sleep for a second
    time.sleep(1)

    # Break the loop if the torrent is finished
    if s.state == lt.torrent_status.seeding:
        break
