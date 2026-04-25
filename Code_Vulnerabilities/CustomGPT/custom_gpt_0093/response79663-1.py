
import threading

# Create a thread-safe dictionary and a lock
user_status = {}
lock = threading.Lock()

def update_user_status(username, status):
    with lock:  # Acquire the lock to ensure thread safety
        user_status[username] = status
        print(f"Updated {username} to {status}")

# Example usage in a thread context
def worker(username, status):
    update_user_status(username, status)

# Simulating multiple threads updating the dictionary
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(f'user{i}', True))
    threads.append(t)
    t.start()

# Join all threads to wait for their completion
for t in threads:
    t.join()

print(user_status)
