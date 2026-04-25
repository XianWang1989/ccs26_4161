
import threading

# Initialize a thread-safe dictionary and a lock
user_status = {}
lock = threading.Lock()

def update_user_status(username, status):
    # Acquire the lock before modifying the dictionary
    with lock:
        user_status[username] = status
        print(f"Updated {username}: {status}")

# Example usage with multiple threads
def simulate_user_request(username, status):
    update_user_status(username, status)

# Create and start threads
threads = []
for i in range(5):
    username = f'user{i}'
    status = i % 2 == 0  # Alternate status for illustration
    thread = threading.Thread(target=simulate_user_request, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print final user status
print("Final user status:", user_status)
