
import threading

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

# Example usage
safe_dict = ThreadSafeDict()

# Simulate setting values in multiple threads
def update_user_status(username, status):
    safe_dict.set(username, status)
    print(f"Updated {username}: {status}")

# Create threads to demonstrate thread safety
threads = []
for i in range(5):
    username = f'user{i}'
    status = True if i % 2 == 0 else False
    thread = threading.Thread(target=update_user_status, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Check the dictionary contents
print("Final dictionary:", safe_dict.data)
