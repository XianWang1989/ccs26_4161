
import threading

# Shared dictionary
user_status = {}
# Lock for synchronizing access to the dictionary
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Acquire the lock
        user_status[username] = status  # Safely update the dictionary

def get_user_status(username):
    with lock:  # Acquire the lock
        return user_status.get(username)  # Safely retrieve the value

# Example usage in a thread
def handle_request(username, status):
    update_user_status(username, status)
    print(f"Status updated for {username}: {status}")

# Simulating concurrent requests
threads = []
for i in range(10):
    username = f'user{i}'
    status = i % 2 == 0  # Simulating a boolean status
    thread = threading.Thread(target=handle_request, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print final user statuses
print(user_status)
