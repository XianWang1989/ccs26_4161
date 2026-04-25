
import threading

# Shared dictionary and lock
user_status = {}
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Acquire the lock before modifying the dictionary
        user_status[username] = status
        print(f"Updated: {username} -> {status}")

def get_user_status(username):
    with lock:  # Acquire the lock before reading the dictionary
        return user_status.get(username)

# Example usage in a thread
def handle_request(username, status):
    update_user_status(username, status)
    print(f"Current status for {username}: {get_user_status(username)}")

# Simulating multiple threads
threads = []
for i in range(1, 6):
    username = f"user_{i}"
    status = i % 2 == 0  # True if even, False if odd
    thread = threading.Thread(target=handle_request, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("Final user statuses:", user_status)
