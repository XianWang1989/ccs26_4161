
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
            return self.data.get(username)

# Example usage
if __name__ == '__main__':
    safe_dict = ThreadSafeDict()

    def worker(username, value):
        safe_dict.update(username, value)
        print(f"{username}: {safe_dict.get(username)}")

    # Simulating multiple threads updating the dictionary
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(f'user{i}', True))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
