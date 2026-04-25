
import sys
import time
import libtorrent as lt

# Create a file storage and add the file
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")

# Create the torrent and set its properties
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")

# Generate the torrent file
torrent = t.generate()
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Start a session and listen on a port
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent with seed mode
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '/tmp', 'seed_mode': True})

# Start seeding
print("Seeding...")
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', 'downloading', 
                 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
           s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    # Exit if the torrent is no longer seeding
    if not h.is_seed():
        print("\nStopped seeding.")
        break

    time.sleep(1)
