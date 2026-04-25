
import threading

class ThreadSafeDictionary:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def get(self, key):
        with self.lock:
            return self.data.get(key, None)

    def set(self, key, value):
        with self.lock:
            self.data[key] = value

    def update(self, key, value):
        with self.lock:
            self.data[key] = value

# Example usage
def worker(username, shared_dict):
    # Simulate setting a value for a user
    shared_dict.set(username, True)
    print(f"{username}: {shared_dict.get(username)}")

if __name__ == "__main__":
    safe_dict = ThreadSafeDictionary()

    threads = []
    for i in range(20):
        username = f"user{i}"
        thread = threading.Thread(target=worker, args=(username, safe_dict))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
