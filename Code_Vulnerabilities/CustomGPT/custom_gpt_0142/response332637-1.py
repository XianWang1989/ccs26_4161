
import sys
import time
import libtorrent as lt
import os

# Creating a torrent
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")
torrent = t.generate()

# Writing the torrent file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Check if the file exists at save_path
save_path = '/tmp'
file_to_seed = os.path.join(save_path, "test.txt")
if not os.path.exists(file_to_seed):
    print(f"Error: {file_to_seed} does not exist. Please check the path.")
    sys.exit(1)

# Starting the session to seed
ses = lt.session()
ses.listen_on(6881, 6891)

# Adding the torrent and starting to seed
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': save_path, 'seed_mode': True})

print("Seeding...")

# Seeding process
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', \
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state])):
    sys.stdout.flush()

    if h.is_seed():
        print("\nSeeding complete!")
        break

    time.sleep(1)
