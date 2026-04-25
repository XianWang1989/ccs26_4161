
import threading

class ThreadSafeDictionary:
    def __init__(self):
        self._lock = threading.Lock()
        self._dict = {}

    def update(self, username, value):
        with self._lock:
            self._dict[username] = value

    def get(self, username):
        with self._lock:
            return self._dict.get(username, None)

# Example usage
if __name__ == "__main__":
    safe_dict = ThreadSafeDictionary()

    def worker(username, value):
        safe_dict.update(username, value)
        print(f"Updated {username} to {value}")

    threads = []
    for i in range(8):
        username = f"user{i}"
        threads.append(threading.Thread(target=worker, args=(username, i % 2 == 0)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # Print the dictionary
    print(safe_dict._dict)
