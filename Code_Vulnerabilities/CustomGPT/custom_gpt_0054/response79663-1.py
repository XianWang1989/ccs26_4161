
import threading

# Create a dictionary to store username and boolean values
user_status = {}
# Create a lock for thread-safe access
lock = threading.Lock()

def update_user_status(username, status):
    with lock:
        user_status[username] = status
        print(f"Updated {username} status to {status}")

def get_user_status(username):
    with lock:
        return user_status.get(username, None)

# Example usage in threads
def handle_request(username, status):
    update_user_status(username, status)
    print(f"{username} status retrieved: {get_user_status(username)}")

# Simulating concurrent access
threads = []
for i in range(10):
    username = f"user{i}"
    status = i % 2 == 0  # Example status
    thread = threading.Thread(target=handle_request, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("Final user statuses:", user_status)
