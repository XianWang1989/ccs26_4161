
import threading

# Thread-safe dictionary
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

# Example usage
if __name__ == "__main__":
    ts_dict = ThreadSafeDict()

    # Simulate thread function
    def update_user(username, status):
        ts_dict.set(username, status)
        print(f"{username} set to {status}")

    # Threads
    threads = []
    for i in range(10):
        username = f'user{i}'
        threads.append(threading.Thread(target=update_user, args=(username, i % 2 == 0)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # Output the dictionary
    print(ts_dict.data)
