
import sys
import time
import libtorrent as lt

# Create a file storage object and add the file
fs = lt.file_storage()
lt.add_files(fs, './test.txt')
t = lt.create_torrent(fs)
t.add_tracker('udp://tracker.publicbt.com:80')
t.set_creator('My Torrent')
t.set_comment('Test')
lt.set_piece_hashes(t, '.')
torrent = t.generate()

# Save the torrent file
with open('mytorrent.torrent', 'wb') as f:
    f.write(lt.bencode(torrent))

# Start seeding
ses = lt.session()
ses.listen_on(6881, 6891)

# Add the torrent to the session
h = ses.add_torrent({'ti': lt.torrent_info(torrent), 'save_path': '/tmp', 'seed_mode': True})

print('Seeding...')

# Monitor the seeding status
while True:
    s = h.status()
    state_str = ['queued', 'checking', 'downloading metadata', 
                 'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']

    print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % 
          (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    sys.stdout.flush()

    if s.state == lt.torrent_status.seeding:
        print("\nSeeding complete!")
        break

    time.sleep(1)
