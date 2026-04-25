
import threading

class ThreadSafeDict:
    def __init__(self):
        self.data = {}
        self.lock = threading.Lock()

    def set(self, key, value):
        with self.lock:
            self.data[key] = value

    def get(self, key):
        with self.lock:
            return self.data.get(key, None)

    def remove(self, key):
        with self.lock:
            if key in self.data:
                del self.data[key]

# Example usage
if __name__ == "__main__":
    thread_safe_dict = ThreadSafeDict()

    # Define a simple worker function to update the dictionary
    def update_dict(username, value):
        thread_safe_dict.set(username, value)

    # Create multiple threads to simulate concurrent access
    threads = []
    for i in range(20):  # Simulating 20 users
        username = f'user{i}'
        value = True if i % 2 == 0 else False
        thread = threading.Thread(target=update_dict, args=(username, value))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Print the thread-safe dictionary contents
    print(thread_safe_dict.data)
