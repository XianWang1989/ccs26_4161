
import threading

# Initialize a dictionary and a lock
user_status = {}
lock = threading.Lock()

def update_user_status(username, status):
    # Acquire the lock before modifying the dictionary
    with lock:
        user_status[username] = status

def get_user_status(username):
    # Acquire the lock before reading from the dictionary
    with lock:
        return user_status.get(username, False)

# Example usage in a threaded environment
def handle_request(username, status):
    update_user_status(username, status)
    print(f"Updated {username} to {status}. Current status: {get_user_status(username)}")

# Simulating multiple threads updating the user status
threads = []
for i in range(10):
    username = f"user{i}"
    status = i % 2 == 0  # Alternating True/False
    thread = threading.Thread(target=handle_request, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Final state of the dictionary
with lock:  # Ensure access to the dictionary for reading
    print("Final user statuses:", user_status)
