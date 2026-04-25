
import threading

class ThreadSafeDictionary:
    def __init__(self):
        self._dict = {}
        self._lock = threading.Lock()

    def set_value(self, username, value):
        with self._lock:
            self._dict[username] = value

    def get_value(self, username):
        with self._lock:
            return self._dict.get(username)

# Example usage
if __name__ == "__main__":
    safe_dict = ThreadSafeDictionary()

    # Simulate two threads updating the dictionary
    def update_dict(username, value):
        safe_dict.set_value(username, value)
        print(f"Updated {username} to {value}")

    thread1 = threading.Thread(target=update_dict, args=("user1", True))
    thread2 = threading.Thread(target=update_dict, args=("user2", False))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(safe_dict.get_value("user1"))
    print(safe_dict.get_value("user2"))
