
import threading

class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set_value(self, username, value):
        with self.lock:
            self.data[username] = value

    def get_value(self, username):
        with self.lock:
            return self.data.get(username, None)

# Example usage
thread_safe_dict = ThreadSafeDict()

def update_user(username, value):
    thread_safe_dict.set_value(username, value)
    print(f"Updated {username} to {value}")

# Simulating concurrent updates
threads = []
for i in range(10):
    username = f"user{i}"
    value = i % 2 == 0
    thread = threading.Thread(target=update_user, args=(username, value))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
