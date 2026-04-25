
import sys
import time
import libtorrent as lt

# Create torrent
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")  # Add your file here
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")
torrent = t.generate()

# Save .torrent file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Set up session
ses = lt.session()
ses.listen_on(6881, 6891)

# Add torrent to session
params = {
    'ti': lt.torrent_info(torrent),
    'save_path': '/tmp',  # Make sure this path is writable
    'seed_mode': True
}
h = ses.add_torrent(params)

# Seeding loop
print("Seeding the torrent...")
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata',
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    # Break the loop if no longer seeding
    if not h.is_seed():
        print("\nSeeding complete.")
        break

    time.sleep(1)
