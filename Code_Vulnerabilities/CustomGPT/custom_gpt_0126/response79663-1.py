
import threading

# Thread-safe dictionary with a lock
class SafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set(self, key, value):
        with self.lock:  # Acquire the lock before modifying the dictionary
            self.data[key] = value

    def get(self, key):
        with self.lock:  # Acquire the lock for reading
            return self.data.get(key)

# Example usage
safe_dict = SafeDict()

def update_dict(username, status):
    safe_dict.set(username, status)
    print(f"Updated: {username} -> {status}")

# Simulate multiple threads updating the dictionary
threads = []
for i in range(10):
    username = f"user{i}"
    status = i % 2 == 0  # Assigning a Boolean value
    thread = threading.Thread(target=update_dict, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Display the safe dictionary contents
print("Final dictionary state:", safe_dict.data)
