
import threading

# Create a thread-safe dictionary
class ThreadSafeDict:
    def __init__(self):
        self._lock = threading.Lock()
        self._data = {}

    def set(self, key, value):
        with self._lock:
            self._data[key] = value

    def get(self, key):
        with self._lock:
            return self._data.get(key)

    def remove(self, key):
        with self._lock:
            if key in self._data:
                del self._data[key]

# Example usage
shared_dict = ThreadSafeDict()

def update_user_status(username, status):
    shared_dict.set(username, status)

def get_user_status(username):
    return shared_dict.get(username)

# Example threads
thread1 = threading.Thread(target=update_user_status, args=('user1', True))
thread2 = threading.Thread(target=update_user_status, args=('user2', False))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(shared_dict.get('user1'))  # Output: True
print(shared_dict.get('user2'))  # Output: False
