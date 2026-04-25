
import threading

class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()  # Initialize a lock
        self.data = {}  # Your dictionary

    def set_value(self, username, value):
        with self.lock:  # Acquire lock before updating
            self.data[username] = value

    def get_value(self, username):
        with self.lock:  # Acquire lock before reading
            return self.data.get(username)

    def remove_user(self, username):
        with self.lock:  # Acquire lock before deletion
            if username in self.data:
                del self.data[username]

# Example usage
thread_safe_dict = ThreadSafeDict()

def update_user_status(username, status):
    thread_safe_dict.set_value(username, status)

def get_user_status(username):
    return thread_safe_dict.get_value(username)

# You can create threads that run these functions
