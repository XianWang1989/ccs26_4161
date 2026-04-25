
import threading

class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set_value(self, username, value):
        with self.lock:  # Acquiring the lock
            self.data[username] = value

    def get_value(self, username):
        with self.lock:  # Acquiring the lock
            return self.data.get(username)

    def remove_value(self, username):
        with self.lock:  # Acquiring the lock
            if username in self.data:
                del self.data[username]

# Example usage
thread_safe_dict = ThreadSafeDict()

def update_user(username, value):
    thread_safe_dict.set_value(username, value)

def check_user(username):
    return thread_safe_dict.get_value(username)

# Sample threads
t1 = threading.Thread(target=update_user, args=('user1', True))
t2 = threading.Thread(target=update_user, args=('user2', False))

t1.start()
t2.start()

t1.join()
t2.join()

print(thread_safe_dict.get_value('user1'))  # Output: True
print(thread_safe_dict.get_value('user2'))  # Output: False
