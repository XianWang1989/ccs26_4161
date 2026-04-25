
import threading

class ThreadSafeDictionary:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

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
    thread_safe_dict = ThreadSafeDictionary()

    # Simulating multiple threads updating the dictionary
    def update_user(username, status):
        thread_safe_dict.set(username, status)

    threads = []
    for i in range(10):
        username = f'user{i}'
        status = bool(i % 2)  # Alternate True/False
        thread = threading.Thread(target=update_user, args=(username, status))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Check the dictionary state
    print(thread_safe_dict.data)
