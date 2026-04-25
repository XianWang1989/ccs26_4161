
import sys
import time
import libtorrent as lt

# Create a file storage object
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")

# Create a torrent object and add a tracker
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")

# Set piece hashes and generate the torrent
lt.set_piece_hashes(t, ".")
torrent = t.generate()

# Save the torrent to a file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Set up the session for seeding
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent to the session in seed mode
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '/tmp', 'seed_mode': True})

# Wait until the torrent is successfully seeded
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', 
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' %
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    # Break the loop if the torrent has finished seeding
    if s.state == lt.torrent_status.seeding:
        print("\nSeeding started successfully!")
        break

    time.sleep(1)
