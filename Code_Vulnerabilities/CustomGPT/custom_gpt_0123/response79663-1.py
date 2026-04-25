
import threading

# Initialize a thread-safe dictionary and a lock
user_status = {}
lock = threading.Lock()

def update_user_status(username, status):
    with lock:
        user_status[username] = status

def get_user_status(username):
    with lock:
        return user_status.get(username, None)

# Example usage
def handle_request(username, status):
    update_user_status(username, status)
    print(f"Updated status for {username}: {status}")

# Simulating requests
threads = []
for i in range(10):  # Simulating 10 user requests
    username = f"user{i}"
    status = i % 2 == 0  # Random boolean status
    thread = threading.Thread(target=handle_request, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Print final user statuses
print(user_status)
