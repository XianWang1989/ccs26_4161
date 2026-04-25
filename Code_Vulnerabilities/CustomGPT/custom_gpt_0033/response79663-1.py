
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

    def delete(self, key):
        with self.lock:
            if key in self.data:
                del self.data[key]

# Example usage
if __name__ == "__main__":
    user_status = ThreadSafeDict()

    # Function to simulate user updates
    def update_user_status(username, status):
        user_status.set(username, status)

    # Simulating multiple threads updating user statuses
    threads = []
    for i in range(10):
        username = f'user{i}'
        # Alternate statuses
        status = i % 2 == 0
        thread = threading.Thread(target=update_user_status, args=(username, status))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Print the final user statuses
    print(user_status.data)
