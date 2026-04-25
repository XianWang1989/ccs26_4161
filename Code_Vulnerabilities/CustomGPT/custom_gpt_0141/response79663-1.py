
import threading

class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set_item(self, key, value):
        with self.lock:  # Acquire the lock before modifying the dictionary
            self.data[key] = value

    def get_item(self, key):
        with self.lock:  # Acquire the lock before reading the dictionary
            return self.data.get(key)

    def remove_item(self, key):
        with self.lock:  # Acquire the lock before modifying the dictionary
            if key in self.data:
                del self.data[key]

# Example usage
if __name__ == "__main__":
    thread_safe_dict = ThreadSafeDict()

    def update_dict(username, value):
        thread_safe_dict.set_item(username, value)
        print(f"Updated {username}: {value}")

    # Simulating multiple threads updating the dictionary
    threads = []
    for i in range(5):
        username = f"user{i}"
        thread = threading.Thread(target=update_dict, args=(username, True))
        threads.append(thread)
        thread.start()

    # Ensure all threads complete
    for thread in threads:
        thread.join()

    # Print the final state of the dictionary
    print(thread_safe_dict.data)
