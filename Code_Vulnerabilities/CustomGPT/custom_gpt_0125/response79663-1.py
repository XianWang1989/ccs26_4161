
import threading

# Initialize a thread-safe dictionary and a lock
safe_dict = {}
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Acquire the lock
        safe_dict[username] = status  # Safely update the dictionary

# Example usage
def handle_request(username, status):
    update_user_status(username, status)
    print(f"Updated {username} to {status}")

# Simulating multiple threads
threads = []
for i in range(20):
    username = f"user_{i}"
    status = True if i % 2 == 0 else False
    t = threading.Thread(target=handle_request, args=(username, status))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print(safe_dict)
