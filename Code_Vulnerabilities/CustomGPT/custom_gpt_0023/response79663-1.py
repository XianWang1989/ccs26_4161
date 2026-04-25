
import threading

class ThreadSafeDictionary:
    def __init__(self):
        self.lock = threading.Lock()
        self.dict = {}

    def update(self, username, value):
        with self.lock:
            self.dict[username] = value

    def get(self, username):
        with self.lock:
            return self.dict.get(username)

# Example usage
thread_safe_dict = ThreadSafeDictionary()

def update_user_status(username, status):
    thread_safe_dict.update(username, status)

def get_user_status(username):
    return thread_safe_dict.get(username)

# This can be called from multiple threads without risking data corruption.
