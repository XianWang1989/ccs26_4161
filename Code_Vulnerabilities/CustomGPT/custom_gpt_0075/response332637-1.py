
import sys
import time
import libtorrent as lt

# Function to create a torrent and seed it
def create_and_seed_torrent(file_path, save_path, tracker_url):
    # Create a file storage object and add files
    fs = lt.file_storage()
    lt.add_files(fs, file_path)

    # Create a torrent
    t = lt.create_torrent(fs)
    t.add_tracker(tracker_url)
    t.set_creator("My Torrent")
    t.set_comment("Test")
    lt.set_piece_hashes(t, ".")
    torrent = t.generate()

    # Save the torrent file
    with open("mytorrent.torrent", "wb") as f:
        f.write(lt.bencode(torrent))

    # Start a session and add the torrent
    ses = lt.session()
    ses.listen_on(6881, 6891)
    h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': save_path, 'seed_mode': True})

    # Monitor the seeding status
    while not h.is_seed():
        s = h.status()
        state_str = ['queued', 'checking', 'downloading metadata', 
                     'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

        print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
              (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, 
               s.num_peers, state_str[s.state]))
        sys.stdout.flush()

        time.sleep(1)

    print("\nSeeding complete!")

# Example Usage
create_and_seed_torrent('./test.txt', '/tmp', 'udp://tracker.publicbt.com:80')
