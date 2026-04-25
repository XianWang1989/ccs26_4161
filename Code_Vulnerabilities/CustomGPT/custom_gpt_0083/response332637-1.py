
import sys
import time
import libtorrent as lt

# Create a file storage object and add files to it
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")

# Generate the torrent file
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")
torrent = t.generate()

# Save the torrent file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Start the session and set the listening ports
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent to the session in seed mode
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '/tmp', 'seed_mode': True})

# Seeding loop
while True:
    # Output the status of the torrent
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', 
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % 
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]), end='')
    sys.stdout.flush()

    # Wait before next status update
    time.sleep(1)

    # Break if we are not seeding anymore (optional)
    if not h.is_seed():
        break
