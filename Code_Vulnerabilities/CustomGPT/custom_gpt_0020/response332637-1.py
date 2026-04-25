
import sys
import time
import libtorrent as lt

# Step 1: Create the torrent file
def create_torrent():
    fs = lt.file_storage()
    lt.add_files(fs, "./test.txt")
    t = lt.create_torrent(fs)
    t.add_tracker("udp://tracker.publicbt.com:80")
    t.set_creator("My Torrent")
    t.set_comment("Test")
    lt.set_piece_hashes(t, ".")
    torrent = t.generate()

    with open("mytorrent.torrent", "wb") as f:
        f.write(lt.bencode(torrent))

# Step 2: Start seeding
def start_seeding():
    # Load the generated torrent
    with open("mytorrent.torrent", "rb") as f:
        torrent_data = f.read()
        t = lt.torrent_info(lt.bdecode(torrent_data))

    ses = lt.session()
    ses.listen_on(6881, 6891)

    # Make sure you specify the directory where the file is (where 'test.txt' is located)
    h = ses.add_torrent({'ti': t, 'save_path': './', 'seed_mode': True})

    print("Seeding...")

    # Step 3: Monitor the seeding status
    while True:
        s = h.status()
        state_str = ['queued', 'checking', 'downloading metadata', 
                     'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

        if s.is_seeding:
            print("Currently seeding...")

        print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
              (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))

        sys.stdout.flush()

        # Sleep for a while to prevent busy-waiting
        time.sleep(1)

# Execute the functions
create_torrent()
start_seeding()
