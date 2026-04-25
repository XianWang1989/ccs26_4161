
import threading

# Define a thread-safe dictionary using a lock
class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def get(self, key):
        with self.lock:
            return self.data.get(key)

    def set(self, key, value):
        with self.lock:
            self.data[key] = value

    def delete(self, key):
        with self.lock:
            if key in self.data:
                del self.data[key]

# Example usage
user_status = ThreadSafeDict()

def update_user_status(username, status):
    user_status.set(username, status)

def get_user_status(username):
    return user_status.get(username)

# Example thread function
def handle_request(username, status):
    update_user_status(username, status)
    print(f"Updated {username} status to {status}")

# Simulating thread requests
threads = []
for i in range(10):
    t = threading.Thread(target=handle_request, args=(f'user{i}', True))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Check results
for i in range(10):
    print(f"user{i}: {user_status.get(f'user{i}')}")
