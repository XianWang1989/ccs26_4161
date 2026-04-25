
import sys
import time
import libtorrent as lt

# Create file storage and add files
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")  # Path to your file

# Create a torrent
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")
torrent = t.generate()

# Save the torrent file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Start a session and listen for incoming connections
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent in seeding mode
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '.',
                     'seed_mode': True})

# Monitor seeding status
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata',
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    if s.state == lt.torrent_status.seeding:
        print("\nSeeding successfully!")
        break  # Stop when seeding

    time.sleep(1)
