
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

# Usage example
user_status = ThreadSafeDict()

# Example function that updates the dictionary
def update_user_status(username, status):
    user_status.set(username, status)
    print(f"Updated {username}: {status}")

# Simulating concurrent updates
threads = []
for i in range(10):
    username = f"user{i}"
    status = i % 2 == 0  # Just an example of Boolean value
    thread = threading.Thread(target=update_user_status, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print the final state of the dictionary
print(user_status.data)
