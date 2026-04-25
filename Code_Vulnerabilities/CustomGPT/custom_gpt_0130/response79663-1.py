
import threading

# Initialize a dictionary and a lock
user_status = {}
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Acquire the lock
        user_status[username] = status  # Update the dictionary safely

def get_user_status(username):
    with lock:  # Acquire the lock
        return user_status.get(username)  # Read the dictionary safely

# Example usage
def handle_request(username, status):
    update_user_status(username, status)
    print(f"Updated {username} status to {status}")

# Simulate multiple threads updating the status
threads = []
for i in range(5):
    t = threading.Thread(target=handle_request, args=(f'user{i}', True))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

# Print final user statuses
print(user_status)
