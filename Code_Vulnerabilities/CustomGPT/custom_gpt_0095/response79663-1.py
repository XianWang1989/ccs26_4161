
import threading

class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def update(self, username, value):
        with self.lock:
            self.data[username] = value

    def get(self, username):
        with self.lock:
            return self.data.get(username, None)

# Example usage
if __name__ == "__main__":
    safe_dict = ThreadSafeDict()

    def worker(username, value):
        safe_dict.update(username, value)
        print(f"Updated {username} to {value}")

    # Simulating multiple threads
    threads = []
    for i in range(20):
        username = f"user{i}"
        value = i % 2 == 0  # Assigning Boolean value
        t = threading.Thread(target=worker, args=(username, value))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Display final dictionary
    print("Final dictionary state:", safe_dict.data)
