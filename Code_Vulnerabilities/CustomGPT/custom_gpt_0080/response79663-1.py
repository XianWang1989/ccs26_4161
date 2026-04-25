
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

# Simulating concurrent updates
threads = []
for i in range(10):
    t = threading.Thread(target=update_user, args=(f'user{i}', i % 2 == 0))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Check results
for user in safe_dict.data:
    print(f'{user}: {safe_dict.get(user)}')
