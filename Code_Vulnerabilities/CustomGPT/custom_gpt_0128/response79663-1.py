
import threading

# Shared dictionary
user_status = {}
# Create a lock for thread-safe access
lock = threading.Lock()

def update_user_status(username, status):
    # Acquire the lock before updating the dictionary
    with lock:
        user_status[username] = status
        print(f"Updated {username} status to {status}")

# Example usage with threads
def handle_request(username, status):
    # Simulate handling a request
    update_user_status(username, status)

# Simulate multiple threads updating the dictionary
threads = []
for i in range(10):
    username = f"user_{i}"
    status = i % 2 == 0  # Assign a boolean value
    thread = threading.Thread(target=handle_request, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Output the final dictionary
print("Final user status:", user_status)
