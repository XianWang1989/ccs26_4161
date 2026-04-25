
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

    def remove(self, key):
        with self.lock:
            if key in self.data:
                del self.data[key]

# Example Usage
if __name__ == "__main__":
    thread_safe_dict = ThreadSafeDict()

    # Function to update the dictionary
    def update_dict(username, status):
        thread_safe_dict.set(username, status)
        print(f"Updated: {username} -> {status}")

    # Simulating multiple threads updating the dictionary
    threads = []
    for i in range(5):
        username = f"user_{i}"
        status = i % 2 == 0  # Random boolean
        t = threading.Thread(target=update_dict, args=(username, status))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Print the final state of the dictionary
    print(thread_safe_dict.data)
