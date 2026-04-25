
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

    def remove(self, key):
        with self.lock:
            if key in self.data:
                del self.data[key]

# Example usage
thread_safe_dict = ThreadSafeDict()

def update_user(username, value):
    thread_safe_dict.set(username, value)
    print(f'Updated {username}: {value}')

# Assuming this function is called by multiple threads
update_user('user1', True)
update_user('user2', False)
