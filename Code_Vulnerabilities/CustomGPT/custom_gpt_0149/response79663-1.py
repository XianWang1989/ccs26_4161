
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

# Example usage
safe_dict = ThreadSafeDict()

def update_user_status(username, status):
    safe_dict.set(username, status)
    print(f"Updated {username}: {status}")

# Simulating multiple threads updating the dictionary
threads = []
for i in range(5):
    username = f"user_{i}"
    thread = threading.Thread(target=update_user_status, args=(username, True))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

# Print the dictionary contents
print(safe_dict.data)
