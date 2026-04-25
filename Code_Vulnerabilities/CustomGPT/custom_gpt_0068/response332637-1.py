
import sys
import time
import libtorrent as lt

# Set up file storage for the files to be added to the torrent
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")  # Ensure the path is correct.

# Create the torrent object
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")  # You may want to add multiple trackers
t.set_creator("My Torrent")
t.set_comment("Test")

# Set piece hashes; the current directory path should contain the files
lt.set_piece_hashes(t, ".")  # This sets the hashes based on files in the current directory.
torrent = t.generate()

# Write the torrent file to disk
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Start the session and listen for incoming connections
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent to the session in seed mode
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '/tmp', 'seed_mode': True})

# Loop to monitor seeding status
while True:
    s = h.status()
    if s.state == lt.torrent_status.seeding:
        print("Seeding complete!")
        break

    # Print torrent status
    state_str = ['queued', 'checking', 'downloading metadata', 
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    # Allow the session to process network events
    ses.start_dht()  # Enable DHT for better peer discovery
    ses.handle()  # Process events
    time.sleep(1)
