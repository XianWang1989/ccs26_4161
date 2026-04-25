
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
            return self.data.get(key)

    def remove(self, key):
        with self.lock:
            if key in self.data:
                del self.data[key]

# Example usage
user_status = ThreadSafeDict()

def update_user_status(username, status):
    user_status.set(username, status)

def check_user_status(username):
    return user_status.get(username)

# Simulating multi-threaded updates
if __name__ == "__main__":
    import threading

    # Simulated threads for updating and checking user status
    threads = []
    for i in range(10):
        t = threading.Thread(target=update_user_status, args=(f'user{i}', i % 2 == 0))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Check statuses
    for i in range(10):
        print(f'user{i} status: {check_user_status(f"user{i}")}')
