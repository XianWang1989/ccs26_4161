
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
            return self.data.get(key)

    def __repr__(self):
        with self.lock:
            return repr(self.data)

# Example usage
safe_dict = ThreadSafeDict()

def update_user_status(username, status):
    safe_dict.set(username, status)

# Assuming you have multiple threads calling update_user_status
