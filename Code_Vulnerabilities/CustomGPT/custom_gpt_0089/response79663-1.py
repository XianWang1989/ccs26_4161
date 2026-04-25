
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

    def delete(self, key):
        with self.lock:
            if key in self.data:
                del self.data[key]

# Usage example
if __name__ == "__main__":
    ts_dict = ThreadSafeDict()

    # Example function to update the dictionary
    def update_user_status(username, status):
        ts_dict.set(username, status)

    # Example threads
    threads = []
    for i in range(8):  # simulating 8 threads
        thread = threading.Thread(target=update_user_status, args=(f'user{i}', True))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Print the dictionary contents
    print(ts_dict.data)
