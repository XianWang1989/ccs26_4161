
import threading

class ThreadSafeDictionary:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set_value(self, key, value):
        with self.lock:  # Acquire the lock before updating the dictionary
            self.data[key] = value

    def get_value(self, key):
        with self.lock:  # Acquire the lock before reading from the dictionary
            return self.data.get(key)

    def remove_value(self, key):
        with self.lock:  # Acquire the lock before removing from the dictionary
            if key in self.data:
                del self.data[key]

# Example usage
if __name__ == "__main__":
    thread_safe_dict = ThreadSafeDictionary()

    # Function that simulates setting values in the dictionary
    def update_user_status(user, status):
        thread_safe_dict.set_value(user, status)
        print(f"Updated {user} to {status}")

    # Function that simulates getting values from the dictionary
    def check_user_status(user):
        status = thread_safe_dict.get_value(user)
        print(f"{user} status is: {status}")

    # Create threads to update and access the dictionary
    threads = []
    for i in range(3):
        threads.append(threading.Thread(target=update_user_status, args=(f"user{i}", True)))
        threads.append(threading.Thread(target=check_user_status, args=(f"user{i}",)))

    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
