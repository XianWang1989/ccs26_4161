
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

    # Function to simulate a thread updating the dictionary
    def update_user(username, value):
        safe_dict.update(username, value)
        print(f"Updated {username} to {value}")

    # Simulating multiple threads
    threads = []
    for i in range(10):
        username = f"user{i}"
        value = i % 2 == 0  # Example Boolean values
        thread = threading.Thread(target=update_user, args=(username, value))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Checking the results
    print(safe_dict.data)
