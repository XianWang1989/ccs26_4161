
import threading

# Define a thread-safe dictionary using a standard dictionary and a lock
class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()  # Create a lock for thread safety
        self.data = {}  # The underlying dictionary

    def set(self, key, value):
        with self.lock:  # Acquire the lock before modifying the dictionary
            self.data[key] = value

    def get(self, key):
        with self.lock:  # Acquire the lock before reading from the dictionary
            return self.data.get(key, None)

    def delete(self, key):
        with self.lock:  # Acquire the lock before deleting an entry
            if key in self.data:
                del self.data[key]

# Example usage
def worker(username, safe_dict):
    safe_dict.set(username, True)  # Update the dictionary

# Create an instance of ThreadSafeDict
thread_safe_dict = ThreadSafeDict()

# Simulating multiple threads updating the dictionary
threads = []
for i in range(20):
    username = f'user{i}'
    thread = threading.Thread(target=worker, args=(username, thread_safe_dict))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Checking the result
print(thread_safe_dict.data)
