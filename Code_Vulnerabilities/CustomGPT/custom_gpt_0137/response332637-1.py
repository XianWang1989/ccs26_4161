
import sys
import time
import libtorrent as lt

# Create a file storage and add a file
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")  # Specify the file to be added
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")  # Add a tracker
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")  # Set piece hashes

# Generate and save the torrent
torrent = t.generate()
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Start the session and listen for connections
ses = lt.session()
ses.listen_on(6881, 6891)  # Listening ports

# Add the torrent to the session with seeding mode enabled
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '/tmp/', 'seed_mode': True})

# Set a flag to check seeding status
is_seeding = True

# Loop to monitor the torrent status and ensure seeding
while True:
    s = h.status()

    if s.state == lt.torrent_status.seeding:
        print("Seeding...")
    elif is_seeding and s.state == lt.torrent_status.finished:
        print("Torrent finished downloading, starting to seed.")
        is_seeding = False  # Prevent printing multiple times

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d)' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers), end=' ')
    sys.stdout.flush()

    if h.is_seed():
        print("The torrent is now seeding.")
        break  # Exit loop when seeding is confirmed

    time.sleep(1)  # Delay for monitoring updates
