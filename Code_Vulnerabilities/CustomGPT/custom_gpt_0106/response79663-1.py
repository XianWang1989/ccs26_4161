
import threading

# Initialize the dictionary and a lock
user_status_dict = {}
lock = threading.Lock()

def update_user_status(username, status):
    with lock:
        user_status_dict[username] = status

def get_user_status(username):
    with lock:
        return user_status_dict.get(username, False)

# Example usage
def worker(username, status):
    update_user_status(username, status)
    print(f"Updated {username} to {status}")

# Simulating multi-threaded access
threads = []
for i in range(20):
    username = f"user{i}"
    status = i % 2 == 0  # Example status
    t = threading.Thread(target=worker, args=(username, status))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

# Display final user statuses
print(user_status_dict)
