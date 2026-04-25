
import threading

# Create a shared dictionary
user_status = {}
# Create a lock
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Acquire the lock
        user_status[username] = status  # Update the dictionary

def get_user_status(username):
    with lock:  # Acquire the lock for reading
        return user_status.get(username, None)

# Example usage
def request_handler(username, status):
    update_user_status(username, status)
    print(f"Updated {username} status to {status}")

# Simulate multiple threads updating the dictionary
threads = []
for i in range(5):
    username = f"user{i}"
    thread = threading.Thread(target=request_handler, args=(username, True))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

# Final dictionary state
print(user_status)
