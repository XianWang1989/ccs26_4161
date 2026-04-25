
import threading

class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()  # Create a lock
        self.data = {}  # This will hold our dictionary

    def update(self, username, value):
        with self.lock:  # Acquire the lock before updating
            self.data[username] = value  # Safely update the dictionary

    def get(self, username):
        with self.lock:  # Acquire the lock before accessing
            return self.data.get(username)  # Safely read from the dictionary

# Example usage
thread_safe_dict = ThreadSafeDict()

def handle_request(username, value):
    # This function could be called by different threads for a web server
    thread_safe_dict.update(username, value)
    print(f"Updated {username} to {value}")

# Assume these function calls are made in different threads
thread1 = threading.Thread(target=handle_request, args=("user1", True))
thread2 = threading.Thread(target=handle_request, args=("user2", False))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
