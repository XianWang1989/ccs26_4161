
import sys
import time
import libtorrent as lt

# Create file storage
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")
torrent = t.generate()

# Save the torrent file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Start the session
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent to session with seed mode
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '/tmp', 'seed_mode': True})

print("Seeding...")  # Let the user know it's seeding now

# Monitor the seeding status
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', 
                 'downloading', 'finished', 'seeding', 
                 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, 
           s.upload_rate / 1000, s.num_peers, state_str[s.state]),
          end='')

    if s.is_seed:
        print("\nSeeding complete!")
        break

    sys.stdout.flush()
    time.sleep(1)
