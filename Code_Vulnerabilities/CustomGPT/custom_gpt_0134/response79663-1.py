
import threading

# Initialize the shared dictionary
user_status = {}
# Create a lock object
lock = threading.Lock()

def update_user_status(username, status):
    # Acquire the lock before modifying the dictionary
    with lock:
        user_status[username] = status  # Update the dictionary

def get_user_status(username):
    # Acquire the lock before reading the dictionary
    with lock:
        return user_status.get(username, False)  # Return the status or False if not found

# Example usage
def handle_request(username, status):
    update_user_status(username, status)
    print(f"Updated {username} status to {status}")

# Simulating multiple threads updating user status
threads = []
for i in range(10):
    username = f"user{i}"
    status = i % 2 == 0  # Even index users are True, odd are False
    thread = threading.Thread(target=handle_request, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Display the final user status
print(user_status)
