
import sys
import time
import libtorrent as lt
import os

# File to be included in the torrent
file_path = "./test.txt"
if not os.path.isfile(file_path):
    print(f"File {file_path} does not exist.")
    sys.exit(1)

# Create a torrent
fs = lt.file_storage()
lt.add_files(fs, file_path)
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

# Specify the path for saving the file that is being seeded
save_path = '/tmp/'  # Ensure this is correct and writable
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': save_path, 'seed_mode': True})

# Create a file in the save_path for seeding
seed_file_path = os.path.join(save_path, os.path.basename(file_path))
with open(seed_file_path, 'wb') as f:
    f.write(b'This is a test file for seeding.')  # Ensure the file exists with some content

# Monitor the seeding status
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', \
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    if s.state == lt.torrent_status.seeding:
        print("\nSeeding!")
    elif s.state == lt.torrent_status.finished:
        print("\nTorrent finished downloading and is now seeding.")

    time.sleep(1)
