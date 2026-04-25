
import sys
import time
import libtorrent as lt

# Create a file storage and add the file
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

# Start a session for seeding
ses = lt.session()
ses.listen_on(6881, 6891)

# Add torrent to the session
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '/tmp', 'seed_mode': True})

# Wait for the torrent to seed
print("Seeding... Press Ctrl+C to stop.")
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', 
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]), end='')

    # Check if the torrent is still seeding
    if not h.is_seed():
        print("\nNot seeding anymore.")
        break

    sys.stdout.flush()
    time.sleep(1)
