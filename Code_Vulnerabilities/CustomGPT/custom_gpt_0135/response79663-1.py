
import threading

# Create a thread-safe dictionary
class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def get(self, key):
        with self.lock:
            return self.data.get(key)

    def set(self, key, value):
        with self.lock:
            self.data[key] = value

    def remove(self, key):
        with self.lock:
            if key in self.data:
                del self.data[key]

# Example usage
def update_user_status(username, status, shared_dict):
    shared_dict.set(username, status)
    print(f"{username} status updated to {status}")

# Create an instance of the thread-safe dictionary
user_status = ThreadSafeDict()

# Simulate multiple threads updating the dictionary
threads = []
for i in range(10):
    username = f"user{i}"
    thread = threading.Thread(target=update_user_status, args=(username, True, user_status))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Check final status of users
print("Final user statuses:", user_status.data)
