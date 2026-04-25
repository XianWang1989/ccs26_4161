
import sys
import time
import libtorrent as lt

def create_torrent(file_path):
    fs = lt.file_storage()
    lt.add_files(fs, file_path)
    t = lt.create_torrent(fs)
    t.add_tracker("udp://tracker.publicbt.com:80")
    t.set_creator("My Torrent")
    t.set_comment("Test")
    lt.set_piece_hashes(t, ".")
    return t.generate()

def seed_torrent(torrent):
    ses = lt.session()
    ses.listen_on(6881, 6891)

    # Specify the save path
    save_path = '/tmp'

    # Ensure the torrent is added with seed_mode enabled
    h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': save_path, 'seed_mode': True})

    while True:
        s = h.status()
        state_str = ['queued', 'checking', 'downloading metadata', 
                     'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

        print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % 
              (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
        sys.stdout.flush()

        # Break the loop when the torrent is done seeding
        if s.state == lt.seeding:
            print("\nSeeding completed!")
            break

        time.sleep(1)

# Usage
if __name__ == '__main__':
    torrent = create_torrent("./test.txt")

    # Writing the torrent file
    with open("mytorrent.torrent", "wb") as f:
        f.write(lt.bencode(torrent))

    seed_torrent(torrent)
