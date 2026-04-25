
import threading

class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def update(self, username, value):
        with self.lock:  # Acquiring the lock
            self.data[username] = value

    def get(self, username):
        with self.lock:  # Acquiring the lock
            return self.data.get(username)

# Example usage
safe_dict = ThreadSafeDict()

def worker(username):
    # Simulate updating the dictionary
    safe_dict.update(username, True)
    print(f"{username} updated status to {safe_dict.get(username)}")

# Simulating multiple threads trying to update the dictionary
threads = []
for i in range(10):
    t = threading.Thread(target=worker, args=(f'user{i}',))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()
