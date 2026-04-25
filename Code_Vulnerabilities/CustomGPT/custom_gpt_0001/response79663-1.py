
import threading

# Create a thread-safe dictionary using a regular dictionary and a lock.
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

# Example usage:
thread_safe_dict = ThreadSafeDict()

def update_user_status(username, status):
    thread_safe_dict.set(username, status)

def get_user_status(username):
    return thread_safe_dict.get(username)

# Simulating multi-threaded updates
def example_request_handler(username, status):
    update_user_status(username, status)
    print(f"Updated {username} to {status}. Current status: {get_user_status(username)}")

# Simulating concurrent requests
threads = []
for i in range(10):
    username = f"user{i}"
    status = True if i % 2 == 0 else False
    thread = threading.Thread(target=example_request_handler, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
