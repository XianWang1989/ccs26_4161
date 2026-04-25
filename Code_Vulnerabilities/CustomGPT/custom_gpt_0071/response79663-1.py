
import threading

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

    def delete(self, key):
        with self.lock:
            if key in self.data:
                del self.data[key]

# Example usage
if __name__ == "__main__":
    ts_dict = ThreadSafeDict()

    # Example of setting values
    ts_dict.set('user1', True)
    print(ts_dict.get('user1'))  # Output: True

    # Example of deleting a value
    ts_dict.delete('user1')
    print(ts_dict.get('user1'))  # Output: None
