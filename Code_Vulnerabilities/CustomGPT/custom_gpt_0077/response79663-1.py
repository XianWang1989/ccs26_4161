
import threading

# Create a shared dictionary
user_status = {}
# Create a lock
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Acquire the lock
        user_status[username] = status  # Update the dictionary

def get_user_status(username):
    with lock:  # Acquire the lock
        return user_status.get(username)  # Access the dictionary safely

# Example usage in a threaded environment
def handle_request(username, status):
    update_user_status(username, status)
    print(f"Updated status for {username}: {get_user_status(username)}")

# Create threads for demonstration
threads = []
for i in range(10):
    username = f"user_{i}"
    status = i % 2 == 0  # Example Boolean status
    thread = threading.Thread(target=handle_request, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("Final user statuses:", user_status)
