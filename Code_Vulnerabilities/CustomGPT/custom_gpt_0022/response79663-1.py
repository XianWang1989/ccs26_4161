
import threading

class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def update(self, username, value):
        with self.lock:
            self.data[username] = value

    def get(self, username):
        with self.lock:
            return self.data.get(username)

# Example usage
safe_dict = ThreadSafeDict()

def handle_request(username, value):
    safe_dict.update(username, value)
    print(f"Updated {username} to {value}")

# Simulating concurrent updates
threads = []
for i in range(10):
    username = f"user{i}"
    value = i % 2 == 0  # Just a sample boolean value
    thread = threading.Thread(target=handle_request, args=(username, value))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
