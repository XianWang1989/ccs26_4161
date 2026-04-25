
import threading

# Create a lock object
lock = threading.Lock()

# Your shared dictionary
user_status = {}

# Function to update the dictionary
def update_user_status(username, status):
    # Acquire the lock before modifying the dictionary
    with lock:
        user_status[username] = status

# Example usage
def handle_request(username, status):
    print(f"Updating status for {username} to {status}")
    update_user_status(username, status)

# Simulating requests from multiple threads
threads = []
for i in range(5):
    username = f"user{i}"
    status = True if i % 2 == 0 else False
    thread = threading.Thread(target=handle_request, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Print the final state of the dictionary
print(user_status)
