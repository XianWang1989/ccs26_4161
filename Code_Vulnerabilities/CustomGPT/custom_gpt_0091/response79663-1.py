
import threading

class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set_value(self, key, value):
        with self.lock:  # Acquire the lock when modifying the dictionary
            self.data[key] = value

    def get_value(self, key):
        with self.lock:  # Acquire the lock when reading from the dictionary
            return self.data.get(key)

# Example usage
safe_dict = ThreadSafeDict()

# Function to update the dictionary
def update_dict(username, status):
    safe_dict.set_value(username, status)

# Function to get the status
def get_status(username):
    return safe_dict.get_value(username)

# Simulate multiple threads (for demonstration)
threads = []
for i in range(10):
    t1 = threading.Thread(target=update_dict, args=(f'user_{i}', True))
    t2 = threading.Thread(target=get_status, args=(f'user_{i}',))
    threads.append(t1)
    threads.append(t2)

for t in threads:
    t.start()

for t in threads:
    t.join()

# Print the dictionary content
print(safe_dict.data)
