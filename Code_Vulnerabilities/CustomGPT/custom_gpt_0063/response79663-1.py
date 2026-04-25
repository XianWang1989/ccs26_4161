
import threading

class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set_value(self, key, value):
        with self.lock:
            self.data[key] = value

    def get_value(self, key):
        with self.lock:
            return self.data.get(key, None)

    def remove_key(self, key):
        with self.lock:
            if key in self.data:
                del self.data[key]

# Example usage
if __name__ == "__main__":
    safe_dict = ThreadSafeDict()

    # Sample function to update the dictionary
    def update_user_status(username, status):
        safe_dict.set_value(username, status)

    # Sample function to read the dictionary
    def read_user_status(username):
        return safe_dict.get_value(username)

    # Launching threads as test cases
    threads = []
    for i in range(10):
        t1 = threading.Thread(target=update_user_status, args=(f'user_{i}', True))
        t2 = threading.Thread(target=read_user_status, args=(f'user_{i}',))
        threads.extend([t1, t2])
        t1.start()
        t2.start()

    for t in threads:
        t.join()

    print(safe_dict.data)
