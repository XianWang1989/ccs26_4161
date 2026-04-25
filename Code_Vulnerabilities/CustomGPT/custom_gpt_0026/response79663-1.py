
import threading

# Initialize the lock
lock = threading.Lock()

# Your thread-safe dictionary
user_status = {}

def update_user_status(username, status):
    # Acquire the lock before updating the dictionary
    with lock:
        user_status[username] = status

def get_user_status(username):
    # Acquire the lock before accessing the dictionary
    with lock:
        return user_status.get(username, None)

# Example usage in a thread
def handle_request(username, status):
    # Update user status
    update_user_status(username, status)
    # Get user status
    print(f"Status for {username}: {get_user_status(username)}")

# Simulating thread requests
threads = []
for i in range(5):
    username = f"user_{i}"
    thread = threading.Thread(target=handle_request, args=(username, True))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
