
import threading

class ThreadSafeDict:
    def __init__(self):
        self._lock = threading.Lock()
        self._dict = {}

    def update(self, username, value):
        with self._lock:  # Acquire the lock before modifying the dictionary
            self._dict[username] = value

    def get(self, username):
        with self._lock:  # Acquire the lock before reading the dictionary
            return self._dict.get(username, None)

# Example usage
def worker(username, value):
    safe_dict.update(username, value)
    print(f"Updated: {username} -> {value}")

safe_dict = ThreadSafeDict()

# Simulating multiple threads updating the dictionary
threads = []
for i in range(10):
    username = f'user{i}'
    value = i % 2 == 0  # Just a sample boolean value
    thread = threading.Thread(target=worker, args=(username, value))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Check the dictionary contents
print("Final dictionary state:", safe_dict._dict)
