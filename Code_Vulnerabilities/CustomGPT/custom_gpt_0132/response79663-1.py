
import threading

class ThreadSafeDict:
    def __init__(self):
        self._lock = threading.Lock()
        self._data = {}

    def update(self, username, value):
        with self._lock:  # Acquire lock to ensure thread safety
            self._data[username] = value

    def get(self, username):
        with self._lock:  # Acquire lock for safe reading
            return self._data.get(username, None)

# Example usage
thread_safe_dict = ThreadSafeDict()

def update_user_status(username, value):
    thread_safe_dict.update(username, value)
    print(f"Updated {username}: {value}")

# Simulating multi-threaded updates
threads = []
for i in range(5):  # Creating 5 threads as an example
    t = threading.Thread(target=update_user_status, args=(f'user{i}', True))
    threads.append(t)
    t.start()

for t in threads:
    t.join()  # Wait for all threads to complete

# Retrieve a value safely
status = thread_safe_dict.get('user0')
print(f"user0 status: {status}")
