
import threading

# Create a thread-safe dictionary
class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set(self, key, value):
        with self.lock:
            self.data[key] = value

    def get(self, key):
        with self.lock:
            return self.data.get(key, None)

# Example usage
user_status = ThreadSafeDict()

def update_user_status(username, status):
    user_status.set(username, status)

def get_user_status(username):
    return user_status.get(username)

# Simulating thread execution
def simulate_request(username, status):
    update_user_status(username, status)
    print(f"Updated {username} to {status}")

# Create threads
threads = []
for i in range(5):
    t = threading.Thread(target=simulate_request, args=(f'user{i}', True))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

# Print final user statuses
for i in range(5):
    print(f"user{i}: {user_status.get(f'user{i}')}")
