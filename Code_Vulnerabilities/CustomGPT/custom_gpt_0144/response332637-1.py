import sys
import time
import libtorrent as lt
import os

# Define the path to the file you want to share
file_path = "./test.txt"
save_path = os.path.dirname(os.path.abspath(file_path))

# Create file storage and add the file
fs = lt.file_storage()
lt.add_files(fs, file_path)

# Create the torrent
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")

# Set piece hashes
lt.set_piece_hashes(t, save_path)

# Generate and save the torrent file
torrent = t.generate()
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Start a session and listen on a port range
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent without using 'seed_mode'
params = {
    'ti': lt.torrent_info(torrent),
    'save_path': save_path,
    'storage_mode': lt.storage_mode_t.storage_mode_sparse,
    'flags': lt.torrent_flags.default_flags
}
h = ses.add_torrent(params)

# Monitor the seeding process
print(f"Seeding {h.name()}...")
while not h.is_seed():
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata',
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']
    print(f'\r{s.progress * 100:.2f}% complete '
          f'(down: {s.download_rate / 1000:.1f} kB/s up: {s.upload_rate / 1000:.1f} kB/s '
          f'peers: {s.num_peers}) {state_str[s.state]}', end='')
    sys.stdout.flush()
    time.sleep(1)

print("\nSeeding complete.")
