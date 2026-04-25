
import sys
import time
import libtorrent as lt

# Create a file storage object and add files
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")
torrent = t.generate()

# Write the torrent to a file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Start a session
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent to the session
params = {
    'ti': lt.torrent_info(torrent),
    'save_path': './',   # Save the file in the current directory
    'seed_mode': True
}
h = ses.add_torrent(params)

# Create a test file and ensure it exists for seeding
with open('./test.txt', 'wb') as f:
    f.write(b"Test data to seed.")

# Seeding loop
print("Seeding...")
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', 
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    # Delay to avoid busy waiting
    time.sleep(1)

    # Break if we want to stop seeding (optional: implement a stop condition)
