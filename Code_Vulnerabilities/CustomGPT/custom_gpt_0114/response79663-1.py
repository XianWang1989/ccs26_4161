
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
            return self.data.get(key, None)

# Example usage
thread_safe_dict = ThreadSafeDict()

def update_user_status(username, status):
    thread_safe_dict.set(username, status)

def get_user_status(username):
    return thread_safe_dict.get(username)

# Simulating thread updates
threads = []
for i in range(10):
    username = f'user{i}'
    status = i % 2 == 0  # Example status, True or False
    t = threading.Thread(target=update_user_status, args=(username, status))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Check results
for i in range(10):
    print(f'user{i}: {thread_safe_dict.get(f"user{i}")}')
