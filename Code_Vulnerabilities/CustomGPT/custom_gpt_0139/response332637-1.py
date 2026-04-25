
import sys
import time
import libtorrent as lt

# Generate the torrent
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")  # Ensure this file exists
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")

torrent = t.generate()

# Save the torrent file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Start the session and add the torrent for seeding
ses = lt.session()
ses.listen_on(6881, 6891)

# Adding the torrent with seed_mode set to True
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '/tmp/', 'seed_mode': True})

print("Seeding started...")

# Monitor seeding status
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', 
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % 
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]), end="")
    sys.stdout.flush()

    if s.state == lt.torrent_status.seeding:
        print("\nSeeding successfully!")

    time.sleep(1)
