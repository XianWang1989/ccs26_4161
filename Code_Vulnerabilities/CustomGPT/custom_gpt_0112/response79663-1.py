
import threading

# Create a thread-safe dictionary using a lock
class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def update(self, key, value):
        with self.lock:
            self.data[key] = value

    def get(self, key):
        with self.lock:
            return self.data.get(key, None)

# Example usage
thread_safe_dict = ThreadSafeDict()

def worker(username, value):
    thread_safe_dict.update(username, value)
    print(f"Updated {username} to {value}")

# Simulating multiple threads updating the dictionary
threads = []
for i in range(10):
    thread = threading.Thread(target=worker, args=(f'user{i}', i % 2 == 0))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Output the final state of the dictionary
print(thread_safe_dict.data)
