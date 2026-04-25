
import threading

# Shared dictionary
user_status = {}
# Create a lock object
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Acquire the lock
        user_status[username] = status  # Update the dictionary

def get_user_status(username):
    with lock:  # Acquire the lock
        return user_status.get(username, False)

# Example of updating user status in threads
def handle_request(username, status):
    update_user_status(username, status)
    print(f"Updated {username} to {status}")

# Simulating concurrent requests
threads = []
for i in range(10):  # Simulate 10 requests
    t = threading.Thread(target=handle_request, args=(f'user{i}', True))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

# Print final user status
print(user_status)
