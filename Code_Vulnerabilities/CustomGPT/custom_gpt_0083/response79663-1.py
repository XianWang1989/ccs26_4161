
import threading

# Create a thread-safe dictionary
class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set(self, key, value):
        with self.lock:  # Acquire the lock before modifying the dictionary
            self.data[key] = value

    def get(self, key):
        with self.lock:  # Acquire the lock before accessing the dictionary
            return self.data.get(key)

# Example usage
safe_dict = ThreadSafeDict()

def update_user_status(username, status):
    safe_dict.set(username, status)

def check_user_status(username):
    return safe_dict.get(username)

# In your web server logic, you can call update_user_status and check_user_status
