
import threading

class ThreadSafeDict:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def set_value(self, username, value):
        with self.lock:
            self.data[username] = value

    def get_value(self, username):
        with self.lock:
            return self.data.get(username)

# Example usage
thread_safe_dict = ThreadSafeDict()

# Function to simulate updating the dictionary in a thread
def update_user_status(username, status):
    thread_safe_dict.set_value(username, status)

# You can create threads to call `update_user_status`
threads = []
for i in range(20):  # Simulating 20 users
    username = f'user{i}'
    status = i % 2 == 0  # Alternate True/False
    thread = threading.Thread(target=update_user_status, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print the final dictionary state
print(thread_safe_dict.data)
