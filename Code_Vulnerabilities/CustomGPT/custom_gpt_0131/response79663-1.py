
import threading

# Create a thread-safe dictionary using a Lock
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
def update_user_status(username, status):
    user_status_dict.set(username, status)

def check_user_status(username):
    return user_status_dict.get(username)

user_status_dict = ThreadSafeDict()

# Simulate concurrent updates
thread1 = threading.Thread(target=update_user_status, args=("user1", True))
thread2 = threading.Thread(target=update_user_status, args=("user2", False))
thread3 = threading.Thread(target=check_user_status, args=("user1",))
thread4 = threading.Thread(target=check_user_status, args=("user2",))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

# Checking results
print(user_status_dict.data)
