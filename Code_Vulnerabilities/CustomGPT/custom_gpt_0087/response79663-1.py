
import threading

# Create a thread-safe dictionary
class ThreadSafeDict:
    def __init__(self):
        self.data = {}
        self.lock = threading.Lock()

    def set_value(self, key, value):
        with self.lock:
            self.data[key] = value

    def get_value(self, key):
        with self.lock:
            return self.data.get(key, None)

# Example usage
user_status = ThreadSafeDict()

def update_user_status(username, status):
    user_status.set_value(username, status)
    print(f"Updated {username} status to {status}")

def get_user_status(username):
    status = user_status.get_value(username)
    print(f"{username} status is {status}")
    return status

# Simulating multi-threaded access
threads = []
for i in range(10):
    username = f'user{i}'
    thread = threading.Thread(target=update_user_status, args=(username, i % 2 == 0))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

# Check status
for i in range(10):
    username = f'user{i}'
    get_user_status(username)
