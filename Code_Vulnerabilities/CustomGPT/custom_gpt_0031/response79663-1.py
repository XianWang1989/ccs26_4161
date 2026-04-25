
import threading

class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set(self, key, value):
        with self.lock:
            self.data[key] = value

    def get(self, key):
        with self.lock:
            return self.data.get(key)

# Example usage
safe_dict = ThreadSafeDict()

def update_user(username, status):
    safe_dict.set(username, status)
    print(f"Updated {username} to {status}")

# Simulating multiple threads updating the dictionary
threads = []
for i in range(10):
    t = threading.Thread(target=update_user, args=(f'user{i}', i % 2 == 0))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Check results
for i in range(10):
    print(f"user{i}: {safe_dict.get(f'user{i}')}")
