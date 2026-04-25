
import threading

# Thread-safe dictionary
class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set(self, key, value):
        with self.lock:  # Acquire the lock
            self.data[key] = value

    def get(self, key):
        with self.lock:  # Acquire the lock
            return self.data.get(key)

    def remove(self, key):
        with self.lock:  # Acquire the lock
            if key in self.data:
                del self.data[key]

# Example usage
user_status = ThreadSafeDict()

def update_user_status(username, status):
    user_status.set(username, status)

def check_user_status(username):
    return user_status.get(username)

# Simulated thread function
def worker(username, status):
    update_user_status(username, status)
    print(f"Updated {username} to {status}. Current status: {check_user_status(username)}")

# Example of creating threads
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(f'user{i}', True))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
