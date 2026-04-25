
import threading

class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def update(self, username, value):
        with self.lock:  # Acquire the lock
            self.data[username] = value

    def get(self, username):
        with self.lock:  # Acquire the lock
            return self.data.get(username)

# Example usage
if __name__ == "__main__":
    thread_safe_dict = ThreadSafeDict()

    # Simulating multiple threads updating the dictionary
    def update_user_status(username, status):
        thread_safe_dict.update(username, status)
        print(f"Updated {username} to {status}")

    # You can use threading to simulate multiple requests
    threads = []
    for i in range(5):
        username = f"user{i}"
        status = i % 2 == 0  # Boolean value
        thread = threading.Thread(target=update_user_status, args=(username, status))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
