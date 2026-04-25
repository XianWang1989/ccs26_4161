
import threading

# Create a thread-safe dictionary
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
safe_dict = ThreadSafeDict()

def worker(username):
    # Update the dictionary for a user
    safe_dict.set(username, True)

# Simulating multiple threads updating the dictionary
threads = []
for i in range(20):
    username = f'user{i}'
    thread = threading.Thread(target=worker, args=(username,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Checking the results
print(safe_dict.data)
