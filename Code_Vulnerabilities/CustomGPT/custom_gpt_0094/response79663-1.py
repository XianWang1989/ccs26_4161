
import threading

# Create a thread-safe dictionary using a standard dict
class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set_value(self, key, value):
        with self.lock:
            self.data[key] = value

    def get_value(self, key):
        with self.lock:
            return self.data.get(key)

    def delete_value(self, key):
        with self.lock:
            if key in self.data:
                del self.data[key]

# Example usage
thread_safe_dict = ThreadSafeDict()

def update_user_status(username, status):
    thread_safe_dict.set_value(username, status)

def get_user_status(username):
    return thread_safe_dict.get_value(username)

# Simulating concurrent updates
def simulate_requests():
    update_user_status("user1", True)
    print(f"user1 status: {get_user_status('user1')}")
    update_user_status("user2", False)
    print(f"user2 status: {get_user_status('user2')}")

# Create and start multiple threads
threads = []
for i in range(5):
    t = threading.Thread(target=simulate_requests)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
