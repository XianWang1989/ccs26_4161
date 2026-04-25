
import threading

class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set_item(self, key, value):
        with self.lock:
            self.data[key] = value

    def get_item(self, key):
        with self.lock:
            return self.data.get(key, None)

    def remove_item(self, key):
        with self.lock:
            if key in self.data:
                del self.data[key]

# Example usage of ThreadSafeDict
if __name__ == "__main__":
    user_status = ThreadSafeDict()

    # Simulating multiple threads updating the dictionary
    def update_user_status(username, status):
        user_status.set_item(username, status)
        print(f"Updated {username} to {status}")

    # Assume these user updates come from different threads
    threads = []
    for i in range(5):
        username = f"user{i}"
        # Simulate both True and False statuses
        status = i % 2 == 0
        thread = threading.Thread(target=update_user_status, args=(username, status))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Print the final dictionary
    print("Final user statuses:", user_status.data)
