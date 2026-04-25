
import threading

# Thread-safe dictionary
class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def update(self, key, value):
        with self.lock:
            self.data[key] = value

    def get(self, key):
        with self.lock:
            return self.data.get(key)

# Example usage
def handle_request(username, value):
    # Assume this function is called by multiple threads
    print(f"Processing request for {username} with value {value}")
    safe_dict.update(username, value)
    print(f"Updated {username}: {safe_dict.get(username)}")

# Create an instance of ThreadSafeDict
safe_dict = ThreadSafeDict()

# Simulating concurrent requests using threads
threads = []
for i in range(5):
    username = f'user{i}'
    value = True if i % 2 == 0 else False
    thread = threading.Thread(target=handle_request, args=(username, value))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Final output of the thread-safe dictionary
print("Final state of users:", safe_dict.data)
