
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

# Example usage
if __name__ == "__main__":
    safe_dict = ThreadSafeDict()

    def update_username(username, value):
        safe_dict.set(username, value)
        print(f"Updated {username} to {value}")

    # Simulate multiple threads updating the dictionary
    threads = []
    for i in range(5):
        t = threading.Thread(target=update_username, args=(f'user{i}', True))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Check final state of the dictionary
    print(safe_dict.data)
