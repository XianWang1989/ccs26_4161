
import threading

# Create a thread-safe dictionary
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

# Example usage
thread_safe_dict = ThreadSafeDict()

def update_user(username, status):
    thread_safe_dict.set(username, status)

def get_user_status(username):
    return thread_safe_dict.get(username)

# Example threads that update the dictionary
thread1 = threading.Thread(target=update_user, args=('user1', True))
thread2 = threading.Thread(target=update_user, args=('user2', False))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# Checking the statuses
print(thread_safe_dict.get('user1'))  # Output: True
print(thread_safe_dict.get('user2'))  # Output: False
