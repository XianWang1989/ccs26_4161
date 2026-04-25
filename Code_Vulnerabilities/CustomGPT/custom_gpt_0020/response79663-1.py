
import threading

class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def update(self, username, value):
        with self.lock:  # Acquires the lock before updating
            self.data[username] = value

    def get(self, username):
        with self.lock:  # Acquires the lock before reading
            return self.data.get(username)

    def __repr__(self):
        with self.lock:  # Acquires the lock for safe representation
            return str(self.data)

# Example usage
def worker(username, value, thread_safe_dict):
    print(f"Updating {username} to {value}")
    thread_safe_dict.update(username, value)
    print(f"Current state: {thread_safe_dict}")

if __name__ == "__main__":
    thread_safe_dict = ThreadSafeDict()

    # Create some threads to simulate requests
    threads = []
    for i in range(5):  # Simulating 5 users
        username = f"user{i}"
        value = True if i % 2 == 0 else False  # alternating True/False
        thread = threading.Thread(target=worker, args=(username, value, thread_safe_dict))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Final state: {thread_safe_dict}")
