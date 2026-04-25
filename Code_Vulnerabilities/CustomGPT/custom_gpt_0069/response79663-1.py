
import threading

class ThreadSafeDictionary:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def update(self, username, value):
        with self.lock:
            self.data[username] = value

    def get(self, username):
        with self.lock:
            return self.data.get(username, None)

# Example usage
safe_dict = ThreadSafeDictionary()

def worker(username, value):
    safe_dict.update(username, value)
    print(f"Updated {username} to {value}")

# Simulate multiple threads updating the dictionary
threads = []
for i in range(10):
    username = f"user{i}"
    value = i % 2 == 0  # Boolean value
    thread = threading.Thread(target=worker, args=(username, value))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print the final state of the dictionary
print(safe_dict.data)
