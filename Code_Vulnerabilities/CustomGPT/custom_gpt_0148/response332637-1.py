
import sys
import time
import libtorrent as lt

# Create a file storage for the torrent
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")

# Generate the torrent file
torrent = t.generate()
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Start a session
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent to the session
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': './', 'seed_mode': True})

# Seed the torrent
print("Seeding...")
while True:
    # Check the status of the torrent
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', 
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    # Break if the user wants to stop the seeding
    if s.state == lt.torrent_status.seeding:
        break

    time.sleep(1)
