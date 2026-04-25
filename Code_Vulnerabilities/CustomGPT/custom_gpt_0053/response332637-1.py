
import sys
import time
import libtorrent as lt

# Create a file storage object and add the file to the torrent
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")  # Ensure this file exists
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")

# Generate the torrent and save it to a file
torrent = t.generate()
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Initialize the session and add the torrent to it
ses = lt.session()
ses.listen_on(6881, 6891)

# Specify the save_path where the seeding file is located
save_path = '/tmp'  # Make sure your file is in this directory
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': save_path, 'seed_mode': True})

# Monitor the seeding status
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', 
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    if s.state == lt.torrent_status.seeding:
        break  # Exit if seeding
    time.sleep(1)
