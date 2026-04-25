
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

    def __repr__(self):
        with self.lock:
            return repr(self.data)

# Example usage
thread_safe_dict = ThreadSafeDict()

# Function for updating the dictionary
def update_user_status(username, status):
    thread_safe_dict.set(username, status)

# Simulating concurrent updates
threads = []
for i in range(20):
    username = f"user_{i}"
    status = i % 2 == 0  # Randomly setting True/False
    thread = threading.Thread(target=update_user_status, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print the final state of the dictionary
print(thread_safe_dict)
