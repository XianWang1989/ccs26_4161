
import threading

# Initialize a thread-safe dictionary
class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set(self, key, value):
        with self.lock:  # This ensures thread-safe access
            self.data[key] = value

    def get(self, key):
        with self.lock:  # Ensure access while reading
            return self.data.get(key)

# Example usage
ts_dict = ThreadSafeDict()

# Function to update the dictionary
def update_user_status(username, status):
    ts_dict.set(username, status)

# Simulating multithreaded updates
threads = []
for i in range(5):
    t = threading.Thread(target=update_user_status, args=(f'user{i}', True))
    threads.append(t)
    t.start()

# Ensure all threads complete
for t in threads:
    t.join()

# Print the dictionary
print(ts_dict.data)
