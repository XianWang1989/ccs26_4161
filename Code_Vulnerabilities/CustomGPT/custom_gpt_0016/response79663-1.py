
import threading

class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()  # Create a lock
        self.data = {}  # Our dictionary

    def set_item(self, key, value):
        with self.lock:  # Acquire the lock before modifying
            self.data[key] = value

    def get_item(self, key):
        with self.lock:  # Acquire the lock before reading
            return self.data.get(key, None)

    def remove_item(self, key):
        with self.lock:  # Acquire the lock before removing
            if key in self.data:
                del self.data[key]

# Example usage
if __name__ == "__main__":
    ts_dict = ThreadSafeDict()

    # Simulating user connections with threads
    def user_connection(username):
        ts_dict.set_item(username, True)  # Set user status to True
        print(f"{username} status: {ts_dict.get_item(username)}")  # Get user status
        ts_dict.remove_item(username)  # Remove user when done

    # Creating threads for each user
    users = ['user1', 'user2', 'user3']
    threads = []

    for user in users:
        thread = threading.Thread(target=user_connection, args=(user,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Wait for all threads to complete
