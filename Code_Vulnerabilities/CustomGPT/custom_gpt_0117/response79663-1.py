
import threading

# Initialize the thread-safe dictionary and lock
safe_dict = {}
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Acquire the lock before modifying the dictionary
        safe_dict[username] = status
        print(f"Updated {username} to {status}")

def get_user_status(username):
    with lock:  # Acquire the lock before reading the dictionary
        return safe_dict.get(username, False)

# Example usage in a thread
def handle_request(username, status):
    update_user_status(username, status)
    print(f"{username}'s status: {get_user_status(username)}")

# Create and start threads
threads = []
for i in range(20):
    username = f'user_{i}'
    status = i % 2 == 0  # Alternate true/false
    thread = threading.Thread(target=handle_request, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Final dictionary state
print("Final user statuses:", safe_dict)
