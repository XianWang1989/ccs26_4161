
import threading

class ThreadSafeDictionary:
    def __init__(self):
        self.lock = threading.Lock()
        self.storage = {}

    def set_value(self, username, value):
        with self.lock:
            self.storage[username] = value

    def get_value(self, username):
        with self.lock:
            return self.storage.get(username, None)

    def remove_user(self, username):
        with self.lock:
            if username in self.storage:
                del self.storage[username]

# Usage
thread_safe_dict = ThreadSafeDictionary()

def handle_request(username, value):
    # Simulate updating the dictionary
    thread_safe_dict.set_value(username, value)
    print(f"Updated {username} to {value}")

# Example of handling multiple threads
threads = []
for i in range(10):
    username = f"user_{i}"
    value = i % 2 == 0  # Boolean value
    thread = threading.Thread(target=handle_request, args=(username, value))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Display final state of the dictionary
print(thread_safe_dict.storage)
