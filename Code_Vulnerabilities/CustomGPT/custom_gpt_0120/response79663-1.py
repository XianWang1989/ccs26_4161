
import threading

class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def update(self, username, value):
        with self.lock:
            self.data[username] = value

    def get(self, username):
        with self.lock:
            return self.data.get(username)

# Example usage
def handle_request(username, value):
    thread_safe_dict = ThreadSafeDict()
    thread_safe_dict.update(username, value)
    print(f"Updated {username}: {value}")

# Simulating multiple threads
threads = []
for i in range(10):
    username = f"user{i}"
    value = True if i % 2 == 0 else False
    thread = threading.Thread(target=handle_request, args=(username, value))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
