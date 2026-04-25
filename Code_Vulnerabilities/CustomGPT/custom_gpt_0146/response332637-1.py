
import sys
import time
import libtorrent as lt

# Generate the torrent
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")  # Make sure test.txt exists in the same directory
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")
torrent = t.generate()

# Write the .torrent file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Create a session and add the torrent
ses = lt.session()
ses.listen_on(6881, 6891)

# Define the saved path for the file being seeded
save_path = '/tmp'
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': save_path, 'seed_mode': True})

# Create the file to be seeded in the save path
with open(f"{save_path}/test.txt", "wb") as f:
    f.write(b"Hello, this is a test file!")  # Ensure a file is there to seed

# Start seeding
print("Seeding...")
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', \
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    time.sleep(1)
