
import threading

class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def update(self, username, value):
        with self.lock:  # Ensure thread-safe access
            self.data[username] = value

    def get(self, username):
        with self.lock:  # Ensure thread-safe access
            return self.data.get(username)

# Example usage
def handle_request(username, value):
    safe_dict = ThreadSafeDict()
    safe_dict.update(username, value)
    status = safe_dict.get(username)
    print(f'User: {username}, Status: {status}')

# Simulating concurrent updates
threads = []
for i in range(5):
    t = threading.Thread(target=handle_request, args=(f'user{i}', True))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
