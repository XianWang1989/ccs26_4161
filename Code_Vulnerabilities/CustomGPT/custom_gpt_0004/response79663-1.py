
import threading

# Create a thread-safe dictionary
class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set_value(self, username, value):
        with self.lock:
            self.data[username] = value

    def get_value(self, username):
        with self.lock:
            return self.data.get(username)

# Example usage
safe_dict = ThreadSafeDict()

def update_user_status(username, status):
    safe_dict.set_value(username, status)

def get_user_status(username):
    return safe_dict.get_value(username)

# Simulating multi-threaded access
threads = []
for i in range(10):
    t = threading.Thread(target=update_user_status, args=(f'user{i}', i % 2 == 0))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Check user statuses
for i in range(10):
    print(f'user{i}: {get_user_status(f"user{i}")}')
