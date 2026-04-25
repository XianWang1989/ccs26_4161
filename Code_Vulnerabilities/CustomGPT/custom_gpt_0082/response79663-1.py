
import threading

class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set_item(self, username, value):
        with self.lock:  # Acquire the lock
            self.data[username] = value

    def get_item(self, username):
        with self.lock:  # Acquire the lock
            return self.data.get(username, None)

# Example usage
safe_dict = ThreadSafeDict()

def update_user(username, value):
    safe_dict.set_item(username, value)

def fetch_user(username):
    return safe_dict.get_item(username)

# Simulating multiple threads updating and fetching
thread1 = threading.Thread(target=update_user, args=("user1", True))
thread2 = threading.Thread(target=fetch_user, args=("user1",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(safe_dict.data)
