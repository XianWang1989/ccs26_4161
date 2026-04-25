
import threading

# Create a thread-safe dictionary
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
thread_safe_dict = ThreadSafeDict()

def handle_request(username, value):
    # Update the dictionary
    thread_safe_dict.update(username, value)
    print(f'Updated {username} to {value}')

# Simulating concurrent access
threads = []
for i in range(5):
    username = f'user{i}'
    value = (i % 2 == 0)  # Example boolean value
    thread = threading.Thread(target=handle_request, args=(username, value))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Print final dictionary state
print(thread_safe_dict.data)
