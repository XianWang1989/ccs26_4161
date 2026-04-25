
import threading

# Create a thread-safe dictionary
class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()  # Initialize the lock
        self.data = {}  # The underlying dictionary

    def set(self, key, value):
        with self.lock:  # Acquire the lock before updating
            self.data[key] = value

    def get(self, key):
        with self.lock:  # Acquire the lock for safe reading
            return self.data.get(key)

    def delete(self, key):
        with self.lock:  # Acquire the lock before deleting
            if key in self.data:
                del self.data[key]

# Example usage
user_status = ThreadSafeDict()

def update_user_status(username, status):
    user_status.set(username, status)

def get_user_status(username):
    return user_status.get(username)

# Simulating updates in different threads
thread1 = threading.Thread(target=update_user_status, args=('user1', True))
thread2 = threading.Thread(target=update_user_status, args=('user2', False))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# Fetching user status
print(get_user_status('user1'))  # Output: True
print(get_user_status('user2'))  # Output: False
