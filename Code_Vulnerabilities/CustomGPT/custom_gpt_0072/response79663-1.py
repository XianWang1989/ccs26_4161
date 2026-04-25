
import threading

# Create a thread-safe dictionary using a regular dictionary and a lock
class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set_value(self, key, value):
        with self.lock:
            self.data[key] = value

    def get_value(self, key):
        with self.lock:
            return self.data.get(key)

    def remove_key(self, key):
        with self.lock:
            if key in self.data:
                del self.data[key]

# Example usage
def update_user_status(username, status, safe_dict):
    safe_dict.set_value(username, status)

# Create an instance of the ThreadSafeDict
user_statuses = ThreadSafeDict()

# Simulate concurrent updates (e.g., in different threads)
threads = []
for i in range(10):
    username = f'user{i}'
    status = i % 2 == 0  # Example Boolean value
    thread = threading.Thread(target=update_user_status, args=(username, status, user_statuses))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Print the final state of user statuses
print(user_statuses.data)
