
import threading

class ThreadSafeDictionary:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set(self, key, value):
        with self.lock:
            self.data[key] = value
            print(f'Set {key} to {value}')

    def get(self, key):
        with self.lock:
            value = self.data.get(key)
            print(f'Get {key}: {value}')
            return value

# Example usage
if __name__ == "__main__":
    safe_dict = ThreadSafeDictionary()

    def update_user_status(username, status):
        safe_dict.set(username, status)

    def retrieve_user_status(username):
        return safe_dict.get(username)

    # Simulate multi-threaded access
    threads = []
    for i in range(5):
        t1 = threading.Thread(target=update_user_status, args=(f'user{i}', True))
        t2 = threading.Thread(target=retrieve_user_status, args=(f'user{i}',))
        threads.append(t1)
        threads.append(t2)
        t1.start()
        t2.start()

    for t in threads:
        t.join()
