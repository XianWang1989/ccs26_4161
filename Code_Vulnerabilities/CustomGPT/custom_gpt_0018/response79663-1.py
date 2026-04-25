
import threading

# Create a thread-safe dictionary
class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()  # Initialize a lock
        self.data = {}  # Internal dictionary

    def set_item(self, key, value):
        with self.lock:  # Acquire lock before changing the dictionary
            self.data[key] = value

    def get_item(self, key):
        with self.lock:  # Acquire lock for read access
            return self.data.get(key)

# Example usage
user_status = ThreadSafeDict()

# Function to update user status
def update_user_status(username, status):
    user_status.set_item(username, status)

# Suppose this function is called in different threads for updating users
update_user_status('User1', True)
