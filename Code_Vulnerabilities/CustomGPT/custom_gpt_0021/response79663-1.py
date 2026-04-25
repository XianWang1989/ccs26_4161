
import threading

# Create a thread-safe dictionary
class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set(self, key, value):
        with self.lock:  # Acquire lock for thread-safe access
            self.data[key] = value

    def get(self, key):
        with self.lock:  # Acquire lock for thread-safe access
            return self.data.get(key)

    def remove(self, key):
        with self.lock:  # Acquire lock for thread-safe access
            if key in self.data:
                del self.data[key]

# Example usage
user_status = ThreadSafeDict()

def update_user_status(username, status):
    user_status.set(username, status)
    print(f"Updated {username} status to {status}")

# Simulating concurrent updates
threads = []
for i in range(10):
    username = f"user{i}"
    status = i % 2 == 0  # Setting Boolean values
    thread = threading.Thread(target=update_user_status, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Display final status
print(user_status.data)
