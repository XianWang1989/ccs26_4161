
import threading

# Create a shared dictionary
user_status = {}
# Create a Lock
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Ensure that only one thread can execute this block at a time
        user_status[username] = status
        print(f"Updated {username} status to {status}")

def get_user_status(username):
    with lock:  # Ensure thread-safe read access
        return user_status.get(username, None)

# Example thread function to simulate requests
def simulate_request(username, status):
    update_user_status(username, status)

# Create threads that will update user statuses
threads = []
for i in range(10):
    username = f"user{i}"
    status = i % 2 == 0  # Alternate True/False statuses
    thread = threading.Thread(target=simulate_request, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Display the final user statuses
print("Final user statuses:", user_status)
