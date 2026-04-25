
import sys
import time
import libtorrent as lt

# Create a file storage and add files
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")

# Generate the torrent
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")

# Save the torrent file
torrent = t.generate()
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Set up the session and start seeding
ses = lt.session()
ses.listen_on(6881, 6891)
h = ses.add_torrent({
    'ti': lt.torrent_info(torrent),
    'save_path': '/tmp',
    'seed_mode': True
})

# Ensure the file exists in the save path before seeding
import os
if not os.path.exists('/tmp/test.txt'):
    print("File to seed not found. Please ensure it exists.")
    sys.exit(1)

# Seed the torrent and print status
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata',
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    # Break the loop if the torrent is no longer seeding
    if not h.is_seed():
        print("\nSeeding stopped.")
        break

    time.sleep(1)
