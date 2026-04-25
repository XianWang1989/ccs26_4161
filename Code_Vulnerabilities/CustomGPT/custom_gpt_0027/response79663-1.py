
import threading

class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def update(self, username, value):
        with self.lock:
            self.data[username] = value

    def get(self, username):
        with self.lock:
            return self.data.get(username, None)

# Example usage
def handle_request(username, value):
    shared_dict.update(username, value)
    print(f"Updated {username}: {shared_dict.get(username)}")

shared_dict = ThreadSafeDict()

# Simulated multi-threaded requests
threads = []
for i in range(10):
    t = threading.Thread(target=handle_request, args=(f"user{i}", i % 2 == 0))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
