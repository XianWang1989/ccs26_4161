
import threading

class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()  # Create a lock
        self.data = {}  # Initialization of the dictionary

    def update(self, username, value):
        with self.lock:  # Acquire the lock before updating
            self.data[username] = value  # Update the dictionary

    def get(self, username):
        with self.lock:  # Acquire the lock before reading
            return self.data.get(username, None)  # Safely read from the dictionary

# Example usage
def worker(username, value, shared_dict):
    # Simulate some processing and then update the dictionary
    print(f"Updating {username} to {value}")
    shared_dict.update(username, value)
    print(f"{username} updated to {shared_dict.get(username)}")

# Create a shared dictionary instance
shared_dict = ThreadSafeDict()

# Create threads
threads = []
for i in range(10):
    username = f"user{i}"
    value = i % 2 == 0  # Random boolean value for demonstration
    thread = threading.Thread(target=worker, args=(username, value, shared_dict))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Display final dictionary state
print("Final dictionary state:", shared_dict.data)
