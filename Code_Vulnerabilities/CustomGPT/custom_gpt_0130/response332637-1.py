
import sys
import time
import libtorrent as lt

# Create the file storage and add the file
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")

# Generate the torrent from the file storage
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")

# Save the torrent to a file
torrent = t.generate()
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Start a session and listen on the specified ports
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent in seed mode
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '/tmp', 'seed_mode': True})

# Manage the seed's status
print("Seeding...")
while True:
    s = h.status()
    state_str = [
        'queued', 'checking', 'downloading metadata',
        'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume'
    ]

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % 
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    # Sleep to reduce CPU usage
    time.sleep(1)

    # Break out of the loop after some time for demo purposes, remove to run indefinitely
    if s.state == lt.torrent_status.seeding:
        break
