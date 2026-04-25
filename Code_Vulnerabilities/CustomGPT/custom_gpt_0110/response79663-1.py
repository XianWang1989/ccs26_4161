
import threading

# Thread-safe dictionary implementation
class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def update(self, username, value):
        with self.lock:  # Acquire the lock before modifying
            self.data[username] = value

    def get(self, username):
        with self.lock:  # Acquire the lock before reading
            return self.data.get(username)

    def remove(self, username):
        with self.lock:  # Acquire the lock before removing
            if username in self.data:
                del self.data[username]

# Example usage
safe_dict = ThreadSafeDict()

def handle_request(username, value):
    # Simulate processing and updating the dictionary
    safe_dict.update(username, value)
    print(f"Updated {username}: {safe_dict.get(username)}")

# Simulate concurrent requests
threads = []
for i in range(5):
    t = threading.Thread(target=handle_request, args=(f'user_{i}', True))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
