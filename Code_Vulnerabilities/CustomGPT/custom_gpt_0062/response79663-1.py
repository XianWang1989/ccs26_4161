
import threading

class ThreadSafeDict:
    def __init__(self):
        self._dict = {}
        self._lock = threading.Lock()

    def update(self, username, value):
        with self._lock:  # Acquire the lock
            self._dict[username] = value  # Safe update

    def get(self, username):
        with self._lock:  # Acquire the lock for reading
            return self._dict.get(username)

# Example usage
if __name__ == "__main__":
    thread_safe_dict = ThreadSafeDict()

    def worker(username, value):
        thread_safe_dict.update(username, value)
        print(f"Updated {username} to {value}")

    # Simulate multithreading
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(f'user{i}', i % 2 == 0))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
