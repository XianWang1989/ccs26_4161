
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
thread_safe_dict = ThreadSafeDict()

def handle_request(username, value):
    # Simulate some processing
    thread_safe_dict.update(username, value)
    print(f'Updated {username}: {value}')

# Example threads
threads = []
for i in range(5):
    t = threading.Thread(target=handle_request, args=(f'user{i}', True))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
