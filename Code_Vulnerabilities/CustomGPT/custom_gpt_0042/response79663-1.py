
import threading

# Create a thread-safe dictionary
class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set(self, key, value):
        with self.lock:  # Acquire the lock before modifying the dictionary
            self.data[key] = value

    def get(self, key):
        with self.lock:  # Acquire the lock before accessing the dictionary
            return self.data.get(key)

    def remove(self, key):
        with self.lock:  # Acquire the lock before modifying the dictionary
            if key in self.data:
                del self.data[key]

# Example usage
safe_dict = ThreadSafeDict()

# Function to update the dictionary
def update_user_status(username, status):
    safe_dict.set(username, status)

# Using the dict in multiple threads
if __name__ == "__main__":
    import threading

    # Create threads for updating user statuses
    threads = []
    for i in range(10):  # Example: 10 users
        username = f"user{i}"
        status = i % 2 == 0  # Randomly set status
        thread = threading.Thread(target=update_user_status, args=(username, status))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Display final dictionary
    print(safe_dict.data)
