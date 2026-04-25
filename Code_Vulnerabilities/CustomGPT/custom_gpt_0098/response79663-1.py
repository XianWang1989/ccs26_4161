
import threading

# Thread-safe dictionary wrapper
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
shared_dict = ThreadSafeDict()

def update_user_status(username, status):
    shared_dict.set(username, status)

def get_user_status(username):
    return shared_dict.get(username)

# Simulating threads
threads = []
for i in range(10):
    t = threading.Thread(target=update_user_status, args=(f'user_{i}', i % 2 == 0))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Print the final status of users
for i in range(10):
    print(f"user_{i}: {shared_dict.get(f'user_{i}')}") 
