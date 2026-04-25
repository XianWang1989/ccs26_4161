
import threading

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

def update_user_status(username, status):
    thread_safe_dict.set(username, status)

def get_user_status(username):
    return thread_safe_dict.get(username)

# Simulating updates from multiple threads
def simulate_requests():
    update_user_status('user1', True)
    print(f'user1 status: {get_user_status("user1")}')

threads = []
for _ in range(8):  # Simulating 8 threads
    thread = threading.Thread(target=simulate_requests)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
