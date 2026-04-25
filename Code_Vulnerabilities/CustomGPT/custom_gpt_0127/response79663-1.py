
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
            return self.data.get(key, None)

    def remove(self, key):
        with self.lock:
            if key in self.data:
                del self.data[key]

# Example usage
safe_dict = ThreadSafeDict()

# Thread function to simulate dictionary access
def update_user_status(username, status):
    safe_dict.set(username, status)

# Simulating multiple threads updating the dictionary
threads = []
for i in range(10):
    t = threading.Thread(target=update_user_status, args=(f"user_{i}", i % 2 == 0))
    threads.append(t)
    t.start()

# Join threads to ensure completion
for t in threads:
    t.join()

# Print dictionary contents
print(safe_dict.data)
