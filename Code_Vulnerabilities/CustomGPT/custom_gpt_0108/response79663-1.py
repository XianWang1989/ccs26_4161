
import threading

class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set_value(self, key, value):
        with self.lock:
            self.data[key] = value

    def get_value(self, key):
        with self.lock:
            return self.data.get(key, None)

# Example usage
thread_safe_dict = ThreadSafeDict()

def update_user_status(username, status):
    thread_safe_dict.set_value(username, status)

def get_user_status(username):
    return thread_safe_dict.get_value(username)

# Example Thread
def user_request(username, status):
    update_user_status(username, status)
    print(f"{username}: {get_user_status(username)}")

# Simulating concurrent requests
threads = []
for i in range(10):
    threads.append(threading.Thread(target=user_request, args=(f'user{i}', i % 2 == 0)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
