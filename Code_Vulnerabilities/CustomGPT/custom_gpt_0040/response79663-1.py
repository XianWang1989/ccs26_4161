
import threading

# Create a thread-safe dictionary
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
if __name__ == "__main__":
    user_status = ThreadSafeDict()

    # Function to simulate updating the dictionary
    def update_user_status(username, status):
        user_status.update(username, status)
        print(f"Updated {username} to {status}")

    # Simulate multiple threads updating the dictionary
    threads = []
    for i in range(5):
        t = threading.Thread(target=update_user_status, args=(f"user{i}", True))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    # Print the dictionary contents
    print(user_status.data)
