
import sys
import time
import libtorrent as lt

# Create a file storage object and add a file to it
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")
t = lt.create_torrent(fs)

# Add a tracker and some metadata
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")

# Generate the torrent and save it
lt.set_piece_hashes(t, ".")
torrent = t.generate()

with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Create a session and listen on specified ports
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent for seeding
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '/tmp', 'seed_mode': True})

# Ensure the file exists in the specified path
with open("./test.txt", "rb") as file:
    data = file.read()
    with open('/tmp/test.txt', "wb") as seed_file:
        seed_file.write(data)

# Seed indefinitely
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', 
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % 
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    time.sleep(1)
