
import threading

class ThreadSafeDictionary:
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
    ts_dict = ThreadSafeDictionary()

    # Simulating multiple threads updating the dictionary
    def update_user(username, value):
        ts_dict.update(username, value)
        print(f"Updated {username} to {value}")

    threads = []
    for i in range(10):  # Simulating 10 users
        t = threading.Thread(target=update_user, args=(f'user{i}', i % 2 == 0))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Final dictionary state:", ts_dict.data)
