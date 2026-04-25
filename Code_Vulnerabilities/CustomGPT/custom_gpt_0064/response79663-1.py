
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

    def remove(self, key):
        with self.lock:
            if key in self.data:
                del self.data[key]

# Example usage
thread_safe_dict = ThreadSafeDict()

def update_user_status(username, status):
    thread_safe_dict.set(username, status)

def fetch_user_status(username):
    return thread_safe_dict.get(username)

# Simulated thread usage
threads = []
for i in range(10):
    t = threading.Thread(target=update_user_status, args=(f'user{i}', i % 2 == 0))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Fetching a user's status
print(fetch_user_status('user1'))  # Output: True or False based on the last update
