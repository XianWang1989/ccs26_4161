
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
shared_dict = ThreadSafeDict()

# Function to update the dictionary
def update_dict(username, status):
    shared_dict.set(username, status)

# Function to read from the dictionary
def check_status(username):
    return shared_dict.get(username)

# Example of multi-threading
if __name__ == "__main__":
    threads = []
    for i in range(5):
        username = f'user{i}'
        t = threading.Thread(target=update_dict, args=(username, True))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Checking the status of a user
    print(check_status('user1'))  # Output: True
