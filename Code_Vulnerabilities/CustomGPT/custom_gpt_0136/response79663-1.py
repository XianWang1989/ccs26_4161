
import threading

class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set_value(self, username, value):
        with self.lock:
            self.data[username] = value

    def get_value(self, username):
        with self.lock:
            return self.data.get(username, None)

# Usage example
safe_dict = ThreadSafeDict()

# Function to update the dictionary
def update_user_status(username, status):
    safe_dict.set_value(username, status)

# Start threads to update the user status
threads = []
for i in range(10):
    username = f'user{i}'
    status = i % 2 == 0  # Assign True for even, False for odd
    thread = threading.Thread(target=update_user_status, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print the dictionary content
print(safe_dict.data)
