
import threading

# Thread-safe dictionary implementation
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

    def delete(self, key):
        with self.lock:
            if key in self.data:
                del self.data[key]

# Example usage
user_status = ThreadSafeDict()

def handle_request(username, status):
    # Update the dictionary in a thread-safe manner
    user_status.set(username, status)
    print(f"{username} status updated to: {status}")

# Simulating multiple threads updating the dictionary
threads = []
for i in range(10):
    username = f"user_{i}"
    status = i % 2 == 0  # Example Boolean value
    thread = threading.Thread(target=handle_request, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Display current users' statuses
for user in user_status.data:
    print(f"{user}: {user_status.get(user)}")
