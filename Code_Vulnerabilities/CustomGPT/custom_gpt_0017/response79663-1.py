
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
            return self.data.get(username, None)

# Example usage
if __name__ == "__main__":
    ts_dict = ThreadSafeDictionary()

    # Example of updating the dictionary from multiple threads
    def update_user(username, value):
        ts_dict.update(username, value)
        print(f'{username} updated to {value}')

    threads = []
    for i in range(8):  # Simulating 8 threads
        username = f'user{i}'
        value = (i % 2 == 0)  # Random True/False
        t = threading.Thread(target=update_user, args=(username, value))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Checking the final state of the dictionary
    print(ts_dict.data)
