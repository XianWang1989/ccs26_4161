
import threading

# Initialize the dictionary and a lock
user_status = {}
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Acquire the lock
        user_status[username] = status  # Safely update the dictionary

def get_user_status(username):
    with lock:  # Acquire the lock
        return user_status.get(username)  # Safely read the dictionary

# Example usage in a thread
def handle_request(username, status):
    update_user_status(username, status)
    print(f"{username}'s status updated to {status}")

# Simulating requests
threads = []
for i in range(5):
    username = f"user{i}"
    threads.append(threading.Thread(target=handle_request, args=(username, True)))

# Start the threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Display the final user status
print(user_status)
