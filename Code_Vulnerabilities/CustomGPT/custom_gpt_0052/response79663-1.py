
import threading

class ThreadSafeDictionary:
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
safe_dict = ThreadSafeDictionary()

def update_user_status(username, status):
    safe_dict.set(username, status)

def get_user_status(username):
    return safe_dict.get(username)

# Example threads
thread1 = threading.Thread(target=update_user_status, args=("user1", True))
thread2 = threading.Thread(target=get_user_status, args=("user1",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(safe_dict.get("user1"))  # Output: True
