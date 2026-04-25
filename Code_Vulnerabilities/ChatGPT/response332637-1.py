
import sys
import time
import libtorrent as lt

# Create file storage
fs = lt.file_storage()
# Add files to torrent
lt.add_files(fs, "./test.txt")  # Ensure this file exists
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")

# Generate the .torrent file
torrent = t.generate()
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Create a session and listen on ports for incoming connections
ses = lt.session()
ses.listen_on(6881, 6891)

# Add torrent with the forementioned save path
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '/tmp', 'seed_mode': True})

# Create a dummy file to seed
with open('/tmp/test.txt', 'wb') as f:
    f.write(b'This is a test file for seeding with libtorrent.')

# Main loop
print("Seeding...")
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata',
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    # Break the loop when the torrent is complete
    if s.state == lt.torrent_status.seeding:
        print("\nTorrent seeding successfully.")
        break

    time.sleep(1)
