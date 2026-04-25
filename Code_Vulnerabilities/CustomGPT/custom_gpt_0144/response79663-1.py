import threading

# Initialize a lock
lock = threading.Lock()

# Shared dictionary (username -> Boolean)
user_status = {}

def update_user_status(username, status):
    # Acquire the lock to ensure thread-safe access
    with lock:
        user_status[username] = status

def get_user_status(username):
    # Acquire the lock to ensure thread-safe access
    with lock:
        return user_status.get(username, None)

# Example usage in threads:
def thread_function(username, status):
    update_user_status(username, status)
    print(f"Updated {username} status to {status}")

# Creating multiple threads to simulate concurrent access
threads = []
for i in range(5):
    username = f"user{i}"
    status = i % 2 == 0  # Assigning alternate True/False
    thread = threading.Thread(target=thread_function, args=(username, status))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Checking final user statuses
print(user_status)
