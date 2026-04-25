
import sys
import time
import libtorrent as lt

# Specify the file to add to the torrent
file_path = "./test.txt"

# Create file storage and add the file
fs = lt.file_storage()
lt.add_files(fs, file_path)
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")

# Set piece hashes
lt.set_piece_hashes(t, ".")

# Generate the torrent
torrent = t.generate()

# Save the torrent file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Start the session
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent to the session, set to seed mode
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '/tmp', 'seed_mode': True})

# Wait for seeding
print("Seeding...")
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
        (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    # Check if we're still seeding
    if s.state != lt.torrent_status.seeding:
        print("\nNot seeding anymore")
        break

    time.sleep(1)
