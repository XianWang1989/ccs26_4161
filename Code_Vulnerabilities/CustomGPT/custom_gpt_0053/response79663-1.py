
import threading

# Shared dictionary
user_status = {}
# Create a lock
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Acquire the lock
        user_status[username] = status  # Safely update the dictionary

def get_user_status(username):
    with lock:  # Acquire the lock before reading
        return user_status.get(username, None)  # Safely read from the dictionary

# Example of usage in a multi-threaded environment
def handle_request(username, status):
    update_user_status(username, status)
    print(f"Updated {username} to {status}. Current status: {get_user_status(username)}")

# Simulated multi-threaded requests
threads = []
for i in range(5):
    t = threading.Thread(target=handle_request, args=(f'user{i}', True))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
