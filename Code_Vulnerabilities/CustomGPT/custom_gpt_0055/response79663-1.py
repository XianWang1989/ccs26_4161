
import threading

# Thread-safe dictionary wrapper
class ThreadSafeDict:
    def __init__(self):
        self.data = {}
        self.lock = threading.Lock()

    def update(self, key, value):
        with self.lock:
            self.data[key] = value

    def get(self, key):
        with self.lock:
            return self.data.get(key, None)

# Example usage
def update_user_status(user_dict, username, status):
    user_dict.update(username, status)
    print(f'Updated {username} to {status}')

if __name__ == "__main__":
    user_dict = ThreadSafeDict()

    # Simulating updates from different threads
    threads = []
    for i in range(5):
        username = f"user{i}"
        status = True if i % 2 == 0 else False
        thread = threading.Thread(target=update_user_status, args=(user_dict, username, status))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(user_dict.data)
