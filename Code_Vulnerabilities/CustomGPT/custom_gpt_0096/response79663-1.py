
import threading

# Create a dictionary to store the username and its status
user_status = {}
# Initialize a Lock
lock = threading.Lock()

def update_user_status(username, status):
    """Update the status of a user in a thread-safe manner."""
    with lock:  # Acquire the lock
        user_status[username] = status

def get_user_status(username):
    """Retrieve the status of a user in a thread-safe manner."""
    with lock:  # Ensure safe access
        return user_status.get(username, None)

# Example usage in a multi-threaded environment
def handle_request(username, status):
    update_user_status(username, status)
    print(f"Updated status for {username}: {get_user_status(username)}")

# Simulating multiple threads
threads = []
for i in range(10):
    username = f"user{i}"
    status = i % 2 == 0  # Alternate true/false
    thread = threading.Thread(target=handle_request, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
