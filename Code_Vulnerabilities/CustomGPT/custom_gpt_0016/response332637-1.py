
import sys
import time
import libtorrent as lt
import os

# Step 1: Create a torrent
fs = lt.file_storage()
lt.add_files(fs, "./test.txt")  # Ensure test.txt exists in the current directory
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.publicbt.com:80")
t.set_creator("My Torrent")
t.set_comment("Test")
lt.set_piece_hashes(t, ".")
torrent = t.generate()

# Save the generated torrent file
with open("mytorrent.torrent", "wb") as f:
    f.write(lt.bencode(torrent))

# Step 2: Start the seeding session
ses = lt.session()
ses.listen_on(6881, 6891)

# Make sure the file exists in the save_path for seeding
save_path = '/tmp'
test_file_path = os.path.join(save_path, "test.txt")
if not os.path.exists(test_file_path):
    print(f"Error: The file '{test_file_path}' does not exist. Ensure the file is present for seeding.")
else:
    # Add torrent to the session in seed mode
    h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': save_path, 'seed_mode': True})

    # Step 3: Monitor seeding status
    while not h.is_seed():  # Loop until it is seeding
        s = h.status()
        state_str = ['queued', 'checking', 'downloading metadata',
                     'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

        print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % 
              (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
        sys.stdout.flush()

        time.sleep(1)

    print("\nSeeding completed successfully!")
