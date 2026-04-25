
import sys
import time
import libtorrent as lt

# Function to create and seed a torrent
def create_and_seed_torrent(file_path, save_path, tracker_url):
    fs = lt.file_storage()
    lt.add_files(fs, file_path)

    # Create a torrent
    t = lt.create_torrent(fs)
    t.add_tracker(tracker_url)
    t.set_creator("My Torrent")
    t.set_comment("Test")
    lt.set_piece_hashes(t, ".")
    torrent = t.generate()

    # Save the .torrent file
    with open("mytorrent.torrent", "wb") as f:
        f.write(lt.bencode(torrent))

    # Start the session
    ses = lt.session()
    ses.listen_on(6881, 6891)

    # Add the torrent to the session
    h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': save_path, 'seed_mode': True})

    # Seed the torrent
    while True:
        s = h.status()
        state_str = ['queued', 'checking', 'downloading metadata', 'downloading', 
                     'finished', 'seeding', 'allocating', 'checking fastresume']

        print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
              (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, 
               s.num_peers, state_str[s.state]))
        sys.stdout.flush()

        # Break if the torrent is removed or not seeding anymore
        if not h.is_seed():
            print("\nNo longer seeding.")
            break

        time.sleep(1)

# Parameters
file_path = "./test.txt"
save_path = "/tmp"
tracker_url = "udp://tracker.publicbt.com:80"

create_and_seed_torrent(file_path, save_path, tracker_url)
